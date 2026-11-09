---
symbol: "GABRG3"
type: "gene"
col: 11266
ensembl_id: "ENSG00000182256"
name: "gamma-aminobutyric acid type A receptor subunit gamma3"
location: "15q12"
module: 140
arm: "+"
pooled_cpm: 2.42
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# GABRG3

*gamma-aminobutyric acid type A receptor subunit gamma3* — 15q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.61× (z +20.5, q 0e+00, up in 22 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0697×; ⚠ cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A-427 0.125×; ⚠ toxic; cell-cycle shift, explains ~24% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SORCS3]] (+0.70, fdr 7e-06), [[PTPRT]] (+0.69, fdr 3e-05), [[ATP8A2]] (+0.68, fdr 1e-05).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11266.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.61×** | +20.5 | 0e+00 | 22/25 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.11×** | +12.9 | 1e-35 | 2/3 (A549, BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.44×** | +11.7 | 1e-29 | 4/10 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.89×** | +8.6 | 2e-15 | 16/39 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.88×** | +8.5 | 3e-15 | 11/29 (BT-474, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.17×** | +7.3 | 2e-11 | 13/39 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +6.2 | 4e-08 | 6/17 (BT-474, SW480, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.82×** | +5.3 | 9e-06 | 0/4 | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +5.3 | 9e-06 | 8/27 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.65×** | +4.8 | 1e-04 | 4/19 (NCI-H1573, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +4.4 | 6e-04 | 7/28 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +4.4 | 6e-04 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.55×** | +4.2 | 0.001 | 10/43 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.002 | 4/39 (BT-474, A498, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.19×** | +3.9 | 0.004 | 2/6 (BT-474, A549) | inconsistent across doses | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.63×** | +3.3 | 0.027 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.079 | 0/14 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0697×; ⚠ cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A-427 0.125×; ⚠ toxic; cell-cycle shift, explains ~24% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11266. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 7.28 | 5 (4 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 10.7× (z +12.5) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0697× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.125× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~24% of this change |
| [[A498 (line)]] | wt | 0.883 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 9.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.0× (z +14.1) | — |
| [[LoVo (line)]] | wt | 0.945 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.7× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 1.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.19× (z +8.6) | — |
| [[SW480 (line)]] | alt | 0.900 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.20× (z +8.8) | — |
| [[A-172 (line)]] | wt | 0.989 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.983 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.968 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.926 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.982 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.863 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.990 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.880 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.836 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.893 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.905 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.874 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.905 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.960 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.934 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.990 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11266), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SORCS3]] | +0.70 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[PTPRT]] | +0.69 | +0.46 / +0.75 | both halves | 3e-05 |  |
| [[ATP8A2]] | +0.68 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[AGBL1]] | +0.67 | +0.49 / +0.72 | both halves | 1e-05 |  |
| [[RBFOX3]] | +0.67 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[CNBD1]] | +0.66 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[GALNT17]] | +0.66 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[SGCZ]] | +0.66 | +0.52 / +0.77 | both halves | 1e-05 |  |
| [[CNTN5]] | +0.65 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[LINC02511]] | +0.64 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[FAT3]] | +0.63 | +0.46 / +0.72 | both halves | 3e-05 |  |
| [[GALNTL6]] | +0.63 | +0.51 / +0.76 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GABRG3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KCNN2]] | B | KCNN2 activity raises GABRG3's level | lines that do not express KCNN2 (14) vs lines expressing it (36) | 1.59× lower at baseline in the lines without KCNN2 | 0.092 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.777). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.4, 30.1); signed map (32.2, 16.2). **Vector** length 44.2, 5.77% of its response variance represented; |z| ≥ 3 in 927 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +20.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +11.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +8.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +12.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +4.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.9 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.2 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -0.3 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | gamma-aminobutyric acid type A receptor subunit gamma3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q12 — chr15:26,971,181-27,541,984 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Gamma-aminobutyric acid type A receptor subunits |
| Reactome | 6 pathways, smallest: GABA receptor activation; Signaling by ERBB4; Neurotransmitter receptors and postsynaptic signal transmission |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99928](https://www.uniprot.org/uniprotkb/Q99928) (Gamma-aminobutyric acid receptor subunit gamma-3):

> Gamma subunit of the heteropentameric ligand-gated chloride channel gated by gamma-aminobutyric acid (GABA), a major inhibitory neurotransmitter in the brain (By similarity). GABA-gated chloride channels, also named GABA(A) receptors (GABAAR), consist of five subunits arranged around a central pore and contain GABA active binding site(s) located at the alpha and beta subunit interface(s) (By similarity). When activated by GABA, GABAARs selectively allow the flow of chloride across the cell …

**Summary**, from NCBI Gene [2567](https://www.ncbi.nlm.nih.gov/gene/2567):

> This gene encodes a gamma-aminobutyric acid (GABA) receptor. GABA is the major inhibitory neurotransmitter in the mammalian brain where it acts at GABA-A receptors, which are ligand-gated chloride channels. Chloride conductance of these channels can be modulated by agents such as benzodiazepines that bind to the GABA-A receptor. GABA-A receptors are pentameric, consisting of proteins from several subunit classes: alpha, beta, gamma, delta and rho. The protein encoded by this gene is a gamma …

**Accessions** — [HGNC:4088](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4088) · Entrez [2567](https://www.ncbi.nlm.nih.gov/gene/2567) · UniProt [Q99928](https://www.uniprot.org/uniprotkb/Q99928) · Ensembl [ENSG00000182256](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182256)

## Data

Gene col 11266: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11266); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11266, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11266]; `tensor/DDL_lfc|DDL_z.npy` [11266]; `embed/gene_vectors.npy` [11266]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11266 or target_col == 11266). Every well: [[GABRG3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GABRG3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
