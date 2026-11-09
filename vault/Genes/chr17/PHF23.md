---
symbol: "PHF23"
type: "gene"
col: 471
ensembl_id: "ENSG00000040633"
name: "PHD finger protein 23"
location: "17p13.1"
module: 7
arm: "+"
pooled_cpm: 9.9
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# PHF23

*PHD finger protein 23* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.37× (z +12.0, q 3e-30, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.732× (z -4.4, q 0.007, down in 17 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF629]] (+0.70, fdr 7e-06), [[PURB]] (+0.65, fdr 1e-05), [[DNAJB12]] (+0.62, fdr 2e-05); moves opposite to [[TUBE1]] (-0.59, fdr 1e-05), [[ANAPC5]] (-0.57, fdr 1e-05), [[HEATR5B]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 471.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.37×** | +12.0 | 3e-30 | 41/46 (LoVo, A-172, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.64×** | +6.6 | 1e-08 | 25/45 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +5.8 | 2e-06 | 5/48 (HEC-1-A, NCI-H1573, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +5.2 | 2e-05 | 19/47 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +4.7 | 3e-04 | 16/43 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.7 | 3e-04 | 13/46 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +4.6 | 3e-04 | 12/29 (LoVo, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Thymol (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.003 | 5/48 (Panc 03.27, SW1417, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.75×** | +4.1 | 0.003 | 16/46 (SW480, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.004 | 13/48 (HEC-1-A, HS-578T, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +3.7 | 0.011 | 12/45 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.015 | 12/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +3.4 | 0.025 | 8/47 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.035 | 12/46 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~13% of this change | **1.27×** | +3.3 | 0.036 | 13/40 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.052 | 9/46 (HT-29, PANC-1, …) | top dose only | position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.51×** | +3.0 | 0.088 | 3/41 (COLO 205, NCI-H2347, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 471.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.732×** | -4.4 | 0.007 | 17/47 (HT-29, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.730×** | -4.2 | 0.007 | 13/47 (NCI-H2030, NCI-H2347, …) | rises with dose | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.748×** | -4.1 | 0.009 | 16/47 (A-172, COLO 205, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.760×** | -3.8 | 0.018 | 17/47 (SW480, SW 900, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.771×** | -3.5 | 0.053 | 14/46 (RPMI-7951, HepG2/C3A, …) | top dose only |  |
| [[Flumatinib (mesylate) (drug)]] 0.5 µM |  | 0.803× | -3.1 | 0.18 | 5/47 (SW480, NCI-H2030, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.803× | -3.1 | 0.18 | 17/47 (A498, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 471. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 7.25 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.109× (z -9.6) |
| [[COLO 205 (line)]] | alt | 9.60 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0746× (z -10.0) |
| [[Hs 766T (line)]] | wt | 6.90 | 0 | 1 (1 ⚠) | — | [[OTS514 (drug)]] 0.05 µM 0.111× (z -8.8) ⚠ transcription drop |
| [[NCI-H1792 (line)]] | alt | 3.94 | 0 | 1 | — | [[Phenytoin (sodium) (drug)]] 0.05 µM 0.0573× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -10.8) ⚠ cell-cycle shift, explains ~7% of this change |
| [[NCI-H460 (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 6.09 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0559× (z -11.7) |
| [[SHP-77 (line)]] | alt | 15.7 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.182× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 9.03 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.140× (z -9.0) |
| [[SNU-1 (line)]] | wt | 12.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0952× (z -8.7) ⚠ cell-cycle shift, explains ~10% of this change |
| [[SNU-423 (line)]] | alt | 9.74 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0680× (z -12.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 13.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +9.1) ⚠ cell-cycle shift, explains ~97% of this change | — |
| [[A-172 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.78 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.31 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.75 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 471), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF629]] | +0.70 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[PURB]] | +0.65 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[DNAJB12]] | +0.62 | +0.46 / +0.67 | both halves | 2e-05 |  |
| [[SMCR8]] | +0.61 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ZBTB40]] | +0.60 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[CD2BP2]] | +0.59 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[HNRNPH2]] | +0.59 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[AP5B1]] | +0.58 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[SPEN]] | +0.58 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[SCAF1]] | +0.58 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[TMEM115]] | +0.57 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ZNF513]] | +0.57 | +0.56 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBE1]] | -0.59 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[ANAPC5]] | -0.57 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[HEATR5B]] | -0.57 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[COG5]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[SGK3]] | -0.53 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[FIG4]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[PPP1R2]] | -0.52 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[SEC23A]] | -0.51 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[NBPF3]] | -0.50 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[VDAC3]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[LCMT1]] | -0.49 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[ANAPC4]] | -0.49 | -0.48 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.599). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-37.9, 16.2); signed map (-1.8, -29.4). **Vector** length 76.5, 13.1% of its response variance represented; |z| ≥ 3 in 902 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.0 | +12.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.2 | +4.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.1 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +4.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.9 | +6.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +0.9 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | -2.4 | -2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.1 | -3.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.1 | -4.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | PHD finger protein 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,235,029-7,239,722 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2941, FLJ16355 |
| Gene groups (HGNC) | PHD finger proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUL5](https://www.uniprot.org/uniprotkb/Q9BUL5) (PHD finger protein 23):

> Acts as a negative regulator of autophagy, through promoting ubiquitination and degradation of LRSAM1, an E3 ubiquitin ligase that promotes autophagy in response to starvation or infecting bacteria.

**Summary**, from NCBI Gene [79142](https://www.ncbi.nlm.nih.gov/gene/79142):

> Predicted to enable zinc ion binding activity. Involved in negative regulation of autophagosome assembly; negative regulation of autophagosome maturation; and positive regulation of protein ubiquitination. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28428](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28428) · Entrez [79142](https://www.ncbi.nlm.nih.gov/gene/79142) · UniProt [Q9BUL5](https://www.uniprot.org/uniprotkb/Q9BUL5) · Ensembl [ENSG00000040633](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000040633)

## Data

Gene col 471: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 471); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 471, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 471]; `tensor/DDL_lfc|DDL_z.npy` [471]; `embed/gene_vectors.npy` [471]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 471 or target_col == 471). Every well: [[PHF23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHF23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
