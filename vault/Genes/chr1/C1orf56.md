---
symbol: "C1orf56"
type: "gene"
col: 6746
ensembl_id: "ENSG00000143443"
name: "chromosome 1 open reading frame 56"
location: "1q21.3"
module: 21
arm: "+"
pooled_cpm: 4.04
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# C1orf56

*chromosome 1 open reading frame 56* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.67× (z +7.8, q 3e-12, up in 18 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.89× (z +7.2, q 1e-10, up in 32 of 38 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pentoxifylline (drug)]] 0.5 µM in 1 line (SW1417 0.0662×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTBP1-AS]] (+0.79, fdr 7e-06, ⚠ CTBP1-AS in the vector space only through flagged drug-doses), [[SMIM27]] (+0.78, fdr 7e-06), [[C2CD5-AS1]] (+0.78, fdr 7e-06), [[ST7-AS2]] (+0.78, fdr 7e-06); moves opposite to [[PRKDC]] (-0.63, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HES7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6746.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.67×** | +7.8 | 3e-12 | 18/22 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.73×** | +7.7 | 4e-12 | 4/6 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +7.2 | 1e-10 | 32/38 (A549, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +5.2 | 3e-05 | 6/9 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +4.5 | 6e-04 | 18/37 (SHP-77, A-427, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +4.2 | 0.003 | 11/34 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.5 | 0.034 | 10/31 (AsPC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +3.4 | 0.041 | 6/37 (NCI-H460, H4, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.4 | 0.044 | 9/27 (LoVo, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.50×** | +3.2 | 0.074 | 8/23 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6746.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pentoxifylline (drug)]] 0.5 µM in 1 line (SW1417 0.0662×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.857× | -4.2 | 0.012 | 20/48 (SNU-1, SW480, …) | inconsistent across doses |  |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | 0.750× | -3.2 | 0.36 | 8/47 (MIA PaCa-2, KATO III, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6746. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 4.16 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0662× (z -9.2) |
| [[A-172 (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6746), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTBP1-AS]] ⚠ | +0.79 | +0.71 / +0.86 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SMIM27]] | +0.78 | +0.64 / +0.79 | both halves | 7e-06 |  |
| [[C2CD5-AS1]] | +0.78 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[ST7-AS2]] | +0.78 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[EAF1-AS1]] | +0.77 | +0.73 / +0.80 | both halves | 7e-06 |  |
| [[A2ML1-AS1]] | +0.76 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[HSPA2-AS1]] | +0.75 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.75 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[SPATC1]] | +0.75 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[TFAP2A-AS1]] | +0.74 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[ZBTB20-AS5]] | +0.74 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[SLC23A1]] | +0.73 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[PAXBP1-AS1]] | +0.73 | +0.73 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKDC]] | -0.63 | -0.49 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HES7]] | B | HES7 activity raises C1orf56's level | lines that do not express HES7 (13) vs lines expressing it (37) | 1.12× lower at baseline in the lines without HES7 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, ACTN2, ENSG00000281091; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers C1orf56's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.798). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.6, 26.6); signed map (32.5, 6.3). **Vector** length 41.1, 4.62% of its response variance represented; |z| ≥ 3 in 745 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +7.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +4.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +7.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.3 | +1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +1.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -4.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -0.7 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.1 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -2.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.1 | -2.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 1 open reading frame 56 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:151,047,751-151,051,986 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20519, MENT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUN1](https://www.uniprot.org/uniprotkb/Q9BUN1) (Protein MENT):

> Involved in control of cellular proliferation. Onconcogenic modifier contributing to the tumor suppressor function of DNMT3B.

**Summary**, from NCBI Gene [54964](https://www.ncbi.nlm.nih.gov/gene/54964):

> This gene is a proto-oncogene whose promoter is methylated by DNA methyltransferase 3B (DNMT3B), which represses the proto-oncogene. However, a catalytically inactive isoform of DNMT3B is overexpressed in lymphomas, leading to hypomethylation of the proto-oncogene's promoter and derepression of the proto-oncogene. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:26045](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26045) · Entrez [54964](https://www.ncbi.nlm.nih.gov/gene/54964) · UniProt [Q9BUN1](https://www.uniprot.org/uniprotkb/Q9BUN1) · Ensembl [ENSG00000143443](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143443)

## Data

Gene col 6746: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6746); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6746, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6746]; `tensor/DDL_lfc|DDL_z.npy` [6746]; `embed/gene_vectors.npy` [6746]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6746 or target_col == 6746). Every well: [[C1orf56 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C1orf56.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
