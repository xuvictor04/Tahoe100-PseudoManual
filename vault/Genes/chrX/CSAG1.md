---
symbol: "CSAG1"
type: "gene"
col: 12743
ensembl_id: "ENSG00000198930"
name: "chondrosarcoma associated gene 1"
location: "Xq28"
module: 24
arm: "+"
pooled_cpm: 3.52
n_lines_expressing: 20
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# CSAG1

*chondrosarcoma associated gene 1* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.37× (z +9.7, q 2e-19, up in 8 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.95× (z +6.0, q 3e-07, up in 6 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM126A]] (+0.58, fdr 1e-05), [[SAT2]] (+0.57, fdr 4e-05), [[IFI27L2]] (+0.55, fdr 3e-05); moves opposite to [[KPNA4]] (-0.50, fdr 1e-04), [[ALMS1]] (-0.47, fdr 8e-05), [[SAE1]] (-0.47, fdr 2e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NLGN4X]] → it (grade C ⚠); 2 go from it, the strongest it → [[NLGN4X]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12743.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.37×** | +9.7 | 2e-19 | 8/12 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.83×** | +8.5 | 5e-15 | 2/4 (HS-578T, LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.95×** | +6.0 | 3e-07 | 6/16 (A-427, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.47×** | +6.0 | 4e-07 | 6/10 (LS 180, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +5.0 | 7e-05 | 3/7 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +4.2 | 0.002 | 5/11 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.0 | 0.004 | 5/15 (A-427, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +4.0 | 0.004 | 6/13 (NCI-H1573, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~23% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +3.9 | 0.005 | 4/12 (NCI-H1573, A-427, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.2 | 0.067 | 7/12 (hTERT-HPNE, RPMI-7951, …) | top dose only |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.59× | +3.1 | 0.11 | 5/13 (LS 180, hTERT-HPNE, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 2.62× | +3.1 | 0.11 | 0/3 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12743.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lucanthone (drug)]] 0.05 µM |  | 0.606× | -3.0 | 0.96 | 2/17 (LS 180, RPMI-7951) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12743. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 0.853 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.305 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.285 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.284 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.769 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.446 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.296 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.307 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.322 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.318 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.269 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.259 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.270 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.268 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.331 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.991 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.243 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.304 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.351 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.655 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.356 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.267 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12743), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 10 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM126A]] | +0.58 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[SAT2]] | +0.57 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[IFI27L2]] | +0.55 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[GLMP]] | +0.55 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[MRPS24]] | +0.54 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[MICU1]] | +0.54 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[SNX2]] | +0.53 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[SMIM26]] ⚠ | +0.52 | +0.46 / +0.48 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CHMP2B]] | +0.52 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[LAMTOR5]] | +0.51 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[RPAIN]] | +0.51 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[YWHAEP7-1]] | +0.51 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[ABCA5]] | +0.51 | +0.46 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNA4]] | -0.50 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[ALMS1]] | -0.47 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[SAE1]] | -0.47 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[NUP50]] | -0.46 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[LMNB2]] | -0.46 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[NUP188]] | -0.46 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[FGD5-AS1]] | -0.46 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[NCBP1]] | -0.45 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[PCNT]] | -0.45 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[MACROH2A1]] | -0.45 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[GEN1]] | -0.44 | -0.29 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NLGN4X]] | C | NLGN4X activity raises CSAG1's level | lines that do not express NLGN4X (37) vs lines expressing it (13) | 2.98× lower at baseline in the lines without NLGN4X | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P; co-absent with the target |
| [[GLMP]] | C | GLMP activity lowers CSAG1's level | lines that do not express GLMP (4) vs lines expressing it (46) | 2.35× higher at baseline in the lines without GLMP | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000255031, SMAD7, TCIRG1 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NLGN4X]] | C | CSAG1 activity raises NLGN4X's level | lines that do not express CSAG1 (30) vs lines expressing it (20) | 2.93× lower at baseline in the lines without CSAG1 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, ENSG00000226043, LINC02616; co-absent with the target |
| [[OVAAL]] | C | CSAG1 activity raises OVAAL's level | lines that do not express CSAG1 (30) vs lines expressing it (20) | 1.64× lower at baseline in the lines without CSAG1 | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, ENSG00000226043, LINC02616; co-absent with the target |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.543). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-36.6, -28.9); signed map (-13.9, -1.4). **Vector** length 21.1, 3.53% of its response variance represented; |z| ≥ 3 in 211 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +1.3 | +6.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.0 | +1.7 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +0.7 | +0.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.7 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.6 | +0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.5 | +1.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.5 | +1.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.5 | +2.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -0.6 | +1.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | +1.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -0.6 | +3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.6 | -1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.5 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.4 | -0.3 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.4 | -2.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.4 | +0.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.4 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | chondrosarcoma associated gene 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:152,727,484-152,733,735 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CSAGE, CT24.1 |
| Gene groups (HGNC) | CSAG family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PB30](https://www.uniprot.org/uniprotkb/Q6PB30) (Chondrosarcoma-associated gene 1 protein):

> May play an important role in maintaining centrosome integrity during mitosis.

**Summary**, from NCBI Gene [158511](https://www.ncbi.nlm.nih.gov/gene/158511):

> This gene encodes a member of a family of tumor antigens. The protein is expressed in chondrosarcomas, but may also be expressed in normal tissues such as testis. Alternative splicing of this gene results in two transcript variants encoding the same protein. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:24294](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24294) · Entrez [158511](https://www.ncbi.nlm.nih.gov/gene/158511) · UniProt [Q6PB30](https://www.uniprot.org/uniprotkb/Q6PB30) · Ensembl [ENSG00000198930](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198930)

## Data

Gene col 12743: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12743); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12743, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12743]; `tensor/DDL_lfc|DDL_z.npy` [12743]; `embed/gene_vectors.npy` [12743]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12743 or target_col == 12743). Every well: [[CSAG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSAG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
