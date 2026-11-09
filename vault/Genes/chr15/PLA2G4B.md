---
symbol: "PLA2G4B"
type: "gene"
col: 14373
ensembl_id: "ENSG00000243708"
name: "phospholipase A2 group IVB"
location: "15q15.1"
module: 2
arm: "+"
pooled_cpm: 2.7
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# PLA2G4B

*phospholipase A2 group IVB* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.01× (z +6.0, q 9e-07, up in 21 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 0.102×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A549 0.0300×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JMJD7]] (+0.73, fdr 7e-06, ⚠ same locus), [[UCKL1]] (+0.68, fdr 1e-05), [[RHOT2]] (+0.67, fdr 7e-06), [[RHPN1]] (+0.66, fdr 1e-05); moves opposite to [[PSENEN]] (-0.57, fdr 7e-06).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADGRB2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14373.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.01×** | +6.0 | 9e-07 | 21/43 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.88×** | +5.4 | 1e-05 | 23/45 (PANC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.58×** | +4.0 | 0.014 | 7/27 (HEC-1-A, A498, …) | inconsistent across doses | position effect removed |
| [[Trimetrexate (drug)]] 0.5 µM |  | **1.51×** | +3.6 | 0.047 | 7/39 (LoVo, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +3.5 | 0.047 | 0/2 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM |  | 1.49× | +3.3 | 0.11 | 3/43 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.49× | +3.2 | 0.12 | 11/30 (LoVo, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | 1.44× | +3.1 | 0.12 | 4/33 (HT-29, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.99× | +3.1 | 0.12 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.43× | +3.1 | 0.12 | 4/44 (hTERT-HPNE, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | 1.42× | +3.0 | 0.14 | 6/43 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14373.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 0.102×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A549 0.0300×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.657× | -3.6 | 0.15 | 15/43 (SW 900, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14373. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 2.56 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0300× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 2.84 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14373), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JMJD7]] | +0.73 | +0.68 / +0.71 | both halves | 7e-06 | STRING 624; ⚠ same locus (0.2 kb, same strand: neighbours can correlate without regulation) |
| [[UCKL1]] | +0.68 | +0.62 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[RHOT2]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[RHPN1]] | +0.66 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[OPLAH]] ⚠ | +0.65 | +0.68 / +0.58 | both halves | 7e-06 | **novel candidate**; ⚠ in the vector space only through flagged drug-doses |
| [[TNFRSF25]] | +0.64 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[ZNF598]] | +0.63 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[TMEM259]] | +0.62 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[KLHL17]] | +0.62 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[FHIP2B]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[APBB3]] | +0.61 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[ARFGAP1]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 | pathway: IRE1alpha activates chaperones |
| [[ADCK5]] | +0.60 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[PGGHG]] | +0.59 | +0.54 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSENEN]] | -0.57 | -0.59 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRB2]] | B | ADGRB2 activity lowers PLA2G4B's level | lines that do not express ADGRB2 (7) vs lines expressing it (43) | 1.25× higher at baseline in the lines without ADGRB2 | 0.025 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |
| [[CCDC120]] | B | CCDC120 activity raises PLA2G4B's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 1.21× lower at baseline in the lines without CCDC120 | 0.062 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.659). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-10.4, -23.6); signed map (-27.6, 0.9). **Vector** length 41.6, 4.05% of its response variance represented; |z| ≥ 3 in 1,054 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +2.4 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +2.0 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.9 | +1.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.6 | +1.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +4.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +3.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.7 | -1.5 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.5 | -3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.1 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.3 | -2.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -2.2 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.2 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase A2 group IVB |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:41,837,775-41,848,147 (+) |
| Ensembl biotype | protein_coding |
| Also known as | cPLA2-beta, HsT16992 |
| Gene groups (HGNC) | Phospholipases; C2 domain containing phospholipases |
| Reactome | 14 pathways, smallest: Hydrolysis of LPC; Acyl chain remodelling of PG; Acyl chain remodelling of PS |
| Matched by | ensembl_id |

**Function**, from UniProt [P0C869](https://www.uniprot.org/uniprotkb/P0C869) (Cytosolic phospholipase A2 beta):

> Calcium-dependent phospholipase A1 and A2 and lysophospholipase that may play a role in membrane phospholipid remodeling.; [Isoform 3]: Calcium-dependent phospholipase A2 and lysophospholipase. Cleaves the ester bond of the fatty acyl group attached to the sn-2 position of phosphatidylethanolamines, producing lysophospholipids that may be used in deacylation-reacylation cycles. Hydrolyzes lysophosphatidylcholines with low efficiency but is inefficient toward phosphatidylcholines.; [Isoform 5]: …

**Summary**, from NCBI Gene [100137049](https://www.ncbi.nlm.nih.gov/gene/100137049):

> This gene encodes a member of the cytosolic phospholipase A2 protein family. Phospholipase A2 enzymes hydrolyze the sn-2 bond of phospholipids, releasing lysophospholipids and fatty acids. This enzyme may be associated with mitochondria and early endosomes. Most tissues also express read-through transcripts from the upstream gene into this gene, some of which may encode fusion proteins combining the N-terminus of the upstream gene including its JmjC domain with the almost complete coding region …

**Accessions** — [HGNC:9036](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9036) · Entrez [100137049](https://www.ncbi.nlm.nih.gov/gene/100137049) · UniProt [P0C869](https://www.uniprot.org/uniprotkb/P0C869) · Ensembl [ENSG00000243708](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243708)

## Data

Gene col 14373: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14373); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14373, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14373]; `tensor/DDL_lfc|DDL_z.npy` [14373]; `embed/gene_vectors.npy` [14373]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14373 or target_col == 14373). Every well: [[PLA2G4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLA2G4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
