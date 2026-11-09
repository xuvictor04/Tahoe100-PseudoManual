---
symbol: "COA4"
type: "gene"
col: 11226
ensembl_id: "ENSG00000181924"
name: "cytochrome c oxidase assembly factor 4 homolog"
location: "11q13.4"
module: 1
arm: "+"
pooled_cpm: 18.45
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# COA4

*cytochrome c oxidase assembly factor 4 homolog* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.96× (z +6.7, q 1e-08, up in 33 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.69× (z +5.2, q 2e-05, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.683× (z -5.4, q 5e-05, down in 27 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.191×, MIA PaCa-2 0.310×, KATO III 0.381×); [[Orlistat (drug)]] 0.05 µM in 1 line (C32 0.0630×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.207×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRS1]] (+0.78, fdr 7e-06), [[BYSL]] (+0.74, fdr 7e-06), [[TRMT10C]] (+0.72, fdr 7e-06); moves opposite to [[GNAS]] (-0.60, fdr 7e-06), [[CD99]] (-0.58, fdr 2e-05), [[PHF1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAGEA4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11226.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.96×** | +6.7 | 1e-08 | 33/42 (NCI-H460, A498, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +5.8 | 2e-06 | 30/44 (MIA PaCa-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.82×** | +5.7 | 2e-06 | 23/31 (NCI-H1792, A498, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +5.6 | 3e-06 | 20/36 (NCI-H1573, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.69×** | +5.2 | 2e-05 | 32/47 (SW480, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.63×** | +4.9 | 9e-05 | 23/44 (PANC-1, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Pralsetinib (drug)]] 5 µM |  | **2.12×** | +3.6 | 0.022 | 17/45 (NCI-H23, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.022 | 22/47 (NCI-H1792, CFPAC-1, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.37× | +3.1 | 0.12 | 17/47 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.24× | +3.1 | 0.12 | 13/48 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Isocorydine (drug)]] 0.5 µM |  | 1.36× | +3.0 | 0.12 | 12/46 (SW480, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11226.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.191×, MIA PaCa-2 0.310×, KATO III 0.381×); [[Orlistat (drug)]] 0.05 µM in 1 line (C32 0.0630×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.207×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.683×** | -5.4 | 5e-05 | 27/47 (A-427, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.872× | -4.5 | 0.002 | 13/48 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11226. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 35.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -14.8) |
| [[BT-474 (line)]] | alt | 42.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.247× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 11.0 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0630× (z -10.9) |
| [[KATO III (line)]] | alt | 39.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 20.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 30.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.247× (z -9.0) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -8.7) ⚠ cell-cycle shift, explains ~66% of this change |
| [[A-172 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11226), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRS1]] | +0.78 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[BYSL]] | +0.74 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[TRMT10C]] | +0.72 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[MRPL15]] | +0.71 | +0.61 / +0.75 | both halves | 7e-06 |  |
| [[EXOSC2]] | +0.70 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[UMPS]] | +0.69 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[PAK1IP1]] | +0.69 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[DDX10]] | +0.69 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[MRTO4]] | +0.68 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[YDJC]] | +0.68 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[ZNF146]] | +0.67 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[CIAPIN1]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.60 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[CD99]] | -0.58 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[PHF1]] | -0.57 | -0.62 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAGEA4]] | B | MAGEA4 activity raises COA4's level | lines that do not express MAGEA4 (41) vs lines expressing it (9) | 1.35× lower at baseline in the lines without MAGEA4 | 0.067 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.718). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-47.0, -7.5); signed map (-1.2, -43.1). **Vector** length 63.4, 13.1% of its response variance represented; |z| ≥ 3 in 549 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.50 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.51 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.51 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +5.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +2.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +1.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +3.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.3 | +2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -1.8 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -1.5 | +6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.5 | -5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -1.5 | +5.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.1 | -0.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -1.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase assembly factor 4 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:73,872,667-73,876,901 (-) |
| Ensembl biotype | protein_coding |
| Also known as | E2IG2, CMC3; previously CHCHD8 |
| Gene groups (HGNC) | Coiled-coil-helix-coiled-coil-helix domain containing proteins; Mitochondrial respiratory chain complex assembly factors |
| Reactome | 2 pathways, smallest: Mitochondrial protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYJ1](https://www.uniprot.org/uniprotkb/Q9NYJ1) (Cytochrome c oxidase assembly factor 4 homolog, mitochondrial):

> Putative COX assembly factor.

**Summary**, from NCBI Gene [51287](https://www.ncbi.nlm.nih.gov/gene/51287):

> Predicted to be involved in mitochondrial respiratory chain complex IV assembly. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24604](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24604) · Entrez [51287](https://www.ncbi.nlm.nih.gov/gene/51287) · UniProt [Q9NYJ1](https://www.uniprot.org/uniprotkb/Q9NYJ1) · Ensembl [ENSG00000181924](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181924)

## Data

Gene col 11226: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11226); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11226, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11226]; `tensor/DDL_lfc|DDL_z.npy` [11226]; `embed/gene_vectors.npy` [11226]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11226 or target_col == 11226). Every well: [[COA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
