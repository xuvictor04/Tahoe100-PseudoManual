---
symbol: "GNRH1"
type: "gene"
col: 7183
ensembl_id: "ENSG00000147437"
name: "gonadotropin releasing hormone 1"
location: "8p21.2"
module: 16
arm: "-"
pooled_cpm: 6.28
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# GNRH1

*gonadotropin releasing hormone 1* — 8p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.66× (z +4.8, q 0.001, up in 19 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Belumosudil (drug)]] 5 µM: 0.468× (z -6.9, q 3e-09, down in 29 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL7]] (+0.70, fdr 7e-06), [[STK32C]] (+0.68, fdr 7e-06), [[TBC1D22A-DT]] (+0.67, fdr 7e-06); moves opposite to [[SMIM15]] (-0.70, fdr 7e-06), [[ZNF260]] (-0.69, fdr 7e-06), [[PABIR1]] (-0.69, fdr 7e-06).
> It sits in the **-** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GPR87]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7183.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +4.8 | 0.001 | 19/47 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +4.5 | 0.002 | 14/36 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.5 | 0.002 | 20/41 (NCI-H23, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.68×** | +3.5 | 0.068 | 12/37 (J82, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +3.4 | 0.077 | 12/45 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | 1.41× | +3.2 | 0.12 | 10/45 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.39× | +3.0 | 0.20 | 10/38 (LOX-IMVI, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7183.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **0.468×** | -6.9 | 3e-09 | 29/42 (NCI-H2347, A549, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.521×** | -5.9 | 8e-07 | 25/46 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.656×** | -3.9 | 0.017 | 18/40 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.666×** | -3.8 | 0.017 | 18/45 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.675×** | -3.7 | 0.022 | 16/44 (HOP62, A-172, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.681×** | -3.6 | 0.022 | 10/45 (hTERT-HPNE, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.661×** | -3.6 | 0.022 | 10/19 (NCI-H460, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.764×** | -3.6 | 0.022 | 17/40 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 5 µM |  | **0.784×** | -3.3 | 0.071 | 10/47 (NCI-H460, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7183. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 13.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -11.1) |
| [[A549 (line)]] | wt | 20.5 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.127× (z -10.4) |
| [[HOP62 (line)]] | alt | 11.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0682× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.112× (z -9.8) |
| [[Hs 766T (line)]] | wt | 9.13 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0786× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Fusidic acid (drug)]] 0.5 µM 0.0782× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 7.28 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0697× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 4.37 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.0748× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 7.71 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 6.52 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -10.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7183), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL7]] | +0.70 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[STK32C]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[TBC1D22A-DT]] | +0.67 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[RAB40C]] | +0.66 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[GET1-SH3BGR]] | +0.66 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[SDHAP4-1]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[ZNF250]] | +0.65 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[PPOX]] | +0.65 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[KCTD9]] | +0.65 | +0.67 / +0.60 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 3.2 kb 3′ of KCTD9 on the same strand (can correlate by spillover, not regulation) |
| [[NARF]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[ECT2L]] | +0.64 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[SAP30-DT]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM15]] | -0.70 | -0.64 / -0.67 | both halves | 7e-06 |  |
| [[ZNF260]] | -0.69 | -0.63 / -0.66 | both halves | 7e-06 |  |
| [[PABIR1]] | -0.69 | -0.68 / -0.69 | both halves | 7e-06 |  |
| [[CSTF2T]] | -0.69 | -0.68 / -0.62 | both halves | 7e-06 |  |
| [[ZNF644]] | -0.67 | -0.71 / -0.57 | both halves | 9e-06 |  |
| [[TMEM185B]] | -0.67 | -0.65 / -0.68 | both halves | 7e-06 |  |
| [[SLC35A4]] | -0.67 | -0.70 / -0.62 | both halves | 7e-06 |  |
| [[MGA]] | -0.66 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[MIS12]] | -0.65 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[TIGD2]] | -0.65 | -0.71 / -0.57 | both halves | 1e-05 |  |
| [[PUF60]] | -0.64 | -0.56 / -0.68 | both halves | 1e-05 |  |
| [[CENPBD1P]] | -0.64 | -0.66 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR87]] | B | GPR87 activity lowers GNRH1's level | lines that do not express GPR87 (36) vs lines expressing it (14) | 1.39× higher at baseline in the lines without GPR87 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, MUC16, HEPHL1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **-** arm (projection on the module's main direction -0.701). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-32.1, 13.6); signed map (-41.2, 13.9). **Vector** length 73.3, 12.8% of its response variance represented; |z| ≥ 3 in 855 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.9 | +2.3 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.5 | +2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +1.0 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +1.3 | +1.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.0 | -5.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.8 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -6.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.3 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -2.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.9 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | gonadotropin releasing hormone 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.2 — chr8:25,419,258-25,424,654 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LNRH; previously GRH, GNRH, LHRH |
| Gene groups (HGNC) | Gonadotropin releasing hormone family |
| Reactome | 5 pathways, smallest: Class A/1 (Rhodopsin-like receptors); G alpha (q) signalling events; GPCR ligand binding |
| Matched by | ensembl_id |

**Function**, from UniProt [P01148](https://www.uniprot.org/uniprotkb/P01148) (Progonadoliberin-1):

> [Gonadoliberin-1]: Hypothalamic decapeptide hormone that functions as the master regulator of the hypothalamic-pituitary-gonadal axis. Released in a pulsatile manner from hypothalamic neuron terminals into the hypophyseal portal circulation, it acts on pituitary gonadotrope cells by binding to and activating its cognate G protein-coupled receptor GNRHR, thereby stimulating the synthesis and secretion of the gonadotropins luteinizing hormone (LH) and follicle-stimulating hormone (FSH), which in …

**Summary**, from NCBI Gene [2796](https://www.ncbi.nlm.nih.gov/gene/2796):

> This gene encodes a preproprotein that is proteolytically processed to generate a peptide that is a member of the gonadotropin-releasing hormone (GnRH) family of peptides. Alternative splicing results in multiple transcript variants, at least one of which is secreted and then cleaved to generate gonadoliberin-1 and GnRH-associated peptide 1. Gonadoliberin-1 stimulates the release of luteinizing and follicle stimulating hormones, which are important for reproduction. Mutations in this gene are …

**Accessions** — [HGNC:4419](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4419) · Entrez [2796](https://www.ncbi.nlm.nih.gov/gene/2796) · UniProt [P01148](https://www.uniprot.org/uniprotkb/P01148) · Ensembl [ENSG00000147437](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147437)

## Data

Gene col 7183: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7183); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7183, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7183]; `tensor/DDL_lfc|DDL_z.npy` [7183]; `embed/gene_vectors.npy` [7183]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7183 or target_col == 7183). Every well: [[GNRH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNRH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
