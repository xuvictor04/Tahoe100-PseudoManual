---
symbol: "TPGS1"
type: "gene"
col: 6580
ensembl_id: "ENSG00000141933"
name: "tubulin polyglutamylase complex subunit 1"
location: "19p13.3"
module: 7
arm: "+"
pooled_cpm: 4.67
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 8
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# TPGS1

*tubulin polyglutamylase complex subunit 1* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.58× (z +5.3, q 6e-05, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.49× (z +3.4, q 0.090, up in 2 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.563× (z -6.9, q 4e-09, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FIZ1]] (+0.68, fdr 7e-06), [[KMT2B]] (+0.62, fdr 8e-06), [[ZBTB45]] (+0.61, fdr 3e-05); moves opposite to [[PPAT]] (-0.47, fdr 1e-04), [[GPR160]] (-0.47, fdr 4e-05), [[CALM2]] (-0.47, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6580.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +5.3 | 6e-05 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +5.0 | 2e-04 | 9/28 (RPMI-7951, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +4.2 | 0.006 | 6/15 (SW1417, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.49×** | +3.4 | 0.090 | 2/29 (Panc 03.27, J82) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.45× | +3.2 | 0.13 | 2/42 (NCI-H1792, hTERT-HPNE) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (drug)]] 0.05 µM |  | 1.33× | +3.2 | 0.13 | 4/36 (NCI-H2030, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6580.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.563×** | -6.9 | 4e-09 | 26/46 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.659×** | -5.0 | 2e-04 | 14/47 (A-427, C-33 A, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.712×** | -4.1 | 0.009 | 14/46 (J82, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.743×** | -3.5 | 0.044 | 13/45 (SW1417, NCI-H460, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.744×** | -3.5 | 0.044 | 14/44 (SK-MEL-2, HT-29, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.746×** | -3.5 | 0.044 | 17/47 (NCI-H1792, PANC-1, …) | inconsistent across doses | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.596×** | -3.2 | 0.097 | 3/42 (LS 180, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.764×** | -3.2 | 0.097 | 13/43 (SNU-423, CFPAC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6580. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 3.77 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0892× (z -9.0) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0906× (z -8.9) |
| [[A549 (line)]] | wt | 4.61 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[NCI-H1573 (line)]] | alt | 4.34 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0914× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 6.15 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.104× (z -9.6) |
| [[SW 900 (line)]] | alt | 4.21 | 0 | 1 | — | [[Mebendazole (drug)]] 0.05 µM 0.0559× (z -8.9) |
| [[A-172 (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6580), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FIZ1]] | +0.68 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[KMT2B]] | +0.62 | +0.58 / +0.63 | both halves | 8e-06 |  |
| [[ZBTB45]] | +0.61 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[TSSC4]] | +0.59 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[LRRC14]] | +0.58 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[PRCC]] | +0.58 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[RBM15B]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[FEM1A]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[WDR6]] | +0.56 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[L3MBTL2]] | +0.56 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ZNF3]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[DPH1]] | +0.56 | +0.54 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPAT]] | -0.47 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[GPR160]] | -0.47 | -0.41 / -0.40 | both halves | 4e-05 |  |
| [[CALM2]] | -0.47 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[DCP2]] | -0.47 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises TPGS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.516). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-39.3, 10.5); signed map (-5.9, -26.9). **Vector** length 39.2, 3.60% of its response variance represented; |z| ≥ 3 in 908 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.4 | +1.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +0.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.8 | +5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.2 | +0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.2 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | -0.1 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | -3.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.3 | -6.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -3.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -2.1 |
|  | [[vincristine (drug)]] 0.05 µM |  | -1.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | tubulin polyglutamylase complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:507,497-519,654 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GTRGEO22, PGs1; previously C19orf20 |
| Gene groups (HGNC) | Tubulin polyglutamylase complex subunits; Centriolar satellite proteins |
| Reactome | 1 pathways, smallest: Carboxyterminal post-translational modifications of tubulin |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZTW0](https://www.uniprot.org/uniprotkb/Q6ZTW0) (Tubulin polyglutamylase complex subunit 1):

> Subunit of the tubulin polyglutamylase complex (TPGC). The complex mediates cilia and flagella polyglutamylation which is essential for their biogenesis and motility (Probable). May act in the targeting of the tubulin polyglutamylase complex. Required for the development of the spermatid flagellum (By similarity).

**Summary**, from NCBI Gene [91978](https://www.ncbi.nlm.nih.gov/gene/91978):

> Predicted to enable microtubule binding activity and tubulin-glutamic acid ligase activity. Predicted to be involved in sperm axoneme assembly. Predicted to act upstream of or within several processes, including adult behavior; chemical synaptic transmission; and protein polyglutamylation. Located in centrosome. [provided by Alliance of Genome Resources, Apr 2025]

**Accessions** — [HGNC:25058](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25058) · Entrez [91978](https://www.ncbi.nlm.nih.gov/gene/91978) · UniProt [Q6ZTW0](https://www.uniprot.org/uniprotkb/Q6ZTW0) · Ensembl [ENSG00000141933](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141933)

## Data

Gene col 6580: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6580); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6580, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6580]; `tensor/DDL_lfc|DDL_z.npy` [6580]; `embed/gene_vectors.npy` [6580]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6580 or target_col == 6580). Every well: [[TPGS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPGS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
