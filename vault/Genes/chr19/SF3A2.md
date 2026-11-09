---
symbol: "SF3A2"
type: "gene"
col: 2521
ensembl_id: "ENSG00000104897"
name: "splicing factor 3a subunit 2"
location: "19p13.3"
module: 107
arm: "+"
pooled_cpm: 25.57
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# SF3A2

*splicing factor 3a subunit 2* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.84× (z +14.7, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.788× (z -4.1, q 0.021, down in 18 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 0.547×, A-427 0.343×; ⚠ cell-cycle shift, explains ~12% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.166×; ⚠ cell-cycle shift, explains ~24% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRPF6]] (+0.68, fdr 8e-06), [[ZNF408]] (+0.66, fdr 7e-06), [[UCK1]] (+0.63, fdr 1e-05); moves opposite to [[PEAK1]] (-0.56, fdr 1e-05), [[ARL15]] (-0.54, fdr 3e-05), [[MEMO1]] (-0.52, fdr 1e-04).
> It is in [[Module 107]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2521.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.84×** | +14.7 | 0e+00 | 46/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.95×** | +12.8 | 7e-35 | 40/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.50×** | +6.9 | 8e-10 | 28/48 (LS 180, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.27×** | +6.0 | 2e-07 | 24/47 (PANC-1, HS-578T, …) | rises with dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +5.9 | 4e-07 | 28/47 (SW480, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +5.9 | 4e-07 | 21/41 (NCI-H23, SW480, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +5.4 | 5e-06 | 25/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +5.3 | 1e-05 | 22/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +5.2 | 1e-05 | 27/48 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.34×** | +5.2 | 1e-05 | 22/47 (PANC-1, LoVo, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +4.8 | 7e-05 | 19/48 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.7 | 1e-04 | 0/48 | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.25×** | +4.0 | 0.003 | 18/43 (NCI-H460, SNU-423, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +3.6 | 0.013 | 14/46 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.5 | 0.019 | 13/31 (HS-578T, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.022 | 15/48 (HEC-1-A, RPMI-7951, …) | all doses, stronger at high dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Isocorydine (drug)]] 5 µM |  | 1.13× | +3.0 | 0.081 | 10/48 (C-33 A, LS 180, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2521.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 0.547×, A-427 0.343×; ⚠ cell-cycle shift, explains ~12% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.166×; ⚠ cell-cycle shift, explains ~24% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.788×** | -4.1 | 0.021 | 18/47 (hTERT-HPNE, A-172, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | 0.864× | -3.7 | 0.052 | 13/48 (RKO, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 0.822× | -3.4 | 0.13 | 14/47 (hTERT-HPNE, C-33 A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.888× | -3.1 | 0.32 | 18/48 (A498, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2521. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 32.5 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 7.85× (z +10.6) | — |
| [[LS 180 (line)]] | wt | 26.6 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 8.84× (z +8.9) | — |
| [[SW480 (line)]] | alt | 25.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.35× (z +9.1) | — |
| [[A-427 (line)]] | wt | 27.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -8.5) ⚠ cell-cycle shift, explains ~12% of this change |
| [[A498 (line)]] | wt | 36.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -9.2) ⚠ cell-cycle shift, explains ~12% of this change |
| [[NCI-H2030 (line)]] | alt | 31.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.12× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 27.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -9.6) ⚠ cell-cycle shift, explains ~24% of this change |
| [[A-172 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2521), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF6]] | +0.68 | +0.74 / +0.57 | both halves | 8e-06 | pathway: Dengue Virus-Host Interactions; STRING 999 |
| [[ZNF408]] | +0.66 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[UCK1]] | +0.63 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[ABCF3]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[PES1]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ZNF180]] | +0.60 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[PCBP1]] | +0.60 | +0.60 / +0.46 | both halves | 3e-05 | pathway: Dengue Virus-Host Interactions; STRING 666 |
| [[ZNF205]] | +0.60 | +0.67 / +0.43 | both halves | 3e-05 |  |
| [[EDC3]] | +0.59 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[ZNF384]] | +0.59 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[ESS2]] | +0.58 | +0.71 / +0.42 | both halves | 4e-05 |  |
| [[ZNF211]] | +0.58 | +0.56 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEAK1]] | -0.56 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[ARL15]] | -0.54 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[MEMO1]] | -0.52 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[ETNK1]] | -0.49 | -0.51 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.642). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.9, -3.3); signed map (-10.6, -25.4). **Vector** length 71.0, 12.6% of its response variance represented; |z| ≥ 3 in 765 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.2 | +14.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.1 | +12.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.5 | +2.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +3.3 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +5.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.5 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +1.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | +0.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.5 | +2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | +1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -4.1 |
|  | [[Berbamine (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -1.2 | -0.5 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | +0.0 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | splicing factor 3a subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:2,236,824-2,248,655 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SF3a66, SAP62, PRPF11, Prp11 |
| Gene groups (HGNC) | Zinc fingers matrin-type; U2 small nuclear ribonucleoprotein; SF3a complex |
| Reactome | 13 pathways, smallest: CHD1 and CHD2 subfamily; CHD chromatin remodelers; mRNA Polyadenylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15428](https://www.uniprot.org/uniprotkb/Q15428) (Splicing factor 3A subunit 2):

> Component of the 17S U2 SnRNP complex of the spliceosome, a large ribonucleoprotein complex that removes introns from transcribed pre-mRNAs. The 17S U2 SnRNP complex (1) directly participates in early spliceosome assembly and (2) mediates recognition of the intron branch site during pre-mRNA splicing by promoting the selection of the pre-mRNA branch-site adenosine, the nucleophile for the first step of splicing. Within the 17S U2 SnRNP complex, SF3A2 is part of the SF3A subcomplex that …

**Summary**, from NCBI Gene [8175](https://www.ncbi.nlm.nih.gov/gene/8175):

> This gene encodes subunit 2 of the splicing factor 3a protein complex. The splicing factor 3a heterotrimer includes subunits 1, 2 and 3 and is necessary for the in vitro conversion of 15S U2 snRNP into an active 17S particle that performs pre-mRNA splicing. Subunit 2 interacts with subunit 1 through its amino-terminus while the single zinc finger domain of subunit 2 plays a role in its binding to the 15S U2 snRNP. Subunit 2 may also function independently of its RNA splicing function as a …

**Accessions** — [HGNC:10766](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10766) · Entrez [8175](https://www.ncbi.nlm.nih.gov/gene/8175) · UniProt [Q15428](https://www.uniprot.org/uniprotkb/Q15428) · Ensembl [ENSG00000104897](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104897)

## Data

Gene col 2521: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2521); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2521, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2521]; `tensor/DDL_lfc|DDL_z.npy` [2521]; `embed/gene_vectors.npy` [2521]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2521 or target_col == 2521). Every well: [[SF3A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SF3A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
