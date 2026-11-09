---
symbol: "MYO1F"
type: "gene"
col: 6618
ensembl_id: "ENSG00000142347"
name: "myosin IF"
location: "19p13.2"
module: 21
arm: "+"
pooled_cpm: 2.16
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# MYO1F

*myosin IF* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.13× (z +12.6, q 1e-33, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.81× (z +8.0, q 3e-13, up in 20 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.577× (z -5.3, q 8e-05, down in 14 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CELF5]] (+0.72, fdr 7e-06), [[SLC26A5]] (+0.65, fdr 1e-05), [[CDH23]] (+0.65, fdr 5e-05); moves opposite to [[ARMC1]] (-0.51, fdr 5e-05), [[GLOD4]] (-0.50, fdr 1e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SSPOP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6618.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.13×** | +12.6 | 1e-33 | 1/3 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.78×** | +9.7 | 7e-20 | 12/13 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +8.0 | 3e-13 | 20/44 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +6.8 | 2e-09 | 8/30 (HEC-1-A, PANC-1, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.43×** | +6.5 | 9e-09 | 1/6 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +4.4 | 1e-03 | 16/36 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.9 | 0.009 | 2/18 (A498, NCI-H23) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +3.8 | 0.009 | 7/45 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.072 | 4/29 (J82, NCI-H460, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.100 | 0/22 | inconsistent across doses | position effect removed |
| [[Orlistat (drug)]] 0.05 µM |  | **1.53×** | +3.1 | 0.100 | 2/23 (NCI-H23, SK-MEL-2) | inconsistent across doses | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.85× | +3.0 | 0.11 | 1/3 (A498) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.40× | +3.0 | 0.11 | 1/29 (NCI-H460) | top dose only | cell-cycle shift (explains ~15% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6618.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.577×** | -5.3 | 8e-05 | 14/42 (BT-474, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.907× | -3.6 | 0.084 | 13/45 (A-427, RKO, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.701×** | -3.4 | 0.100 | 12/45 (COLO 205, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.703×** | -3.4 | 0.100 | 12/42 (A-172, SW480, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | 0.729× | -3.0 | 0.27 | 2/39 (NCI-H460, NCI-H1573) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6618. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 2.62 | 0 | 1 | — | [[Zileuton (drug)]] 0.05 µM 0.0767× (z -8.7) |
| [[A-172 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.50 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6618), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CELF5]] | +0.72 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[SLC26A5]] | +0.65 | +0.49 / +0.74 | both halves | 1e-05 |  |
| [[CDH23]] | +0.65 | +0.40 / +0.78 | both halves | 5e-05 | STRING 713 |
| [[CRLF1]] | +0.63 | +0.46 / +0.70 | both halves | 2e-05 |  |
| [[PPM1N]] | +0.63 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[MEI1]] | +0.62 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[IL3RA]] | +0.62 | +0.46 / +0.70 | both halves | 3e-05 |  |
| [[ETFBKMT]] | +0.61 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[AKAP13-AS1]] | +0.59 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[EFHD1]] | +0.59 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[TMPRSS9]] | +0.58 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[OMG]] | +0.58 | +0.46 / +0.59 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC1]] | -0.51 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[GLOD4]] | -0.50 | -0.34 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SSPOP]] | B | SSPOP activity raises MYO1F's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 1.24× lower at baseline in the lines without SSPOP | 0.032 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |
| [[RHBDL3]] | B | RHBDL3 activity raises MYO1F's level | lines that do not express RHBDL3 (9) vs lines expressing it (41) | 1.30× lower at baseline in the lines without RHBDL3 | 0.093 | ⚠ within organs, on part of the lines; also absent: PRDM6, DZIP1L, CACNB4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.581). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.5, 32.5); signed map (27.5, 19.3). **Vector** length 35.6, 3.34% of its response variance represented; |z| ≥ 3 in 862 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +9.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +1.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.0 | +1.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.0 | +2.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -1.9 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.4 | -5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.2 | -3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.1 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -0.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | myosin IF |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:8,520,778-8,577,442 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Myosin heavy chains, class I; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O00160](https://www.uniprot.org/uniprotkb/O00160) (Unconventional myosin-If):

> Molecular adapter required for the movement of immune cells, such as mast cells, neutrophils and T-cells, to sites of inflammation or infection (By similarity). Acts as a regulator of antifungal immunity in macrophages by acting as a molecular adapter between ATAT1 and alpha-tubulin, promoting alpha-tubulin acetylation and antifungal immune response. Also acts as a positive regulator of cGAS-STING signaling by promoting plasma membrane localization of CGAS: following phosphorylation by SYK, …

**Summary**, from NCBI Gene [4542](https://www.ncbi.nlm.nih.gov/gene/4542):

> Myosins are molecular motors that use the energy from ATP hydrolysis to generate force on actin filaments. The protein encoded by this gene is an unconventional myosin that may be involved in the intracellular movement of membrane-enclosed compartments. There is evidence to suggest that mutations in this gene can result in hearing loss. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:7600](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7600) · Entrez [4542](https://www.ncbi.nlm.nih.gov/gene/4542) · UniProt [O00160](https://www.uniprot.org/uniprotkb/O00160) · Ensembl [ENSG00000142347](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142347)

## Data

Gene col 6618: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6618); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6618, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6618]; `tensor/DDL_lfc|DDL_z.npy` [6618]; `embed/gene_vectors.npy` [6618]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6618 or target_col == 6618). Every well: [[MYO1F — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYO1F.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
