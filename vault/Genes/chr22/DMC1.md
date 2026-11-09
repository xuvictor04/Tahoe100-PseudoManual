---
symbol: "DMC1"
type: "gene"
col: 1888
ensembl_id: "ENSG00000100206"
name: "DNA meiotic recombinase 1"
location: "22q13.1"
module: 71
arm: "+"
pooled_cpm: 2.08
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# DMC1

*DNA meiotic recombinase 1* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.64× (z +15.4, q 0e+00, up in 20 of 21 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0337×; ⚠ cell-cycle shift, explains ~82% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TLCD3B]] (+0.77, fdr 7e-06), [[GPR19]] (+0.76, fdr 7e-06), [[BRME1]] (+0.72, fdr 7e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 12 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1888.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.64×** | +15.4 | 0e+00 | 20/21 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.50×** | +12.2 | 1e-31 | 3/3 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.92×** | +11.5 | 3e-28 | 8/9 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.41×** | +9.5 | 2e-19 | 2/3 (NCI-H2347, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.96×** | +5.4 | 6e-06 | 9/21 (NCI-H2030, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.89×** | +5.2 | 2e-05 | 5/11 (A-427, NCI-H2347, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +4.1 | 0.003 | 1/8 (SK-MEL-2) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +4.1 | 0.003 | 6/27 (C32, LoVo, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.65×** | +4.0 | 0.004 | 2/17 (NCI-H1573, NCI-H2347) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.47×** | +4.0 | 0.004 | 1/5 (PANC-1) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.53×** | +3.4 | 0.032 | 4/24 (HOP62, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.46×** | +3.2 | 0.072 | 1/17 (NCI-H2347) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.46×** | +3.1 | 0.072 | 5/41 (A498, NCI-H1792, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +3.1 | 0.080 | 0/5 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0337×; ⚠ cell-cycle shift, explains ~82% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1888. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 3.55 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.05 µM 0.0337× (z -11.0) ⚠ cell-cycle shift, explains ~82% of this change |
| [[A-172 (line)]] | wt | 0.862 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.702 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.756 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.770 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.791 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.586 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.607 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.594 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.586 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.812 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.761 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.766 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.712 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.656 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.874 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1888), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLCD3B]] | +0.77 | +0.73 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[GPR19]] | +0.76 | +0.70 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[BRME1]] | +0.72 | +0.66 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[E2F2]] | +0.69 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[C21orf58]] | +0.67 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[E2F1]] | +0.66 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[FAM111B]] | +0.66 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[CHAF1A]] | +0.65 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[SMC1B]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 | pathway: Meiosis; STRING 496 |
| [[FBXO43]] | +0.65 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[CENPH]] | +0.65 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[ATAD5]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DMC1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | DMC1's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | DMC1's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.59 | 0.483 over the table, 0.078 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.626). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.4, -47.1); signed map (-40.8, -46.8). **Vector** length 34.5, 3.86% of its response variance represented; |z| ≥ 3 in 821 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +15.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +3.8 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +9.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +2.2 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | +1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +0.9 | +1.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +0.8 | +1.8 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -1.3 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.0 | -0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | DNA meiotic recombinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:38,518,948-38,570,204 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LIM15 |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 4 pathways, smallest: Meiotic recombination; Meiosis; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14565](https://www.uniprot.org/uniprotkb/Q14565) (Meiotic recombination protein DMC1 homolog):

> Homologous DNA recombinase that catalyzes strand exchange during meiotic recombination. Specifically required for meiotic recombination, facilitating the search and repair of DNA using the homolog rather than the sister chromatid, and can tolerate mismatches in heteroduplex DNA, unlike the higher-fidelity RAD51.

**Summary**, from NCBI Gene [11144](https://www.ncbi.nlm.nih.gov/gene/11144):

> This gene encodes a member of the superfamily of recombinases (also called DNA strand-exchange proteins). Recombinases are important for repairing double-strand DNA breaks during mitosis and meiosis. This protein, which is evolutionarily conserved, is reported to be essential for meiotic homologous recombination and may thus play an important role in generating diversity of genetic information. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2013]

**Accessions** — [HGNC:2927](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2927) · Entrez [11144](https://www.ncbi.nlm.nih.gov/gene/11144) · UniProt [Q14565](https://www.uniprot.org/uniprotkb/Q14565) · Ensembl [ENSG00000100206](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100206)

## Data

Gene col 1888: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1888); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1888, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1888]; `tensor/DDL_lfc|DDL_z.npy` [1888]; `embed/gene_vectors.npy` [1888]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1888 or target_col == 1888). Every well: [[DMC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DMC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
