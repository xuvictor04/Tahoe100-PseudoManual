---
symbol: "ZSCAN16"
type: "gene"
col: 12287
ensembl_id: "ENSG00000196812"
name: "zinc finger and SCAN domain containing 16"
location: "6p22.1"
module: 12
arm: "+"
pooled_cpm: 2.09
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# ZSCAN16

*zinc finger and SCAN domain containing 16* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.00× (z +9.6, q 4e-19, up in 39 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF205]] (+0.60, fdr 2e-05), [[ZSCAN26]] (+0.59, fdr 1e-05), [[CRB3]] (+0.58, fdr 4e-05); moves opposite to [[PTDSS1]] (-0.54, fdr 4e-05), [[MYO19]] (-0.52, fdr 4e-05), [[ELOVL6]] (-0.52, fdr 4e-04).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ELF3-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12287.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.00×** | +9.6 | 4e-19 | 39/44 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.87×** | +9.2 | 7e-18 | 31/40 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.09×** | +9.1 | 2e-17 | 14/30 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.33×** | +7.4 | 2e-11 | 22/40 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +6.5 | 1e-08 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.02×** | +6.2 | 7e-08 | 3/12 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.60×** | +5.8 | 4e-07 | 6/41 (CFPAC-1, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +5.2 | 1e-05 | 2/3 (PANC-1, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.9 | 6e-05 | 5/27 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.68×** | +4.5 | 3e-04 | 10/26 (NCI-H1792, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.69×** | +4.4 | 5e-04 | 7/38 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +4.3 | 6e-04 | 7/25 (LS 180, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +4.2 | 0.001 | 7/43 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.90×** | +4.0 | 0.002 | 3/13 (HT-29, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.011 | 5/41 (J82, NCI-H2030, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.76×** | +3.5 | 0.016 | 0/19 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.47×** | +3.3 | 0.028 | 4/23 (SW480, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12287. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.566 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.567 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.609 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.941 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.915 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.790 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.777 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.686 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.792 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.782 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.719 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12287), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF205]] | +0.60 | +0.46 / +0.59 | both halves | 2e-05 | same gene group |
| [[ZSCAN26]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 | same gene group |
| [[CRB3]] | +0.58 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[MED7]] | +0.54 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[ZNF19]] | +0.54 | +0.70 / +0.51 | both halves | 1e-05 | same gene group |
| [[ZNF212]] | +0.54 | +0.33 / +0.48 | both halves | 1e-04 | same gene group |
| [[NUDT14]] | +0.53 | +0.32 / +0.51 | both halves | 2e-04 |  |
| [[SNHG11]] | +0.53 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[ASB8]] | +0.53 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[ACBD4]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[TBC1D17]] | +0.53 | +0.25 / +0.52 | both halves | 4e-04 |  |
| [[C2orf68]] | +0.52 | +0.37 / +0.52 | both halves | 8e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTDSS1]] | -0.54 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[MYO19]] | -0.52 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[ELOVL6]] | -0.52 | -0.25 / -0.54 | both halves | 4e-04 |  |
| [[NETO2]] | -0.52 | -0.23 / -0.41 | both halves | 5e-04 |  |
| [[PRPS2]] | -0.51 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[EOGT]] | -0.50 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[TOP3A]] | -0.48 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[TXNDC5]] | -0.48 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[VDAC1]] | -0.48 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[TBXAS1]] | -0.47 | -0.25 / -0.49 | both halves | 4e-04 |  |
| [[GDI2]] | -0.47 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[SNX5]] | -0.47 | -0.08 / -0.53 | ⚠ one half (not replicated) | 0.003 |  |
| [[SLC16A1]] | -0.47 | -0.42 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises ZSCAN16's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 1.42× lower at baseline in the lines without ELF3-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.490). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-53.9, -3.9); signed map (-10.3, -3.2). **Vector** length 30.0, 2.52% of its response variance represented; |z| ≥ 3 in 928 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.0 | +2.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.6 | +5.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.4 | +9.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.3 | +9.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.1 | +1.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.0 | +2.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.0 | +1.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.0 | +1.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -2.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.1 | +4.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | +1.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | +2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.9 | -0.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.8 | -1.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -0.8 | -1.2 |
|  | [[EX229 (drug)]] 5 µM |  | -0.8 | -1.3 |
|  | [[EX229 (drug)]] 0.05 µM |  | -0.8 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and SCAN domain containing 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.1 — chr6:28,107,689-28,130,082 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22191, dJ265C24.3; previously ZNF392, ZNF435 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4T2](https://www.uniprot.org/uniprotkb/Q9H4T2) (Zinc finger and SCAN domain-containing protein 16):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [80345](https://www.ncbi.nlm.nih.gov/gene/80345):

> Enables sequence-specific double-stranded DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20813](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20813) · Entrez [80345](https://www.ncbi.nlm.nih.gov/gene/80345) · UniProt [Q9H4T2](https://www.uniprot.org/uniprotkb/Q9H4T2) · Ensembl [ENSG00000196812](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196812)

## Data

Gene col 12287: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12287); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12287, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12287]; `tensor/DDL_lfc|DDL_z.npy` [12287]; `embed/gene_vectors.npy` [12287]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12287 or target_col == 12287). Every well: [[ZSCAN16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSCAN16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
