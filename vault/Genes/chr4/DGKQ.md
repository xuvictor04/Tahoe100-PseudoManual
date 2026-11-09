---
symbol: "DGKQ"
type: "gene"
col: 6963
ensembl_id: "ENSG00000145214"
name: "diacylglycerol kinase theta"
location: "4p16.3"
module: 2
arm: "+"
pooled_cpm: 4.73
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 7
n_dd_up_clean: 14
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# DGKQ

*diacylglycerol kinase theta* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.84× (z +12.7, q 6e-34, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.533× (z -7.6, q 1e-11, down in 22 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPND]] (+0.65, fdr 1e-05), [[ADCK5]] (+0.64, fdr 2e-05), [[KIFC2]] (+0.64, fdr 1e-05); moves opposite to [[MBNL1]] (-0.53, fdr 2e-05), [[XRCC5]] (-0.51, fdr 4e-05), [[TFAM]] (-0.50, fdr 4e-04).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6963.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.84×** | +12.7 | 6e-34 | 42/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.66×** | +11.9 | 6e-30 | 37/46 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.03×** | +8.6 | 2e-15 | 29/46 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.7 | 4e-09 | 17/39 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +6.6 | 5e-09 | 4/9 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +5.6 | 2e-06 | 10/24 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.5 | 5e-04 | 11/27 (HEC-1-A, KATO III, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +4.3 | 0.001 | 5/12 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.64×** | +4.3 | 0.001 | 9/34 (HOP62, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +4.1 | 0.002 | 8/29 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +3.9 | 0.005 | 1/12 (SW480) | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.38×** | +3.9 | 0.005 | 6/35 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.007 | 11/39 (KATO III, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.008 | 3/39 (HT-29, J82, …) | inconsistent across doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.52×** | +3.6 | 0.010 | 4/38 (SW480, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +3.5 | 0.016 | 7/47 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.48×** | +3.4 | 0.020 | 5/27 (SW48, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.47×** | +3.3 | 0.027 | 4/38 (LoVo, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.044 | 7/45 (COLO 205, HepG2/C3A, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.053 | 8/35 (HEC-1-A, NCI-H23, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6963.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.533×** | -7.6 | 1e-11 | 22/44 (hTERT-HPNE, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.366×** | -6.1 | 3e-07 | 15/40 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.625×** | -5.7 | 2e-06 | 21/44 (LOX-IMVI, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.444×** | -4.9 | 1e-04 | 15/37 (PANC-1, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.692×** | -4.5 | 8e-04 | 16/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.745×** | -3.6 | 0.032 | 13/36 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.736×** | -3.5 | 0.034 | 10/43 (BT-474, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.779× | -3.0 | 0.16 | 4/44 (SK-MEL-2, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6963. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 3.24 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0701× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 2.88 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.137× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 4.04 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0867× (z -8.5) |
| [[A-172 (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6963), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPND]] | +0.65 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[ADCK5]] | +0.64 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[KIFC2]] | +0.64 | +0.55 / +0.61 | both halves | 1e-05 | STRING 446 |
| [[RHOT2]] | +0.62 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[PKD1]] | +0.60 | +0.39 / +0.58 | both halves | 6e-05 |  |
| [[RFNG]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[ZNF598]] | +0.58 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[CAPN10]] | +0.57 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[MIIP]] | +0.57 | +0.30 / +0.56 | both halves | 2e-04 |  |
| [[UCKL1]] | +0.57 | +0.36 / +0.58 | both halves | 1e-04 |  |
| [[NSMF]] | +0.57 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[NSUN5P1-1]] | +0.57 | +0.62 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBNL1]] | -0.53 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[XRCC5]] | -0.51 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[TFAM]] | -0.50 | -0.26 / -0.43 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.653). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-9.3, -23.1); signed map (-27.0, 2.0). **Vector** length 45.6, 5.16% of its response variance represented; |z| ≥ 3 in 852 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.0 | +12.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.9 | +11.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +4.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.8 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +6.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +3.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.0 | +3.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.0 | +3.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.7 | +2.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -7.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.7 | -4.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.6 | -6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -0.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.5 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -4.9 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.2 | -3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | diacylglycerol kinase theta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:958,887-986,895 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DAGK, DAGK7; previously DAGK4 |
| Gene groups (HGNC) | Diacylglycerol kinase family |
| Reactome | 6 pathways, smallest: Effects of PIP2 hydrolysis; G alpha (q) signalling events; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [P52824](https://www.uniprot.org/uniprotkb/P52824) (Diacylglycerol kinase theta):

> Diacylglycerol kinase that converts diacylglycerol/DAG into phosphatidic acid/phosphatidate/PA and regulates the respective levels of these two bioactive lipids. Thereby, acts as a central switch between the signaling pathways activated by these second messengers with different cellular targets and opposite effects in numerous biological processes. Within the adrenocorticotropic hormone signaling pathway, produces phosphatidic acid which in turn activates NR5A1 and subsequent steroidogenic gene …

**Summary**, from NCBI Gene [1609](https://www.ncbi.nlm.nih.gov/gene/1609):

> The protein encoded by this gene contains three cysteine-rich domains, a proline-rich region, and a pleckstrin homology domain with an overlapping Ras-associating domain. It is localized in the speckle domains of the nucleus, and mediates the regeneration of phosphatidylinositol (PI) from diacylglycerol in the PI-cycle during cell signal transduction. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2856](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2856) · Entrez [1609](https://www.ncbi.nlm.nih.gov/gene/1609) · UniProt [P52824](https://www.uniprot.org/uniprotkb/P52824) · Ensembl [ENSG00000145214](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145214)

## Data

Gene col 6963: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6963); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6963, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6963]; `tensor/DDL_lfc|DDL_z.npy` [6963]; `embed/gene_vectors.npy` [6963]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6963 or target_col == 6963). Every well: [[DGKQ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DGKQ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
