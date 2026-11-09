---
symbol: "RPUSD1"
type: "gene"
col: 144
ensembl_id: "ENSG00000007376"
name: "RNA pseudouridine synthase domain containing 1"
location: "16p13.3"
module: 58
arm: "+"
pooled_cpm: 2.62
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# RPUSD1

*RNA pseudouridine synthase domain containing 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.03× (z +12.5, q 6e-33, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.455× (z -6.2, q 4e-07, down in 25 of 45 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPTP]] (+0.77, fdr 7e-06), [[STUB1]] (+0.73, fdr 1e-05), [[MRPL4]] (+0.68, fdr 1e-05); moves opposite to [[USP34-DT]] (-0.61, fdr 2e-04), [[KMT2E-AS1]] (-0.61, fdr 3e-04), [[LINC00938]] (-0.60, fdr 1e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 144.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.03×** | +12.5 | 6e-33 | 44/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.34×** | +11.3 | 3e-27 | 41/42 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.32×** | +9.2 | 4e-18 | 35/42 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.94×** | +8.0 | 2e-13 | 3/3 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.61×** | +7.4 | 2e-11 | 11/14 (A498, HEC-1-A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.59×** | +6.8 | 1e-09 | 2/4 (SW1417, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.99×** | +5.3 | 9e-06 | 8/15 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.82×** | +4.4 | 6e-04 | 11/33 (PANC-1, NCI-H1792, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.69×** | +4.0 | 0.003 | 9/29 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.8 | 0.008 | 6/19 (J82, A498, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.50×** | +3.1 | 0.096 | 7/21 (LS 180, HT-29, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.48× | +3.0 | 0.12 | 6/45 (HOP62, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 144.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.455×** | -6.2 | 4e-07 | 25/45 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.515×** | -5.2 | 6e-05 | 20/39 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.715×** | -3.7 | 0.034 | 16/33 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.657× | -3.3 | 0.13 | 10/21 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.761× | -3.1 | 0.24 | 16/33 (PANC-1, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 144. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 3.84 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0686× (z -11.3) ⚠ cell-cycle shift, explains ~53% of this change |
| [[A-172 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.559 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.847 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 144), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPTP]] | +0.77 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[STUB1]] | +0.73 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[MRPL4]] | +0.68 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[SLC39A3]] | +0.68 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[RGS19]] | +0.66 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[WRAP73]] | +0.63 | +0.33 / +0.42 | both halves | 1e-04 |  |
| [[CDK5]] | +0.62 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[SNRNP25]] | +0.61 | +0.34 / +0.50 | both halves | 1e-04 |  |
| [[PIGQ]] | +0.61 | +0.37 / +0.58 | both halves | 8e-05 |  |
| [[BAIAP2-DT]] | +0.61 | +0.49 / +0.40 | both halves | 4e-05 |  |
| [[TSR3]] | +0.61 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[RRP1B]] | +0.60 | +0.33 / +0.51 | both halves | 1e-04 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP34-DT]] | -0.61 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[KMT2E-AS1]] | -0.61 | -0.34 / -0.26 | both halves | 3e-04 |  |
| [[LINC00938]] | -0.60 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[C12orf57]] | -0.60 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[TPTE2P6]] | -0.59 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[NDUFA6-DT]] | -0.58 | -0.26 / -0.40 | both halves | 4e-04 |  |
| [[LHFPL3]] | -0.58 | -0.22 / -0.37 | both halves | 6e-04 |  |
| [[TSTD3]] | -0.58 | -0.31 / -0.26 | both halves | 4e-04 |  |
| [[PSMD14-DT]] | -0.58 | -0.32 / -0.29 | both halves | 2e-04 |  |
| [[HOXB-AS3]] | -0.58 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[HOXB-AS1]] | -0.56 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[TYMSOS]] | -0.56 | -0.32 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers RPUSD1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.521). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.7, 13.7); signed map (-31.5, 2.6). **Vector** length 52.4, 7.55% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.4 | +12.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.0 | +11.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.2 | +9.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.1 | +3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +4.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.3 | +2.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.1 | +1.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.1 | +1.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -0.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | +0.1 |
|  | [[NVP-BHG712 (drug)]] 0.05 µM |  | -0.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | RNA pseudouridine synthase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:784,974-788,397 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RLUCL, MGC19600; previously C16orf40 |
| Gene groups (HGNC) | RNA pseudouridylate synthase domain containing; Pseudouridine synthases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJJ7](https://www.uniprot.org/uniprotkb/Q9UJJ7) (Pseudouridylate synthase RPUSD1):

> Pseudouridylate synthase that catalyzes the conversion of uridine to pseudouridine in cytoplasmic tRNAs. Catalyzes pseudouridylation of pseudouridine-30 and pseudouridine-72 from uracil-30 and uracil-72 within the anticodon stem of cytoplasmic tRNAs.

**Summary**, from NCBI Gene [113000](https://www.ncbi.nlm.nih.gov/gene/113000):

> Predicted to enable pseudouridine synthase activity. Predicted to be involved in enzyme-directed rRNA pseudouridine synthesis. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14173](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14173) · Entrez [113000](https://www.ncbi.nlm.nih.gov/gene/113000) · UniProt [Q9UJJ7](https://www.uniprot.org/uniprotkb/Q9UJJ7) · Ensembl [ENSG00000007376](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000007376)

## Data

Gene col 144: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 144); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 144, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 144]; `tensor/DDL_lfc|DDL_z.npy` [144]; `embed/gene_vectors.npy` [144]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 144 or target_col == 144). Every well: [[RPUSD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPUSD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
