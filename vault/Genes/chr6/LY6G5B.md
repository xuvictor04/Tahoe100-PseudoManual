---
symbol: "LY6G5B"
type: "gene"
col: 14222
ensembl_id: "ENSG00000240053"
name: "lymphocyte antigen 6 family member G5B"
location: "6p21.33"
module: 126
arm: "+"
pooled_cpm: 3.13
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# LY6G5B

*lymphocyte antigen 6 family member G5B* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 4.28× (z +10.4, q 1e-22, up in 5 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.44× (z +4.0, q 0.009, up in 11 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.488× (z -5.3, q 5e-05, down in 21 of 43 measured lines) ⚠ cell-cycle shift, explains ~42% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM in 1 line (SW480 0.0541×); [[5-Azacytidine (drug)]] 0.5 µM in 1 line (HOP62 0.0632×); [[Vilanterol (drug)]] 0.5 µM in 1 line (LoVo 0.0776×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPTLC1]] (+0.72, fdr 1e-05), [[LENG8]] (+0.72, fdr 7e-06), [[CERS2]] (+0.72, fdr 1e-05); moves opposite to [[PITPNA-AS1]] (-0.68, fdr 1e-05), [[HPF1]] (-0.67, fdr 7e-06), [[BTG1]] (-0.64, fdr 3e-05).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FRMD4B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14222.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.28×** | +10.4 | 1e-22 | 5/7 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.06×** | +8.4 | 2e-14 | 6/7 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.62×** | +5.8 | 1e-06 | 9/16 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.009 | 11/36 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +3.3 | 0.092 | 6/31 (BT-474, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.51× | +3.2 | 0.13 | 5/46 (BT-474, SW1417, …) | top dose only | position effect removed |
| [[Tadalafil (drug)]] 5 µM |  | 1.53× | +3.2 | 0.13 | 4/43 (C32, SK-MEL-2, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14222.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM in 1 line (SW480 0.0541×); [[5-Azacytidine (drug)]] 0.5 µM in 1 line (HOP62 0.0632×); [[Vilanterol (drug)]] 0.5 µM in 1 line (LoVo 0.0776×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.488×** | -5.3 | 5e-05 | 21/43 (LoVo, NCI-H2030, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14222. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 3.29 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0632× (z -9.6) |
| [[LoVo (line)]] | wt | 3.18 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0776× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 2.92 | 0 | 1 | — | [[Relugolix (drug)]] 0.5 µM 0.0506× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 1.90 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 0.05 µM 0.0682× (z -9.0) |
| [[PANC-1 (line)]] | alt | 2.91 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.104× (z -9.3) |
| [[SW480 (line)]] | alt | 3.01 | 0 | 1 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM 0.0541× (z -12.3) |
| [[A-172 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14222), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTLC1]] | +0.72 | +0.55 / +0.78 | both halves | 1e-05 |  |
| [[LENG8]] | +0.72 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[CERS2]] | +0.72 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[U2AF2]] | +0.71 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[IL18BP]] | +0.71 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[GTF3C2-AS2]] | +0.69 | +0.41 / +0.71 | both halves | 4e-05 |  |
| [[MFN2]] | +0.69 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[HCFC1]] | +0.69 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[AKT2]] | +0.68 | +0.57 / +0.74 | both halves | 1e-05 |  |
| [[ERVK13-1]] | +0.67 | +0.27 / +0.68 | both halves | 3e-04 |  |
| [[NCSTN]] | +0.66 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[EIF3F]] | +0.66 | +0.36 / +0.71 | both halves | 9e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PITPNA-AS1]] | -0.68 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[HPF1]] | -0.67 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[BTG1]] | -0.64 | -0.43 / -0.64 | both halves | 3e-05 |  |
| [[SNAPIN]] | -0.63 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[KRTCAP2]] | -0.63 | -0.28 / -0.64 | both halves | 3e-04 |  |
| [[SUMO4]] | -0.62 | -0.41 / -0.70 | both halves | 4e-05 |  |
| [[ATP5PO]] ⚠ | -0.62 | -0.43 / -0.57 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TTBK2]] | -0.61 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[ISCA2]] | -0.61 | -0.24 / -0.67 | both halves | 5e-04 |  |
| [[CTR9]] | -0.61 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[MARCKS]] | -0.60 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[MTLN]] ⚠ | -0.60 | -0.35 / -0.57 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[PIGBOS1]] | -0.60 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[TCAF1]] | -0.60 | -0.44 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRMD4B]] | B | FRMD4B activity lowers LY6G5B's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 1.20× higher at baseline in the lines without FRMD4B | 0.063 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.786). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.5, -25.1); signed map (-16.7, -32.9). **Vector** length 52.8, 6.61% of its response variance represented; |z| ≥ 3 in 1,056 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +10.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +0.9 | +2.3 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +0.9 | +0.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.8 | -5.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -1.0 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | lymphocyte antigen 6 family member G5B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,669,976-31,673,776 (+) |
| Ensembl biotype | protein_coding |
| Also known as | G5b; previously C6orf19 |
| Gene groups (HGNC) | LY6/PLAUR domain containing |
| Matched by | ensembl_id |

UniProt [Q8NDX9](https://www.uniprot.org/uniprotkb/Q8NDX9) carries no function annotation.

**Summary**, from NCBI Gene [58496](https://www.ncbi.nlm.nih.gov/gene/58496):

> LY6G5B belongs to a cluster of leukocyte antigen-6 (LY6) genes located in the major histocompatibility complex (MHC) class III region on chromosome 6. Members of the LY6 superfamily typically contain 70 to 80 amino acids, including 8 to 10 cysteines. Most LY6 proteins are attached to the cell surface by a glycosylphosphatidylinositol (GPI) anchor that is directly involved in signal transduction (Mallya et al., 2002 [PubMed 12079290]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:13931](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13931) · Entrez [58496](https://www.ncbi.nlm.nih.gov/gene/58496) · UniProt [Q8NDX9](https://www.uniprot.org/uniprotkb/Q8NDX9) · Ensembl [ENSG00000240053](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240053)

## Data

Gene col 14222: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14222); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14222, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14222]; `tensor/DDL_lfc|DDL_z.npy` [14222]; `embed/gene_vectors.npy` [14222]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14222 or target_col == 14222). Every well: [[LY6G5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LY6G5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
