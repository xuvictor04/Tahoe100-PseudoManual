---
symbol: "DEPDC4"
type: "gene"
col: 9247
ensembl_id: "ENSG00000166153"
name: "DEP domain containing 4"
location: "12q23.1"
module: 21
arm: "+"
pooled_cpm: 5.31
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# DEPDC4

*DEP domain containing 4* — 12q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.98× (z +23.0, q 0e+00, up in 39 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.586× (z -6.3, q 2e-07, down in 18 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALG1L9P]] (+0.68, fdr 1e-05), [[RAD9B]] (+0.68, fdr 1e-05), [[LINC02608]] (+0.67, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9247.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.98×** | +23.0 | 0e+00 | 39/39 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.55×** | +11.0 | 8e-26 | 21/25 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.60×** | +10.8 | 6e-25 | 7/8 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.94×** | +7.8 | 6e-13 | 25/45 (LoVo, SHP-77, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.05×** | +7.8 | 6e-13 | 8/13 (HT-29, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.78×** | +6.5 | 6e-09 | 19/37 (SW480, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.65×** | +5.7 | 1e-06 | 16/40 (SW480, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +4.1 | 0.003 | 10/46 (LoVo, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.40×** | +4.0 | 0.004 | 9/46 (LoVo, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.35×** | +3.5 | 0.023 | 8/47 (BT-474, A498, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.060 | 9/44 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.30×** | +3.1 | 0.089 | 3/26 (NCI-H2030, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.20× | +3.0 | 0.11 | 4/47 (PANC-1, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9247.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.586×** | -6.3 | 2e-07 | 18/45 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.708×** | -4.1 | 0.010 | 15/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.709×** | -4.0 | 0.010 | 10/44 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.812×** | -3.5 | 0.079 | 14/46 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Asciminib (drug)]] 0.05 µM |  | 0.759× | -3.2 | 0.13 | 9/45 (NCI-H1792, NCI-H2030, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.767× | -3.1 | 0.18 | 9/46 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9247. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.46 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.34× (z +8.7) | [[Cyclosporin A (drug)]] 0.05 µM 0.0474× (z -10.1) |
| [[PANC-1 (line)]] | alt | 9.41 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 5.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +9.1) | — |
| [[A549 (line)]] | wt | 4.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.38× (z +9.0) | — |
| [[AsPC-1 (line)]] | alt | 2.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 4.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.87× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 11.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.49× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 4.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.97× (z +9.9) | — |
| [[LoVo (line)]] | wt | 6.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +9.5) | — |
| [[NCI-H460 (line)]] | wt | 4.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.44× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 5.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.61× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 3.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.29× (z +8.6) | — |
| [[SW480 (line)]] | alt | 7.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +10.8) | — |
| [[A-427 (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9247), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG1L9P]] | +0.68 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[RAD9B]] | +0.68 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[LINC02608]] | +0.67 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[LMNB1-DT]] | +0.66 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[LANCL1-AS1]] | +0.66 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[DNAJC9-AS1-1]] | +0.65 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[C2CD5-AS1]] | +0.65 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[PPP1R15B-AS1]] | +0.64 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[HRG-AS1]] | +0.64 | +0.37 / +0.64 | both halves | 8e-05 |  |
| [[SPATA1]] | +0.63 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[SPEN-AS1]] | +0.63 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[CCNO-DT]] | +0.63 | +0.37 / +0.65 | both halves | 9e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DEPDC4's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.1, 23.9); signed map (31.1, 2.0). **Vector** length 53.7, 6.95% of its response variance represented; |z| ≥ 3 in 929 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +23.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +11.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.7 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +4.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.3 | +3.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -6.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.4 | -2.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.2 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | +2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | DEP domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.1 — chr12:100,203,669-100,267,079 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DEP.4, FLJ33505 |
| Gene groups (HGNC) | DEP domain containing |
| Matched by | ensembl_id |

UniProt [Q8N2C3](https://www.uniprot.org/uniprotkb/Q8N2C3) carries no function annotation.

**Summary**, from NCBI Gene [120863](https://www.ncbi.nlm.nih.gov/gene/120863):

> Predicted to be involved in intracellular signal transduction. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22952](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22952) · Entrez [120863](https://www.ncbi.nlm.nih.gov/gene/120863) · UniProt [Q8N2C3](https://www.uniprot.org/uniprotkb/Q8N2C3) · Ensembl [ENSG00000166153](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166153)

## Data

Gene col 9247: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9247); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9247, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9247]; `tensor/DDL_lfc|DDL_z.npy` [9247]; `embed/gene_vectors.npy` [9247]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9247 or target_col == 9247). Every well: [[DEPDC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DEPDC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
