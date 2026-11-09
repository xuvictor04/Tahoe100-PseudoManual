---
symbol: "WDR24"
type: "gene"
col: 4823
ensembl_id: "ENSG00000127580"
name: "WD repeat domain 24"
location: "16p13.3"
module: 107
arm: "+"
pooled_cpm: 2.84
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 3
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# WDR24

*WD repeat domain 24* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.00× (z +7.3, q 1e-10, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.32× (z +4.4, q 0.002, up in 5 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.688× (z -5.9, q 3e-06, down in 14 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[L3MBTL2]] (+0.64, fdr 1e-05), [[EDC3]] (+0.64, fdr 7e-06), [[NEURL4]] (+0.62, fdr 1e-05); moves opposite to [[FNBP1L]] (-0.51, fdr 1e-05), [[TRIM33]] (-0.50, fdr 3e-05), [[TMSB4X]] (-0.49, fdr 6e-05).
> It is in [[Module 107]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4823.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +7.3 | 1e-10 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.60×** | +5.2 | 6e-05 | 6/13 (A498, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.7 | 6e-04 | 3/15 (LS 180, J82, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +4.4 | 0.002 | 5/43 (SHP-77, NCI-H460, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.74×** | +4.3 | 0.002 | 1/6 (PANC-1) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +4.0 | 0.006 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +3.5 | 0.044 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.044 | 6/40 (NCI-H460, COLO 205, …) | inconsistent across doses |  |
| [[Orlistat (drug)]] 0.05 µM |  | **1.39×** | +3.4 | 0.045 | 2/29 (MIA PaCa-2, RKO) | inconsistent across doses | position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.045 | 4/30 (LS 180, A498, …) | top dose only | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.70× | +3.1 | 0.11 | 0/5 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4823.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.688×** | -5.9 | 3e-06 | 14/44 (A498, RPMI-7951, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.739×** | -4.7 | 6e-04 | 17/35 (A498, J82, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.657×** | -4.7 | 6e-04 | 8/45 (A498, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | 0.746× | -3.3 | 0.16 | 8/41 (SNU-423, RPMI-7951, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 0.751× | -3.1 | 0.26 | 8/39 (H4, RKO, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4823. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 7.87 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -9.4) |
| [[HT-29 (line)]] | alt | 2.33 | 0 | 1 | — | [[Rosiglitazone (drug)]] 0.5 µM 0.0603× (z -8.5) |
| [[J82 (line)]] | alt | 3.36 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.125× (z -10.7) |
| [[A-172 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.947 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.50 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4823), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[L3MBTL2]] | +0.64 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[EDC3]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[NEURL4]] | +0.62 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[BAP1]] | +0.62 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[TRMT2A]] | +0.61 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[SPATA2]] | +0.58 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[AARS2]] | +0.58 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[ZBTB48]] | +0.58 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ZNF408]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 | STRING 538 |
| [[EDC4]] | +0.56 | +0.52 / +0.59 | both halves | 1e-05 | same gene group |
| [[RNF25]] | +0.55 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[WDR6]] | +0.55 | +0.41 / +0.61 | both halves | 4e-05 | same gene group |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FNBP1L]] | -0.51 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[TRIM33]] | -0.50 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[TMSB4X]] | -0.49 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[FAM81A]] | -0.46 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[EPB41L5]] | -0.46 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises WDR24's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.574). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.5, -4.1); signed map (-11.9, -25.3). **Vector** length 37.5, 3.51% of its response variance represented; |z| ≥ 3 in 890 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +1.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.4 | +4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.4 | +2.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.3 | +5.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +1.3 | -2.9 |
|  | [[Budesonide (drug)]] 5 µM |  | +0.9 | +1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +0.8 | +1.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +0.7 | +0.0 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +0.7 | +2.6 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +0.7 | +1.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -5.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.6 | -2.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | -3.3 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.0 | -2.2 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:684,622-690,444 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434F054, JFP7; previously C16orf21 |
| Gene groups (HGNC) | WD repeat domain containing; GATOR2 subcomplex |
| Reactome | 4 pathways, smallest: Amino acids regulate mTORC1; Cellular response to starvation; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96S15](https://www.uniprot.org/uniprotkb/Q96S15) (GATOR2 complex protein WDR24):

> Catalytic component of the GATOR2 complex, a multiprotein complex that acts as an activator of the amino acid-sensing branch of the mTORC1 signaling pathway. The GATOR2 complex indirectly activates mTORC1 through the inhibition of the GATOR1 subcomplex. GATOR2 probably acts as an E3 ubiquitin-protein ligase toward GATOR1. In the presence of abundant amino acids, the GATOR2 complex mediates ubiquitination of the NPRL2 core component of the GATOR1 complex, leading to GATOR1 inactivation. In the …

**Summary**, from NCBI Gene [84219](https://www.ncbi.nlm.nih.gov/gene/84219):

> Enables ubiquitin protein ligase activity. Involved in several processes, including cellular response to amino acid starvation; positive regulation of TORC1 signaling; and protein K6-linked ubiquitination. Acts upstream of or within protein localization to plasma membrane. Located in lysosomal membrane. Part of GATOR2 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20852](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20852) · Entrez [84219](https://www.ncbi.nlm.nih.gov/gene/84219) · UniProt [Q96S15](https://www.uniprot.org/uniprotkb/Q96S15) · Ensembl [ENSG00000127580](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127580)

## Data

Gene col 4823: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4823); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4823, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4823]; `tensor/DDL_lfc|DDL_z.npy` [4823]; `embed/gene_vectors.npy` [4823]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4823 or target_col == 4823). Every well: [[WDR24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
