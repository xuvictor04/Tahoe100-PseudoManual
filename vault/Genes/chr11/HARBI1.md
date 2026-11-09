---
symbol: "HARBI1"
type: "gene"
col: 11106
ensembl_id: "ENSG00000180423"
name: "harbinger transposase derived 1"
location: "11p11.2"
module: 170
arm: "+"
pooled_cpm: 2.49
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 7
n_dd_up_clean: 13
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/170"]
generated_by: "tahoemap"
---

# HARBI1

*harbinger transposase derived 1* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.24× (z +12.7, q 6e-34, up in 23 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.688× (z -4.2, q 0.010, down in 16 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFAF1]] (+0.70, fdr 1e-05), [[HELQ]] (+0.65, fdr 1e-05), [[TJAP1]] (+0.63, fdr 1e-05); moves opposite to [[LDHB]] (-0.62, fdr 3e-05), [[METAP1]] (-0.59, fdr 3e-05), [[AHSA1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 170]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11106.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +12.7 | 6e-34 | 23/32 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.05×** | +11.3 | 5e-27 | 22/32 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.25×** | +9.0 | 4e-17 | 19/31 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.98×** | +7.3 | 4e-11 | 16/37 (MIA PaCa-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.87×** | +6.9 | 4e-10 | 20/43 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.85×** | +6.8 | 9e-10 | 16/45 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.81×** | +6.6 | 4e-09 | 15/42 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +6.4 | 1e-08 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +6.0 | 9e-08 | 9/16 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.58×** | +5.5 | 2e-06 | 6/35 (SW480, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +5.5 | 2e-06 | 2/13 (SW480, MIA PaCa-2) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +5.0 | 3e-05 | 1/4 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.46×** | +4.2 | 0.001 | 7/38 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +4.1 | 0.002 | 0/13 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +3.7 | 0.009 | 3/44 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.39×** | +3.6 | 0.009 | 4/16 (PANC-1, NCI-H1573, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.012 | 5/42 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.53×** | +3.4 | 0.021 | 1/26 (NCI-H1573) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11106.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.688×** | -4.2 | 0.010 | 16/42 (A549, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.690×** | -4.1 | 0.010 | 13/36 (HT-29, MIA PaCa-2, …) | top dose only |  |
| [[Verapamil (drug)]] 0.05 µM |  | **0.692×** | -3.8 | 0.027 | 5/38 (SK-MEL-2, SNU-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.716×** | -3.6 | 0.049 | 8/21 (LoVo, A549, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dorzolamide (hydrochloride) (drug)]] 5 µM |  | **0.721×** | -3.5 | 0.051 | 6/41 (LS 180, AsPC-1, …) | top dose only |  |
| [[Menadione (drug)]] 5 µM |  | **0.737×** | -3.3 | 0.092 | 10/34 (HEC-1-A, NCI-H1792, …) | top dose only |  |
| [[Roxadustat (drug)]] 5 µM |  | **0.738×** | -3.3 | 0.092 | 9/39 (A-172, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11106. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 2.96 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.5 µM 0.0562× (z -9.2) |
| [[KATO III (line)]] | alt | 4.36 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0764× (z -9.2) |
| [[LoVo (line)]] | wt | 2.68 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0931× (z -8.5) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 1.71 | 0 | 1 | — | [[Sodium Salicylate (drug)]] 0.5 µM 0.0457× (z -9.8) |
| [[PANC-1 (line)]] | alt | 2.24 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0981× (z -8.6) ⚠ toxic |
| [[A-172 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.788 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11106), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFAF1]] | +0.70 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[HELQ]] | +0.65 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[TJAP1]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[KMT5B]] | +0.62 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[BCDIN3D]] | +0.62 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[ZSCAN21]] | +0.61 | +0.73 / +0.41 | both halves | 4e-05 |  |
| [[NAIF1]] | +0.61 | +0.69 / +0.50 | both halves | 1e-05 | STRING 922 |
| [[TCEANC]] | +0.61 | +0.76 / +0.45 | both halves | 3e-05 |  |
| [[COQ5]] | +0.60 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[SMIM19]] | +0.60 | +0.68 / +0.46 | both halves | 3e-05 |  |
| [[CUTALP]] | +0.60 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[CYP20A1]] | +0.59 | +0.64 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LDHB]] | -0.62 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[METAP1]] | -0.59 | -0.67 / -0.44 | both halves | 3e-05 |  |
| [[AHSA1]] | -0.58 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[HSPE1]] | -0.57 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[PRDX3]] | -0.57 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[HSPD1]] | -0.56 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[CACYBP]] | -0.56 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[CHRNA5]] | -0.56 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[APP]] | -0.55 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[HACD3]] | -0.55 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[LAPTM4B]] | -0.54 | -0.54 / -0.40 | both halves | 4e-05 |  |
| [[DPY19L1]] | -0.54 | -0.65 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 170]]; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.753). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-28.5, 8.3); signed map (6.7, -18.1). **Vector** length 41.3, 4.38% of its response variance represented; |z| ≥ 3 in 992 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +3.1 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +12.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.0 | +11.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.7 | +9.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.5 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.0 | +1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.0 | +1.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.4 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.9 | -4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -2.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -0.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.0 | -0.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -0.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | harbinger transposase derived 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:46,602,861-46,617,909 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32675; previously C11orf77 |
| Gene groups (HGNC) | Harbinger transposase derived genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96MB7](https://www.uniprot.org/uniprotkb/Q96MB7) (Putative nuclease HARBI1):

> Transposase-derived protein that may have nuclease activity (Potential). Does not have transposase activity.

**Summary**, from NCBI Gene [283254](https://www.ncbi.nlm.nih.gov/gene/283254):

> Predicted to enable hydrolase activity; metal ion binding activity; and nuclease activity. Located in cytosol and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26522](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26522) · Entrez [283254](https://www.ncbi.nlm.nih.gov/gene/283254) · UniProt [Q96MB7](https://www.uniprot.org/uniprotkb/Q96MB7) · Ensembl [ENSG00000180423](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180423)

## Data

Gene col 11106: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11106); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11106, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11106]; `tensor/DDL_lfc|DDL_z.npy` [11106]; `embed/gene_vectors.npy` [11106]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11106 or target_col == 11106). Every well: [[HARBI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HARBI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
