---
symbol: "TMEM256"
type: "gene"
col: 12987
ensembl_id: "ENSG00000205544"
name: "transmembrane protein 256"
location: "17p13.1"
module: 58
arm: "+"
pooled_cpm: 7.75
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 3
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# TMEM256

*transmembrane protein 256* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.92× (z +6.6, q 3e-08, up in 25 of 30 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.35× (z +5.4, q 1e-05, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.533× (z -5.6, q 1e-05, down in 30 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP5MJ]] (+0.83, fdr 7e-06), [[METTL26]] (+0.82, fdr 7e-06), [[ELOB]] (+0.80, fdr 7e-06); moves opposite to [[U2AF2]] (-0.70, fdr 1e-04), [[AVEN]] (-0.69, fdr 1e-05), [[EIF4G2]] (-0.68, fdr 1e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12987.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.92×** | +6.6 | 3e-08 | 25/30 (A549, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.76×** | +6.1 | 3e-07 | 14/17 (A549, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **2.37×** | +5.4 | 1e-05 | 30/36 (HOP62, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.35×** | +5.4 | 1e-05 | 38/47 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.10×** | +4.6 | 4e-04 | 33/47 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.08×** | +4.6 | 4e-04 | 29/47 (KATO III, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.43× | +3.2 | 0.11 | 17/47 (C32, SHP-77, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.65× | +3.1 | 0.12 | 12/47 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | 1.63× | +3.0 | 0.14 | 18/41 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | 1.69× | +3.0 | 0.14 | 13/21 (SNU-423, KATO III, …) | all doses, stronger at high dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12987.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.533×** | -5.6 | 1e-05 | 30/41 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.458×** | -4.9 | 3e-04 | 27/40 (KATO III, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.523×** | -3.8 | 0.025 | 26/44 (C32, HOP62, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.590× | -3.3 | 0.13 | 23/46 (AsPC-1, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 0.594× | -3.3 | 0.13 | 18/46 (SNU-423, AN3 CA, …) | top dose only | position effect removed |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.592× | -3.0 | 0.23 | 15/47 (AN3 CA, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12987. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 13.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.128× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 7.67 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -8.8) |
| [[A-172 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.23 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12987), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 8 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5MJ]] | +0.83 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[METTL26]] | +0.82 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[ELOB]] | +0.80 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[ANAPC11]] | +0.79 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[POLR2I]] | +0.77 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[C4orf48]] | +0.77 | +0.58 / +0.76 | both halves | 7e-06 |  |
| [[POLR2J]] ⚠ | +0.77 | +0.32 / +0.79 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[RBIS]] | +0.76 | +0.57 / +0.72 | both halves | 8e-06 |  |
| [[BBLN]] | +0.74 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[COX6A1]] | +0.74 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[MICOS13]] | +0.74 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[ARL3]] | +0.74 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.73 | +0.59 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[U2AF2]] | -0.70 | -0.33 / -0.66 | both halves | 1e-04 |  |
| [[AVEN]] | -0.69 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.68 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[PCBP1-AS1]] | -0.68 | -0.56 / -0.36 | both halves | 9e-05 |  |
| [[KRR1]] | -0.67 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[SRSF1]] | -0.66 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[ST7L]] | -0.65 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[ANKRD18A]] | -0.65 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[CRPPA]] | -0.65 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[ARSB]] | -0.65 | -0.51 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers TMEM256's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PITPNA-AS1]] | C | PITPNA-AS1's natural level strengthens TMEM256's drug response | PITPNA-AS1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.40; direction not clear | 0.060 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.815). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-46.4, -19.0); signed map (-33.5, 7.3). **Vector** length 69.2, 16.0% of its response variance represented; |z| ≥ 3 in 603 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cristae formation* (reactome, mean cos +0.56 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.7 | +5.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.4 | +4.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.4 | +4.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.8 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +0.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +1.6 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.1 | +1.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.1 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -0.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 256 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,402,975-7,404,097 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC40107; previously C17orf61 |
| Matched by | ensembl_id |

UniProt [Q8N2U0](https://www.uniprot.org/uniprotkb/Q8N2U0) carries no function annotation.

**Summary**, from NCBI Gene [254863](https://www.ncbi.nlm.nih.gov/gene/254863):

> Located in extracellular exosome and mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28618](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28618) · Entrez [254863](https://www.ncbi.nlm.nih.gov/gene/254863) · UniProt [Q8N2U0](https://www.uniprot.org/uniprotkb/Q8N2U0) · Ensembl [ENSG00000205544](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205544)

## Data

Gene col 12987: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12987); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12987, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12987]; `tensor/DDL_lfc|DDL_z.npy` [12987]; `embed/gene_vectors.npy` [12987]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12987 or target_col == 12987). Every well: [[TMEM256 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM256.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
