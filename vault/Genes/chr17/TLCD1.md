---
symbol: "TLCD1"
type: "gene"
col: 8361
ensembl_id: "ENSG00000160606"
name: "TLC domain containing 1"
location: "17q11.2"
module: 14
arm: "+"
pooled_cpm: 3.44
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# TLCD1

*TLC domain containing 1* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.12× (z +14.0, q 7e-42, up in 27 of 29 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Tofacitinib (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0693×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACOT2]] (+0.63, fdr 6e-05), [[FDX2]] (+0.60, fdr 7e-05), [[SLC2A6]] (+0.60, fdr 1e-05); moves opposite to [[OPA1]] (-0.52, fdr 4e-05), [[EPN1]] (-0.50, fdr 9e-05), [[GFM2]] (-0.49, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8361.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.12×** | +14.0 | 7e-42 | 27/29 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.23×** | +11.1 | 2e-26 | 5/6 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.73×** | +10.9 | 3e-25 | 12/15 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.91×** | +6.4 | 2e-08 | 16/43 (NCI-H2347, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.46×** | +5.8 | 7e-07 | 7/8 (SW1417, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.35×** | +5.8 | 8e-07 | 12/18 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +4.8 | 9e-05 | 19/33 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.63×** | +4.8 | 9e-05 | 13/42 (SW1417, HS-578T, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +4.7 | 2e-04 | 13/28 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.85×** | +4.3 | 8e-04 | 9/18 (NCI-H2347, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.74×** | +3.7 | 0.010 | 15/40 (NCI-H2030, J82, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.69×** | +3.7 | 0.010 | 13/43 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.64×** | +3.5 | 0.021 | 10/42 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.57×** | +3.2 | 0.058 | 9/44 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8361.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Tofacitinib (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0693×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | 0.624× | -3.1 | 0.94 | 13/38 (SW480, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8361. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 3.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.05× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 2.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.28× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.08 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.0693× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 2.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.46× (z +9.8) | — |
| [[A-172 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.404 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.939 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.999 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8361), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACOT2]] | +0.63 | +0.38 / +0.62 | both halves | 6e-05 |  |
| [[FDX2]] | +0.60 | +0.38 / +0.67 | both halves | 7e-05 |  |
| [[SLC2A6]] | +0.60 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[OXLD1]] | +0.60 | +0.34 / +0.66 | both halves | 1e-04 |  |
| [[CXCL3]] | +0.59 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[CCDC24]] | +0.59 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[POLR1H]] | +0.59 | +0.38 / +0.63 | both halves | 7e-05 |  |
| [[NDUFB1]] | +0.59 | +0.37 / +0.63 | both halves | 8e-05 |  |
| [[WTAP]] | +0.59 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[PSME2]] | +0.58 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[TFAP2A-AS1]] | +0.58 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[C1orf56]] | +0.58 | +0.31 / +0.60 | both halves | 2e-04 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OPA1]] | -0.52 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[EPN1]] | -0.50 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[GFM2]] | -0.49 | -0.43 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TLCD1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RPP25]] | B | RPP25 activity raises TLCD1's level | lines that do not express RPP25 (14) vs lines expressing it (36) | 1.64× lower at baseline in the lines without RPP25 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, ODF3B, EPHA10 |
| [[HSD11B2]] | B | HSD11B2 activity raises TLCD1's level | lines that do not express HSD11B2 (16) vs lines expressing it (34) | 1.32× lower at baseline in the lines without HSD11B2 | 0.097 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.548). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.9, -6.3); signed map (40.4, 6.3). **Vector** length 51.9, 8.43% of its response variance represented; |z| ≥ 3 in 742 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +14.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.0 | +6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +4.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +2.7 | +3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +4.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +3.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.4 | +2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.2 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -0.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.2 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -0.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | TLC domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,724,348-28,727,935 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | TLC domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CP7](https://www.uniprot.org/uniprotkb/Q96CP7) (TLC domain-containing protein 1):

> Regulates the composition and fluidity of the plasma membrane. Inhibits the incorporation of membrane-fluidizing phospholipids containing omega-3 long-chain polyunsaturated fatty acids (LCPUFA) and thereby promotes membrane rigidity. Does not appear to have any effect on LCPUFA synthesis.

**Summary**, from NCBI Gene [116238](https://www.ncbi.nlm.nih.gov/gene/116238):

> Involved in several processes, including membrane assembly; phospholipid homeostasis; and regulation of membrane lipid distribution. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25177](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25177) · Entrez [116238](https://www.ncbi.nlm.nih.gov/gene/116238) · UniProt [Q96CP7](https://www.uniprot.org/uniprotkb/Q96CP7) · Ensembl [ENSG00000160606](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160606)

## Data

Gene col 8361: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8361); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8361, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8361]; `tensor/DDL_lfc|DDL_z.npy` [8361]; `embed/gene_vectors.npy` [8361]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8361 or target_col == 8361). Every well: [[TLCD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLCD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
