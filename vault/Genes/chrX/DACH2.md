---
symbol: "DACH2"
type: "gene"
col: 4754
ensembl_id: "ENSG00000126733"
name: "dachshund family transcription factor 2"
location: "Xq21.2"
module: 61
arm: "+"
pooled_cpm: 2.51
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# DACH2

*dachshund family transcription factor 2* — Xq21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.70× (z +17.8, q 0e+00, up in 23 of 24 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGCZ]] (+0.79, fdr 7e-06), [[SEMA6D]] (+0.72, fdr 7e-06), [[PTPRT]] (+0.69, fdr 1e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4754.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.70×** | +17.8 | 0e+00 | 23/24 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.83×** | +10.9 | 3e-25 | 24/41 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.61×** | +10.4 | 3e-23 | 4/7 (PANC-1, HOP62, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.23×** | +9.5 | 2e-19 | 24/43 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.26×** | +9.3 | 1e-18 | 13/27 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.23×** | +9.2 | 4e-18 | 21/42 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.12×** | +8.5 | 1e-15 | 0/2 | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.91×** | +8.3 | 6e-15 | 0/2 | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.51×** | +7.5 | 5e-12 | 21/41 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.20×** | +6.4 | 9e-09 | 21/41 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +5.8 | 3e-07 | 7/28 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +5.6 | 1e-06 | 5/18 (NCI-H460, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.95×** | +5.4 | 3e-06 | 11/31 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +5.3 | 4e-06 | 5/44 (A549, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.92×** | +5.3 | 5e-06 | 18/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +3.9 | 0.002 | 6/16 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +3.7 | 0.007 | 4/23 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.032 | 8/42 (A549, hTERT-HPNE, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.13×** | +3.1 | 0.051 | 10/32 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4754. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1.97 | 8 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 27.4× (z +13.8) | — |
| [[PANC-1 (line)]] | alt | 1.30 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 70.9× (z +12.6) | — |
| [[NCI-H23 (line)]] | alt | 2.23 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 113× (z +11.0) | — |
| [[NCI-H1573 (line)]] | alt | 2.12 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 48.6× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 1.65 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 70.0× (z +10.5) | — |
| [[A-427 (line)]] | wt | 1.50 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 61.1× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 1.91 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 35.3× (z +8.8) | — |
| [[SW480 (line)]] | alt | 1.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.87× (z +9.1) | — |
| [[A-172 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 178 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.974 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.968 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.914 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.958 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.984 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4754), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGCZ]] | +0.79 | +0.79 / +0.82 | both halves | 7e-06 |  |
| [[SEMA6D]] | +0.72 | +0.62 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[PTPRT]] | +0.69 | +0.57 / +0.78 | both halves | 1e-05 |  |
| [[CNBD1]] | +0.69 | +0.59 / +0.77 | both halves | 7e-06 |  |
| [[HS6ST3]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[USH2A]] | +0.68 | +0.55 / +0.83 | both halves | 1e-05 |  |
| [[LINC02511]] | +0.68 | +0.53 / +0.81 | both halves | 1e-05 |  |
| [[XIRP2]] | +0.68 | +0.43 / +0.82 | both halves | 3e-05 |  |
| [[PLD5]] | +0.67 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[CNTN5]] | +0.67 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[CCDC39]] | +0.67 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[PKNOX2]] | +0.66 | +0.71 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DACH2's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.0% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PCSK2]] | B | PCSK2 activity raises DACH2's level | lines that do not express PCSK2 (27) vs lines expressing it (23) | 1.68× lower at baseline in the lines without PCSK2 | 0.024 | ⚠ within organs, on part of the lines; also absent: PGR, UNC5D, PDE3A; maybe low, not absent |
| [[COX7B2]] | B | COX7B2 activity raises DACH2's level | lines that do not express COX7B2 (42) vs lines expressing it (8) | 1.21× lower at baseline in the lines without COX7B2 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000285751, GCG, LINC01205 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | C | DACH2's natural level lowers the cells' numbers under Mitoxantrone (dihydrochloride) 0.5 µM (makes them more sensitive) | DACH2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.65 | 0.361 over the table, 0.091 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.733). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.9, 31.7); signed map (31.7, 19.7). **Vector** length 43.2, 5.30% of its response variance represented; |z| ≥ 3 in 1,019 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +17.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.0 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +5.0 | +10.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +5.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +1.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.3 | +1.8 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.4 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -2.4 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.2 | -2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | dachshund family transcription factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq21.2 — chrX:86,148,451-86,832,604 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96NX9](https://www.uniprot.org/uniprotkb/Q96NX9) (Dachshund homolog 2):

> Transcription factor that is involved in regulation of organogenesis. Seems to be a regulator for SIX1 and SIX6. Seems to act as a corepressor of SIX6 in regulating proliferation by directly repressing cyclin-dependent kinase inhibitors, including the p27Kip1 promoter. Is recruited with SIX6 to the p27Kip1 promoter in embryonal retina. SIX6 corepression also seems to involve NCOR1, TBL1, HDAC1 and HDAC3. May be involved together with PAX3, SIX1, and EYA2 in regulation of myogenesis. In the …

**Summary**, from NCBI Gene [117154](https://www.ncbi.nlm.nih.gov/gene/117154):

> This gene is one of two genes which encode a protein similar to the Drosophila protein dachshund, a transcription factor involved in cell fate determination in the eye, limb and genital disc of the fly. The encoded protein contains two characteristic dachshund domains: an N-terminal domain responsible for DNA binding and a C-terminal domain responsible for protein-protein interactions. This gene is located on the X chromosome and is subject to inactivation by DNA methylation. The encoded …

**Accessions** — [HGNC:16814](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16814) · Entrez [117154](https://www.ncbi.nlm.nih.gov/gene/117154) · UniProt [Q96NX9](https://www.uniprot.org/uniprotkb/Q96NX9) · Ensembl [ENSG00000126733](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126733)

## Data

Gene col 4754: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4754); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4754, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4754]; `tensor/DDL_lfc|DDL_z.npy` [4754]; `embed/gene_vectors.npy` [4754]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4754 or target_col == 4754). Every well: [[DACH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DACH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
