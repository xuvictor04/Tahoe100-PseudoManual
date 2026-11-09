---
symbol: "PAX9"
type: "gene"
col: 12686
ensembl_id: "ENSG00000198807"
name: "paired box 9"
location: "14q13.3"
module: 82
arm: "+"
pooled_cpm: 4.03
n_lines_expressing: 42
n_dd_up: 19
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# PAX9

*paired box 9* — 14q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.23× (z +14.7, q 0e+00, up in 31 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.604× (z -6.3, q 2e-07, down in 13 of 37 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POMGNT2]] (+0.60, fdr 3e-05), [[ESYT3]] (+0.59, fdr 1e-05), [[WASF3]] (+0.58, fdr 2e-05); moves opposite to [[EOLA2-DT]] (-0.55, fdr 3e-05), [[ALOX12-AS1]] (-0.51, fdr 2e-04), [[ACYP2]] (-0.50, fdr 1e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12686.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.23×** | +14.7 | 0e+00 | 31/37 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.10×** | +14.2 | 4e-43 | 31/37 (NCI-H2030, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.90×** | +13.3 | 3e-38 | 32/38 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.12×** | +13.3 | 3e-38 | 28/37 (NCI-H2347, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.28×** | +10.3 | 8e-23 | 22/37 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +9.7 | 4e-20 | 19/32 (A549, RKO, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.07×** | +9.1 | 7e-18 | 19/30 (NCI-H2030, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.04×** | +7.3 | 3e-11 | 14/33 (NCI-H2347, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +7.1 | 8e-11 | 21/35 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.80×** | +7.1 | 9e-11 | 12/19 (SW 900, A498, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.73×** | +4.9 | 5e-05 | 3/15 (SHP-77, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.06×** | +4.7 | 1e-04 | 0/13 | top dose only | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.45×** | +4.6 | 2e-04 | 7/37 (NCI-H460, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.40×** | +4.2 | 9e-04 | 6/37 (NCI-H2347, SW 900, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.42×** | +4.2 | 9e-04 | 4/31 (SW 900, Panc 03.27, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.003 | 3/36 (SHP-77, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.030 | 4/30 (HT-29, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.27×** | +3.0 | 0.083 | 5/37 (SW 900, SW1417, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12686.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.604×** | -6.3 | 2e-07 | 13/37 (KATO III, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.878× | -5.7 | 3e-06 | 14/38 (SNU-1, LS 180, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.646×** | -5.5 | 9e-06 | 14/28 (NCI-H460, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.749×** | -3.6 | 0.045 | 5/37 (SNU-1, NCI-H661, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.758×** | -3.5 | 0.063 | 6/37 (NCI-H460, A549, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.597×** | -3.4 | 0.073 | 7/33 (HS-578T, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12686. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 11.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0671× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Sonidegib (drug)]] 5 µM 0.0721× (z -8.5) |
| [[BT-474 (line)]] | alt | 24.9 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0880× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 5.46 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 6.57 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.0865× (z -8.7) |
| [[A-172 (line)]] | wt | 0.306 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.349 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.352 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.325 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.541 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.252 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.02 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12686), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POMGNT2]] | +0.60 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[ESYT3]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[WASF3]] | +0.58 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[SDHAF3]] | +0.56 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[METAP1]] | +0.55 | +0.39 / +0.49 | both halves | 6e-05 |  |
| [[PRRG1]] | +0.55 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[LPAR3]] | +0.55 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[SEMA4F]] | +0.54 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[LHX6]] | +0.53 | +0.34 / +0.54 | both halves | 1e-04 | STRING 526 |
| [[FITM2]] | +0.53 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[MCOLN2]] | +0.52 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[IMPDH1]] | +0.52 | +0.39 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EOLA2-DT]] | -0.55 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ALOX12-AS1]] | -0.51 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[ACYP2]] | -0.50 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[LARP7]] | -0.50 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[CDKN2B-AS1]] | -0.50 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[FBXL19-AS1]] | -0.50 | -0.26 / -0.49 | both halves | 4e-04 |  |
| [[PMF1]] | -0.50 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[EFCAB6]] | -0.50 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[TBCE-1]] | -0.49 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[KANSL1L]] | -0.49 | -0.36 / -0.29 | both halves | 2e-04 |  |
| [[BCAS3]] | -0.49 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[C11orf58]] | -0.49 | -0.26 / -0.43 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.507). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.6, 39.7); signed map (-24.9, 33.9). **Vector** length 53.9, 8.04% of its response variance represented; |z| ≥ 3 in 963 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +13.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +7.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.7 | +10.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | +2.6 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +2.4 | +3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +7.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.4 | -0.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | -6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.8 | +3.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | +0.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -0.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -0.5 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.0 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | paired box 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q13.3 — chr14:36,657,568-36,679,362 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Paired boxes |
| Matched by | ensembl_id |

**Function**, from UniProt [P55771](https://www.uniprot.org/uniprotkb/P55771) (Paired box protein Pax-9):

> Transcription factor required for normal development of thymus, parathyroid glands, ultimobranchial bodies, teeth, skeletal elements of skull and larynx as well as distal limbs.

**Summary**, from NCBI Gene [5083](https://www.ncbi.nlm.nih.gov/gene/5083):

> This gene is a member of the paired box (PAX) family of transcription factors. Members of this gene family typically contain a paired box domain, an octapeptide, and a paired-type homeodomain. These genes play critical roles during fetal development and cancer growth. Mice lacking this gene exhibit impaired development of organs, musculature and the skeleton, including absent and abnormally developed teeth, and neonatal lethality. Mutations in the human gene are associated with selective tooth …

**Accessions** — [HGNC:8623](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8623) · Entrez [5083](https://www.ncbi.nlm.nih.gov/gene/5083) · UniProt [P55771](https://www.uniprot.org/uniprotkb/P55771) · Ensembl [ENSG00000198807](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198807)

## Data

Gene col 12686: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12686); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12686, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12686]; `tensor/DDL_lfc|DDL_z.npy` [12686]; `embed/gene_vectors.npy` [12686]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12686 or target_col == 12686). Every well: [[PAX9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAX9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
