---
symbol: "PWRN1"
type: "gene"
col: 15244
ensembl_id: "ENSG00000259905"
name: "Prader-Willi region non-protein coding RNA 1"
location: "15q11.2"
module: 90
arm: "+"
pooled_cpm: 2.63
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# PWRN1

*Prader-Willi region non-protein coding RNA 1* — 15q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.53× (z +14.3, q 1e-43, up in 20 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPRT]] (+0.81, fdr 7e-06), [[USH2A]] (+0.78, fdr 7e-06), [[SORCS1]] (+0.76, fdr 7e-06).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CCDC144NL-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15244.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.53×** | +14.3 | 1e-43 | 20/25 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.63×** | +11.9 | 2e-30 | 1/2 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.71×** | +11.3 | 3e-27 | 19/28 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.12×** | +9.2 | 4e-18 | 2/7 (PANC-1, SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.30×** | +8.9 | 4e-17 | 2/2 (BT-474, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.94×** | +7.5 | 6e-12 | 18/42 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.10×** | +6.0 | 1e-07 | 19/39 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.96×** | +5.5 | 3e-06 | 14/44 (BT-474, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +5.0 | 4e-05 | 1/8 (SW480) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +4.9 | 6e-05 | 4/18 (A498, A549, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +4.5 | 4e-04 | 11/30 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +4.0 | 0.002 | 6/25 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.64×** | +4.0 | 0.003 | 14/39 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.60×** | +3.8 | 0.006 | 5/27 (SK-MEL-2, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +3.6 | 0.011 | 11/27 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +3.6 | 0.011 | 10/32 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.80×** | +3.4 | 0.023 | 1/14 (HOP62) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.025 | 3/26 (SNU-423, LS 180, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.49×** | +3.2 | 0.041 | 10/40 (BT-474, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15244. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 1.08 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 9.22× (z +9.0) | — |
| [[A549 (line)]] | wt | 1.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.1× (z +8.9) | — |
| [[BT-474 (line)]] | alt | 77.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.66× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 2.50 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.94× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 1.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +11.0) | — |
| [[A-172 (line)]] | wt | 0.955 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.865 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.986 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.901 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.887 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.911 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.980 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.864 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.882 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.861 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15244), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRT]] | +0.81 | +0.59 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[USH2A]] | +0.78 | +0.68 / +0.86 | both halves | 7e-06 |  |
| [[SORCS1]] | +0.76 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[CNTNAP5]] | +0.76 | +0.59 / +0.79 | both halves | 7e-06 |  |
| [[SLC26A5]] | +0.75 | +0.47 / +0.83 | both halves | 2e-05 |  |
| [[SCHLAP1]] | +0.75 | +0.63 / +0.79 | both halves | 7e-06 | same gene group |
| [[DLGAP2]] | +0.75 | +0.61 / +0.80 | both halves | 7e-06 |  |
| [[ASB14]] | +0.75 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[XKR4]] | +0.74 | +0.63 / +0.82 | both halves | 7e-06 |  |
| [[TEX11]] | +0.73 | +0.50 / +0.74 | both halves | 1e-05 |  |
| [[LINC02208]] | +0.73 | +0.56 / +0.85 | both halves | 1e-05 |  |
| [[IL1RAPL2]] | +0.73 | +0.66 / +0.81 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC144NL-1]] | B | CCDC144NL-1 activity raises PWRN1's level | lines that do not express CCDC144NL-1 (5) vs lines expressing it (45) | 1.46× lower at baseline in the lines without CCDC144NL-1 | 0.074 | ⚠ within organs, on part of the lines; also absent: LINC00298, ARHGAP15, XIRP2; maybe low, not absent |
| [[LINC01579]] | B | LINC01579 activity raises PWRN1's level | lines that do not express LINC01579 (13) vs lines expressing it (37) | 1.39× lower at baseline in the lines without LINC01579 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, CNTNAP2, CACNA1C; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.763). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.1, 29.5); signed map (32.5, 14.6). **Vector** length 38.5, 4.32% of its response variance represented; |z| ≥ 3 in 912 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +14.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +7.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +11.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +3.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -0.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -1.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -1.2 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.8 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | Prader-Willi region non-protein coding RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q11.2 — chr15:24,101,827-24,823,365 (+) |
| Ensembl biotype | lncRNA |
| Also known as | NCRNA00198, LOHAN1 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [791114](https://www.ncbi.nlm.nih.gov/gene/791114):

> This gene is located in the Prader-Willi syndrome (PWS) region of chromosome 15, which is known to undergo imprinting. The transcript is believed to be non-coding. It is bi-allelically expressed in testis and kidney, but mono-allelically expressed from the paternal allele in brain. This gene is poly-adenylated and is known to undergo alternative splicing. Transcript variants may represent part of a complex imprinting center-SNURF-SNRPN transcription unit. The contribution of this gene to the …

**Accessions** — [HGNC:33235](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33235) · Entrez [791114](https://www.ncbi.nlm.nih.gov/gene/791114) · Ensembl [ENSG00000259905](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259905)

## Data

Gene col 15244: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15244); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15244, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15244]; `tensor/DDL_lfc|DDL_z.npy` [15244]; `embed/gene_vectors.npy` [15244]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15244 or target_col == 15244). Every well: [[PWRN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PWRN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
