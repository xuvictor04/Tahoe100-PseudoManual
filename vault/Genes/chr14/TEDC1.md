---
symbol: "TEDC1"
type: "gene"
col: 11666
ensembl_id: "ENSG00000185347"
name: "tubulin epsilon and delta complex 1"
location: "14q32.33"
module: 6
arm: "+"
pooled_cpm: 2.68
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# TEDC1

*tubulin epsilon and delta complex 1* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.37× (z +7.7, q 8e-12, up in 2 of 5 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.81× (z +3.9, q 0.006, up in 4 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.261×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0667×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKMYT1]] (+0.65, fdr 7e-06), [[RECQL4]] (+0.64, fdr 7e-06), [[WDR62]] (+0.62, fdr 1e-05); moves opposite to [[NSA2]] (-0.57, fdr 2e-05), [[C9orf85]] (-0.53, fdr 2e-04), [[BTF3]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[YBX2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11666.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.37×** | +7.7 | 8e-12 | 2/5 (NCI-H2347, CFPAC-1) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.24×** | +7.5 | 3e-11 | 4/13 (HOP62, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.77×** | +4.9 | 2e-04 | 2/7 (J82, NCI-H2030) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.65×** | +4.7 | 4e-04 | 12/41 (SW480, MIA PaCa-2, …) | two highest doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +4.5 | 7e-04 | 4/14 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.55×** | +4.1 | 0.004 | 12/44 (SW480, A549, …) | two highest doses | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.36×** | +4.0 | 0.005 | 5/42 (NCI-H2030, NCI-H2347, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.81×** | +3.9 | 0.006 | 4/15 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +3.4 | 0.045 | 0/5 | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.29×** | +3.3 | 0.048 | 7/30 (Hs 766T, A549, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.059 | 6/34 (NCI-H1792, LoVo, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.61×** | +3.1 | 0.080 | 3/28 (SK-MEL-2, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.39×** | +3.1 | 0.098 | 6/36 (SW1417, SW48, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | 1.42× | +3.0 | 0.10 | 3/26 (NCI-H2347, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11666.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.261×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0667×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.877× | -4.4 | 0.006 | 11/46 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.494× | -3.4 | 0.18 | 11/39 (A-427, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.719× | -3.1 | 0.37 | 15/37 (LOX-IMVI, A-427, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11666. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 10.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.261× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 1.78 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0667× (z -8.8) |
| [[A-172 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.736 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.785 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11666), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKMYT1]] | +0.65 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[RECQL4]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[WDR62]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[CHTF18]] | +0.61 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ZWINT]] | +0.60 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[SUV39H1]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[WDR90]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[E2F1]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[ESCO2]] | +0.57 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[TONSL]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[E2F8]] | +0.57 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[TUBG1]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSA2]] | -0.57 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[C9orf85]] | -0.53 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[BTF3]] | -0.53 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[POLR1D]] | -0.51 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[C8orf44-SGK3]] | -0.48 | -0.36 / -0.52 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YBX2]] | B | YBX2 activity raises TEDC1's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 1.37× lower at baseline in the lines without YBX2 | 0.052 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.503). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.0, -42.2); signed map (-35.3, -46.1). **Vector** length 44.0, 5.16% of its response variance represented; |z| ≥ 3 in 880 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.2 | +4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +2.8 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +1.6 | +3.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.5 | +2.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.1 | +3.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.1 | +2.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.1 | +3.1 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -3.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.7 | -1.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.5 | -3.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.9 |
|  | [[EX229 (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | tubulin epsilon and delta complex 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:105,489,855-105,499,575 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C14orf80 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86SX3](https://www.uniprot.org/uniprotkb/Q86SX3) (Tubulin epsilon and delta complex protein 1):

> Acts as a positive regulator of ciliary hedgehog signaling. Required for centriole stability (By similarity). May play a role in counteracting perturbation of actin filaments, such as after treatment with the actin depolymerizing microbial metabolite Chivosazole F.

**Summary**, from NCBI Gene [283643](https://www.ncbi.nlm.nih.gov/gene/283643):

> Involved in microtubule cytoskeleton organization. Located in centrosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20127](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20127) · Entrez [283643](https://www.ncbi.nlm.nih.gov/gene/283643) · UniProt [Q86SX3](https://www.uniprot.org/uniprotkb/Q86SX3) · Ensembl [ENSG00000185347](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185347)

## Data

Gene col 11666: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11666); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11666, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11666]; `tensor/DDL_lfc|DDL_z.npy` [11666]; `embed/gene_vectors.npy` [11666]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11666 or target_col == 11666). Every well: [[TEDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TEDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
