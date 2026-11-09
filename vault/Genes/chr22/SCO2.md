---
symbol: "SCO2"
type: "gene"
col: 16049
ensembl_id: "ENSG00000284194"
name: "synthesis of cytochrome C oxidase 2"
location: "22q13.33"
module: 32
arm: "+"
pooled_cpm: 2.92
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 3
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 17
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# SCO2

*synthesis of cytochrome C oxidase 2* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.45× (z +6.5, q 4e-08, up in 13 of 18 measured lines) ⚠ toxic. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.484× (z -5.9, q 2e-06, down in 25 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MX1]] (+0.67, fdr 7e-06), [[TYMP]] (+0.67, fdr 7e-06, ⚠ same locus), [[IFI44L]] (+0.66, fdr 7e-06), [[OAS2]] (+0.64, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[IFI27]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16049.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.45×** | +6.5 | 4e-08 | 13/18 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +5.4 | 2e-05 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +4.7 | 5e-04 | 1/12 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.68×** | +4.2 | 0.004 | 7/13 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.33× | +3.2 | 0.14 | 5/34 (MIA PaCa-2, LS 180, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16049.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.484×** | -5.9 | 2e-06 | 25/45 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.621×** | -3.9 | 0.029 | 16/40 (LS 180, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.630×** | -3.6 | 0.070 | 12/39 (NCI-H1573, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16049. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 6.44 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -8.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 4.27 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0812× (z -8.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16049), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MX1]] | +0.67 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[TYMP]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 | STRING 743; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[IFI44L]] | +0.66 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[OAS2]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[OAS1]] | +0.63 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[UBE2L6]] | +0.62 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[BATF2]] | +0.62 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[CMPK2]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[ZNFX1]] | +0.61 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[IFIT1]] | +0.61 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[XAF1]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[IFIT3]] | +0.60 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[PLSCR1]] | +0.60 | +0.49 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 15, C 2. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFI27]] | B | IFI27 activity raises SCO2's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 1.41× lower at baseline in the lines without IFI27 | 0.001 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[OAS1]] | B | OAS1 activity raises SCO2's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.41× lower at baseline in the lines without OAS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[TRIM22]] | B | TRIM22 activity raises SCO2's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 1.33× lower at baseline in the lines without TRIM22 | 0.018 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[BATF2]] | B | BATF2 activity raises SCO2's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 1.39× lower at baseline in the lines without BATF2 | 0.019 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[OAS2]] | B | OAS2 activity raises SCO2's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 1.27× lower at baseline in the lines without OAS2 | 0.021 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[NRIR]] | B | NRIR activity raises SCO2's level | lines that do not express NRIR (14) vs lines expressing it (36) | 1.22× lower at baseline in the lines without NRIR | 0.032 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[SAMD9L]] | B | SAMD9L activity raises SCO2's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 1.24× lower at baseline in the lines without SAMD9L | 0.038 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[RSAD2]] | B | RSAD2 activity raises SCO2's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 1.30× lower at baseline in the lines without RSAD2 | 0.040 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[OAS3]] | B | OAS3 activity raises SCO2's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 1.40× lower at baseline in the lines without OAS3 | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[CMPK2]] | B | CMPK2 activity raises SCO2's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 1.28× lower at baseline in the lines without CMPK2 | 0.045 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[HERC6]] | B | HERC6 activity raises SCO2's level | lines that do not express HERC6 (5) vs lines expressing it (45) | 1.36× lower at baseline in the lines without HERC6 | 0.068 | ⚠ within organs, on part of the lines; also absent: IFIH1, IFI35, PARP9; maybe low, not absent |
| [[MX1]] | B | MX1 activity raises SCO2's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.27× lower at baseline in the lines without MX1 | 0.068 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.3, 52.4); signed map (65.3, 30.0). **Vector** length 46.0, 5.49% of its response variance represented; |z| ≥ 3 in 899 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.52 to 56); *interferon gamma response* (hallmark, mean cos +0.52 to 60); *interferon* (control, mean cos +0.57 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.3 | +6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | -1.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.1 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.1 | +1.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +0.9 | +0.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +0.9 | +0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.8 | -0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.8 | +2.0 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.9 | -1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -5.9 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.8 | -1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | synthesis of cytochrome C oxidase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:50,523,568-50,526,461 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SCO1L; previously MYP6 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 5 pathways, smallest: Complex IV assembly; TP53 Regulates Metabolic Genes; Respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O43819](https://www.uniprot.org/uniprotkb/O43819) (Cytochrome c oxidase assembly factor SCO2):

> Copper metallochaperone essential for the synthesis and maturation of cytochrome c oxidase subunit II (MT-CO2/COX2); together with SCO1, facilitates the incorporation of copper into the Cu(A) site of MT-CO2/COX2. Could also act as a thiol-disulfide oxidoreductase to regulate the redox state of the cysteines in SCO1 during maturation of MT-CO2/COX2.

**Summary**, from NCBI Gene [9997](https://www.ncbi.nlm.nih.gov/gene/9997):

> Cytochrome c oxidase (COX) catalyzes the transfer of electrons from cytochrome c to molecular oxygen, which helps to maintain the proton gradient across the inner mitochondrial membrane that is necessary for aerobic ATP production. Human COX is a multimeric protein complex that requires several assembly factors; this gene encodes one of the COX assembly factors. The encoded protein is a metallochaperone that is involved in the biogenesis of cytochrome c oxidase subunit II. Mutations in this …

**Accessions** — [HGNC:10604](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10604) · Entrez [9997](https://www.ncbi.nlm.nih.gov/gene/9997) · UniProt [O43819](https://www.uniprot.org/uniprotkb/O43819) · Ensembl [ENSG00000284194](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000284194)

## Data

Gene col 16049: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16049); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16049, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16049]; `tensor/DDL_lfc|DDL_z.npy` [16049]; `embed/gene_vectors.npy` [16049]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16049 or target_col == 16049). Every well: [[SCO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
