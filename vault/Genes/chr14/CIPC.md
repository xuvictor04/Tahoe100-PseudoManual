---
symbol: "CIPC"
type: "gene"
col: 12724
ensembl_id: "ENSG00000198894"
name: "CLOCK interacting pacemaker"
location: "14q24.3"
module: 29
arm: "+"
pooled_cpm: 6.95
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# CIPC

*CLOCK interacting pacemaker* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.53× (z +5.3, q 6e-05, up in 24 of 47 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.67× (z +4.5, q 0.002, up in 21 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (LS 180 0.0586×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.166×; ⚠ toxic; transcription drop); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (RKO 0.0797×); [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (SHP-77 0.109×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPT1]] (+0.80, fdr 7e-06), [[COPS7B]] (+0.76, fdr 7e-06), [[NAXD]] (+0.74, fdr 7e-06); moves opposite to [[LINC02804]] (-0.66, fdr 7e-06), [[NBPF10]] (-0.65, fdr 7e-06), [[TINCR]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LAMB3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SPG21]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12724.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.53×** | +5.3 | 6e-05 | 24/47 (LOX-IMVI, RKO, …) | rises with dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.67×** | +4.5 | 0.002 | 21/47 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.48× | +3.4 | 0.11 | 8/47 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +3.3 | 0.12 | 5/48 (C-33 A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.48× | +3.2 | 0.14 | 5/47 (HOP62, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 1.99× | +3.2 | 0.14 | 11/47 (KATO III, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.45× | +3.1 | 0.15 | 8/48 (Panc 03.27, SW480, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.42× | +3.1 | 0.16 | 8/36 (SW1417, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 1.92× | +3.0 | 0.16 | 11/42 (LS 180, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12724.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (LS 180 0.0586×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.166×; ⚠ toxic; transcription drop); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (RKO 0.0797×); [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (SHP-77 0.109×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.665× | -3.5 | 0.28 | 17/42 (Panc 03.27, NCI-H23, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.692× | -3.2 | 0.32 | 13/45 (NCI-H23, C-33 A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.780× | -3.1 | 0.32 | 18/44 (SW480, LOX-IMVI, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12724. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 4.07 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM 0.0670× (z -8.5) |
| [[LS 180 (line)]] | wt | 6.23 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0586× (z -10.5) |
| [[RKO (line)]] | wt | 8.00 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0797× (z -9.1) |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.109× (z -8.9) |
| [[SW480 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.166× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.59 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12724), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPT1]] | +0.80 | +0.81 / +0.78 | both halves | 7e-06 |  |
| [[COPS7B]] | +0.76 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[NAXD]] | +0.74 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[PPP2R1B]] | +0.72 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[PGAM1]] | +0.69 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[ZC3HAV1L]] | +0.68 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[USF1]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[C1orf198]] | +0.67 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[CRKL]] | +0.66 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[RPE]] | +0.66 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[FKBP9]] | +0.66 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[FUCA2]] | +0.65 | +0.52 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02804]] | -0.66 | -0.65 / -0.67 | both halves | 7e-06 |  |
| [[NBPF10]] | -0.65 | -0.69 / -0.59 | both halves | 7e-06 |  |
| [[TINCR]] | -0.59 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[OFD1]] | -0.59 | -0.71 / -0.57 | both halves | 1e-05 |  |
| [[RAP1B]] | -0.58 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[ATF4]] | -0.58 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[IER5]] | -0.58 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[ZSWIM6]] | -0.58 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[INAFM1]] | -0.57 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[MIDN]] | -0.57 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[NBPF14]] | -0.57 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[METTL23]] | -0.57 | -0.59 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMB3]] | B | LAMB3 activity lowers CIPC's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 1.31× higher at baseline in the lines without LAMB3 | 0.013 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPG21]] | C | CIPC's natural level weakens SPG21's drug response | CIPC's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.04; direction not clear | 0.036 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.771). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-26.2, -22.7); signed map (-20.4, -38.2). **Vector** length 67.9, 11.1% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.8 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.0 | +2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.6 | +1.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.5 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.6 | +2.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.5 | +1.5 |
|  | [[Erlotinib (drug)]] 5 µM |  | +1.4 | +0.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.9 | -3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.8 | -3.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.7 | -2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | CLOCK interacting pacemaker |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:77,098,126-77,117,287 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA1737 |
| Reactome | 2 pathways, smallest: Phosphorylated BMAL1:CLOCK (ARNTL:CLOCK) activates expression of core clock genes; Circadian clock |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0C6](https://www.uniprot.org/uniprotkb/Q9C0C6) (CLOCK-interacting pacemaker):

> Transcriptional repressor which may act as a negative-feedback regulator of CLOCK-BMAL1 transcriptional activity in the circadian-clock mechanism. May stimulate BMAL1-dependent phosphorylation of CLOCK. However, the physiological relevance of these observations is unsure, since experiments in an animal model showed that CIPC is not critially required for basic circadian clock.

**Summary**, from NCBI Gene [85457](https://www.ncbi.nlm.nih.gov/gene/85457):

> Predicted to be involved in negative regulation of DNA-templated transcription and negative regulation of circadian rhythm. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20365](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20365) · Entrez [85457](https://www.ncbi.nlm.nih.gov/gene/85457) · UniProt [Q9C0C6](https://www.uniprot.org/uniprotkb/Q9C0C6) · Ensembl [ENSG00000198894](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198894)

## Data

Gene col 12724: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12724); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12724, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12724]; `tensor/DDL_lfc|DDL_z.npy` [12724]; `embed/gene_vectors.npy` [12724]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12724 or target_col == 12724). Every well: [[CIPC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CIPC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
