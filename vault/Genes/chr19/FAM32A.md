---
symbol: "FAM32A"
type: "gene"
col: 2543
ensembl_id: "ENSG00000105058"
name: "family with sequence similarity 32 member A"
location: "19p13.11"
module: 12
arm: "+"
pooled_cpm: 38.77
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# FAM32A

*family with sequence similarity 32 member A* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.88× (z +8.8, q 7e-16, up in 45 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF791]] (+0.75, fdr 7e-06), [[GPANK1]] (+0.73, fdr 7e-06), [[DNTTIP2]] (+0.73, fdr 7e-06); moves opposite to [[STT3B]] (-0.64, fdr 7e-06), [[SUMF2]] (-0.63, fdr 1e-05), [[KDM1A]] (-0.61, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF175]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2543.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +8.8 | 7e-16 | 45/48 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.34×** | +8.4 | 2e-14 | 44/48 (SW480, SK-MEL-2, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.86×** | +6.1 | 2e-07 | 43/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +5.8 | 1e-06 | 41/47 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.71×** | +5.1 | 4e-05 | 36/48 (LOX-IMVI, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.60×** | +4.6 | 3e-04 | 37/48 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.61×** | +4.5 | 5e-04 | 23/38 (A-172, SK-MEL-2, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.38×** | +4.5 | 5e-04 | 31/47 (LoVo, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.2 | 0.001 | 29/48 (HOP62, SW1417, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.53×** | +4.2 | 0.001 | 33/47 (LoVo, C32, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.53×** | +4.2 | 0.001 | 34/46 (HS-578T, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.50×** | +4.0 | 0.003 | 30/48 (A549, NCI-H460, …) | two highest doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +3.8 | 0.007 | 30/48 (NCI-H2030, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +3.7 | 0.010 | 31/48 (HOP62, A-427, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.45×** | +3.4 | 0.028 | 29/47 (NCI-H460, A-427, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2543.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.705× | -3.4 | 0.33 | 27/48 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.730× | -3.1 | 0.56 | 26/48 (SK-MEL-2, A498, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2543. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 46.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.86× (z +11.4) | — |
| [[A549 (line)]] | wt | 27.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +10.3) | — |
| [[HOP62 (line)]] | alt | 20.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 31.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 40.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +10.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 42.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.47× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 24.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 34.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +11.0) | — |
| [[RPMI-7951 (line)]] | alt | 43.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 47.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.98× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 44.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +8.8) | — |
| [[A-172 (line)]] | wt | 46.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2543), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF791]] | +0.75 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[GPANK1]] | +0.73 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[DNTTIP2]] | +0.73 | +0.79 / +0.64 | both halves | 7e-06 |  |
| [[ZNF830]] | +0.71 | +0.77 / +0.67 | both halves | 7e-06 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[MFAP1]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[TSSC4]] | +0.69 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[LENG1]] | +0.69 | +0.68 / +0.70 | both halves | 7e-06 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[UTP3]] | +0.69 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.69 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[KIN]] | +0.69 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[SLC4A1AP]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[BOD1L1]] | +0.68 | +0.71 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STT3B]] | -0.64 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[SUMF2]] | -0.63 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[KDM1A]] | -0.61 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[SMG1P1]] | -0.60 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[PPT1]] | -0.60 | -0.58 / -0.65 | both halves | 7e-06 |  |
| [[CS]] | -0.60 | -0.44 / -0.69 | both halves | 3e-05 |  |
| [[TWSG1]] | -0.59 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[CPSF6]] | -0.59 | -0.53 / -0.59 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[CRTAP]] | -0.58 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[LAMP2]] | -0.57 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[SELENON]] | -0.57 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[PON2]] | -0.57 | -0.57 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF175]] | C | ZNF175 activity raises FAM32A's level | lines that do not express ZNF175 (4) vs lines expressing it (46) | 1.28× lower at baseline in the lines without ZNF175 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF567, ZNF675; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.556). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-39.3, 3.1); signed map (-0.8, -16.5). **Vector** length 90.7, 28.1% of its response variance represented; |z| ≥ 3 in 716 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.4 | +8.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.8 | +4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +8.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.0 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +3.7 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.7 | +1.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | -4.7 | +4.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.8 | -0.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.6 | -3.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.6 | -1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.1 | -1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 32 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:16,185,380-16,192,046 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP586O0120, OTAG-12 |
| Gene groups (HGNC) | Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y421](https://www.uniprot.org/uniprotkb/Q9Y421) (Protein FAM32A):

> Isoform 1, but not isoform 2 or isoform 3, may induce G2 arrest and apoptosis. May also increase cell sensitivity to apoptotic stimuli.

**Summary**, from NCBI Gene [26017](https://www.ncbi.nlm.nih.gov/gene/26017):

> Enables RNA binding activity. Predicted to be involved in mRNA splicing, via spliceosome. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24563](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24563) · Entrez [26017](https://www.ncbi.nlm.nih.gov/gene/26017) · UniProt [Q9Y421](https://www.uniprot.org/uniprotkb/Q9Y421) · Ensembl [ENSG00000105058](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105058)

## Data

Gene col 2543: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2543); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2543, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2543]; `tensor/DDL_lfc|DDL_z.npy` [2543]; `embed/gene_vectors.npy` [2543]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2543 or target_col == 2543). Every well: [[FAM32A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM32A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
