---
symbol: "EIF4H"
type: "gene"
col: 2792
ensembl_id: "ENSG00000106682"
name: "eukaryotic translation initiation factor 4H"
location: "7q11.23"
module: 25
arm: "+"
pooled_cpm: 100.64
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 3
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# EIF4H

*eukaryotic translation initiation factor 4H* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.27× (z +8.4, q 2e-14, up in 43 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.10× (z +4.0, q 0.006, up in 40 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 0.582× (z -3.9, q 0.035, down in 42 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ipatasertib (drug)]] 0.5 µM in 1 line (HCT15 0.144×); [[Sulfatinib (drug)]] 0.05 µM in 1 line (SW 1088 0.0938×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NONO]] (+0.82, fdr 7e-06), [[LIN7C]] (+0.82, fdr 7e-06), [[EEF1A1]] (+0.80, fdr 7e-06); moves opposite to [[ZBTB7A]] (-0.66, fdr 1e-05), [[RPL36AL]] (-0.65, fdr 8e-05, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[CROCCP2-1]] (-0.64, fdr 7e-06), [[SNHG9]] (-0.64, fdr 4e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CTSZ]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2792.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.27×** | +8.4 | 2e-14 | 43/50 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +6.0 | 7e-07 | 41/49 (SW480, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +5.5 | 8e-06 | 35/44 (A-427, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +5.1 | 5e-05 | 38/45 (HS-578T, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.10×** | +4.0 | 0.006 | 40/49 (NCI-H1573, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.47×** | +4.0 | 0.006 | 37/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.017 | 31/48 (KATO III, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.93×** | +3.5 | 0.028 | 33/48 (NCI-H1573, SW48, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2792.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ipatasertib (drug)]] 0.5 µM in 1 line (HCT15 0.144×); [[Sulfatinib (drug)]] 0.05 µM in 1 line (SW 1088 0.0938×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.582×** | -3.9 | 0.035 | 42/48 (HCT15, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.690×** | -3.8 | 0.035 | 43/49 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.614×** | -3.5 | 0.093 | 39/48 (Hs 766T, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.643× | -3.2 | 0.22 | 33/47 (SW 900, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 0.811× | -3.1 | 0.24 | 27/49 (HEC-1-A, H4, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2792. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 80.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.40× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 162 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.144× (z -9.9) |
| [[SW 1088 (line)]] | alt | 139 | 0 | 1 | — | [[Sulfatinib (drug)]] 0.05 µM 0.0938× (z -8.6) |
| [[A-172 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 91.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 151 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 98.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 91.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 198 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 86.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 141 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 63.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 84.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 99.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 81.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 133 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 99.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 75.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 79.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 95.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 87.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 87.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 98.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2792), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NONO]] | +0.82 | +0.76 / +0.84 | both halves | 7e-06 | same gene group; STRING 403 |
| [[LIN7C]] | +0.82 | +0.59 / +0.84 | both halves | 7e-06 |  |
| [[EEF1A1]] | +0.80 | +0.74 / +0.81 | both halves | 7e-06 | STRING 494 |
| [[DCTN1]] | +0.79 | +0.74 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[DHFR]] | +0.78 | +0.69 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[TWF1]] | +0.76 | +0.63 / +0.78 | both halves | 7e-06 |  |
| [[CAPRIN1]] | +0.73 | +0.55 / +0.80 | both halves | 1e-05 |  |
| [[EEF1A1P5]] | +0.73 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[FKBP9]] | +0.72 | +0.61 / +0.76 | both halves | 7e-06 |  |
| [[AP2M1]] | +0.72 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[RPN1]] | +0.72 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[ZNF664]] | +0.72 | +0.49 / +0.77 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB7A]] | -0.66 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | -0.65 | -0.37 / -0.70 | both halves | 8e-05 | pathway: Cap-dependent Translation Initiation; ⚠ in the vector space only through flagged drug-doses |
| [[CROCCP2-1]] | -0.64 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[SNHG9]] | -0.64 | -0.42 / -0.71 | both halves | 4e-05 |  |
| [[SMIM26]] ⚠ | -0.63 | -0.41 / -0.67 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[DNLZ]] | -0.63 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[CTBP1-AS]] ⚠ | -0.62 | -0.44 / -0.62 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PPP1R35]] ⚠ | -0.62 | -0.47 / -0.62 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF593]] | -0.61 | -0.33 / -0.70 | both halves | 1e-04 |  |
| [[NSUN5P2-1]] ⚠ | -0.60 | -0.40 / -0.65 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LINC00685]] | -0.60 | -0.47 / -0.68 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSZ]] | B | CTSZ activity raises EIF4H's level | lines that do not express CTSZ (8) vs lines expressing it (42) | 1.14× lower at baseline in the lines without CTSZ | 0.062 | ⚠ within organs, on part of the lines; also absent: LRRK1, CAV2, PIWIL4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.840). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-29.4, -23.9); signed map (-20.4, -35.8). **Vector** length 120, 39.4% of its response variance represented; |z| ≥ 3 in 662 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.1 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.5 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.1 | +5.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.3 | +1.8 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +3.0 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +2.9 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +2.8 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.7 | +1.5 |
|  | [[Riluzole hydrochloride (drug)]] 0.5 µM |  | +2.7 | +2.2 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -4.8 | -3.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.6 | +0.7 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -3.7 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +1.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -3.2 | -3.5 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -3.1 | -1.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 4H |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:74,174,231-74,197,122 (+) |
| Ensembl biotype | protein_coding |
| Also known as | WSCR1, KIAA0038; previously WBSCR1 |
| Gene groups (HGNC) | RNA binding motif containing; MicroRNA protein coding host genes |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 8 pathways, smallest: Ribosomal scanning and start codon recognition; Translation initiation complex formation; Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15056](https://www.uniprot.org/uniprotkb/Q15056) (Eukaryotic translation initiation factor 4H):

> Stimulates the RNA helicase activity of EIF4A in the translation initiation complex. Binds weakly mRNA.

**Summary**, from NCBI Gene [7458](https://www.ncbi.nlm.nih.gov/gene/7458):

> This gene encodes one of the translation initiation factors, which functions to stimulate the initiation of protein synthesis at the level of mRNA utilization. This gene is deleted in Williams syndrome, a multisystem developmental disorder caused by the deletion of contiguous genes at 7q11.23. Alternative splicing of this gene generates 2 transcript variants. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12741](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12741) · Entrez [7458](https://www.ncbi.nlm.nih.gov/gene/7458) · UniProt [Q15056](https://www.uniprot.org/uniprotkb/Q15056) · Ensembl [ENSG00000106682](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106682)

## Data

Gene col 2792: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2792); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2792, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2792]; `tensor/DDL_lfc|DDL_z.npy` [2792]; `embed/gene_vectors.npy` [2792]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2792 or target_col == 2792). Every well: [[EIF4H — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF4H.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
