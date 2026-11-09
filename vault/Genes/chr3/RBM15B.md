---
symbol: "RBM15B"
type: "gene"
col: 15248
ensembl_id: "ENSG00000259956"
name: "RNA binding motif protein 15B"
location: "3p21.2"
module: 7
arm: "+"
pooled_cpm: 12.86
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# RBM15B

*RNA binding motif protein 15B* — 3p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 1.81× (z +6.5, q 6e-08, up in 17 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.44× (z +6.1, q 4e-07, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.612× (z -5.8, q 2e-06, down in 27 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.612× (z -5.8, q 2e-06, down in 29 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FEM1A]] (+0.78, fdr 7e-06), [[MOCS3]] (+0.78, fdr 7e-06), [[ZBTB45]] (+0.75, fdr 7e-06); moves opposite to [[HSPB11]] (-0.63, fdr 7e-06), [[SGK3]] (-0.60, fdr 1e-05), [[GMCL1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15248.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +6.5 | 6e-08 | 17/32 (J82, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +6.1 | 4e-07 | 26/48 (CFPAC-1, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.52×** | +4.9 | 1e-04 | 19/39 (LoVo, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.34×** | +4.9 | 1e-04 | 22/47 (NCI-H460, AsPC-1, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.11×** | +4.6 | 5e-04 | 22/48 (LoVo, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.49×** | +4.5 | 6e-04 | 19/47 (NCI-H2347, A-172, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +4.5 | 6e-04 | 22/44 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.93×** | +4.0 | 0.004 | 16/43 (LoVo, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.8 | 0.008 | 17/41 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.57×** | +3.8 | 0.009 | 16/44 (SHP-77, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +3.8 | 0.009 | 21/46 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +3.5 | 0.024 | 12/24 (SW1417, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.046 | 13/47 (A498, A549, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.67×** | +3.2 | 0.064 | 6/44 (NCI-H23, NCI-H1573, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.45×** | +3.1 | 0.072 | 12/45 (LoVo, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.072 | 12/45 (Panc 03.27, A-172, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.30×** | +3.1 | 0.072 | 8/48 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | **1.20×** | +3.0 | 0.072 | 11/48 (NCI-H23, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15248.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.612×** | -5.8 | 2e-06 | 27/46 (C-33 A, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.612×** | -5.8 | 2e-06 | 29/46 (NCI-H23, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.661×** | -4.9 | 2e-04 | 25/47 (AN3 CA, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.664×** | -4.8 | 2e-04 | 23/48 (NCI-H2030, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.738×** | -3.6 | 0.041 | 19/46 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15248. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 16.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -11.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[BT-474 (line)]] | alt | 13.2 | 0 | 1 | — | [[Meloxicam (drug)]] 0.5 µM 0.142× (z -9.7) |
| [[C-33 A (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0761× (z -12.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0820× (z -10.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -8.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0730× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15248), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FEM1A]] | +0.78 | +0.80 / +0.71 | both halves | 7e-06 |  |
| [[MOCS3]] | +0.78 | +0.81 / +0.68 | both halves | 7e-06 |  |
| [[ZBTB45]] | +0.75 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[ZNF629]] | +0.74 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[CENPBD1P]] | +0.72 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[ZSCAN29]] | +0.71 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[IRF2BP1]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[ZNF747]] | +0.71 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[ZNF268]] | +0.70 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[LINC00667]] | +0.70 | +0.75 / +0.49 | both halves | 1e-05 |  |
| [[ZC3H4]] | +0.69 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[TASOR]] | +0.69 | +0.76 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPB11]] | -0.63 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[SGK3]] | -0.60 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.60 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[SRP54-AS1]] | -0.59 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[CBFA2T2]] | -0.59 | -0.68 / -0.40 | both halves | 4e-05 |  |
| [[HDAC3]] | -0.59 | -0.68 / -0.41 | both halves | 4e-05 |  |
| [[KYAT1]] | -0.59 | -0.63 / -0.38 | both halves | 6e-05 |  |
| [[PIK3C2A]] | -0.57 | -0.61 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.734). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-37.5, 11.3); signed map (-2.3, -27.5). **Vector** length 76.5, 14.5% of its response variance represented; |z| ≥ 3 in 776 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.2 | +4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +5.8 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +3.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.6 | +4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +6.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +3.8 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.1 | -5.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -5.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 15B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.2 — chr3:51,391,285-51,397,908 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HUMAGCGB, OTT3 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NDT2](https://www.uniprot.org/uniprotkb/Q8NDT2) (Putative RNA-binding protein 15B):

> RNA-binding protein that acts as a key regulator of N6-methyladenosine (m6A) methylation of RNAs, thereby regulating different processes, such as alternative splicing of mRNAs and X chromosome inactivation mediated by Xist RNA. Associated component of the WMM complex, a complex that mediates N6-methyladenosine (m6A) methylation of RNAs, a modification that plays a role in the efficiency of mRNA splicing and RNA processing. Plays a key role in m6A methylation, possibly by binding target RNAs and …

**Summary**, from NCBI Gene [29890](https://www.ncbi.nlm.nih.gov/gene/29890):

> Members of the SPEN (Split-end) family of proteins, including RBM15B, have repressor function in several signaling pathways and may bind to RNA through interaction with spliceosome components (Hiriart et al., 2005 [PubMed 16129689]).[supplied by OMIM, Feb 2009]

**Accessions** — [HGNC:24303](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24303) · Entrez [29890](https://www.ncbi.nlm.nih.gov/gene/29890) · UniProt [Q8NDT2](https://www.uniprot.org/uniprotkb/Q8NDT2) · Ensembl [ENSG00000259956](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259956)

## Data

Gene col 15248: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15248); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15248, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15248]; `tensor/DDL_lfc|DDL_z.npy` [15248]; `embed/gene_vectors.npy` [15248]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15248 or target_col == 15248). Every well: [[RBM15B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM15B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
