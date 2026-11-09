---
symbol: "SNX32"
type: "gene"
col: 10298
ensembl_id: "ENSG00000172803"
name: "sorting nexin 32"
location: "11q13.1"
module: 21
arm: "+"
pooled_cpm: 9.43
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# SNX32

*sorting nexin 32* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.70× (z +12.4, q 2e-32, up in 16 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.98× (z +9.5, q 3e-19, up in 35 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Larotrectinib (drug)]] 5 µM: 0.721× (z -4.5, q 0.003, down in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 900 0.128×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TICAM2-AS1]] (+0.68, fdr 3e-05), [[SYN3]] (+0.66, fdr 1e-05), [[SPATA21]] (+0.66, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[STAG3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10298.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.70×** | +12.4 | 2e-32 | 16/16 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.47×** | +12.2 | 7e-32 | 33/35 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.16×** | +10.4 | 3e-23 | 24/27 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +9.5 | 3e-19 | 35/44 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.91×** | +6.4 | 2e-08 | 29/45 (SW480, PANC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.86×** | +6.1 | 9e-08 | 28/43 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +5.0 | 6e-05 | 24/45 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.0 | 0.005 | 18/38 (CFPAC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.006 | 21/46 (HOP62, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.44×** | +3.6 | 0.019 | 19/48 (HS-578T, Panc 03.27, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.019 | 15/48 (Hs 766T, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.42×** | +3.4 | 0.027 | 17/48 (HS-578T, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.39×** | +3.2 | 0.057 | 13/46 (PANC-1, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10298.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 900 0.128×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Larotrectinib (drug)]] 5 µM |  | **0.721×** | -4.5 | 0.003 | 19/48 (C32, NCI-H23, …) | top dose only | position effect removed |
| [[Sulfisoxazole (drug)]] 5 µM |  | **0.725×** | -4.4 | 0.003 | 24/48 (C32, NCI-H23, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -3.3 | 0.20 | 11/48 (LS 180, A-172, …) | inconsistent across doses |  |
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | 0.793× | -3.2 | 0.20 | 12/48 (C32, hTERT-HPNE, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10298. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.77 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.22× (z +10.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 9.27 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.88× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[KATO III (line)]] | alt | 8.89 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.53× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[LS 180 (line)]] | wt | 8.30 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.73× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[PANC-1 (line)]] | alt | 9.91 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.33× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW 900 (line)]] | alt | 8.64 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.128× (z -8.6) |
| [[A-172 (line)]] | wt | 8.34 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.84 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10298), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TICAM2-AS1]] | +0.68 | +0.44 / +0.75 | both halves | 3e-05 |  |
| [[SYN3]] | +0.66 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[SPATA21]] | +0.66 | +0.56 / +0.77 | both halves | 1e-05 |  |
| [[CNTN5]] | +0.65 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[DCC]] | +0.65 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[SPTBN1-AS2]] | +0.65 | +0.45 / +0.72 | both halves | 3e-05 |  |
| [[BTNL12P]] | +0.65 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[FAM217A]] | +0.64 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[PTPRT]] | +0.63 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[CRLF1]] | +0.62 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[FLJ40194]] | +0.61 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[ABHD15-AS1]] | +0.61 | +0.41 / +0.72 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STAG3]] | B | STAG3 activity raises SNX32's level | lines that do not express STAG3 (14) vs lines expressing it (36) | 1.23× lower at baseline in the lines without STAG3 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000290931, ENSG00000283674; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.3, 29.7); signed map (35.1, 8.5). **Vector** length 49.6, 7.06% of its response variance represented; |z| ≥ 3 in 664 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +7.0 | +12.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +12.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +3.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +2.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | +1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -2.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -3.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -1.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.4 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 32 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,833,834-65,856,896 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30934; previously SNX6B |
| Gene groups (HGNC) | Sorting nexins; PX-BAR domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86XE0](https://www.uniprot.org/uniprotkb/Q86XE0) (Sorting nexin-32):

> Involved in endosomal trafficking of cargo proteins, including transferrin-bound transferrin receptor (TFRC), cation-independent mannose-6-phosphate receptor (IGF2R) and epidermal growth factor receptor (EGFR). Functions redundantly with other BAR domain-containing sorting nexins in endosome to trans-Golgi network transport of IGF2R. Regulates in coordination with SNX5 sorting and trafficking of EGF-activated EGFR to multivesicular bodies for lysosomal degradation. Plays an essential role in …

**Summary**, from NCBI Gene [254122](https://www.ncbi.nlm.nih.gov/gene/254122):

> Predicted to enable dynactin binding activity and phosphatidylinositol binding activity. Involved in endosome to lysosome transport via multivesicular body sorting pathway. Located in endosome; plasma membrane; and trans-Golgi network. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26423](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26423) · Entrez [254122](https://www.ncbi.nlm.nih.gov/gene/254122) · UniProt [Q86XE0](https://www.uniprot.org/uniprotkb/Q86XE0) · Ensembl [ENSG00000172803](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172803)

## Data

Gene col 10298: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10298); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10298, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10298]; `tensor/DDL_lfc|DDL_z.npy` [10298]; `embed/gene_vectors.npy` [10298]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10298 or target_col == 10298). Every well: [[SNX32 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX32.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
