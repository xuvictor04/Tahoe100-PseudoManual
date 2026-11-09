---
symbol: "U2AF1"
type: "gene"
col: 8316
ensembl_id: "ENSG00000160201"
name: "U2 small nuclear RNA auxiliary factor 1"
location: "21q22.3"
module: 52
arm: "+"
pooled_cpm: 9.76
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# U2AF1

*U2 small nuclear RNA auxiliary factor 1* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.44× (z +5.3, q 5e-05, up in 22 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 0.629× (z -3.8, q 0.076, down in 15 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (AsPC-1 0.0793×; ⚠ transcription drop; cell-cycle shift, would explain all of this change); [[Bergenin (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.150×); [[Ipatasertib (drug)]] 0.05 µM in 1 line (SHP-77 0.0942×); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (HCT15 0.111×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNL2]] (+0.57, fdr 1e-05), [[HTATSF1]] (+0.52, fdr 3e-05), [[BMS1]] (+0.52, fdr 3e-05); moves opposite to [[ATP5MG]] (-0.46, fdr 3e-05), [[PTOV1]] (-0.43, fdr 3e-04), [[CCDC142]] (-0.42, fdr 3e-04).
> It sits in the **+** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8316.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.44×** | +5.3 | 5e-05 | 22/47 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.41×** | +5.2 | 5e-05 | 20/42 (HEC-1-A, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.58×** | +5.0 | 1e-04 | 16/36 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +4.9 | 1e-04 | 20/43 (LOX-IMVI, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.52×** | +4.8 | 2e-04 | 21/47 (NCI-H460, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~17% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.45×** | +4.3 | 0.002 | 11/47 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.44×** | +4.1 | 0.003 | 17/48 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **1.44×** | +4.0 | 0.005 | 5/18 (SW480, LOX-IMVI, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.49×** | +3.8 | 0.009 | 14/42 (NCI-H460, LS 180, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.41×** | +3.8 | 0.010 | 13/47 (NCI-H460, MIA PaCa-2, …) | all doses, flat | composition shift; position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.025 | 16/46 (HEC-1-A, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Pimozide (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.032 | 15/47 (NCI-H1573, HOP62, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.33×** | +3.2 | 0.055 | 18/46 (NCI-H460, PANC-1, …) | rises with dose | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.70×** | +3.1 | 0.068 | 3/45 (A498, H4, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8316.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (AsPC-1 0.0793×; ⚠ transcription drop; cell-cycle shift, would explain all of this change); [[Bergenin (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.150×); [[Ipatasertib (drug)]] 0.05 µM in 1 line (SHP-77 0.0942×); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (HCT15 0.111×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.629×** | -3.8 | 0.076 | 15/42 (SW48, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.726×** | -3.6 | 0.076 | 10/48 (NCI-H2030, SW1417, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.735× | -3.3 | 0.19 | 11/46 (BT-474, SW1417, …) | inconsistent across doses | position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | 0.763× | -3.1 | 0.24 | 13/46 (SNU-423, CHP-212, …) | rises with dose | position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.828× | -3.0 | 0.24 | 13/48 (NCI-H23, NCI-H1792, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8316. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0793× (z -14.3) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 13.4 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.111× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 14.9 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.150× (z -10.5) |
| [[SHP-77 (line)]] | alt | 11.6 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.05 µM 0.0942× (z -9.8) |
| [[A-172 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.60 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.97 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8316), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNL2]] | +0.57 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[HTATSF1]] | +0.52 | +0.51 / +0.43 | both halves | 3e-05 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[BMS1]] | +0.52 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[PDHA1]] | +0.50 | +0.56 / +0.38 | both halves | 7e-05 |  |
| [[FIGNL1]] | +0.49 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[LRRC59]] | +0.48 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[TMEM214]] | +0.47 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[UTP6]] | +0.47 | +0.38 / +0.41 | both halves | 6e-05 |  |
| [[PDAP1]] | +0.47 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[UCHL5]] | +0.47 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[LTN1]] | +0.46 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[SSRP1]] | +0.46 | +0.52 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5MG]] | -0.46 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[PTOV1]] | -0.43 | -0.27 / -0.54 | both halves | 3e-04 |  |
| [[CCDC142]] | -0.42 | -0.46 / -0.29 | both halves | 3e-04 |  |
| [[MKLN1]] | -0.42 | -0.36 / -0.28 | both halves | 3e-04 |  |
| [[B3GALNT2]] | -0.41 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[UBE2Q2P1-1]] | -0.41 | -0.29 / -0.39 | both halves | 2e-04 |  |
| [[SPPL3]] | -0.40 | -0.32 / -0.32 | both halves | 2e-04 |  |
| [[LRP10]] | -0.39 | -0.24 / -0.33 | both halves | 4e-04 |  |
| [[PLEKHM2]] | -0.39 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[TMEM80]] | -0.39 | -0.33 / -0.22 | both halves | 6e-04 |  |
| [[EIF3J-DT]] | -0.38 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[RPL38]] | -0.38 | -0.32 / -0.45 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.285). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-29.2, -35.9); signed map (-18.6, -46.1). **Vector** length 43.9, 4.79% of its response variance represented; |z| ≥ 3 in 820 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.3 | +4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.2 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.2 | +0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +1.2 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.0 | +1.4 |
|  | [[Malotilate (drug)]] 0.05 µM |  | +1.0 | +2.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +0.9 | +2.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | -1.8 | +3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.6 | -3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +1.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.5 | -1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -3.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.4 | -1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | U2 small nuclear RNA auxiliary factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:43,092,956-43,107,570 (-) |
| Ensembl biotype | protein_coding |
| Also known as | U2AF35, RNU2AF1, RN; previously U2AFBP |
| Gene groups (HGNC) | Zinc fingers CCCH-type; RNA binding motif containing; Spliceosomal A complex; Spliceosomal E complex |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 11 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; mRNA Polyadenylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01081](https://www.uniprot.org/uniprotkb/Q01081) (Splicing factor U2AF 35 kDa subunit):

> Plays a critical role in both constitutive and enhancer-dependent splicing by mediating protein-protein interactions and protein-RNA interactions required for accurate 3'-splice site selection. Recruits U2 snRNP to the branch point. Directly mediates interactions between U2AF2 and proteins bound to the enhancers and thus may function as a bridge between U2AF2 and the enhancer complex to recruit it to the adjacent intron.

**Summary**, from NCBI Gene [7307](https://www.ncbi.nlm.nih.gov/gene/7307):

> This gene belongs to the splicing factor SR family of genes. U2 auxiliary factor, comprising a large and a small subunit, is a non-snRNP protein required for the binding of U2 snRNP to the pre-mRNA branch site. This gene encodes the small subunit which plays a critical role in both constitutive and enhancer-dependent RNA splicing by directly mediating interactions between the large subunit and proteins bound to the enhancers. Alternatively spliced transcript variants encoding different isoforms …

**Accessions** — [HGNC:12453](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12453) · Entrez [7307](https://www.ncbi.nlm.nih.gov/gene/7307) · UniProt [Q01081](https://www.uniprot.org/uniprotkb/Q01081) · Ensembl [ENSG00000160201](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160201)

## Data

Gene col 8316: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8316); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8316, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8316]; `tensor/DDL_lfc|DDL_z.npy` [8316]; `embed/gene_vectors.npy` [8316]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8316 or target_col == 8316). Every well: [[U2AF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/U2AF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
