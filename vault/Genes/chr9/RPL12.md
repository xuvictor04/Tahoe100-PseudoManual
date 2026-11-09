---
symbol: "RPL12"
type: "gene"
col: 12497
ensembl_id: "ENSG00000197958"
name: "ribosomal protein L12"
location: "9q33.3"
module: 43
arm: "+"
pooled_cpm: 423.07
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPL12

*ribosomal protein L12* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.96× (z +6.3, q 1e-07, up in 43 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.54× (z +3.7, q 0.020, up in 37 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.85×).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.480× (z -6.3, q 2e-07, down in 44 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (RKO 0.235×, C-33 A 0.279×, RPMI-7951 0.289×, SNU-1 0.287×, …).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL26]] (+0.95, fdr 7e-06), [[RPS8]] (+0.93, fdr 7e-06), [[RPLP1]] (+0.93, fdr 7e-06); moves opposite to [[SLC35A4]] (-0.67, fdr 7e-06), [[MIS12]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF69]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12497.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.85×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.96×** | +6.3 | 1e-07 | 43/44 (HS-578T, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.71×** | +6.1 | 3e-07 | 49/49 (C32, SW 900, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.16×** | +4.3 | 0.003 | 42/45 (C32, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +4.2 | 0.003 | 47/47 (HepG2/C3A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.97×** | +4.1 | 0.004 | 47/48 (SW 900, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.020 | 37/49 (NCI-H2347, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12497.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (RKO 0.235×, C-33 A 0.279×, RPMI-7951 0.289×, SNU-1 0.287×, …).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.480×** | -6.3 | 2e-07 | 44/48 (RKO, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.587× | -3.2 | 0.38 | 37/48 (SNU-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12497. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 423 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -10.1) |
| [[C-33 A (line)]] | alt | 377 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -11.1) |
| [[CHP-212 (line)]] | wt | 342 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 391 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 630 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 310 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 429 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 453 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +9.0) | — |
| [[RKO (line)]] | wt | 760 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -12.1) |
| [[RPMI-7951 (line)]] | alt | 258 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -10.3) |
| [[SNU-1 (line)]] | wt | 471 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -10.2) |
| [[A-172 (line)]] | wt | 274 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 434 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 408 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 496 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 410 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 446 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 194 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 249 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 337 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 327 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 529 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 506 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 361 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 340 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 409 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 370 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 378 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 379 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 647 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 524 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 635 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 272 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 318 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 546 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 448 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 367 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 483 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 381 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 299 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 401 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 235 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 328 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 319 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 530 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 646 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 436 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12497), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 22 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL26]] | +0.95 | +0.93 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.93 | +0.91 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPLP1]] | +0.93 | +0.90 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL19]] | +0.93 | +0.89 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL31]] | +0.93 | +0.93 / +0.91 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL13]] | +0.93 | +0.95 / +0.91 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS12]] | +0.93 | +0.87 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS20]] | +0.92 | +0.92 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL11]] | +0.92 | +0.94 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS14]] | +0.92 | +0.92 / +0.89 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS27]] | +0.92 | +0.90 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL27A]] | +0.92 | +0.89 / +0.89 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35A4]] | -0.67 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[MIS12]] | -0.67 | -0.60 / -0.64 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF69]] | B | ZNF69 activity lowers RPL12's level | lines that do not express ZNF69 (15) vs lines expressing it (35) | 1.17× higher at baseline in the lines without ZNF69 | 0.060 | ⚠ within organs, on part of the lines; also absent: TNFRSF14, TNFRSF14-AS1, CIART |
| [[RGS10]] | C | RGS10 activity raises RPL12's level | lines that do not express RGS10 (4) vs lines expressing it (46) | 1.55× lower at baseline in the lines without RGS10 | 0.031 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HOMER3, ARHGEF17, CHST3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.947). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.9, -28.6); signed map (-60.6, -5.2). **Vector** length 96.6, 64.9% of its response variance represented; |z| ≥ 3 in 485 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.80 to 19); *Translation initiation complex formation* (reactome, mean cos +0.77 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.77 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +1.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.3 | +1.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +0.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.4 | +1.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.2 | +0.7 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.1 | -0.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | +0.3 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.0 | +0.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -7.3 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -6.9 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -6.7 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.8 | -3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.3 | -6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -1.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:127,447,674-127,451,406 (-) |
| Ensembl biotype | protein_coding |
| Also known as | L12, uL11 |
| Gene groups (HGNC) | L ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P30050](https://www.uniprot.org/uniprotkb/P30050) (Large ribosomal subunit protein uL11):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. Binds directly to 26S ribosomal RNA.

**Summary**, from NCBI Gene [6136](https://www.ncbi.nlm.nih.gov/gene/6136):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L11P family of ribosomal proteins. It is located in the cytoplasm. The protein binds directly to the 26S rRNA. This gene is co-transcribed with the U65 snoRNA, which is …

**Accessions** — [HGNC:10302](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10302) · Entrez [6136](https://www.ncbi.nlm.nih.gov/gene/6136) · UniProt [P30050](https://www.uniprot.org/uniprotkb/P30050) · Ensembl [ENSG00000197958](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197958)

## Data

Gene col 12497: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12497); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12497, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12497]; `tensor/DDL_lfc|DDL_z.npy` [12497]; `embed/gene_vectors.npy` [12497]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12497 or target_col == 12497). Every well: [[RPL12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
