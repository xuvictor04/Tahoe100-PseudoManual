---
symbol: "BCS1L"
type: "gene"
col: 1082
ensembl_id: "ENSG00000074582"
name: "BCS1 ubiquinol-cytochrome c reductase complex chaperone"
location: "2q35"
module: 1
arm: "+"
pooled_cpm: 5.04
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 4
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# BCS1L

*BCS1 ubiquinol-cytochrome c reductase complex chaperone* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.61× (z +12.0, q 3e-30, up in 10 of 10 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 2.00× (z +4.7, q 1e-04, up in 12 of 29 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 7.27×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.547× (z -5.8, q 3e-06, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IMP4]] (+0.73, fdr 7e-06), [[NOC4L]] (+0.72, fdr 7e-06), [[RITA1]] (+0.70, fdr 7e-06); moves opposite to [[CD63]] (-0.59, fdr 2e-05), [[GNAS]] (-0.58, fdr 3e-05), [[PABPN1]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1082.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 7.27×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.61×** | +12.0 | 3e-30 | 10/10 (SW480, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.06×** | +10.9 | 6e-25 | 21/23 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.98×** | +6.6 | 8e-09 | 28/47 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.29×** | +5.5 | 6e-06 | 10/15 (SW1417, CFPAC-1, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +5.2 | 3e-05 | 11/28 (NCI-H2347, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.67×** | +5.0 | 6e-05 | 21/45 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.67×** | +5.0 | 6e-05 | 22/46 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.00×** | +4.7 | 1e-04 | 12/29 (A498, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.60×** | +4.5 | 4e-04 | 14/46 (HepG2/C3A, A549, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.45×** | +3.6 | 0.019 | 7/28 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.58×** | +3.1 | 0.085 | 10/42 (A498, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.1 | 0.100 | 4/48 (LS 180, HCT15, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.82× | +3.0 | 0.10 | 2/13 (SW480, PANC-1) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1082.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.547×** | -5.8 | 3e-06 | 28/47 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.566×** | -5.5 | 9e-06 | 21/45 (BT-474, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.642×** | -4.3 | 0.003 | 19/45 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Rifaximin (drug)]] 5 µM |  | **0.692×** | -3.4 | 0.086 | 10/44 (HEC-1-A, NCI-H1792, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.727× | -3.1 | 0.22 | 14/38 (PANC-1, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1082. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 2.96 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0755× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 4.10 | 0 | 1 | — | [[Furosemide (drug)]] 0.05 µM 0.0656× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 7.98 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.124× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 4.09 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.27× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[RKO (line)]] | wt | 7.26 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0358× (z -11.8) |
| [[SHP-77 (line)]] | alt | 8.10 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.0889× (z -9.0) |
| [[A-172 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1082), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IMP4]] | +0.73 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[NOC4L]] | +0.72 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[RITA1]] | +0.70 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[ALKBH2]] | +0.69 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[BOP1]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[NLE1]] | +0.69 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[HGH1]] | +0.69 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[IFRD2]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[PRMT5]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[PSMG1]] | +0.67 | +0.73 / +0.61 | both halves | 7e-06 | STRING 510 |
| [[CLUH]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[WDR18]] | +0.67 | +0.65 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD63]] | -0.59 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[GNAS]] | -0.58 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[PABPN1]] | -0.57 | -0.43 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.609). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.2, -39.8); signed map (-3.4, -44.3). **Vector** length 51.0, 6.96% of its response variance represented; |z| ≥ 3 in 764 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.51 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.53 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.53 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.3 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +3.3 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +3.0 | +10.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | +2.5 | +3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.7 | +1.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +3.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.5 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -5.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -4.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.9 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.9 | -5.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.2 | -0.7 |
|  | [[Rifaximin (drug)]] 5 µM |  | -1.1 | -3.4 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -1.1 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | BCS1 ubiquinol-cytochrome c reductase complex chaperone |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:218,658,764-218,663,443 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Hs.6719, BCS, h-BCS, BJS |
| Gene groups (HGNC) | AAA ATPases; Mitochondrial respiratory chain complex assembly factors |
| Reactome | 5 pathways, smallest: Complex III assembly; Mitochondrial protein import; Respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y276](https://www.uniprot.org/uniprotkb/Q9Y276) (Mitochondrial chaperone BCS1):

> Chaperone necessary for the incorporation of Rieske iron-sulfur protein UQCRFS1 into the mitochondrial respiratory chain complex III. Plays an important role in the maintenance of mitochondrial tubular networks, respiratory chain assembly and formation of the LETM1 complex.

**Summary**, from NCBI Gene [617](https://www.ncbi.nlm.nih.gov/gene/617):

> This gene encodes a homolog of the S. cerevisiae bcs1 protein which is involved in the assembly of complex III of the mitochondrial respiratory chain. The encoded protein does not contain a mitochondrial targeting sequence but experimental studies confirm that it is imported into mitochondria. Mutations in this gene are associated with mitochondrial complex III deficiency and the GRACILE syndrome. Several alternatively spliced transcripts encoding two different isoforms have been described. …

**Accessions** — [HGNC:1020](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1020) · Entrez [617](https://www.ncbi.nlm.nih.gov/gene/617) · UniProt [Q9Y276](https://www.uniprot.org/uniprotkb/Q9Y276) · Ensembl [ENSG00000074582](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074582)

## Data

Gene col 1082: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1082); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1082, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1082]; `tensor/DDL_lfc|DDL_z.npy` [1082]; `embed/gene_vectors.npy` [1082]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1082 or target_col == 1082). Every well: [[BCS1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCS1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
