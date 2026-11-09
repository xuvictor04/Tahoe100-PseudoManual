---
symbol: "TSPEAR"
type: "gene"
col: 10661
ensembl_id: "ENSG00000175894"
name: "thrombospondin type laminin G domain and EAR repeats"
location: "21q22.3"
module: 90
arm: "+"
pooled_cpm: 2.32
n_lines_expressing: 45
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# TSPEAR

*thrombospondin type laminin G domain and EAR repeats* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.79× (z +15.8, q 0e+00, up in 16 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.580× (z -4.6, q 0.003, down in 9 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.05 µM in 1 line (SW480 0.0380×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.240×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00298]] (+0.71, fdr 7e-06), [[NCALD]] (+0.71, fdr 7e-06), [[CES3]] (+0.69, fdr 7e-06).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC01814]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10661.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.79×** | +15.8 | 0e+00 | 16/21 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.70×** | +11.8 | 1e-29 | 14/24 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.91×** | +9.8 | 1e-20 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.92×** | +9.0 | 3e-17 | 27/40 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.87×** | +8.8 | 1e-16 | 21/36 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.06×** | +8.7 | 4e-16 | 1/2 (SW48) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.47×** | +7.6 | 3e-12 | 1/7 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.19×** | +6.6 | 4e-09 | 11/25 (HEC-1-A, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.67×** | +6.1 | 7e-08 | 5/36 (SW48, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +6.0 | 8e-08 | 13/35 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.93×** | +5.5 | 2e-06 | 6/28 (SW48, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.85×** | +5.2 | 1e-05 | 7/35 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.76×** | +4.7 | 1e-04 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +4.3 | 8e-04 | 4/21 (SW48, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.96×** | +4.0 | 0.002 | 1/7 (SHP-77) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.51×** | +3.4 | 0.019 | 4/25 (SW480, HCT15, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +3.4 | 0.019 | 1/21 (LoVo) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.57×** | +3.2 | 0.035 | 3/18 (SW480, HCT15, …) | rises with dose | position effect removed |
| [[Arbutin (drug)]] 0.5 µM |  | **1.45×** | +3.1 | 0.050 | 0/34 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10661.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.05 µM in 1 line (SW480 0.0380×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.240×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.580×** | -4.6 | 0.003 | 9/23 (SW480, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10661. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 41.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -9.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 2.94 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0380× (z -11.7) |
| [[A-172 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.797 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.579 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.924 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.968 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.683 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.684 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.623 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.829 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.892 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.705 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.754 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.779 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.703 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.629 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.553 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.684 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.934 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.666 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.620 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.900 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.729 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.863 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.988 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.643 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.658 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10661), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00298]] | +0.71 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[NCALD]] | +0.71 | +0.68 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[CES3]] | +0.69 | +0.79 / +0.60 | both halves | 7e-06 |  |
| [[LINC02694]] | +0.68 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[MIR325HG]] | +0.66 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[LINC02223]] | +0.64 | +0.64 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[GRM7]] | +0.64 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[LINC01811]] | +0.63 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[LINC02208]] | +0.63 | +0.59 / +0.75 | both halves | 7e-06 |  |
| [[PKHD1]] | +0.63 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[SLC7A8]] | +0.63 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[DIP2C-AS1]] | +0.62 | +0.63 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01814]] | B | LINC01814 activity raises TSPEAR's level | lines that do not express LINC01814 (30) vs lines expressing it (20) | 2.03× lower at baseline in the lines without LINC01814 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC00299, TMEM45B, EPS8L3 |
| [[PHYHIPL]] | B | PHYHIPL activity raises TSPEAR's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 1.68× lower at baseline in the lines without PHYHIPL | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.702). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.5, 38.5); signed map (35.7, 17.0). **Vector** length 38.4, 4.87% of its response variance represented; |z| ≥ 3 in 899 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +11.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +15.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +6.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +3.2 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -0.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.1 | -1.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -0.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | thrombospondin type laminin G domain and EAR repeats |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:44,497,893-44,711,572 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC11251, TSP-EAR; previously C21orf29, DFNB98 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WU66](https://www.uniprot.org/uniprotkb/Q8WU66) (Thrombospondin-type laminin G domain and EAR repeat-containing protein):

> Plays a critical role in tooth and hair follicle morphogenesis through regulation of the Notch signaling pathway. May play a role in development or function of the auditory system.

**Summary**, from NCBI Gene [54084](https://www.ncbi.nlm.nih.gov/gene/54084):

> This gene encodes a protein that contains a N-terminal thrombospondin-type laminin G domain and several tandem arranged epilepsy-associated repeats (EARs). A mutation in this gene is the cause of autosomal recessive deafness-98. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:1268](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1268) · Entrez [54084](https://www.ncbi.nlm.nih.gov/gene/54084) · UniProt [Q8WU66](https://www.uniprot.org/uniprotkb/Q8WU66) · Ensembl [ENSG00000175894](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175894)

## Data

Gene col 10661: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10661); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10661, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10661]; `tensor/DDL_lfc|DDL_z.npy` [10661]; `embed/gene_vectors.npy` [10661]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10661 or target_col == 10661). Every well: [[TSPEAR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSPEAR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
