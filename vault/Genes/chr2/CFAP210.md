---
symbol: "CFAP210"
type: "gene"
col: 7809
ensembl_id: "ENSG00000154479"
name: "cilia and flagella associated protein 210"
location: "2q31.1"
module: 205
arm: "+"
pooled_cpm: 6.07
n_lines_expressing: 49
n_dd_up: 40
n_dd_down: 9
n_dd_up_clean: 32
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/205"]
generated_by: "tahoemap"
---

# CFAP210

*cilia and flagella associated protein 210* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 9.99× (z +12.7, q 2e-34, up in 46 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[TAK-733 (drug)]] 0.05 µM: 0.449× (z -4.2, q 0.015, down in 18 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MLF1]] (+0.76, fdr 7e-06), [[OSR2]] (+0.75, fdr 7e-06), [[CCDC157]] (+0.74, fdr 7e-06); moves opposite to [[SDHC]] (-0.47, fdr 8e-05), [[MICALL1]] (-0.46, fdr 8e-05), [[WASH2P-1]] (-0.46, fdr 1e-04).
> It is in [[Module 205]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7809.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **9.99×** | +12.7 | 2e-34 | 46/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **7.22×** | +10.9 | 2e-25 | 42/45 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.72×** | +7.8 | 1e-12 | 29/38 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **4.37×** | +6.3 | 4e-08 | 38/46 (NCI-H460, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +6.3 | 5e-08 | 25/38 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.96×** | +6.0 | 2e-07 | 31/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **2.79×** | +5.7 | 1e-06 | 27/46 (HOP62, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **2.44×** | +4.7 | 2e-04 | 4/10 (HOP62, PANC-1, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **2.31×** | +4.5 | 5e-04 | 13/27 (SW480, CFPAC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.23×** | +4.4 | 5e-04 | 17/37 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **2.28×** | +4.2 | 0.001 | 7/17 (HEC-1-A, J82, …) | all doses, flat | composition shift |
| [[Artemether (drug)]] 0.05 µM |  | **2.06×** | +4.0 | 0.003 | 19/46 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **3.94×** | +4.0 | 0.003 | 16/43 (SW480, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cyclosporin A (drug)]] 0.05 µM |  | **2.04×** | +3.9 | 0.003 | 21/46 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.99×** | +3.8 | 0.006 | 12/24 (AsPC-1, SW480, …) | all doses, flat | composition shift |
| [[Sulfatinib (drug)]] 5 µM |  | **2.02×** | +3.7 | 0.007 | 20/45 (HOP62, SW 900, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.05 µM |  | **1.92×** | +3.6 | 0.011 | 17/42 (A498, LOX-IMVI, …) | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.89×** | +3.5 | 0.013 | 20/46 (SW480, AsPC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.88×** | +3.5 | 0.014 | 16/46 (NCI-H2030, NCI-H1573, …) | inconsistent across doses |  |
| [[Procainamide (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +3.4 | 0.015 | 16/41 (NCI-H1573, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7809.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-733 (drug)]] 0.05 µM |  | **0.449×** | -4.2 | 0.015 | 18/46 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.634×** | -3.6 | 0.065 | 17/44 (HS-578T, SW 900, …) | all doses, stronger at high dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | **0.435×** | -3.6 | 0.065 | 18/46 (HOP62, SNU-423, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.449×** | -3.4 | 0.081 | 16/46 (hTERT-HPNE, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.548×** | -3.3 | 0.083 | 19/39 (RKO, HS-578T, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.05 µM |  | **0.536×** | -3.3 | 0.083 | 13/43 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses |  |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | **0.537×** | -3.3 | 0.083 | 15/46 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.471×** | -3.2 | 0.083 | 20/46 (NCI-H2030, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | **0.478×** | -3.2 | 0.093 | 13/46 (HOP62, H4, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.84 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7809. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.72 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 18.8× (z +10.3) | — |
| [[LoVo (line)]] | wt | 2.26 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 17.4× (z +8.6) | — |
| [[SW480 (line)]] | alt | 5.83 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 10.7× (z +9.1) | — |
| [[A-172 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7809), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLF1]] | +0.76 | +0.71 / +0.78 | both halves | 7e-06 |  |
| [[OSR2]] | +0.75 | +0.71 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[CCDC157]] | +0.74 | +0.71 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[KIF9]] | +0.70 | +0.77 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[FOSB]] | +0.70 | +0.69 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[TMEM67]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[CCDC40]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[NUP62CL]] | +0.60 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[FOS]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ZNF487]] | +0.58 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[MAK]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[PRKCG]] | +0.58 | +0.58 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHC]] | -0.47 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[MICALL1]] | -0.46 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[WASH2P-1]] | -0.46 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[LTO1]] | -0.45 | -0.25 / -0.51 | both halves | 4e-04 |  |
| [[EXO5-DT]] | -0.45 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[PGS1]] | -0.44 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[NACC1]] | -0.44 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[ZNF562]] | -0.43 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[SNRNP35]] | -0.43 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[CCDC120]] | -0.43 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[PIGC]] | -0.42 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[ZNF746]] | -0.42 | -0.39 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 205]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.747). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.1, -28.4); signed map (-0.0, 18.3). **Vector** length 88.5, 20.9% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | +3.5 | +5.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | +3.0 | +1.5 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +2.4 | +3.9 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | +2.3 | +1.4 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | +2.3 | +3.3 |
|  | [[Artemether (drug)]] 0.05 µM |  | +2.2 | +4.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.9 | -0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.9 | -3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -0.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | -2.2 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | -2.9 | -3.6 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -2.7 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.7 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | cilia and flagella associated protein 210 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:169,645,425-169,694,405 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LOC129881; previously C2orf77, CCDC173 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q0VFZ6](https://www.uniprot.org/uniprotkb/Q0VFZ6) (Cilia- and flagella- associated protein 210):

> Microtubule inner protein (MIP) part of the dynein-decorated doublet microtubules (DMTs) in cilia axoneme, which is required for motile cilia beating.

**Summary**, from NCBI Gene [129881](https://www.ncbi.nlm.nih.gov/gene/129881):

> Predicted to be involved in flagellated sperm motility. Located in axonemal microtubule. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25064](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25064) · Entrez [129881](https://www.ncbi.nlm.nih.gov/gene/129881) · UniProt [Q0VFZ6](https://www.uniprot.org/uniprotkb/Q0VFZ6) · Ensembl [ENSG00000154479](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154479)

## Data

Gene col 7809: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7809); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7809, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7809]; `tensor/DDL_lfc|DDL_z.npy` [7809]; `embed/gene_vectors.npy` [7809]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7809 or target_col == 7809). Every well: [[CFAP210 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP210.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
