---
symbol: "ATP6V0B"
type: "gene"
col: 3904
ensembl_id: "ENSG00000117410"
name: "ATPase H+ transporting V0 subunit b"
location: "1p34.1"
module: 24
arm: "+"
pooled_cpm: 21.11
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# ATP6V0B

*ATPase H+ transporting V0 subunit b* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.32× (z +7.6, q 1e-11, up in 38 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.84× (z +6.4, q 3e-08, up in 38 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.106×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP6V1F]] (+0.72, fdr 1e-05), [[RABAC1]] (+0.71, fdr 3e-05), [[COPS9]] (+0.69, fdr 7e-06); moves opposite to [[HNRNPD]] (-0.62, fdr 3e-05), [[SYNCRIP]] (-0.59, fdr 4e-05), [[DDX39B]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3904.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **3.32×** | +7.6 | 1e-11 | 38/40 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **2.69×** | +7.0 | 6e-10 | 28/31 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.51×** | +6.5 | 1e-08 | 40/44 (CFPAC-1, J82, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +6.4 | 3e-08 | 38/47 (A549, KATO III, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **2.09×** | +5.4 | 6e-06 | 41/48 (HOP62, HS-578T, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.06×** | +5.3 | 9e-06 | 37/45 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **2.02×** | +4.8 | 1e-04 | 29/37 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.89×** | +4.7 | 2e-04 | 39/48 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.88×** | +4.7 | 2e-04 | 37/44 (CFPAC-1, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +4.5 | 3e-04 | 35/47 (SW480, COLO 205, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.81×** | +4.4 | 7e-04 | 35/48 (HOP62, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.66×** | +3.8 | 0.008 | 26/46 (HEC-1-A, HS-578T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.62×** | +3.6 | 0.017 | 26/47 (SW480, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +3.4 | 0.023 | 24/48 (NCI-H2030, PANC-1, …) | two highest doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.59×** | +3.4 | 0.026 | 28/48 (SW480, NCI-H460, …) | rises with dose | composition shift |
| [[Arbutin (drug)]] 5 µM |  | **1.61×** | +3.4 | 0.028 | 25/46 (A498, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3904.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.106×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | 0.596× | -3.7 | 0.13 | 27/47 (HepG2/C3A, C32, …) | top dose only | position effect removed |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.650× | -3.1 | 0.63 | 24/47 (A549, KATO III, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.61 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3904. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 18.9 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.106× (z -8.7) |
| [[A-172 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3904), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 14 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1F]] | +0.72 | +0.55 / +0.78 | both halves | 1e-05 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[RABAC1]] | +0.71 | +0.45 / +0.76 | both halves | 3e-05 |  |
| [[COPS9]] | +0.69 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[CIAO2B]] | +0.69 | +0.37 / +0.78 | both halves | 8e-05 |  |
| [[RNASEK]] | +0.68 | +0.67 / +0.69 | both halves | 7e-06 | STRING 997 |
| [[ALKBH7]] | +0.67 | +0.32 / +0.76 | both halves | 2e-04 |  |
| [[MIEN1]] | +0.64 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[RANGRF]] | +0.64 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[C19orf53]] | +0.64 | +0.46 / +0.67 | both halves | 2e-05 |  |
| [[OST4]] | +0.64 | +0.39 / +0.68 | both halves | 5e-05 |  |
| [[FAU]] | +0.64 | +0.47 / +0.69 | both halves | 2e-05 | pathway: Cellular response to starvation |
| [[C1orf122]] | +0.63 | +0.46 / +0.67 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPD]] | -0.62 | -0.43 / -0.65 | both halves | 3e-05 |  |
| [[SYNCRIP]] | -0.59 | -0.43 / -0.60 | both halves | 4e-05 |  |
| [[DDX39B]] | -0.58 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[YWHAE]] | -0.55 | -0.32 / -0.60 | both halves | 2e-04 | pathway: MITF-M-regulated melanocyte development |
| [[RUVBL1]] | -0.54 | -0.30 / -0.62 | both halves | 2e-04 |  |
| [[SF3B3]] | -0.54 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[SRSF3]] | -0.54 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[EWSR1]] | -0.53 | -0.23 / -0.64 | both halves | 5e-04 |  |
| [[LAS1L]] | -0.53 | -0.33 / -0.63 | both halves | 1e-04 |  |
| [[HNRNPA2B1]] | -0.53 | -0.29 / -0.56 | both halves | 2e-04 |  |
| [[FARSB]] | -0.52 | -0.28 / -0.59 | both halves | 3e-04 |  |
| [[U2SURP]] | -0.52 | -0.35 / -0.55 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.588). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-44.7, -21.3); signed map (-32.7, 10.6). **Vector** length 55.7, 13.3% of its response variance represented; |z| ≥ 3 in 653 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +2.5 | +3.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +2.4 | +5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +2.3 | +3.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +2.0 | +3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +2.1 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +1.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.1 | -0.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.0 | +1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +0.9 | +0.9 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | -2.6 | +4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | -2.5 | +7.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -1.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | -2.2 | +7.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -0.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ATPase H+ transporting V0 subunit b |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:43,974,487-43,978,295 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VMA16, HATPL; previously ATP6F |
| Gene groups (HGNC) | V-type ATPase subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 16 pathways, smallest: Regulation of MITF-M-dependent genes involved in lysosome biogenesis and autophagy; Insulin receptor recycling; ROS and RNS production in phagocytes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99437](https://www.uniprot.org/uniprotkb/Q99437) (V-type proton ATPase 21 kDa proteolipid subunit c''):

> Proton-conducting pore forming subunit of the V0 complex of vacuolar(H+)-ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that translocates protons. V-ATPase is responsible for acidifying and maintaining the pH of intracellular compartments and in some cell types, is targeted to the plasma membrane, where it promotes acidification of the extracellular environment (By similarity). The V-ATPase complex also …

**Summary**, from NCBI Gene [533](https://www.ncbi.nlm.nih.gov/gene/533):

> This gene encodes a portion of the V0 domain of vacuolar ATPase (V-ATPase), a multisubunit enzyme that mediates acidification of eukaryotic intracellular organelles. Activity of this enzyme is necessary for such varied processes as protein sorting, zymogen activation, receptor-mediated endocytosis, and synaptic vesicle proton gradient generation. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2014]

**Accessions** — [HGNC:861](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:861) · Entrez [533](https://www.ncbi.nlm.nih.gov/gene/533) · UniProt [Q99437](https://www.uniprot.org/uniprotkb/Q99437) · Ensembl [ENSG00000117410](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117410)

## Data

Gene col 3904: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3904); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3904, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3904]; `tensor/DDL_lfc|DDL_z.npy` [3904]; `embed/gene_vectors.npy` [3904]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3904 or target_col == 3904). Every well: [[ATP6V0B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP6V0B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
