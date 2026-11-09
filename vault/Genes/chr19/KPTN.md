---
symbol: "KPTN"
type: "gene"
col: 3966
ensembl_id: "ENSG00000118162"
name: "kaptin, actin binding protein"
location: "19q13.32"
module: 53
arm: "+"
pooled_cpm: 2.97
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# KPTN

*kaptin, actin binding protein* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.22× (z +17.9, q 0e+00, up in 26 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.686× (z -4.1, q 0.025, down in 11 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Azithromycin (hydrate) (drug)]] 0.5 µM in 1 line (HT-29 0.0487×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0867×; ⚠ cell-cycle shift, explains ~0% of this change); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.0892×; ⚠ toxic); [[Belinostat (drug)]] 0.5 µM in 1 line (A-427 0.105×); [[Oxaprozin (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0900×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC8A2]] (+0.74, fdr 7e-06, ⚠ same locus), [[GARIN1B]] (+0.69, fdr 1e-05), [[USP50]] (+0.67, fdr 2e-05), [[MPDU1]] (+0.67, fdr 1e-05); moves opposite to [[NBPF3]] (-0.58, fdr 4e-05), [[MRPS31P5-1]] (-0.56, fdr 2e-05), [[TMEM185A]] (-0.56, fdr 3e-05).
> It is in [[Module 053]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3966.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.22×** | +17.9 | 0e+00 | 26/36 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.10×** | +17.3 | 0e+00 | 30/34 (SW1417, HS-578T, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.44×** | +12.8 | 2e-35 | 3/4 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.87×** | +11.4 | 6e-28 | 15/17 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.59×** | +9.5 | 3e-19 | 2/4 (CFPAC-1, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +6.1 | 9e-08 | 15/42 (H4, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +5.0 | 4e-05 | 6/18 (Hs 766T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +4.4 | 7e-04 | 3/46 (A-427, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +4.0 | 0.004 | 11/35 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.48×** | +3.9 | 0.005 | 5/31 (NCI-H2030, NCI-H1573, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.45×** | +3.8 | 0.007 | 4/42 (HEC-1-A, CFPAC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.42×** | +3.5 | 0.020 | 7/30 (BT-474, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Larotrectinib (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.027 | 3/44 (PANC-1, NCI-H1573, …) | rises with dose | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.034 | 5/33 (SNU-423, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.35×** | +3.2 | 0.044 | 6/46 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.064 | 5/39 (HOP62, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3966.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Azithromycin (hydrate) (drug)]] 0.5 µM in 1 line (HT-29 0.0487×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0867×; ⚠ cell-cycle shift, explains ~0% of this change); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.0892×; ⚠ toxic); [[Belinostat (drug)]] 0.5 µM in 1 line (A-427 0.105×); [[Oxaprozin (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0900×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.686×** | -4.1 | 0.025 | 11/34 (A-427, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Erlotinib (drug)]] 5 µM |  | 0.713× | -3.5 | 0.12 | 10/40 (HOP62, SNU-423, …) | rises with dose |  |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | 0.803× | -3.4 | 0.14 | 6/44 (A-427, AN3 CA, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.819× | -3.1 | 0.30 | 8/45 (H4, NCI-H661, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3966. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 4.38 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.105× (z -8.7) |
| [[HT-29 (line)]] | alt | 4.40 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0487× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 2.73 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0900× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 4.53 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0867× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 6.55 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0892× (z -10.1) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 1.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.7× (z +13.7) | — |
| [[A-172 (line)]] | wt | 0.988 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3966), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC8A2]] | +0.74 | +0.75 / +0.63 | both halves | 7e-06 | ⚠ same locus (3.3 kb, same strand: neighbours can correlate without regulation) |
| [[GARIN1B]] | +0.69 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[USP50]] | +0.67 | +0.74 / +0.47 | both halves | 2e-05 |  |
| [[MPDU1]] | +0.67 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[ZNF34]] | +0.67 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[GPR137]] | +0.66 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[UBE2D3-AS1]] | +0.66 | +0.74 / +0.44 | both halves | 3e-05 |  |
| [[MMP25]] | +0.66 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[AXDND1]] | +0.66 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[SPART-AS1]] | +0.65 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[AP5S1]] | +0.65 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[GRIK5]] | +0.65 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[C19orf54]] | +0.64 | +0.66 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF3]] | -0.58 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[MRPS31P5-1]] | -0.56 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[TMEM185A]] | -0.56 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[RECK]] | -0.55 | -0.56 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.645). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.7, -11.0); signed map (20.5, 11.1). **Vector** length 52.5, 6.32% of its response variance represented; |z| ≥ 3 in 1,081 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +12.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +17.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +17.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +3.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.9 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -2.2 | -4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Ciclopirox (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | kaptin, actin binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:47,475,150-47,484,265 (-) |
| Ensembl biotype | protein_coding |
| Also known as | 2E4, KICS4 |
| Gene groups (HGNC) | KICSTOR complex |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 4 pathways, smallest: Amino acids regulate mTORC1; Cellular response to starvation; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y664](https://www.uniprot.org/uniprotkb/Q9Y664) (KICSTOR complex protein kaptin):

> As part of the KICSTOR complex functions in the amino acid-sensing branch of the TORC1 signaling pathway. Recruits, in an amino acid-independent manner, the GATOR1 complex to the lysosomal membranes and allows its interaction with GATOR2 and the RAG GTPases. Functions upstream of the RAG GTPases and is required to negatively regulate mTORC1 signaling in absence of amino acids. In absence of the KICSTOR complex mTORC1 is constitutively localized to the lysosome and activated. The KICSTOR complex …

**Summary**, from NCBI Gene [11133](https://www.ncbi.nlm.nih.gov/gene/11133):

> This gene encodes a filamentous-actin-associated protein, which is involved in actin dynamics and plays an important role in neuromorphogenesis. This protein is part of the KICSTOR protein complex that localizes to lysosomes. Mutations in this gene result in an autosomal recessive form of intellectual disability. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jul 2017]

**Accessions** — [HGNC:6404](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6404) · Entrez [11133](https://www.ncbi.nlm.nih.gov/gene/11133) · UniProt [Q9Y664](https://www.uniprot.org/uniprotkb/Q9Y664) · Ensembl [ENSG00000118162](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118162)

## Data

Gene col 3966: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3966); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3966, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3966]; `tensor/DDL_lfc|DDL_z.npy` [3966]; `embed/gene_vectors.npy` [3966]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3966 or target_col == 3966). Every well: [[KPTN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KPTN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
