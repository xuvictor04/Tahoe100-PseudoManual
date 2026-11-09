---
symbol: "GCNT7"
type: "gene"
col: 4475
ensembl_id: "ENSG00000124091"
name: "glucosaminyl (N-acetyl) transferase family member 7"
location: "20q13.31"
module: 21
arm: "+"
pooled_cpm: 2.41
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# GCNT7

*glucosaminyl (N-acetyl) transferase family member 7* — 20q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.59× (z +9.3, q 6e-18, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.64× (z +7.1, q 2e-10, up in 18 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SW480 0.111×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBOX5-AS1]] (+0.84, fdr 7e-06), [[HRG-AS1]] (+0.77, fdr 7e-06), [[ZRANB2-AS1]] (+0.76, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MYT1L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4475.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.59×** | +9.3 | 6e-18 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.31×** | +8.5 | 4e-15 | 12/16 (Hs 766T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +7.1 | 2e-10 | 18/34 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.93×** | +6.7 | 3e-09 | 7/14 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +6.4 | 2e-08 | 2/5 (PANC-1, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +4.8 | 1e-04 | 7/29 (A-172, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.57×** | +4.3 | 0.001 | 4/40 (CFPAC-1, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +4.0 | 0.005 | 2/15 (Hs 766T, A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.03×** | +3.8 | 0.010 | 0/38 | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.66×** | +3.7 | 0.013 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.91×** | +3.4 | 0.030 | 0/5 | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.86×** | +3.3 | 0.045 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.048 | 8/41 (BT-474, A498, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 0.05 µM |  | **1.39×** | +3.1 | 0.084 | 2/41 (A-427, RKO) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4475.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SW480 0.111×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.869× | -5.0 | 3e-04 | 18/47 (HepG2/C3A, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4475. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 2.65 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.111× (z -9.7) |
| [[A-172 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4475), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBOX5-AS1]] | +0.84 | +0.71 / +0.82 | both halves | 7e-06 |  |
| [[HRG-AS1]] | +0.77 | +0.60 / +0.78 | both halves | 7e-06 |  |
| [[ZRANB2-AS1]] | +0.76 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[C2CD5-AS1]] | +0.74 | +0.59 / +0.77 | both halves | 7e-06 |  |
| [[BIRC6-AS2-1]] | +0.73 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[VPS39-DT]] | +0.72 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[TICAM2-AS1]] | +0.72 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[EOGT-DT]] | +0.72 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[LANCL1-AS1]] | +0.72 | +0.50 / +0.75 | both halves | 1e-05 |  |
| [[SLC23A1]] | +0.71 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[A2ML1-AS1]] | +0.71 | +0.47 / +0.75 | both halves | 2e-05 |  |
| [[PP2D1]] | +0.70 | +0.60 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYT1L]] | B | MYT1L activity raises GCNT7's level | lines that do not express MYT1L (6) vs lines expressing it (44) | 1.15× lower at baseline in the lines without MYT1L | 0.063 | ⚠ within organs, on part of the lines; also absent: LINC01811, XIRP2, ENSG00000232855; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.768). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.3, 27.9); signed map (34.5, 4.7). **Vector** length 26.0, 1.64% of its response variance represented; |z| ≥ 3 in 988 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.8 | +1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +0.8 | +1.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -1.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | +0.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.7 | +1.7 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.6 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.6 | +0.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | glucosaminyl (N-acetyl) transferase family member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.31 — chr20:56,491,492-56,525,925 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1153D9.2; previously C20orf105 |
| Gene groups (HGNC) | Glucosaminyl (N-acetyl) transferases/xylosyltransferases |
| Reactome | 2 pathways, smallest: O-linked glycosylation of mucins; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZNI0](https://www.uniprot.org/uniprotkb/Q6ZNI0) (Probable beta-1,3-galactosyl-O-glycosyl-glycoprotein beta-1,6-N-acetylglucosaminyltransferase 7):

> Probable glycosyltransferase.

**Summary**, from NCBI Gene [140687](https://www.ncbi.nlm.nih.gov/gene/140687):

> Predicted to enable acetylglucosaminyltransferase activity. Predicted to be located in Golgi membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16099](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16099) · Entrez [140687](https://www.ncbi.nlm.nih.gov/gene/140687) · UniProt [Q6ZNI0](https://www.uniprot.org/uniprotkb/Q6ZNI0) · Ensembl [ENSG00000124091](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124091)

## Data

Gene col 4475: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4475); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4475, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4475]; `tensor/DDL_lfc|DDL_z.npy` [4475]; `embed/gene_vectors.npy` [4475]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4475 or target_col == 4475). Every well: [[GCNT7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GCNT7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
