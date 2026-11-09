---
symbol: "ACOT2"
type: "gene"
col: 4094
ensembl_id: "ENSG00000119673"
name: "acyl-CoA thioesterase 2"
location: "14q24.3"
module: 46
arm: "+"
pooled_cpm: 7.2
n_lines_expressing: 48
n_dd_up: 9
n_dd_down: 5
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# ACOT2

*acyl-CoA thioesterase 2* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.88× (z +14.8, q 0e+00, up in 38 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.470× (z -7.5, q 4e-11, down in 27 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DICER1-AS1]] (+0.69, fdr 1e-05), [[UNK]] (+0.68, fdr 1e-05), [[ATAD2B]] (+0.67, fdr 2e-05); moves opposite to [[KIF21B]] (-0.57, fdr 7e-04), [[PRKCZ]] (-0.57, fdr 7e-05), [[TPCN2]] (-0.56, fdr 4e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4094.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.88×** | +14.8 | 0e+00 | 38/40 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.83×** | +5.9 | 8e-07 | 15/30 (NCI-H2030, SW 900, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +5.8 | 1e-06 | 8/13 (NCI-H2030, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +5.3 | 2e-05 | 18/32 (NCI-H2030, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.60×** | +4.6 | 4e-04 | 18/41 (NCI-H1573, LOX-IMVI, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.040 | 12/46 (A-427, HEC-1-A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.040 | 7/39 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.4 | 0.043 | 9/41 (NCI-H1792, BT-474, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.40×** | +3.3 | 0.058 | 11/31 (BT-474, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4094.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.470×** | -7.5 | 4e-11 | 27/45 (HepG2/C3A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.473×** | -7.4 | 4e-11 | 26/45 (HepG2/C3A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.548×** | -5.9 | 5e-07 | 25/45 (HepG2/C3A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.656×** | -4.2 | 0.004 | 16/44 (A498, SK-MEL-2, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.696×** | -3.6 | 0.038 | 15/45 (HepG2/C3A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | 0.450× | -3.2 | 0.13 | 6/45 (NCI-H23, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (drug)]] 5 µM |  | 0.804× | -3.0 | 0.19 | 10/45 (SW1417, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4094. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 27.7 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.151× (z -9.7) |
| [[HOP62 (line)]] | alt | 3.14 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.04× (z +8.7) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0856× (z -8.5) |
| [[SHP-77 (line)]] | alt | 7.23 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0841× (z -8.9) |
| [[LoVo (line)]] | wt | 6.05 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0567× (z -13.3) |
| [[MIA PaCa-2 (line)]] | alt | 8.89 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H2030 (line)]] | alt | 28.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 13.4 | 0 | 1 | — | [[Cepharanthine (drug)]] 5 µM 0.186× (z -9.2) |
| [[SW480 (line)]] | alt | 6.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.01× (z +11.9) | — |
| [[A-172 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.22 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4094), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DICER1-AS1]] | +0.69 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[UNK]] | +0.68 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[ATAD2B]] | +0.67 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[RAF1]] | +0.67 | +0.34 / +0.53 | both halves | 1e-04 |  |
| [[C2orf42]] | +0.66 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[HOXB7]] | +0.65 | +0.31 / +0.58 | both halves | 2e-04 |  |
| [[CASD1]] | +0.65 | +0.58 / +0.38 | both halves | 6e-05 |  |
| [[C1orf56]] | +0.65 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[SMIM27]] | +0.65 | +0.41 / +0.67 | both halves | 4e-05 |  |
| [[NDUFC1]] | +0.64 | +0.39 / +0.65 | both halves | 5e-05 |  |
| [[SIAH1]] | +0.64 | +0.45 / +0.39 | both halves | 5e-05 |  |
| [[ENDOG]] | +0.64 | +0.46 / +0.61 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF21B]] | -0.57 | -0.51 / -0.21 | both halves | 7e-04 |  |
| [[PRKCZ]] | -0.57 | -0.37 / -0.38 | both halves | 7e-05 |  |
| [[TPCN2]] | -0.56 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[CADM4]] | -0.56 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[CMIP]] | -0.55 | -0.43 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ACOT2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers ACOT2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[EMP1]] | B | EMP1 activity lowers ACOT2's level | lines that do not express EMP1 (10) vs lines expressing it (40) | 2.01× higher at baseline in the lines without EMP1 | 0.059 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.757). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-5.2, 15.5); signed map (25.3, -15.8). **Vector** length 63.8, 12.1% of its response variance represented; |z| ≥ 3 in 587 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +14.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.6 | +1.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.5 | -4.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.7 | -7.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.4 | -5.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.3 | -7.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.2 | -3.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -3.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.8 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -0.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA thioesterase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:73,567,620-73,575,658 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Mte1, ZAP128 |
| Gene groups (HGNC) | Acyl-CoA thioesterases; Thioester hydrolases |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Reactome | 10 pathways, smallest: Mitochondrial Fatty Acid Beta-Oxidation; Maturation of DENV proteins; Peroxisomal protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [P49753](https://www.uniprot.org/uniprotkb/P49753) (Acyl-coenzyme A thioesterase 2, mitochondrial):

> Catalyzes the hydrolysis of acyl-CoAs into free fatty acids and coenzyme A (CoASH), regulating their respective intracellular levels. Displays higher activity toward long chain acyl CoAs (C14-C20). The enzyme is involved in enhancing the hepatic fatty acid oxidation in mitochondria (By similarity).

**Summary**, from NCBI Gene [10965](https://www.ncbi.nlm.nih.gov/gene/10965):

> This gene encodes a member of the acyl-CoA thioesterase protein family, and is one of four acyl-CoA hydrolase genes located in a cluster on chromosome 14. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:18431](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18431) · Entrez [10965](https://www.ncbi.nlm.nih.gov/gene/10965) · UniProt [P49753](https://www.uniprot.org/uniprotkb/P49753) · Ensembl [ENSG00000119673](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119673)

## Data

Gene col 4094: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4094); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4094, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4094]; `tensor/DDL_lfc|DDL_z.npy` [4094]; `embed/gene_vectors.npy` [4094]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4094 or target_col == 4094). Every well: [[ACOT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACOT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
