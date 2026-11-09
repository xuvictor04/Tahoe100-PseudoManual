---
symbol: "MTLN"
type: "gene"
col: 10639
ensembl_id: "ENSG00000175701"
name: "mitoregulin"
location: "2q13"
module: 24
arm: "+"
pooled_cpm: 5.08
n_lines_expressing: 47
n_dd_up: 4
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/024", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# MTLN

*mitoregulin* — 2q13

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.49× (z +4.5, q 0.002, up in 6 of 10 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (HOP62 0.0397×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dihydroartemisinin (drug)]] 5 µM in 1 line (HS-578T 0.0470×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 0.131×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GADD45GIP1]] (+0.76, fdr 1e-05), [[POLR2I]] (+0.73, fdr 1e-05), [[MRPL57]] (+0.72, fdr 1e-05); moves opposite to [[MOB1A]] (-0.71, fdr 1e-05), [[HCFC1]] (-0.67, fdr 1e-05), [[CERS2]] (-0.65, fdr 4e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Carbamazepine (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10639.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.49×** | +4.5 | 0.002 | 6/10 (NCI-H1792, PANC-1, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **2.21×** | +4.5 | 0.002 | 17/26 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.29×** | +4.1 | 0.008 | 16/29 (CFPAC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **2.12×** | +3.6 | 0.048 | 13/25 (A549, CFPAC-1, …) | rises with dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10639.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (HOP62 0.0397×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dihydroartemisinin (drug)]] 5 µM in 1 line (HS-578T 0.0470×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 0.131×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.521× | -3.7 | 0.13 | 19/41 (RKO, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | 0.314× | -3.3 | 0.27 | 15/43 (SNU-1, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.571× | -3.2 | 0.30 | 17/41 (SW 900, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10639. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 2.39 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0397× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 5.12 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 5 µM 0.0470× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 2.78 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.539 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.931 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10639), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 12 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GADD45GIP1]] | +0.76 | +0.53 / +0.76 | both halves | 1e-05 |  |
| [[POLR2I]] | +0.73 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[MRPL57]] | +0.72 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[PET117]] | +0.71 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[RPP21]] | +0.70 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[BLOC1S4]] | +0.70 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[TRAPPC5]] | +0.70 | +0.46 / +0.71 | both halves | 2e-05 |  |
| [[NDUFA7]] | +0.69 | +0.42 / +0.75 | both halves | 4e-05 |  |
| [[RP9]] | +0.68 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[ATP5PO]] ⚠ | +0.68 | +0.45 / +0.70 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL36]] | +0.68 | +0.46 / +0.72 | both halves | 3e-05 |  |
| [[C16orf91]] | +0.68 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[LEO1]] | +0.68 | +0.46 / +0.70 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1A]] | -0.71 | -0.53 / -0.70 | both halves | 1e-05 |  |
| [[HCFC1]] | -0.67 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[CERS2]] | -0.65 | -0.40 / -0.63 | both halves | 4e-05 |  |
| [[TARDBP]] | -0.62 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[IL18BP]] | -0.62 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[DHFR]] | -0.62 | -0.28 / -0.68 | both halves | 3e-04 |  |
| [[EEF1A1]] | -0.61 | -0.32 / -0.70 | both halves | 2e-04 |  |
| [[LY6G5B]] | -0.60 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[M6PR]] | -0.60 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[RCN1]] | -0.60 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[DDX3X]] | -0.59 | -0.32 / -0.61 | both halves | 2e-04 |  |
| [[UBQLN4]] | -0.59 | -0.35 / -0.59 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Carbamazepine (drug)]] 5 µM | C | MTLN activity raises the cells' numbers under Carbamazepine 5 µM (protects the cells) | lines that do not express MTLN (3) vs lines expressing it (45) | the lines without MTLN: 0.69× the cells of the other lines | 0.036 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: C1RL, DOCK5 |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.668). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-45.6, -13.6); signed map (-18.0, -7.2). **Vector** length 51.9, 9.95% of its response variance represented; |z| ≥ 3 in 467 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +1.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.2 | +0.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.1 | +0.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.1 | -0.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.0 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.0 | +1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | +0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +2.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +0.9 | +1.0 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -4.3 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | -4.0 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.7 | +1.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -3.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | -0.3 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.0 | +0.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | mitoregulin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q13 — chr2:110,211,529-110,245,420 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MOXI, LEMP, MPM, TILR; previously NCRNA00116, LINC00116, SMIM37 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCU8](https://www.uniprot.org/uniprotkb/Q8NCU8) (Mitoregulin):

> Positively regulates mitochondrial complex assembly and/or stability (By similarity). Increases mitochondrial membrane potential while decreasing mitochondrial reactive oxygen species. Increases mitochondrial respiration rate. Increased mitochondrial respiratory activity promotes myogenic differentiation which facilitates muscle growth and regeneration (By similarity). Increases mitochondrial calcium retention capacity. Plays a role in maintenance of cellular lipid composition through its …

**Summary**, from NCBI Gene [205251](https://www.ncbi.nlm.nih.gov/gene/205251):

> Involved in several processes, including obsolete positive regulation of sequestering of calcium ion; positive regulation of mitochondrial membrane potential; and triglyceride homeostasis. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27339](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27339) · Entrez [205251](https://www.ncbi.nlm.nih.gov/gene/205251) · UniProt [Q8NCU8](https://www.uniprot.org/uniprotkb/Q8NCU8) · Ensembl [ENSG00000175701](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175701)

## Data

Gene col 10639: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10639); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10639, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10639]; `tensor/DDL_lfc|DDL_z.npy` [10639]; `embed/gene_vectors.npy` [10639]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10639 or target_col == 10639). Every well: [[MTLN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTLN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
