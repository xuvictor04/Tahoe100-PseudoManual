---
symbol: "SLC13A4"
type: "gene"
col: 8993
ensembl_id: "ENSG00000164707"
name: "solute carrier family 13 member 4"
location: "7q33"
module: 21
arm: "+"
pooled_cpm: 3.32
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# SLC13A4

*solute carrier family 13 member 4* — 7q33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.67× (z +12.4, q 1e-32, up in 6 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.11× (z +10.1, q 1e-21, up in 21 of 28 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Phenylephrine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H460 0.0510×); [[Valdecoxib (drug)]] 0.5 µM in 1 line (SW480 0.0662×); [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM in 1 line (PANC-1 0.0811×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[A2ML1-AS1]] (+0.79, fdr 7e-06), [[PKD2L2]] (+0.77, fdr 7e-06), [[SLC23A1]] (+0.77, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TP53TG5]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8993.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.67×** | +12.4 | 1e-32 | 6/8 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.57×** | +11.7 | 4e-29 | 1/2 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +10.1 | 1e-21 | 21/28 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.37×** | +7.3 | 6e-11 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +4.9 | 9e-05 | 8/25 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.58×** | +4.3 | 0.001 | 8/23 (LoVo, SW480, …) | inconsistent across doses | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.78×** | +3.9 | 0.007 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.9 | 0.008 | 6/31 (NCI-H460, KATO III, …) | top dose only | position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.8 | 0.008 | 4/24 (A498, HEC-1-A, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.7 | 0.012 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.013 | 7/33 (SW480, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.65×** | +3.4 | 0.030 | 0/29 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.95×** | +3.3 | 0.037 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.47×** | +3.2 | 0.051 | 3/20 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.056 | 1/15 (HOP62) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.077 | 3/36 (HT-29, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.079 | 3/28 (LoVo, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8993.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Phenylephrine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H460 0.0510×); [[Valdecoxib (drug)]] 0.5 µM in 1 line (SW480 0.0662×); [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM in 1 line (PANC-1 0.0811×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.858× | -5.0 | 4e-04 | 17/46 (MIA PaCa-2, SNU-423, …) | inconsistent across doses |  |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.704× | -3.4 | 0.17 | 6/42 (HCT15, LS 180, …) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.674× | -3.3 | 0.17 | 2/43 (AsPC-1, HOP62) | inconsistent across doses |  |
| [[Clopidogrel (drug)]] 0.5 µM |  | 0.721× | -3.1 | 0.25 | 12/42 (SW1417, NCI-H460, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.699× | -3.0 | 0.26 | 4/43 (Panc 03.27, HCT15, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8993. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1.68 | 0 | 1 | — | [[Phenylephrine (hydrochloride) (drug)]] 0.05 µM 0.0510× (z -10.3) |
| [[PANC-1 (line)]] | alt | 1.43 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM 0.0811× (z -9.0) |
| [[SW480 (line)]] | alt | 1.66 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0662× (z -9.7) |
| [[A-172 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 71.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8993), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[A2ML1-AS1]] | +0.79 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[PKD2L2]] | +0.77 | +0.67 / +0.78 | both halves | 7e-06 |  |
| [[SLC23A1]] | +0.77 | +0.53 / +0.83 | both halves | 1e-05 |  |
| [[ZRANB2-AS1]] | +0.77 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[TOMM20L-DT]] | +0.76 | +0.53 / +0.78 | both halves | 1e-05 |  |
| [[ST7-AS2]] | +0.76 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[SPATC1]] | +0.75 | +0.58 / +0.75 | both halves | 8e-06 |  |
| [[HRG-AS1]] | +0.75 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[RN7SL2]] | +0.75 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[CFAP20DC-AS1]] | +0.75 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[PP2D1]] | +0.75 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[USH2A]] | +0.75 | +0.49 / +0.71 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53TG5]] | C | TP53TG5's natural level weakens SLC13A4's drug response | TP53TG5's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.68, reverse -0.14; direction not clear | 0.031 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.827). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.0, 27.3); signed map (32.4, 6.7). **Vector** length 29.3, 2.14% of its response variance represented; |z| ≥ 3 in 1,051 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +12.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | +2.8 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -2.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.9 | -5.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 13 member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q33 — chr7:135,681,231-135,729,258 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SUT-1, SUT1 |
| Gene groups (HGNC) | Solute carrier family 13 |
| Reactome | 3 pathways, smallest: SLC-mediated transport of inorganic anions; SLC-mediated transmembrane transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKG4](https://www.uniprot.org/uniprotkb/Q9UKG4) (Solute carrier family 13 member 4):

> Sodium:sulfate symporter that mediates sulfate reabsorption in the high endothelial venules (HEV).

**Summary**, from NCBI Gene [26266](https://www.ncbi.nlm.nih.gov/gene/26266):

> Enables sodium:sulfate symporter activity. Predicted to be involved in transmembrane transport. Predicted to be located in membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15827](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15827) · Entrez [26266](https://www.ncbi.nlm.nih.gov/gene/26266) · UniProt [Q9UKG4](https://www.uniprot.org/uniprotkb/Q9UKG4) · Ensembl [ENSG00000164707](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164707)

## Data

Gene col 8993: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8993); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8993, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8993]; `tensor/DDL_lfc|DDL_z.npy` [8993]; `embed/gene_vectors.npy` [8993]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8993 or target_col == 8993). Every well: [[SLC13A4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC13A4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
