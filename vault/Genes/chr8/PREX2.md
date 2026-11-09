---
symbol: "PREX2"
type: "gene"
col: 507
ensembl_id: "ENSG00000046889"
name: "phosphatidylinositol-3,4,5-trisphosphate dependent Rac exchange factor 2"
location: "8q13.2"
module: 8
arm: "+"
pooled_cpm: 7.88
n_lines_expressing: 5
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# PREX2

*phosphatidylinositol-3,4,5-trisphosphate dependent Rac exchange factor 2* — 8q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.44× (z +13.6, q 4e-39, up in 0 of 4 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIMD4]] (+0.70, fdr 7e-06), [[SLC4A4]] (+0.66, fdr 7e-06), [[LINC01508]] (+0.57, fdr 1e-05); moves opposite to [[NEFM]] (-0.48, fdr 9e-05), [[MFGE8]] (-0.38, fdr 1e-04), [[NIBAN2]] (-0.37, fdr 2e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CNTN6]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 507.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.44×** | +13.6 | 4e-39 | 0/4 | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.20×** | +12.8 | 5e-35 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.09×** | +10.5 | 1e-23 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.31×** | +8.6 | 1e-15 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +5.9 | 5e-07 | 3/4 (C-33 A, NCI-H661, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +5.6 | 2e-06 | 2/4 (HEC-1-A, C-33 A) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +5.0 | 6e-05 | 0/4 | top dose only | cell-cycle shift (explains ~8% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.1 | 0.003 | 1/4 (HEC-1-A) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.67×** | +4.0 | 0.004 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +4.0 | 0.004 | 0/4 | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.59×** | +3.9 | 0.005 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.64×** | +3.9 | 0.005 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here); position effect removed |
| [[Decitabine (drug)]] 0.5 µM |  | **1.59×** | +3.6 | 0.013 | 0/4 | inconsistent across doses |  |
| [[Silodosin (drug)]] 5 µM |  | **1.55×** | +3.3 | 0.036 | 0/4 | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.58×** | +3.3 | 0.036 | 0/3 | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.81×** | +3.3 | 0.036 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.78×** | +3.2 | 0.046 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +3.1 | 0.052 | 0/4 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.51×** | +3.1 | 0.052 | 0/4 | rises with dose | position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.69×** | +2.9 | 0.084 | 0/4 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.44×** | +2.9 | 0.092 | 0/4 | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 507. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 0.701 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.847 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 163 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.930 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.715 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.970 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.947 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.825 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.967 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.952 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.862 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.796 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.860 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.957 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.779 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.698 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.767 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.710 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.928 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.810 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.793 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.643 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.826 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.706 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.805 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.995 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.788 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.720 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.790 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.869 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.706 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.808 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.747 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 507), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMD4]] | +0.70 | +0.61 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[SLC4A4]] | +0.66 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[LINC01508]] | +0.57 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[RHEX]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[ABCC6]] | +0.55 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[TEX41]] | +0.53 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[LRRK2]] | +0.52 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[ENPP3]] | +0.52 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[PTH2R]] | +0.52 | +0.43 / +0.54 | both halves | 4e-05 |  |
| [[GRIN2B]] | +0.50 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[TSHZ2]] | +0.50 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[CXCL10]] | +0.49 | +0.48 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEFM]] | -0.48 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[MFGE8]] | -0.38 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[NIBAN2]] | -0.37 | -0.32 / -0.31 | both halves | 2e-04 |  |
| [[AKAP13]] | -0.36 | -0.35 / -0.27 | both halves | 3e-04 | same gene group; pathway: RHOA GTPase cycle |
| [[MFSD10]] | -0.36 | -0.32 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNTN6]] | C | CNTN6 activity raises PREX2's level | lines that do not express CNTN6 (38) vs lines expressing it (12) | 1.77× lower at baseline in the lines without CNTN6 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC02476, SPARC; maybe low, not absent; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.155). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.3, 43.5); signed map (51.3, 27.7). **Vector** length 15.0, 5.78% of its response variance represented; |z| ≥ 3 in 90 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +0.7 | +13.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +0.7 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.6 | +5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.6 | +10.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.6 | +1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.5 | +0.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +0.5 | +1.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.4 | +1.0 |
| fall | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.4 | -2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.4 | +1.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -0.4 | +0.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.4 | -0.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.4 | -0.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.4 | -1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.3 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol-3,4,5-trisphosphate dependent Rac exchange factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q13.2 — chr8:67,952,046-68,237,032 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DEP.2, FLJ12987, P-REX2, PPP1R129; previously DEPDC2 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Dbl family Rho GEFs; PDZ domain containing; DEP domain containing |
| Reactome | 10 pathways, smallest: Regulation of PTEN stability and activity; PTEN Regulation; RHOA GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q70Z35](https://www.uniprot.org/uniprotkb/Q70Z35) (Phosphatidylinositol 3,4,5-trisphosphate-dependent Rac exchanger 2 protein):

> Functions as a RAC1 guanine nucleotide exchange factor (GEF), activating Rac proteins by exchanging bound GDP for free GTP. Its activity is synergistically activated by phosphatidylinositol 3,4,5-trisphosphate and the beta gamma subunits of heterotrimeric G protein. Mediates the activation of RAC1 in a PI3K-dependent manner. May be an important mediator of Rac signaling, acting directly downstream of both G protein-coupled receptors and phosphoinositide 3-kinase.

**Summary**, from NCBI Gene [80243](https://www.ncbi.nlm.nih.gov/gene/80243):

> The protein encoded by this gene belongs to the phosphatidylinositol 3,4,5-trisphosphate (PIP3)-dependent Rac exchanger (PREX) family, which are Dbl-type guanine-nucleotide exchange factors for Rac family small G proteins. Structural domains of this protein include the catalytic diffuse B-cell lymphoma homology and pleckstrin homology (DHPH) domain, two disheveled, EGL-10, and pleckstrin homology (DEP) domains, two PDZ domains, and a C-terminal inositol polyphosphate-4 phosphatase (IP4P) domain …

**Accessions** — [HGNC:22950](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22950) · Entrez [80243](https://www.ncbi.nlm.nih.gov/gene/80243) · UniProt [Q70Z35](https://www.uniprot.org/uniprotkb/Q70Z35) · Ensembl [ENSG00000046889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000046889)

## Data

Gene col 507: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 507); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 507, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 507]; `tensor/DDL_lfc|DDL_z.npy` [507]; `embed/gene_vectors.npy` [507]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 507 or target_col == 507). Every well: [[PREX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PREX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
