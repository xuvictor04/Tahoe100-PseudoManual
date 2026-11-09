---
symbol: "NME3"
type: "gene"
col: 2304
ensembl_id: "ENSG00000103024"
name: "NME/NM23 nucleoside diphosphate kinase 3"
location: "16p13.3"
module: 58
arm: "+"
pooled_cpm: 4.16
n_lines_expressing: 45
n_dd_up: 4
n_dd_down: 9
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# NME3

*NME/NM23 nucleoside diphosphate kinase 3* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.94× (z +6.9, q 3e-09, up in 19 of 20 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.428× (z -7.7, q 6e-12, down in 28 of 35 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX14]] (+0.74, fdr 3e-05), [[C15orf61]] (+0.72, fdr 5e-05, ⚠ C15orf61 in the vector space only through flagged drug-doses), [[TMEM276]] (+0.72, fdr 2e-05), [[DPM3]] (+0.71, fdr 1e-05); moves opposite to [[ELK4]] (-0.60, fdr 1e-04), [[KRR1]] (-0.59, fdr 9e-05), [[KRT8P12]] (-0.59, fdr 4e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BTBD6]] → it (grade B ⚠); 3 go from it, the strongest it → [[BTBD6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2304.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.94×** | +6.9 | 3e-09 | 19/20 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.88×** | +6.5 | 2e-08 | 5/6 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +3.6 | 0.054 | 7/12 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.72×** | +3.5 | 0.078 | 11/24 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.68× | +3.3 | 0.10 | 11/33 (NCI-H2030, SW48, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2304.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.428×** | -7.7 | 6e-12 | 28/35 (NCI-H2030, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.398×** | -5.9 | 8e-07 | 21/35 (LOX-IMVI, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.299×** | -4.0 | 0.012 | 18/32 (NCI-H1573, NCI-H460, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.537×** | -3.8 | 0.022 | 16/38 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.573×** | -3.6 | 0.032 | 16/40 (SNU-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.574×** | -3.6 | 0.032 | 19/41 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.693×** | -3.3 | 0.066 | 19/35 (SW48, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.369×** | -3.3 | 0.066 | 15/38 (LOX-IMVI, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.610×** | -3.2 | 0.090 | 13/41 (J82, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2304. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 5.90 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0612× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 4.63 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0684× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -10.4) |
| [[A-172 (line)]] | wt | 0.364 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.292 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.358 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.912 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.349 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.87 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2304), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 10 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX14]] | +0.74 | +0.46 / +0.72 | both halves | 3e-05 |  |
| [[C15orf61]] ⚠ | +0.72 | +0.39 / +0.72 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM276]] | +0.72 | +0.48 / +0.75 | both halves | 2e-05 |  |
| [[DPM3]] | +0.71 | +0.50 / +0.78 | both halves | 1e-05 |  |
| [[RAC3]] | +0.69 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[MRPL34]] | +0.69 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[LAMTOR2]] | +0.68 | +0.54 / +0.75 | both halves | 1e-05 |  |
| [[MICOS13]] | +0.68 | +0.47 / +0.72 | both halves | 2e-05 |  |
| [[NAT14]] | +0.68 | +0.43 / +0.70 | both halves | 3e-05 |  |
| [[TMEM256]] | +0.68 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[ALKBH7]] | +0.67 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[LSM2]] | +0.67 | +0.39 / +0.67 | both halves | 6e-05 |  |
| [[MHENCR]] | +0.67 | +0.55 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELK4]] | -0.60 | -0.36 / -0.61 | both halves | 1e-04 |  |
| [[KRR1]] | -0.59 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[KRT8P12]] | -0.59 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[ZNF655]] | -0.57 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[EIF4G2]] | -0.57 | -0.29 / -0.52 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BTBD6]] | B | BTBD6 activity raises NME3's level | lines that do not express BTBD6 (8) vs lines expressing it (42) | 1.76× lower at baseline in the lines without BTBD6 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000225647, ENSG00000254394, RPL23AP49 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BTBD6]] | B | NME3 activity raises BTBD6's level | lines that do not express NME3 (5) vs lines expressing it (45) | 2.80× lower at baseline in the lines without NME3 | 0.060 | ⚠ within organs, on part of the lines; also absent: TACC2; its own permutation p |
| [[FLVCR1-DT]] | B | NME3 activity lowers FLVCR1-DT's level | lines that do not express NME3 (5) vs lines expressing it (45) | 1.14× higher at baseline in the lines without NME3 | 0.060 | ⚠ within organs, on part of the lines; also absent: TACC2; its own permutation p |
| [[DNPH1]] | B | NME3 activity lowers DNPH1's level | lines that do not express NME3 (5) vs lines expressing it (45) | 1.24× higher at baseline in the lines without NME3 | 0.066 | ⚠ within organs, on part of the lines; also absent: TACC2 |

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.776). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-46.8, -16.6); signed map (-31.9, 5.6). **Vector** length 43.8, 6.70% of its response variance represented; |z| ≥ 3 in 594 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | -2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | -1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | -2.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.5 | +1.9 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.0 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +1.8 |
|  | [[Bendamustine (drug)]] 5 µM |  | +0.9 | +2.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.8 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -5.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | +0.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | NME/NM23 nucleoside diphosphate kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:1,770,320-1,771,561 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DR-nm23, NM23-H3, NDPKC |
| Gene groups (HGNC) | NME/NM23 family |
| Hallmark sets | DNA_REPAIR |
| Reactome | 2 pathways, smallest: Interconversion of nucleotide di- and triphosphates; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13232](https://www.uniprot.org/uniprotkb/Q13232) (Nucleoside diphosphate kinase C):

> Catalyzes the transfer of a gamma-phosphoryl group from a nucleoside triphosphate, mainly ATP, to a nucleoside diphosphate via a ping-pong mechanism involving a phosphohistidine intermediate, therefore contributing to the nucleoside triphosphate homeostasis. In vitro, can also use other phosphate donors such as UTP and GTP. Independently of its nucleoside diphosphate kinase activity, involved in mitochondrial membrane tethering, a prerequisite for fusion through direct membrane-binding and …

**Summary**, from NCBI Gene [4832](https://www.ncbi.nlm.nih.gov/gene/4832):

> Enables several functions, including mitochondrion-mitochondrion outer membrane tether activity; nucleoside diphosphate kinase activity; and purine ribonucleotide binding activity. Involved in several processes, including dTTP biosynthetic process; mitochondrial outer membrane fusion; and protein hexamerization. Located in cytoplasm. Is active in mitochondrial outer membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7851](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7851) · Entrez [4832](https://www.ncbi.nlm.nih.gov/gene/4832) · UniProt [Q13232](https://www.uniprot.org/uniprotkb/Q13232) · Ensembl [ENSG00000103024](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103024)

## Data

Gene col 2304: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2304); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2304, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2304]; `tensor/DDL_lfc|DDL_z.npy` [2304]; `embed/gene_vectors.npy` [2304]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2304 or target_col == 2304). Every well: [[NME3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NME3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
