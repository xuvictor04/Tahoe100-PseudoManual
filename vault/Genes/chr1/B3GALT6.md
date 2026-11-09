---
symbol: "B3GALT6"
type: "gene"
col: 10672
ensembl_id: "ENSG00000176022"
name: "beta-1,3-galactosyltransferase 6"
location: "1p36.33"
module: 7
arm: "+"
pooled_cpm: 2.42
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# B3GALT6

*beta-1,3-galactosyltransferase 6* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.42× (z +7.9, q 2e-12, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.97× (z +4.3, q 0.002, up in 13 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.409× (z -5.9, q 2e-06, down in 25 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPB]] (+0.70, fdr 7e-06), [[MRPL20-AS1]] (+0.68, fdr 7e-06), [[TMEM250]] (+0.66, fdr 7e-06); moves opposite to [[PRCP]] (-0.51, fdr 1e-04), [[VDAC1P8]] (-0.50, fdr 3e-05), [[CEP44]] (-0.49, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10672.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.42×** | +7.9 | 2e-12 | 1/3 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.73×** | +6.7 | 7e-09 | 8/13 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.64×** | +6.0 | 5e-07 | 1/5 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.97×** | +4.3 | 0.002 | 13/35 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.84×** | +4.1 | 0.006 | 6/14 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +3.4 | 0.055 | 2/19 (NCI-H2347, PANC-1) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.3 | 0.076 | 3/12 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10672.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.409×** | -5.9 | 2e-06 | 25/45 (BT-474, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.564×** | -5.4 | 2e-05 | 20/28 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.451×** | -5.3 | 2e-05 | 20/40 (LoVo, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.626×** | -4.4 | 0.002 | 14/32 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10672. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 4.59 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0804× (z -8.5) |
| [[BT-474 (line)]] | alt | 3.97 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0331× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 4.20 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0854× (z -9.3) ⚠ cell-cycle shift, explains ~6% of this change |
| [[NCI-H460 (line)]] | wt | 1.65 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0870× (z -10.4) |
| [[A-172 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.935 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10672), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPB]] | +0.70 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[MRPL20-AS1]] | +0.68 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[TMEM250]] | +0.66 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[HPS6]] | +0.65 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[JMJD4]] | +0.64 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[PLPP6]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[DDX28]] | +0.62 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[EIF4E]] | +0.61 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[RRS1]] | +0.60 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[FAM83H]] | +0.59 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[TMEM177]] | +0.59 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[INTS5]] | +0.58 | +0.62 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRCP]] | -0.51 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[VDAC1P8]] | -0.50 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[CEP44]] | -0.49 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[NSD3]] | -0.49 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[ACADSB]] | -0.48 | -0.24 / -0.48 | both halves | 5e-04 |  |
| [[CEP57]] | -0.47 | -0.44 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.375). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-48.2, -0.0); signed map (-4.6, -27.8). **Vector** length 46.8, 6.04% of its response variance represented; |z| ≥ 3 in 887 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +4.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +1.7 | +3.4 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.3 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +0.9 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.2 | +1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | -1.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -5.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.7 | -5.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.1 | +0.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.0 | -2.2 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | -1.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | beta-1,3-galactosyltransferase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,232,237-1,235,041 (+) |
| Ensembl biotype | protein_coding |
| Also known as | beta3GalT6 |
| Gene groups (HGNC) | Beta 3-glycosyltransferases |
| Hallmark sets | GLYCOLYSIS, HYPOXIA |
| Reactome | 7 pathways, smallest: Defective B3GALT6 causes EDSP2 and SEMDJL1; Glycosaminoglycan-protein linkage region biosynthesis; Diseases associated with glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96L58](https://www.uniprot.org/uniprotkb/Q96L58) (Beta-1,3-galactosyltransferase 6):

> Beta-1,3-galactosyltransferase that transfers galactose from UDP-galactose to substrates with a terminal beta-linked galactose residue. Has a preference for galactose-beta-1,4-xylose that is found in the linker region of glycosaminoglycans, such as heparan sulfate and chondroitin sulfate. Has no activity towards substrates with terminal glucosamine or galactosamine residues.

**Summary**, from NCBI Gene [126792](https://www.ncbi.nlm.nih.gov/gene/126792):

> The enzyme encoded by this intronless gene is a beta-1,3-galactosyltransferase found in the medial Golgi apparatus, where it catalyzes the transfer of galactose from UDP-galactose to substrates containing a terminal beta-linked galactose moiety. The encoded enzyme has a particular affinity for galactose-beta-1,4-xylose found in the linker region of glycosamines. This enzyme is required for glycosaminoglycan synthesis. [provided by RefSeq, Jun 2013]

**Accessions** — [HGNC:17978](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17978) · Entrez [126792](https://www.ncbi.nlm.nih.gov/gene/126792) · UniProt [Q96L58](https://www.uniprot.org/uniprotkb/Q96L58) · Ensembl [ENSG00000176022](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176022)

## Data

Gene col 10672: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10672); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10672, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10672]; `tensor/DDL_lfc|DDL_z.npy` [10672]; `embed/gene_vectors.npy` [10672]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10672 or target_col == 10672). Every well: [[B3GALT6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B3GALT6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
