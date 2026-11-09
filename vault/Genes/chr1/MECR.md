---
symbol: "MECR"
type: "gene"
col: 3792
ensembl_id: "ENSG00000116353"
name: "mitochondrial trans-2-enoyl-CoA reductase"
location: "1p35.3"
module: 5
arm: "+"
pooled_cpm: 19.96
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# MECR

*mitochondrial trans-2-enoyl-CoA reductase* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.69× (z +6.9, q 3e-09, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.628× (z -5.9, q 2e-06, down in 25 of 45 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.745× (z -5.5, q 9e-06, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF696]] (+0.68, fdr 7e-06), [[TIMM9]] (+0.66, fdr 7e-06), [[TSEN2]] (+0.64, fdr 7e-06); moves opposite to [[MTMR11]] (-0.58, fdr 1e-05), [[ADD3]] (-0.55, fdr 1e-05), [[NUCB1]] (-0.52, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3792.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +6.9 | 3e-09 | 30/48 (hTERT-HPNE, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +6.3 | 1e-07 | 33/48 (SW 900, A-172, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +6.1 | 2e-07 | 29/48 (HT-29, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +5.7 | 2e-06 | 25/44 (NCI-H1573, SW1417, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +4.1 | 0.004 | 0/48 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +3.5 | 0.046 | 11/45 (COLO 205, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.30×** | +3.3 | 0.068 | 19/46 (HT-29, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3792.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.628×** | -5.9 | 2e-06 | 25/45 (C-33 A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.745×** | -5.5 | 9e-06 | 23/47 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.661×** | -5.5 | 9e-06 | 24/47 (RPMI-7951, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.696×** | -4.8 | 3e-04 | 22/48 (C32, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.530×** | -4.4 | 0.001 | 20/48 (PANC-1, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.540×** | -4.2 | 0.002 | 19/46 (A-427, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.732×** | -4.1 | 0.003 | 23/47 (SW48, SW480, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.620×** | -3.3 | 0.071 | 8/24 (MIA PaCa-2, NCI-H23, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3792. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 38.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -14.2) |
| [[MIA PaCa-2 (line)]] | alt | 37.2 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -9.9) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A-172 (line)]] | wt | 9.58 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0937× (z -11.7) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 40.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.130× (z -12.7) ⚠ toxic |
| [[C32 (line)]] | wt | 13.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.110× (z -10.7) |
| [[HS-578T (line)]] | alt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -10.6) |
| [[LoVo (line)]] | wt | 20.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.103× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 43.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.273× (z -11.0) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 18.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.189× (z -9.0) |
| [[SNU-1 (line)]] | wt | 23.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 20.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.127× (z -9.4) |
| [[A-427 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3792), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF696]] | +0.68 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[TIMM9]] | +0.66 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[TSEN2]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[ANGEL1]] | +0.64 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[PINX1]] | +0.63 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[ATR]] | +0.63 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[PDCD11]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[POLR1G]] | +0.63 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[SDAD1]] | +0.63 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[MRTO4]] | +0.62 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[PUS1]] | +0.61 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[ACTR3B]] | +0.61 | +0.66 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTMR11]] | -0.58 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[ADD3]] | -0.55 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[NUCB1]] | -0.52 | -0.51 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers MECR's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.572). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-13.7, -37.5); signed map (0.6, -49.4). **Vector** length 88.5, 19.3% of its response variance represented; |z| ≥ 3 in 835 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | -0.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | -0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.2 | +2.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.8 | -4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | -1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.5 | -5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -0.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial trans-2-enoyl-CoA reductase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:29,192,657-29,230,942 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-63, NRBF1, FASN2B, ETR1 |
| Gene groups (HGNC) | Oxidoreductases |
| Reactome | 5 pathways, smallest: Beta oxidation of decanoyl-CoA to octanoyl-CoA-CoA; mitochondrial fatty acid beta-oxidation of saturated fatty acids; Mitochondrial Fatty Acid Beta-Oxidation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BV79](https://www.uniprot.org/uniprotkb/Q9BV79) (Enoyl-[acyl-carrier-protein] reductase, mitochondrial):

> Catalyzes the NADPH-dependent reduction of trans-2-enoyl thioesters in mitochondrial fatty acid synthesis (fatty acid synthesis type II). Fatty acid chain elongation in mitochondria uses acyl carrier protein (ACP) as an acyl group carrier, but the enzyme accepts both ACP and CoA thioesters as substrates in vitro. Displays a preference for medium-chain over short- and long-chain substrates. May provide the octanoyl chain used for lipoic acid biosynthesis, regulating protein lipoylation and …

**Summary**, from NCBI Gene [51102](https://www.ncbi.nlm.nih.gov/gene/51102):

> The protein encoded by this gene is an oxidoreductase that catalyzes the last step in mitochondrial fatty acid synthesis. Defects in this gene are a cause of childhood-onset dystonia and optic atrophy. [provided by RefSeq, Mar 2017]

**Accessions** — [HGNC:19691](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19691) · Entrez [51102](https://www.ncbi.nlm.nih.gov/gene/51102) · UniProt [Q9BV79](https://www.uniprot.org/uniprotkb/Q9BV79) · Ensembl [ENSG00000116353](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116353)

## Data

Gene col 3792: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3792); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3792, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3792]; `tensor/DDL_lfc|DDL_z.npy` [3792]; `embed/gene_vectors.npy` [3792]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3792 or target_col == 3792). Every well: [[MECR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MECR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
