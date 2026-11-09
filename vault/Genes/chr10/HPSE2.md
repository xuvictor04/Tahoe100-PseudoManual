---
symbol: "HPSE2"
type: "gene"
col: 10327
ensembl_id: "ENSG00000172987"
name: "heparanase 2 (inactive)"
location: "10q24.2"
module: 166
arm: "+"
pooled_cpm: 2.99
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/166"]
generated_by: "tahoemap"
---

# HPSE2

*heparanase 2 (inactive)* — 10q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.02× (z +27.9, q 0e+00, up in 29 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Sunitinib (drug)]] 0.05 µM in 1 line (SW480 0.0516×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OBI1-AS1]] (+0.88, fdr 7e-06), [[SLC27A6]] (+0.81, fdr 7e-06), [[CCDC26]] (+0.81, fdr 7e-06).
> It is in [[Module 166]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10327.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.02×** | +27.9 | 0e+00 | 29/30 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **5.16×** | +15.7 | 0e+00 | 37/40 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **4.81×** | +15.0 | 0e+00 | 29/39 (NCI-H460, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.92×** | +14.6 | 0e+00 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.04×** | +13.3 | 2e-38 | 7/10 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.10×** | +10.4 | 3e-23 | 16/26 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.09×** | +9.9 | 4e-21 | 18/33 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.42×** | +8.1 | 5e-14 | 19/34 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.74×** | +6.9 | 3e-10 | 1/3 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +6.8 | 8e-10 | 21/45 (HOP62, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +5.8 | 3e-07 | 10/45 (A498, NCI-H460, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.41×** | +4.6 | 2e-04 | 7/43 (A549, AN3 CA, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +4.3 | 6e-04 | 1/7 (PANC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.71×** | +3.6 | 0.011 | 0/24 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.6 | 0.011 | 1/20 (KATO III) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.39×** | +3.0 | 0.087 | 2/33 (NCI-H23, AsPC-1) | rises with dose | position effect removed |
| [[Thymol (drug)]] 5 µM |  | **1.25×** | +2.9 | 0.091 | 2/43 (CFPAC-1, COLO 205) | rises with dose |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.36×** | +2.9 | 0.098 | 3/23 (C32, NCI-H460, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Sunitinib (drug)]] 0.05 µM in 1 line (SW480 0.0516×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10327. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1.86 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +12.0) | — |
| [[SW480 (line)]] | alt | 1.63 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +13.1) | [[Sunitinib (drug)]] 0.05 µM 0.0516× (z -10.4) |
| [[A-172 (line)]] | wt | 1.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +9.3) | — |
| [[A498 (line)]] | wt | 1.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +11.2) | — |
| [[A549 (line)]] | wt | 2.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.5× (z +10.2) | — |
| [[HEC-1-A (line)]] | alt | 1.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.5× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 1.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +8.9) | — |
| [[LoVo (line)]] | wt | 1.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.6× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 1.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.5× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 1.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.07× (z +8.7) | — |
| [[PANC-1 (line)]] | alt | 1.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.2× (z +12.1) | — |
| [[A-427 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10327), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OBI1-AS1]] | +0.88 | +0.78 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[SLC27A6]] | +0.81 | +0.59 / +0.79 | both halves | 7e-06 |  |
| [[CCDC26]] | +0.81 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[HRG-AS1]] | +0.81 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[DPP6]] | +0.80 | +0.61 / +0.78 | both halves | 7e-06 |  |
| [[LANCL1-AS1]] | +0.79 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[SORCS3]] | +0.79 | +0.55 / +0.84 | both halves | 1e-05 |  |
| [[LINC02006]] | +0.78 | +0.59 / +0.79 | both halves | 7e-06 |  |
| [[USH2A]] | +0.78 | +0.67 / +0.81 | both halves | 7e-06 |  |
| [[DCC]] | +0.76 | +0.58 / +0.81 | both halves | 7e-06 | same gene group |
| [[CFAP20DC-AS1]] | +0.76 | +0.55 / +0.74 | both halves | 1e-05 |  |
| [[LINC00861]] | +0.76 | +0.61 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HPSE2's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.0% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[LEF1-AS1]] | B | LEF1-AS1 activity raises HPSE2's level | lines that do not express LEF1-AS1 (33) vs lines expressing it (17) | 1.58× lower at baseline in the lines without LEF1-AS1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent |
| [[LINC02932]] | B | LINC02932 activity raises HPSE2's level | lines that do not express LINC02932 (5) vs lines expressing it (45) | 1.30× lower at baseline in the lines without LINC02932 | 0.092 | ⚠ within organs, on part of the lines; also absent: RBFOX1, DNAH6, ESRRB; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 166]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.845). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.7, 28.4); signed map (32.4, 12.7). **Vector** length 52.7, 7.21% of its response variance represented; |z| ≥ 3 in 948 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +27.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.5 | +15.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +13.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +5.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.6 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -2.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -0.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +1.2 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | heparanase 2 (inactive) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.2 — chr10:98,457,077-99,235,862 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HPA2, HPR2; previously UFS |
| Gene groups (HGNC) | Heparanase family; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: HS-GAG degradation; Heparan sulfate/heparin (HS-GAG) metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWQ2](https://www.uniprot.org/uniprotkb/Q8WWQ2) (Inactive heparanase-2):

> Binds heparin and heparan sulfate with high affinity, but lacks heparanase activity. Inhibits HPSE, possibly by competing for its substrates (in vitro).

**Summary**, from NCBI Gene [60495](https://www.ncbi.nlm.nih.gov/gene/60495):

> This gene encodes a heparanase enzyme. The encoded protein is a endoglycosidase that degrades heparin sulfate proteoglycans located on the extracellular matrix and cell surface. This protein may be involved in biological processes involving remodeling of the extracellular matrix including angiogenesis and tumor progression. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:18374](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18374) · Entrez [60495](https://www.ncbi.nlm.nih.gov/gene/60495) · UniProt [Q8WWQ2](https://www.uniprot.org/uniprotkb/Q8WWQ2) · Ensembl [ENSG00000172987](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172987)

## Data

Gene col 10327: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10327); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10327, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10327]; `tensor/DDL_lfc|DDL_z.npy` [10327]; `embed/gene_vectors.npy` [10327]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10327 or target_col == 10327). Every well: [[HPSE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HPSE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
