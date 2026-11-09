---
symbol: "FAAP20"
type: "gene"
col: 8534
ensembl_id: "ENSG00000162585"
name: "FA core complex associated protein 20"
location: "1p36.33"
module: 3
arm: "+"
pooled_cpm: 17.14
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# FAAP20

*FA core complex associated protein 20* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.13× (z +9.4, q 2e-18, up in 37 of 40 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.480× (z -8.6, q 4e-15, down in 39 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (C-33 A 0.244×, SW480 0.318×, BT-474 0.144×, Panc 03.27 0.234×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C-33 A 0.177×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (H4 0.117×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSNK1G2]] (+0.68, fdr 7e-06), [[B3GAT3]] (+0.66, fdr 7e-06), [[MARK4]] (+0.65, fdr 9e-06); moves opposite to [[NBN]] (-0.60, fdr 1e-05), [[CFL2]] (-0.59, fdr 1e-05), [[ZNF280D]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[C19orf33]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8534.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.13×** | +9.4 | 2e-18 | 37/40 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +6.9 | 2e-09 | 26/30 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.88×** | +4.8 | 2e-04 | 29/38 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +4.8 | 3e-04 | 25/42 (NCI-H2030, A498, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.52×** | +3.5 | 0.056 | 22/44 (HEC-1-A, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.46× | +3.1 | 0.18 | 19/46 (SW1417, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8534.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (C-33 A 0.244×, SW480 0.318×, BT-474 0.144×, Panc 03.27 0.234×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C-33 A 0.177×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (H4 0.117×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.480×** | -8.6 | 4e-15 | 39/47 (C-33 A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.503×** | -5.7 | 3e-06 | 35/47 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.651× | -3.3 | 0.18 | 21/47 (J82, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.664× | -3.1 | 0.23 | 20/48 (LS 180, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8534. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 36.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -10.9) |
| [[BT-474 (line)]] | alt | 9.08 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -10.5) |
| [[H4 (line)]] | wt | 20.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.117× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 9.02 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -9.2) |
| [[SW480 (line)]] | alt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -10.7) |
| [[A-172 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8534), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSNK1G2]] | +0.68 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[B3GAT3]] | +0.66 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[MARK4]] | +0.65 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[RABGEF1P1]] | +0.64 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[SLC39A4]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[TRPT1]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[NFATC2IP-AS1]] | +0.61 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[UBL5]] | +0.61 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[TTLL3]] | +0.61 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[ANKRD13D]] | +0.61 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[METRN]] | +0.61 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[MYO9B]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBN]] | -0.60 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[CFL2]] | -0.59 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[ZNF280D]] | -0.58 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[MBTPS2]] | -0.57 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[DIS3L]] | -0.57 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[FUBP1]] | -0.56 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[TRUB1]] | -0.55 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[SCRN1]] | -0.54 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[ZBTB33]] | -0.54 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[ZXDA]] | -0.53 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[DCLRE1A]] | -0.53 | -0.46 / -0.47 | both halves | 2e-05 | pathway: Fanconi Anemia Pathway; STRING 704 |
| [[DDX1]] | -0.53 | -0.54 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C19orf33]] | B | C19orf33 activity lowers FAAP20's level | lines that do not express C19orf33 (19) vs lines expressing it (31) | 1.26× higher at baseline in the lines without C19orf33 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: KRT80, MISP, AREG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.560). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-11.8, -3.5); signed map (-31.8, 12.6). **Vector** length 53.7, 10.3% of its response variance represented; |z| ≥ 3 in 588 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | -1.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +0.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +0.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.8 | +0.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.1 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.3 | +1.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.2 | +1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | -5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.4 | -8.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.2 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.5 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | FA core complex associated protein 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:2,184,461-2,212,720 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31031; previously C1orf86 |
| Gene groups (HGNC) | Zinc fingers UBZ2 CCHC-type |
| Reactome | 6 pathways, smallest: Fanconi Anemia Pathway; PKR-mediated signaling; Antimicrobial mechanism of IFN-stimulated genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NZ36](https://www.uniprot.org/uniprotkb/Q6NZ36) (Fanconi anemia core complex-associated protein 20):

> Component of the Fanconi anemia (FA) complex required to recruit the FA complex to DNA interstrand cross-links (ICLs) and promote ICLs repair. Following DNA damage recognizes and binds 'Lys-63'-linked ubiquitin generated by RNF8 at ICLs and recruits other components of the FA complex. Promotes translesion synthesis via interaction with REV1.

**Summary**, from NCBI Gene [199990](https://www.ncbi.nlm.nih.gov/gene/199990):

> Enables K63-linked polyubiquitin modification-dependent protein binding activity and ubiquitin-modified protein reader activity. Involved in interstrand cross-link repair and translesion synthesis. Located in chromatin and nuclear body. Part of Fanconi anaemia nuclear complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26428](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26428) · Entrez [199990](https://www.ncbi.nlm.nih.gov/gene/199990) · UniProt [Q6NZ36](https://www.uniprot.org/uniprotkb/Q6NZ36) · Ensembl [ENSG00000162585](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162585)

## Data

Gene col 8534: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8534); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8534, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8534]; `tensor/DDL_lfc|DDL_z.npy` [8534]; `embed/gene_vectors.npy` [8534]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8534 or target_col == 8534). Every well: [[FAAP20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAAP20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
