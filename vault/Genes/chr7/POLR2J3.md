---
symbol: "POLR2J3"
type: "gene"
col: 9617
ensembl_id: "ENSG00000168255"
name: "RNA polymerase II subunit J3"
location: "7q22.1"
module: 25
arm: "+"
pooled_cpm: 6.25
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# POLR2J3

*RNA polymerase II subunit J3* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.25× (z +8.2, q 1e-13, up in 35 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Nimesulide (drug)]] 5 µM in 1 line (A-427 0.0818×; ⚠ toxic; unreliable plate only); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (HT-29 0.0966×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 0.148×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Apalutamide (drug)]] 5 µM in 1 line (LOX-IMVI 0.0553×); [[Cobimetinib (drug)]] 0.05 µM in 1 line (J82 0.0881×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANAPC2]] (+0.67, fdr 1e-05), [[CEP170B]] (+0.67, fdr 1e-05), [[SF3A1]] (+0.66, fdr 7e-06); moves opposite to [[GPHN]] (-0.53, fdr 1e-04), [[C15orf61]] (-0.49, fdr 4e-05, ⚠ C15orf61 in the vector space only through flagged drug-doses), [[MPLKIP]] (-0.49, fdr 0.002, ⚠ one half only (not replicated)), [[SUMO4]] (-0.47, fdr 2e-04), [[DMAC1]] (-0.45, fdr 6e-04).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9617.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.25×** | +8.2 | 1e-13 | 35/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.98×** | +7.0 | 1e-09 | 28/45 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.92×** | +6.3 | 5e-08 | 26/47 (SW480, J82, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +4.9 | 1e-04 | 16/40 (PANC-1, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.58×** | +4.7 | 3e-04 | 17/46 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +4.5 | 5e-04 | 4/12 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.7 | 0.017 | 4/48 (NCI-H23, A-427, …) | inconsistent across doses |  |
| [[Valdecoxib (drug)]] 0.5 µM |  | **1.43×** | +3.7 | 0.018 | 10/43 (SW 900, H4, …) | inconsistent across doses | position effect removed |
| [[Folic acid (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.033 | 7/48 (Hs 766T, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[Saquinavir (drug)]] 0.5 µM |  | 1.36× | +3.1 | 0.10 | 4/40 (COLO 205, LS 180, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9617.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Nimesulide (drug)]] 5 µM in 1 line (A-427 0.0818×; ⚠ toxic; unreliable plate only); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (HT-29 0.0966×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 0.148×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Apalutamide (drug)]] 5 µM in 1 line (LOX-IMVI 0.0553×); [[Cobimetinib (drug)]] 0.05 µM in 1 line (J82 0.0881×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 0.730× | -3.1 | 0.60 | 11/34 (HS-578T, J82, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[AT7519 (drug)]] 0.05 µM |  | 0.728× | -3.1 | 0.60 | 7/45 (hTERT-HPNE, SW480, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9617. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 6.26 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0818× (z -9.8) ⚠ toxic; unreliable plate only |
| [[HT-29 (line)]] | alt | 8.00 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0966× (z -9.3) |
| [[J82 (line)]] | alt | 5.84 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0881× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 3.70 | 0 | 1 | — | [[Apalutamide (drug)]] 5 µM 0.0553× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 9.62 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.148× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SW 900 (line)]] | alt | 5.72 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0716× (z -8.8) |
| [[A-172 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.78 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9617), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC2]] | +0.67 | +0.51 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[CEP170B]] | +0.67 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[SF3A1]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[WASH8P]] ⚠ | +0.65 | +0.43 / +0.79 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[DLST]] | +0.60 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[EIF4H]] | +0.59 | +0.39 / +0.61 | both halves | 6e-05 |  |
| [[ACADVL]] | +0.58 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[HIF1AN]] | +0.57 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[DCTN1]] | +0.56 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[DBN1]] | +0.56 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[CCDC61]] | +0.56 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[LIN7C]] | +0.56 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[BAG6]] | +0.56 | +0.52 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 4 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPHN]] | -0.53 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[C15orf61]] ⚠ | -0.49 | -0.41 / -0.48 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MPLKIP]] | -0.49 | -0.12 / -0.55 | ⚠ one half (not replicated) | 0.002 |  |
| [[F12]] | -0.49 | -0.18 / -0.48 | ⚠ not reproduced | 9e-04 |  |
| [[SUMO4]] | -0.47 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[DMAC1]] | -0.45 | -0.21 / -0.49 | both halves | 6e-04 |  |
| [[MTLN]] ⚠ | -0.45 | -0.28 / -0.50 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[HOXB5]] | -0.45 | -0.42 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers POLR2J3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.413). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-19.2, -23.9); signed map (-14.6, -33.2). **Vector** length 39.6, 3.75% of its response variance represented; |z| ≥ 3 in 919 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.7 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.2 | +1.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.8 | +2.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.6 | +8.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.9 | +1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +0.9 | +2.5 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | +0.8 | +1.1 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +0.7 | +2.8 |
|  | [[Adenine (drug)]] 0.05 µM |  | +0.7 | +1.8 |
| fall | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -0.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +0.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | +1.3 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.5 | +6.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -2.6 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.1 | -2.0 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase II subunit J3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:102,537,918-102,572,653 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RNA polymerase subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H1A7](https://www.uniprot.org/uniprotkb/Q9H1A7) (DNA-directed RNA polymerase II subunit RPB11-b2):

> DNA-dependent RNA polymerase catalyzes the transcription of DNA into RNA using the four ribonucleoside triphosphates as substrates. Component of RNA polymerase II which synthesizes mRNA precursors and many functional non-coding RNAs. Pol II is the central component of the basal RNA polymerase II transcription machinery. It is composed of mobile elements that move relative to each other. RPB11 is part of the core element with the central large cleft (By similarity).

**Summary**, from NCBI Gene [548644](https://www.ncbi.nlm.nih.gov/gene/548644):

> This gene is a member of the RNA polymerase II subunit 11 gene family, which includes three genes in a cluster on chromosome 7q22.1 and a pseudogene on chromosome 7p13. The founding member of this family, DNA directed RNA polymerase II polypeptide J, has been shown to encode a subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. This locus produces multiple, alternatively spliced transcripts that potentially express isoforms with distinct …

**Accessions** — [HGNC:33853](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33853) · Entrez [548644](https://www.ncbi.nlm.nih.gov/gene/548644) · UniProt [Q9H1A7](https://www.uniprot.org/uniprotkb/Q9H1A7) · Ensembl [ENSG00000168255](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168255)

## Data

Gene col 9617: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9617); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9617, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9617]; `tensor/DDL_lfc|DDL_z.npy` [9617]; `embed/gene_vectors.npy` [9617]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9617 or target_col == 9617). Every well: [[POLR2J3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR2J3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
