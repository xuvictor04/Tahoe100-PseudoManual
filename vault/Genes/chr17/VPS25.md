---
symbol: "VPS25"
type: "gene"
col: 5216
ensembl_id: "ENSG00000131475"
name: "vacuolar protein sorting 25 homolog"
location: "17q21.31"
module: 7
arm: "+"
pooled_cpm: 15.75
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# VPS25

*vacuolar protein sorting 25 homolog* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.30× (z +8.1, q 3e-13, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.627× (z -4.6, q 0.003, down in 28 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 0.170×, HEC-1-A 0.215×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (C32 0.0776×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.326×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BLOC1S4]] (+0.67, fdr 1e-05), [[FADD]] (+0.67, fdr 1e-05), [[TMEM70]] (+0.67, fdr 1e-05); moves opposite to [[USF2]] (-0.56, fdr 7e-05), [[FAM81A]] (-0.54, fdr 1e-04), [[RPS3A]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5216.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.30×** | +8.1 | 3e-13 | 42/46 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.06×** | +6.8 | 4e-09 | 38/46 (C32, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.74×** | +5.4 | 1e-05 | 27/42 (KATO III, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.92×** | +4.5 | 8e-04 | 28/42 (PANC-1, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.88×** | +4.4 | 0.001 | 33/45 (HOP62, NCI-H2030, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +3.9 | 0.008 | 6/48 (SW480, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +3.8 | 0.011 | 23/47 (LOX-IMVI, A498, …) | inconsistent across doses | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.71×** | +3.7 | 0.015 | 23/45 (HOP62, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.4 | 0.038 | 14/42 (SK-MEL-2, AsPC-1, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.61×** | +3.3 | 0.058 | 15/44 (A-427, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.079 | 11/45 (NCI-H460, KATO III, …) | inconsistent across doses | position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.57×** | +3.1 | 0.080 | 15/47 (MIA PaCa-2, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.090 | 10/45 (A549, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 0.5 µM |  | 1.55× | +3.0 | 0.11 | 13/47 (NCI-H1573, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5216.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 0.170×, HEC-1-A 0.215×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (C32 0.0776×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.326×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.627×** | -4.6 | 0.003 | 28/47 (NCI-H460, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.729× | -3.1 | 0.52 | 19/47 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5216. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 13.4 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0776× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5216), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLOC1S4]] | +0.67 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[FADD]] | +0.67 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[TMEM70]] | +0.67 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[RBM42]] | +0.66 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[RPP14]] | +0.64 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[STOML2]] | +0.62 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[NDUFB3]] | +0.62 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[KTI12]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[RPUSD3]] | +0.61 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[MRPL10]] | +0.61 | +0.47 / +0.70 | both halves | 2e-05 |  |
| [[INTS5]] | +0.61 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[TIMM17B]] ⚠ | +0.61 | +0.47 / +0.66 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NSUN5]] | +0.60 | +0.53 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USF2]] | -0.56 | -0.58 / -0.38 | both halves | 7e-05 |  |
| [[FAM81A]] | -0.54 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[RPS3A]] | -0.54 | -0.34 / -0.64 | both halves | 1e-04 |  |
| [[STT3B]] | -0.54 | -0.39 / -0.60 | both halves | 6e-05 |  |
| [[SMG1P1]] | -0.54 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[PTMS]] | -0.53 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[EMC10]] | -0.52 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[DHFR]] | -0.51 | -0.27 / -0.57 | both halves | 3e-04 |  |
| [[CRTAP]] | -0.51 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[YBX1]] | -0.51 | -0.29 / -0.51 | both halves | 2e-04 |  |
| [[CCDC183]] | -0.51 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[VAMP1]] | -0.51 | -0.43 / -0.54 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.534). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-44.8, 0.2); signed map (-4.0, -19.8). **Vector** length 80.3, 19.4% of its response variance represented; |z| ≥ 3 in 568 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.1 | +8.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.6 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +2.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.2 | +3.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.5 | +3.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +4.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +2.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.0 | +2.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.6 | +0.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.0 | +1.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.5 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.7 | -0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -2.2 | -1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -1.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | vacuolar protein sorting 25 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:42,773,449-42,779,599 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10540, EAP20, DERP9 |
| Gene groups (HGNC) | ESCRT-II |
| Reactome | 6 pathways, smallest: Endosomal Sorting Complex Required For Transport (ESCRT); HCMV Late Events; HCMV Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRG1](https://www.uniprot.org/uniprotkb/Q9BRG1) (Vacuolar protein-sorting-associated protein 25):

> Component of the ESCRT-II complex (endosomal sorting complex required for transport II), which is required for multivesicular body (MVB) formation and sorting of endosomal cargo proteins into MVBs. The MVB pathway mediates delivery of transmembrane proteins into the lumen of the lysosome for degradation. The ESCRT-II complex is probably involved in the recruitment of the ESCRT-III complex. The ESCRT-II complex may also play a role in transcription regulation, possibly via its interaction with …

**Summary**, from NCBI Gene [84313](https://www.ncbi.nlm.nih.gov/gene/84313):

> This gene encodes a protein that is a subunit of the endosomal sorting complex required for transport II (ESCRT-II). This protein complex functions in sorting of ubiquitinated membrane proteins during endocytosis. A pseudogene of this gene is present on chromosome 1. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:28122](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28122) · Entrez [84313](https://www.ncbi.nlm.nih.gov/gene/84313) · UniProt [Q9BRG1](https://www.uniprot.org/uniprotkb/Q9BRG1) · Ensembl [ENSG00000131475](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131475)

## Data

Gene col 5216: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5216); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5216, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5216]; `tensor/DDL_lfc|DDL_z.npy` [5216]; `embed/gene_vectors.npy` [5216]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5216 or target_col == 5216). Every well: [[VPS25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
