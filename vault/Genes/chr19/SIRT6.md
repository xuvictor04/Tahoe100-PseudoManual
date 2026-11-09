---
symbol: "SIRT6"
type: "gene"
col: 1189
ensembl_id: "ENSG00000077463"
name: "sirtuin 6"
location: "19p13.3"
module: 20
arm: "-"
pooled_cpm: 10.81
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# SIRT6

*sirtuin 6* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.16× (z +8.8, q 9e-16, up in 40 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (AsPC-1 0.0800×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.138×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED10]] (+0.67, fdr 1e-05), [[GGT7]] (+0.66, fdr 9e-06), [[RCE1]] (+0.66, fdr 1e-05); moves opposite to [[IPO5]] (-0.66, fdr 1e-05), [[CAPRIN1]] (-0.66, fdr 1e-05), [[RCN1]] (-0.65, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1189.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.16×** | +8.8 | 9e-16 | 40/46 (SW480, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +6.7 | 6e-09 | 22/40 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.50×** | +6.5 | 2e-08 | 30/47 (PANC-1, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +6.4 | 3e-08 | 30/43 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.68×** | +5.9 | 4e-07 | 28/45 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.71×** | +5.2 | 2e-05 | 27/46 (PANC-1, A498, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.58×** | +5.2 | 2e-05 | 25/46 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.52×** | +4.7 | 2e-04 | 22/47 (LoVo, SW480, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.7 | 2e-04 | 20/44 (A498, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +4.6 | 2e-04 | 20/47 (LS 180, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.45×** | +4.2 | 0.001 | 20/47 (PANC-1, SW480, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.43×** | +4.0 | 0.002 | 17/47 (LoVo, RKO, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +4.0 | 0.002 | 18/43 (HEC-1-A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +3.9 | 0.004 | 19/47 (LS 180, SW48, …) | rises with dose | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.86×** | +3.7 | 0.008 | 9/22 (HS-578T, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +3.5 | 0.014 | 18/45 (RKO, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.57×** | +3.0 | 0.073 | 6/42 (SHP-77, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (AsPC-1 0.0800×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.138×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1189. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 9.39 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0800× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 5.94 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +9.0) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[RKO (line)]] | wt | 12.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +8.6) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[A-172 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.99 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.83 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1189), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED10]] | +0.67 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[GGT7]] | +0.66 | +0.57 / +0.71 | both halves | 9e-06 |  |
| [[RCE1]] | +0.66 | +0.53 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT |
| [[INAFM1]] | +0.66 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | +0.66 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | +0.65 | +0.51 / +0.65 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NOSIP]] | +0.65 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[ARID3A]] | +0.65 | +0.42 / +0.68 | both halves | 4e-05 |  |
| [[ZNF791]] | +0.64 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[RNF181]] | +0.63 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[RGP1]] | +0.62 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[UBE2B]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[MARCHF9]] | +0.60 | +0.41 / +0.65 | both halves | 4e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO5]] | -0.66 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[CAPRIN1]] | -0.66 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[RCN1]] | -0.65 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[CD99L2]] | -0.64 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[HNRNPA3]] | -0.63 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[HNRNPR]] | -0.63 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[PIGK]] | -0.63 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[TFDP1]] | -0.63 | -0.61 / -0.57 | both halves | 9e-06 | pathway: Pre-NOTCH Expression and Processing |
| [[NONO]] | -0.62 | -0.47 / -0.65 | both halves | 2e-05 |  |
| [[MTHFD1]] | -0.62 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[DHFR]] | -0.62 | -0.40 / -0.63 | both halves | 5e-05 |  |
| [[FKBP9]] | -0.61 | -0.51 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.692). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-31.5, -27.2); signed map (-15.7, 0.1). **Vector** length 60.6, 10.1% of its response variance represented; |z| ≥ 3 in 654 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.9 | +8.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +2.4 | +6.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +1.8 | +6.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +1.7 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +3.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.4 | +2.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +2.0 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.7 | -1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.4 | -1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.3 | -0.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.6 | -1.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -0.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.1 | -0.4 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | sirtuin 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:4,174,109-4,182,566 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sirtuins |
| Hallmark sets | COMPLEMENT |
| Reactome | 11 pathways, smallest: NAD+ and Sirtuins regulate the circadian clock; Regulation of the circadian clock; Pre-NOTCH Transcription and Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N6T7](https://www.uniprot.org/uniprotkb/Q8N6T7) (NAD-dependent protein deacylase sirtuin-6):

> NAD-dependent protein deacetylase, deacylase and mono-ADP-ribosyltransferase that plays an essential role in DNA damage repair, telomere maintenance, metabolic homeostasis, inflammation, tumorigenesis and aging. Displays protein-lysine deacetylase or defatty-acylase (demyristoylase and depalmitoylase) activity, depending on the context. Acts as a key histone deacetylase by catalyzing deacetylation of histone H3 at 'Lys-9', 'Lys-18' and 'Lys-56' (H3K9ac, H3K18ac and H3K56ac, respectively), …

**Summary**, from NCBI Gene [51548](https://www.ncbi.nlm.nih.gov/gene/51548):

> This gene encodes a member of the sirtuin family of NAD-dependent enzymes that are implicated in cellular stress resistance, genomic stability, aging and energy homeostasis. The encoded protein is localized to the nucleus, exhibits ADP-ribosyl transferase and histone deacetylase activities, and plays a role in DNA repair, maintenance of telomeric chromatin, inflammation, lipid and glucose metabolism. Alternative splicing results in multiple transcript variants encoding different isoforms. …

**Accessions** — [HGNC:14934](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14934) · Entrez [51548](https://www.ncbi.nlm.nih.gov/gene/51548) · UniProt [Q8N6T7](https://www.uniprot.org/uniprotkb/Q8N6T7) · Ensembl [ENSG00000077463](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077463)

## Data

Gene col 1189: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1189); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1189, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1189]; `tensor/DDL_lfc|DDL_z.npy` [1189]; `embed/gene_vectors.npy` [1189]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1189 or target_col == 1189). Every well: [[SIRT6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIRT6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
