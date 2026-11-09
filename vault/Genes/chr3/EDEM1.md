---
symbol: "EDEM1"
type: "gene"
col: 5512
ensembl_id: "ENSG00000134109"
name: "ER degradation enhancing alpha-mannosidase like protein 1"
location: "3p26.1"
module: 20
arm: "+"
pooled_cpm: 51.35
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# EDEM1

*ER degradation enhancing alpha-mannosidase like protein 1* — 3p26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.50× (z +3.8, q 0.073, up in 29 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.48× (z +3.7, q 0.073, up in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 3.12×, A498 2.79×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 2.91×).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2347 0.274×; ⚠ cell-cycle shift, explains ~69% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 0.411×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 0.183×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Filgotinib (drug)]] 0.5 µM in 1 line (NCI-H661 0.0681×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHFR]] (+0.70, fdr 1e-05), [[RPN1]] (+0.69, fdr 9e-06), [[TMEM30A]] (+0.68, fdr 7e-06); moves opposite to [[SMIM26]] (-0.66, fdr 1e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[RPP21]] (-0.66, fdr 5e-05), [[USP42]] (-0.65, fdr 1e-04), [[ZNF593]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5512.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 3.12×, A498 2.79×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 2.91×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +3.8 | 0.073 | 29/48 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +3.7 | 0.073 | 26/48 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.08×** | +3.6 | 0.073 | 30/47 (C32, HS-578T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +3.4 | 0.082 | 25/44 (C-33 A, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | 1.89× | +3.1 | 0.23 | 26/49 (A498, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5512.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2347 0.274×; ⚠ cell-cycle shift, explains ~69% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 0.411×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 0.183×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Filgotinib (drug)]] 0.5 µM in 1 line (NCI-H661 0.0681×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | 0.678× | -3.6 | 0.12 | 29/48 (SK-MEL-2, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.684× | -3.5 | 0.12 | 29/48 (SW48, BT-474, …) | rises with dose | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5512. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 104 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.274× (z -10.6) ⚠ cell-cycle shift, explains ~69% of this change |
| [[A498 (line)]] | wt | 34.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +11.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[COLO 205 (line)]] | alt | 38.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 32.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +13.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H661 (line)]] | alt | 34.0 | 0 | 1 | — | [[Filgotinib (drug)]] 0.5 µM 0.0681× (z -9.0) |
| [[PANC-1 (line)]] | alt | 32.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 56.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -8.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 88.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 69.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 69.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 72.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 66.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 77.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 39.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5512), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHFR]] | +0.70 | +0.52 / +0.72 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[RPN1]] | +0.69 | +0.57 / +0.75 | both halves | 9e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 477 |
| [[TMEM30A]] | +0.68 | +0.58 / +0.77 | both halves | 7e-06 |  |
| [[MOB1A]] | +0.67 | +0.44 / +0.73 | both halves | 3e-05 |  |
| [[EIF4H]] | +0.66 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[ANKRD30BL]] | +0.66 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[TXNDC5]] | +0.65 | +0.60 / +0.69 | both halves | 7e-06 | STRING 443 |
| [[BPNT2]] | +0.64 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[FKBP9]] | +0.64 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[FAM91A1]] | +0.62 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[PRKAR1A]] | +0.61 | +0.40 / +0.67 | both halves | 4e-05 |  |
| [[BAG6]] | +0.61 | +0.55 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM26]] ⚠ | -0.66 | -0.51 / -0.68 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPP21]] | -0.66 | -0.40 / -0.70 | both halves | 5e-05 |  |
| [[USP42]] | -0.65 | -0.33 / -0.65 | both halves | 1e-04 |  |
| [[ZNF593]] | -0.64 | -0.53 / -0.72 | both halves | 1e-05 |  |
| [[MAP2K7]] | -0.64 | -0.33 / -0.68 | both halves | 1e-04 |  |
| [[PUS3]] | -0.63 | -0.44 / -0.72 | both halves | 3e-05 |  |
| [[CROCCP2-1]] | -0.63 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[PIGBOS1]] | -0.62 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[PRPF38B]] | -0.61 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[MRPL32]] | -0.61 | -0.59 / -0.69 | both halves | 7e-06 |  |
| [[RBMX2]] | -0.61 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[MTRES1]] | -0.60 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[MRPL36]] | -0.60 | -0.48 / -0.63 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.665). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-24.7, -22.3); signed map (-24.1, -39.2). **Vector** length 107, 33.3% of its response variance represented; |z| ≥ 3 in 579 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +9.4 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +9.1 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.1 | +3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | +1.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.1 | +1.4 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +1.9 | +2.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.8 | +2.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -1.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -1.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.6 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -1.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ER degradation enhancing alpha-mannosidase like protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p26.1 — chr3:5,187,646-5,219,958 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0212, EDEM |
| Gene groups (HGNC) | Mannosidases alpha class 1 |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, MTORC1_SIGNALING |
| Reactome | 9 pathways, smallest: ER Quality Control Compartment (ERQC); Calnexin/calreticulin cycle; N-glycan trimming in the ER and Calnexin/Calreticulin cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92611](https://www.uniprot.org/uniprotkb/Q92611) (ER degradation-enhancing alpha-mannosidase-like protein 1):

> Extracts misfolded glycoproteins, but not glycoproteins undergoing productive folding, from the calnexin cycle. It is directly involved in endoplasmic reticulum-associated degradation (ERAD) and targets misfolded glycoproteins for degradation in an N-glycan-independent manner, probably by forming a complex with SEL1L. It has low mannosidase activity, catalyzing mannose trimming from Man8GlcNAc2 to Man7GlcNAc2.

**Summary**, from NCBI Gene [9695](https://www.ncbi.nlm.nih.gov/gene/9695):

> Enables mannosyl-oligosaccharide 1,2-alpha-mannosidase activity and misfolded protein binding activity. Involved in several processes, including endoplasmic reticulum mannose trimming; positive regulation of retrograde protein transport, ER to cytosol; and protein catabolic process. Located in endoplasmic reticulum quality control compartment. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18967](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18967) · Entrez [9695](https://www.ncbi.nlm.nih.gov/gene/9695) · UniProt [Q92611](https://www.uniprot.org/uniprotkb/Q92611) · Ensembl [ENSG00000134109](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134109)

## Data

Gene col 5512: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5512); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5512, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5512]; `tensor/DDL_lfc|DDL_z.npy` [5512]; `embed/gene_vectors.npy` [5512]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5512 or target_col == 5512). Every well: [[EDEM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EDEM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
