---
symbol: "LBHD1"
type: "gene"
col: 8489
ensembl_id: "ENSG00000162194"
name: "LBH domain containing 1"
location: "11q12.3"
module: 7
arm: "+"
pooled_cpm: 15.79
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# LBHD1

*LBH domain containing 1* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.73× (z +8.0, q 6e-13, up in 25 of 30 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.88× (z +7.1, q 2e-10, up in 40 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.317×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM174C]] (+0.67, fdr 7e-06, ⚠ FAM174C in the vector space only through flagged drug-doses), [[PWP2]] (+0.66, fdr 1e-05), [[MRPS17]] (+0.66, fdr 7e-06), [[MRPL36]] (+0.64, fdr 1e-04); moves opposite to [[CD99]] (-0.55, fdr 1e-05), [[RBM3]] (-0.51, fdr 0.004, ⚠ one half only (not replicated)), [[SARAF]] (-0.49, fdr 3e-05), [[EMC10]] (-0.49, fdr 2e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RPP25]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8489.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **2.73×** | +8.0 | 6e-13 | 25/30 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **2.53×** | +7.7 | 4e-12 | 34/39 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +7.1 | 2e-10 | 40/46 (A549, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **2.13×** | +6.3 | 5e-08 | 36/47 (HEC-1-A, HOP62, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **2.05×** | +6.0 | 3e-07 | 34/47 (A549, HOP62, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +5.8 | 5e-07 | 31/43 (CFPAC-1, A549, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.89×** | +5.3 | 1e-05 | 34/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.89×** | +5.3 | 1e-05 | 35/46 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.86×** | +4.9 | 5e-05 | 28/46 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.81×** | +4.9 | 5e-05 | 30/41 (HOP62, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +3.7 | 0.012 | 22/47 (HEC-1-A, SW 900, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.020 | 24/48 (SNU-423, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.53×** | +3.5 | 0.020 | 23/46 (AsPC-1, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +3.5 | 0.020 | 18/47 (PANC-1, SW 900, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.078 | 15/47 (NCI-H1573, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8489.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.317×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.666× | -3.4 | 0.23 | 19/48 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.744× | -3.3 | 0.23 | 19/48 (Hs 766T, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.69 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8489. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 42.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 11.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.03× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | — |
| [[A-172 (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8489), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 5 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM174C]] ⚠ | +0.67 | +0.63 / +0.72 | both halves | 7e-06 | **novel candidate**; ⚠ in the vector space only through flagged drug-doses |
| [[PWP2]] | +0.66 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[MRPS17]] | +0.66 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[MRPL36]] | +0.64 | +0.35 / +0.77 | both halves | 1e-04 |  |
| [[EXOSC4]] | +0.64 | +0.36 / +0.73 | both halves | 9e-05 |  |
| [[MRPS12]] | +0.64 | +0.31 / +0.72 | both halves | 2e-04 |  |
| [[GEMIN6]] | +0.64 | +0.41 / +0.73 | both halves | 4e-05 |  |
| [[RRS1]] | +0.62 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[CCDC137]] | +0.61 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[EMC6]] | +0.60 | +0.32 / +0.73 | both halves | 2e-04 |  |
| [[COA4]] | +0.60 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[MRPL12]] | +0.59 | +0.39 / +0.75 | both halves | 6e-05 |  |
| [[NIP7]] | +0.59 | +0.64 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD99]] | -0.55 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[RBM3]] | -0.51 | -0.06 / -0.59 | ⚠ one half (not replicated) | 0.004 |  |
| [[SARAF]] | -0.49 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[EMC10]] | -0.49 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[ATP6AP2]] | -0.48 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[MORF4L1]] | -0.47 | -0.24 / -0.64 | both halves | 4e-04 |  |
| [[PCBP2]] | -0.47 | -0.07 / -0.61 | ⚠ one half (not replicated) | 0.004 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPP25]] | B | RPP25 activity raises LBHD1's level | lines that do not express RPP25 (14) vs lines expressing it (36) | 1.45× lower at baseline in the lines without RPP25 | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, ODF3B, EPHA10 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.497). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-45.3, -10.2); signed map (-3.3, -20.8). **Vector** length 46.9, 8.95% of its response variance represented; |z| ≥ 3 in 578 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.3 | +5.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +2.5 | +4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.4 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +3.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.3 | +1.9 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | -1.6 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -0.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.0 | -2.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -0.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | LBH domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,662,817-62,672,267 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2477; previously C11orf48 |
| Matched by | ensembl_id |

UniProt [Q9BQE6](https://www.uniprot.org/uniprotkb/Q9BQE6) carries no function annotation.

**Summary**, from NCBI Gene [79081](https://www.ncbi.nlm.nih.gov/gene/79081):

> This gene shares three exons in common with another gene, chromosome 11 open reading frame 98 (GeneID:102288414), but the encoded protein uses a reading frame that is different from that of the chromosome 11 open reading frame 98 gene. [provided by RefSeq, Nov 2017]

**Accessions** — [HGNC:28351](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28351) · Entrez [79081](https://www.ncbi.nlm.nih.gov/gene/79081) · UniProt [Q9BQE6](https://www.uniprot.org/uniprotkb/Q9BQE6) · Ensembl [ENSG00000162194](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162194)

## Data

Gene col 8489: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8489); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8489, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8489]; `tensor/DDL_lfc|DDL_z.npy` [8489]; `embed/gene_vectors.npy` [8489]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8489 or target_col == 8489). Every well: [[LBHD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LBHD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
