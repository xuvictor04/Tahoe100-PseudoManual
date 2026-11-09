---
symbol: "C4orf48"
type: "gene"
col: 14360
ensembl_id: "ENSG00000243449"
name: "NELL2 interacting cell ontogeny regulator 1"
location: "4p16.3"
module: 48
arm: "+"
pooled_cpm: 7.16
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# C4orf48

*NELL2 interacting cell ontogeny regulator 1* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.18× (z +6.5, q 5e-08, up in 26 of 29 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.515× (z -4.1, q 0.027, down in 26 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (LoVo 0.137×); [[Roxadustat (drug)]] 5 µM in 1 line (A549 0.0489×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ROMO1]] (+0.84, fdr 7e-06), [[MICOS13]] (+0.82, fdr 7e-06), [[ATP5MJ]] (+0.80, fdr 7e-06); moves opposite to [[U2AF2]] (-0.70, fdr 5e-05), [[ZNF460]] (-0.69, fdr 1e-05), [[EIF4G2]] (-0.67, fdr 3e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC39A4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14360.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **4.18×** | +6.5 | 5e-08 | 26/29 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **3.23×** | +5.1 | 1e-04 | 11/13 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.96×** | +4.7 | 5e-04 | 29/33 (CFPAC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **2.70×** | +4.5 | 0.001 | 24/32 (A-172, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | 2.07× | +3.3 | 0.12 | 23/42 (LS 180, SW480, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | 2.08× | +3.1 | 0.21 | 13/20 (SNU-423, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Bendamustine (drug)]] 5 µM |  | 2.00× | +3.0 | 0.21 | 19/40 (A498, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14360.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (LoVo 0.137×); [[Roxadustat (drug)]] 5 µM in 1 line (A549 0.0489×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.515×** | -4.1 | 0.027 | 26/42 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | 0.263× | -3.2 | 0.31 | 25/47 (H4, SW48, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.501× | -3.1 | 0.31 | 22/40 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.69 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14360. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 5.52 | 0 | 1 | — | [[Roxadustat (drug)]] 5 µM 0.0489× (z -8.6) |
| [[LoVo (line)]] | wt | 8.92 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -9.1) |
| [[A-172 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14360), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 24 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ROMO1]] | +0.84 | +0.72 / +0.83 | both halves | 7e-06 |  |
| [[MICOS13]] | +0.82 | +0.64 / +0.82 | both halves | 7e-06 |  |
| [[ATP5MJ]] | +0.80 | +0.58 / +0.81 | both halves | 7e-06 |  |
| [[MRPL41]] ⚠ | +0.80 | +0.52 / +0.82 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[UQCR11]] | +0.80 | +0.68 / +0.80 | both halves | 7e-06 |  |
| [[ELOB]] | +0.80 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[ANAPC11]] | +0.79 | +0.59 / +0.80 | both halves | 7e-06 |  |
| [[POLR2J]] ⚠ | +0.79 | +0.51 / +0.79 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36AL]] ⚠ | +0.79 | +0.56 / +0.85 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MK]] | +0.78 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[MIEN1]] | +0.78 | +0.57 / +0.81 | both halves | 1e-05 |  |
| [[LAMTOR5]] | +0.78 | +0.50 / +0.81 | both halves | 1e-05 |  |
| [[PCSK1N]] | +0.78 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[TMEM256]] | +0.77 | +0.58 / +0.76 | both halves | 7e-06 |  |
| [[COX6A1]] | +0.77 | +0.66 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[U2AF2]] | -0.70 | -0.39 / -0.70 | both halves | 5e-05 |  |
| [[ZNF460]] | -0.69 | -0.52 / -0.67 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.67 | -0.46 / -0.62 | both halves | 3e-05 |  |
| [[SRSF1]] | -0.65 | -0.44 / -0.67 | both halves | 3e-05 |  |
| [[NRAS]] | -0.65 | -0.40 / -0.65 | both halves | 4e-05 |  |
| [[LIN7C]] | -0.65 | -0.44 / -0.74 | both halves | 3e-05 |  |
| [[DDX39B]] | -0.64 | -0.52 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC39A4]] | B | SLC39A4 activity lowers C4orf48's level | lines that do not express SLC39A4 (6) vs lines expressing it (44) | 1.52× higher at baseline in the lines without SLC39A4 | 0.023 | ⚠ within organs, on part of the lines; also absent: LRRC8B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.852). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-46.1, -19.4); signed map (-33.5, 7.9). **Vector** length 61.0, 15.5% of its response variance represented; |z| ≥ 3 in 469 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.66 to 31); *Respiratory electron transport* (reactome, mean cos +0.64 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.66 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | +2.7 | +3.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | -0.5 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.3 | +1.7 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.2 | +2.2 |
|  | [[Darolutamide (drug)]] 5 µM |  | +1.1 | +2.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | -3.3 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | -3.0 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -0.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -2.5 | +6.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -0.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | NELL2 interacting cell ontogeny regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:2,041,995-2,043,964 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NICOL; previously C4orf48 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5BLP8](https://www.uniprot.org/uniprotkb/Q5BLP8) (NELL2-interacting cell ontogeny regulator 1):

> mRNA-binding protein which interacts with a range of target mRNAs including SERPINE1, ACTA2, CCN2 and COL4A1 and may promote extracellular matrix production. Binds to the 3'-UTR of SERPINE1 mRNA and stabilizes the mRNA, possibly by competing for binding with SERBP1 and preventing SERBP1-mediated mRNA degradation. Also binds to the 3'-UTR of ACTA2. Testis-derived lumicrine factor that triggers epididymal differentiation and sperm maturation.

**Summary**, from NCBI Gene [401115](https://www.ncbi.nlm.nih.gov/gene/401115):

> Predicted to enable mRNA 3'-UTR binding activity. Predicted to be involved in 3'-UTR-mediated mRNA stabilization and spermatogenesis. Predicted to be located in perinuclear region of cytoplasm. Predicted to be active in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:34437](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34437) · Entrez [401115](https://www.ncbi.nlm.nih.gov/gene/401115) · UniProt [Q5BLP8](https://www.uniprot.org/uniprotkb/Q5BLP8) · Ensembl [ENSG00000243449](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243449)

## Data

Gene col 14360: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14360); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14360, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14360]; `tensor/DDL_lfc|DDL_z.npy` [14360]; `embed/gene_vectors.npy` [14360]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14360 or target_col == 14360). Every well: [[C4orf48 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C4orf48.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
