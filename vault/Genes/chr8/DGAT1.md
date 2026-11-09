---
symbol: "DGAT1"
type: "gene"
col: 11605
ensembl_id: "ENSG00000185000"
name: "diacylglycerol O-acyltransferase 1"
location: "8q24.3"
module: 2
arm: "+"
pooled_cpm: 9.13
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# DGAT1

*diacylglycerol O-acyltransferase 1* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.91× (z +10.8, q 3e-24, up in 28 of 33 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.66× (z +3.2, q 0.054, up in 10 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 5.32×, KATO III 5.58×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 4.23×; ⚠ cell-cycle shift, explains ~43% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.122×); [[Tadalafil (drug)]] 5 µM in 1 line (A-172 0.0868×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (HS-578T 0.161×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM38]] (+0.63, fdr 1e-05), [[RCE1]] (+0.62, fdr 1e-05), [[RHOT2]] (+0.62, fdr 1e-05); moves opposite to [[CCT5]] (-0.52, fdr 2e-05), [[SRFBP1]] (-0.52, fdr 3e-05), [[NAA50]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 11 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11605.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 5.32×, KATO III 5.58×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 4.23×; ⚠ cell-cycle shift, explains ~43% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.91×** | +10.8 | 3e-24 | 28/33 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.44×** | +8.6 | 2e-15 | 16/17 (LS 180, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.25×** | +7.1 | 2e-10 | 14/19 (LS 180, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.89×** | +6.4 | 2e-08 | 31/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +5.8 | 1e-06 | 23/34 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.41×** | +4.8 | 2e-04 | 22/40 (AsPC-1, COLO 205, …) | top dose only | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.60×** | +4.7 | 2e-04 | 19/38 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.59×** | +4.7 | 2e-04 | 23/47 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.52×** | +4.2 | 0.001 | 23/47 (RKO, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.36×** | +4.2 | 0.001 | 19/41 (AsPC-1, A549, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.39×** | +3.3 | 0.048 | 12/43 (HEC-1-A, J82, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.66×** | +3.2 | 0.054 | 10/37 (HS-578T, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11605.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.122×); [[Tadalafil (drug)]] 5 µM in 1 line (A-172 0.0868×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (HS-578T 0.161×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | 0.694× | -3.6 | 0.13 | 18/44 (SHP-77, SW1417, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.518× | -3.5 | 0.13 | 16/42 (LS 180, HCT15, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 0.695× | -3.2 | 0.15 | 9/46 (LoVo, HS-578T, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.545× | -3.2 | 0.15 | 12/45 (LS 180, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.696× | -3.2 | 0.15 | 11/47 (LoVo, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11605. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.66 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0868× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 15.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +11.6) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[HS-578T (line)]] | alt | 12.6 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.161× (z -9.2) |
| [[KATO III (line)]] | alt | 13.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.58× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[LS 180 (line)]] | wt | 24.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.32× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H1573 (line)]] | alt | 9.60 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.122× (z -10.4) |
| [[A-427 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.05 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11605), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM38]] | +0.63 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[RCE1]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[RHOT2]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[RPS6KB2]] | +0.59 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[LRCH4]] | +0.59 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[KIFC2]] | +0.59 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[MIB2]] | +0.58 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[TCIRG1]] | +0.58 | +0.41 / +0.53 | both halves | 4e-05 | same gene group |
| [[SLC26A6]] | +0.58 | +0.51 / +0.47 | both halves | 2e-05 | same gene group |
| [[RHPN1]] | +0.57 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[PHF1]] | +0.57 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[FGFR3]] | +0.56 | +0.53 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT5]] | -0.52 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[SRFBP1]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[NAA50]] | -0.52 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ATIC]] | -0.49 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[XRCC6]] | -0.49 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[ZNF507]] | -0.48 | -0.29 / -0.46 | both halves | 2e-04 |  |
| [[LARP4]] | -0.48 | -0.44 / -0.36 | both halves | 9e-05 |  |
| [[MBTPS2]] | -0.47 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[C1QBP]] | -0.47 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[RBM12B]] | -0.47 | -0.38 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.486). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-12.9, -25.4); signed map (-26.4, 1.6). **Vector** length 54.6, 8.47% of its response variance represented; |z| ≥ 3 in 645 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +2.4 | +10.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +2.1 | +4.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.1 | +2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +2.1 | +6.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.8 | +1.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.7 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -3.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.4 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | +0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -3.2 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | diacylglycerol O-acyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,314,584-144,326,910 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARGP1; previously DGAT |
| Gene groups (HGNC) | Membrane bound O-acyltransferase family; MicroRNA protein coding host genes |
| Hallmark sets | UV_RESPONSE_UP, ADIPOGENESIS |
| Reactome | 8 pathways, smallest: Acyl chain remodeling of DAG and TAG; Triglyceride biosynthesis; Triglyceride metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O75907](https://www.uniprot.org/uniprotkb/O75907) (Diacylglycerol O-acyltransferase 1):

> Catalyzes the terminal and only committed step in triacylglycerol synthesis by using diacylglycerol and fatty acyl CoA as substrates. Highly expressed in epithelial cells of the small intestine and its activity is essential for the absorption of dietary fats. In liver, plays a role in esterifying exogenous fatty acids to glycerol, and is required to synthesize fat for storage. Also present in female mammary glands, where it produces fat in the milk (By similarity). May be involved in VLDL (very …

**Summary**, from NCBI Gene [8694](https://www.ncbi.nlm.nih.gov/gene/8694):

> This gene encodes an multipass transmembrane protein that functions as a key metabolic enzyme. The encoded protein catalyzes the conversion of diacylglycerol and fatty acyl CoA to triacylglycerol. This enzyme can also transfer acyl CoA to retinol. Activity of this protein may be associated with obesity and other metabolic diseases. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:2843](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2843) · Entrez [8694](https://www.ncbi.nlm.nih.gov/gene/8694) · UniProt [O75907](https://www.uniprot.org/uniprotkb/O75907) · Ensembl [ENSG00000185000](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185000)

## Data

Gene col 11605: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11605); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11605, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11605]; `tensor/DDL_lfc|DDL_z.npy` [11605]; `embed/gene_vectors.npy` [11605]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11605 or target_col == 11605). Every well: [[DGAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DGAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
