---
symbol: "DCC"
type: "gene"
col: 11909
ensembl_id: "ENSG00000187323"
name: "DCC netrin 1 receptor"
location: "18q21.2"
module: 166
arm: "+"
pooled_cpm: 2.82
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/166"]
generated_by: "tahoemap"
---

# DCC

*DCC netrin 1 receptor* — 18q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.38× (z +20.8, q 0e+00, up in 24 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (LOX-IMVI 0.0625×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Selinexor (drug)]] 5 µM in 1 line (C32 0.205×; ⚠ cell-cycle shift, explains ~0% of this change); [[DT-061 (drug)]] 0.05 µM in 1 line (HT-29 0.0514×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OBI1-AS1]] (+0.84, fdr 7e-06), [[ST8SIA1]] (+0.83, fdr 7e-06), [[SORCS1]] (+0.79, fdr 7e-06).
> It is in [[Module 166]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11909.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.38×** | +20.8 | 0e+00 | 24/30 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.24×** | +11.7 | 5e-29 | 7/11 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.34×** | +11.5 | 2e-28 | 1/2 (LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.01×** | +9.8 | 1e-20 | 28/45 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.86×** | +9.5 | 3e-19 | 1/3 (LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.54×** | +9.3 | 2e-18 | 21/42 (BT-474, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.75×** | +7.8 | 4e-13 | 10/35 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.09×** | +7.3 | 2e-11 | 2/7 (LoVo, HT-29) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +6.5 | 4e-09 | 8/28 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +6.3 | 1e-08 | 12/35 (NCI-H460, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +5.4 | 4e-06 | 8/37 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +4.3 | 1e-03 | 5/38 (MIA PaCa-2, SW 1271, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.011 | 3/45 (KATO III, A549, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.5 | 0.022 | 6/19 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Flutamide (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.023 | 4/37 (CHP-212, A-172, …) | inconsistent across doses |  |
| [[Terfenadine (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.052 | 3/44 (C-33 A, MIA PaCa-2, …) | top dose only |  |
| [[palbociclib (drug)]] 0.05 µM |  | **1.38×** | +3.0 | 0.074 | 3/37 (NCI-H23, J82, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.074 | 4/42 (NCI-H460, SW 900, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.0 | 0.095 | 3/43 (NCI-H1792, SNU-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11909.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (LOX-IMVI 0.0625×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Selinexor (drug)]] 5 µM in 1 line (C32 0.205×; ⚠ cell-cycle shift, explains ~0% of this change); [[DT-061 (drug)]] 0.05 µM in 1 line (HT-29 0.0514×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Gemfibrozil (drug)]] 0.5 µM |  | 0.737× | -3.0 | 0.98 | 6/35 (SW 900, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11909. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 1.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +8.7) | — |
| [[C32 (line)]] | wt | 31.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.205× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 1.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 2.52 | 0 | 1 | — | [[DT-061 (drug)]] 0.05 µM 0.0514× (z -8.6) |
| [[LoVo (line)]] | wt | 1.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +9.7) | — |
| [[LOX-IMVI (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0625× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 1.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 2.21 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.68× (z +9.6) | — |
| [[A-172 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11909), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OBI1-AS1]] | +0.84 | +0.71 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[ST8SIA1]] | +0.83 | +0.75 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[SORCS1]] | +0.79 | +0.65 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[SGCD]] | +0.78 | +0.77 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[LINC02208]] | +0.76 | +0.65 / +0.82 | both halves | 7e-06 |  |
| [[CNTN5]] | +0.76 | +0.65 / +0.78 | both halves | 7e-06 | same gene group |
| [[HPSE2]] | +0.76 | +0.58 / +0.81 | both halves | 7e-06 | same gene group |
| [[CNTN4]] | +0.76 | +0.64 / +0.77 | both halves | 7e-06 | same gene group |
| [[PTPRT]] | +0.75 | +0.49 / +0.82 | both halves | 1e-05 | same gene group |
| [[USH2A]] | +0.74 | +0.53 / +0.80 | both halves | 1e-05 | same gene group |
| [[SEMA6D]] | +0.72 | +0.45 / +0.76 | both halves | 3e-05 |  |
| [[SLC9C1]] | +0.72 | +0.56 / +0.71 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DCC's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PAMR1]] | B | PAMR1 activity raises DCC's level | lines that do not express PAMR1 (28) vs lines expressing it (22) | 1.59× lower at baseline in the lines without PAMR1 | 0.095 | ⚠ within organs, on part of the lines; also absent: MARCHF4, FLRT2, ESM1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 166]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.869). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.7, 28.2); signed map (32.3, 15.4). **Vector** length 42.6, 4.45% of its response variance represented; |z| ≥ 3 in 1,044 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +20.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +11.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +1.3 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.0 | -1.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.0 | -0.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | DCC netrin 1 receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.2 — chr18:52,340,197-53,535,899 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IGDCC1, NTN1R1 |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; MicroRNA protein coding host genes |
| Hallmark sets | SPERMATOGENESIS, KRAS_SIGNALING_DN |
| Reactome | 13 pathways, smallest: DSCAM interactions; Role of second messengers in netrin-1 signaling; Netrin mediated repulsion signals |
| Matched by | ensembl_id |

**Function**, from UniProt [P43146](https://www.uniprot.org/uniprotkb/P43146) (Netrin receptor DCC):

> Receptor for netrin required for axon guidance. Mediates axon attraction of neuronal growth cones in the developing nervous system upon ligand binding. Its association with UNC5 proteins may trigger signaling for axon repulsion. It also acts as a dependence receptor required for apoptosis induction when not associated with netrin ligand. Implicated as a tumor suppressor gene.

**Summary**, from NCBI Gene [1630](https://www.ncbi.nlm.nih.gov/gene/1630):

> This gene encodes a netrin 1 receptor. The transmembrane protein is a member of the immunoglobulin superfamily of cell adhesion molecules, and mediates axon guidance of neuronal growth cones towards sources of netrin 1 ligand. The cytoplasmic tail interacts with the tyrosine kinases Src and focal adhesion kinase (FAK, also known as PTK2) to mediate axon attraction. The protein partially localizes to lipid rafts, and induces apoptosis in the absence of ligand. The protein functions as a tumor …

**Accessions** — [HGNC:2701](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2701) · Entrez [1630](https://www.ncbi.nlm.nih.gov/gene/1630) · UniProt [P43146](https://www.uniprot.org/uniprotkb/P43146) · Ensembl [ENSG00000187323](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187323)

## Data

Gene col 11909: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11909); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11909, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11909]; `tensor/DDL_lfc|DDL_z.npy` [11909]; `embed/gene_vectors.npy` [11909]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11909 or target_col == 11909). Every well: [[DCC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
