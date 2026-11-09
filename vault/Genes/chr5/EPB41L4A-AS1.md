---
symbol: "EPB41L4A-AS1"
type: "gene"
col: 13374
ensembl_id: "ENSG00000224032"
name: "EPB41L4A antisense RNA 1"
location: "5q22.1"
module: 20
arm: "-"
pooled_cpm: 22.63
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# EPB41L4A-AS1

*EPB41L4A antisense RNA 1* — 5q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.11× (z +4.9, q 7e-04, up in 38 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.101×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNHG7]] (+0.92, fdr 7e-06), [[SNHG32]] (+0.88, fdr 7e-06), [[SNHG6]] (+0.87, fdr 7e-06); moves opposite to [[GPAA1]] (-0.71, fdr 7e-06), [[ACTR2]] (-0.69, fdr 7e-06), [[DR1]] (-0.68, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FSTL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13374.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.11×** | +4.9 | 7e-04 | 38/47 (H4, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.01×** | +4.3 | 0.005 | 38/47 (H4, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.83×** | +3.9 | 0.013 | 33/48 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +3.9 | 0.013 | 27/44 (NCI-H2030, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.03×** | +3.8 | 0.016 | 31/40 (SK-MEL-2, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +3.8 | 0.016 | 27/47 (NCI-H23, C32, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.56×** | +3.6 | 0.026 | 37/45 (SW480, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.69×** | +3.4 | 0.046 | 27/45 (Panc 03.27, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +3.2 | 0.097 | 23/46 (A-427, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.64× | +3.1 | 0.11 | 26/45 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13374.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.101×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.623× | -3.1 | 0.86 | 25/47 (PANC-1, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13374. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 18.9 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.101× (z -9.4) |
| [[A-172 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 58.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 29.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13374), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 21 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG7]] | +0.92 | +0.91 / +0.91 | both halves | 7e-06 | same gene group |
| [[SNHG32]] | +0.88 | +0.87 / +0.86 | both halves | 7e-06 | same gene group |
| [[SNHG6]] | +0.87 | +0.84 / +0.89 | both halves | 7e-06 | same gene group |
| [[SNHG8]] | +0.87 | +0.82 / +0.90 | both halves | 7e-06 | same gene group |
| [[SNHG12]] | +0.86 | +0.84 / +0.86 | both halves | 7e-06 | same gene group |
| [[NACA4P]] ⚠ | +0.83 | +0.71 / +0.86 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ZFAS1]] | +0.80 | +0.79 / +0.80 | both halves | 7e-06 | same gene group |
| [[TAF1D]] | +0.79 | +0.79 / +0.77 | both halves | 7e-06 |  |
| [[GAS5]] | +0.79 | +0.70 / +0.82 | both halves | 7e-06 | same gene group |
| [[NACA]] ⚠ | +0.79 | +0.64 / +0.81 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SMIM26]] ⚠ | +0.77 | +0.69 / +0.77 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[CAMLG]] | +0.76 | +0.60 / +0.84 | both halves | 7e-06 |  |
| [[ADPRM]] | +0.76 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[NOP53]] | +0.76 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[RPS27]] | +0.76 | +0.56 / +0.84 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPAA1]] | -0.71 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[ACTR2]] | -0.69 | -0.65 / -0.68 | both halves | 7e-06 |  |
| [[DR1]] | -0.68 | -0.49 / -0.74 | both halves | 1e-05 |  |
| [[TGOLN2]] | -0.67 | -0.65 / -0.70 | both halves | 7e-06 |  |
| [[EIF5A]] | -0.67 | -0.68 / -0.59 | both halves | 7e-06 |  |
| [[TARDBP]] | -0.67 | -0.50 / -0.69 | both halves | 1e-05 |  |
| [[VMA21]] | -0.66 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[CBX5]] | -0.66 | -0.47 / -0.70 | both halves | 2e-05 |  |
| [[TMX1]] | -0.66 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[POGLUT3]] | -0.66 | -0.52 / -0.72 | both halves | 1e-05 |  |
| [[BANF1]] | -0.65 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[MOB1A]] | -0.65 | -0.51 / -0.70 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSTL1]] | B | FSTL1 activity raises EPB41L4A-AS1's level | lines that do not express FSTL1 (21) vs lines expressing it (29) | 1.09× lower at baseline in the lines without FSTL1 | 0.075 | ⚠ within organs, on part of the lines; also absent: SLC8A1, ABI3BP, TFPI2 |
| [[PSMB5]] | B | PSMB5 activity lowers EPB41L4A-AS1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[BEX2]] | B | BEX2 activity raises EPB41L4A-AS1's level | lines that do not express BEX2 (18) vs lines expressing it (32) | 1.05× lower at baseline in the lines without BEX2 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000232386, BEX4, PAPLN |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.571). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.4, -28.5); signed map (-15.6, -2.4). **Vector** length 104, 36.0% of its response variance represented; |z| ≥ 3 in 477 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +5.0 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.9 | +4.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +3.4 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +3.6 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +3.0 | +2.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.7 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +3.9 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.8 | -0.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.7 | -3.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.6 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.6 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -2.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.6 | -1.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.5 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | EPB41L4A antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q22.1 — chr5:112,160,526-112,164,818 (+) |
| Ensembl biotype | lncRNA |
| Also known as | EAS1, TIGA1; previously C5orf26, NCRNA00219 |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes; Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [114915](https://www.ncbi.nlm.nih.gov/gene/114915):

> Predicted to be involved in RNA processing. Predicted to be located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30749](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30749) · Entrez [114915](https://www.ncbi.nlm.nih.gov/gene/114915) · Ensembl [ENSG00000224032](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224032)

## Data

Gene col 13374: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13374); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13374, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13374]; `tensor/DDL_lfc|DDL_z.npy` [13374]; `embed/gene_vectors.npy` [13374]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13374 or target_col == 13374). Every well: [[EPB41L4A-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPB41L4A-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
