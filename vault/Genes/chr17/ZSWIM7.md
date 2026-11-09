---
symbol: "ZSWIM7"
type: "gene"
col: 13232
ensembl_id: "ENSG00000214941"
name: "zinc finger SWIM-type containing 7"
location: "17p12"
module: 28
arm: "+"
pooled_cpm: 17.71
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# ZSWIM7

*zinc finger SWIM-type containing 7* — 17p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.41× (z +12.2, q 1e-31, up in 30 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.53× (z +6.0, q 3e-07, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.641× (z -6.1, q 5e-07, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF354A]] (+0.61, fdr 7e-06), [[TLCD5]] (+0.55, fdr 7e-06), [[MDM4]] (+0.54, fdr 1e-05); moves opposite to [[TPI1]] (-0.54, fdr 2e-05), [[GUCD1]] (-0.51, fdr 3e-05), [[SERPINH1]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13232.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.41×** | +12.2 | 1e-31 | 30/38 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.46×** | +12.0 | 7e-31 | 23/28 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +8.9 | 1e-16 | 25/35 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +6.0 | 3e-07 | 22/48 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +5.3 | 2e-05 | 24/47 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +5.2 | 2e-05 | 17/48 (SW480, HOP62, …) | rises with dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.45×** | +5.0 | 6e-05 | 19/47 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +4.4 | 7e-04 | 19/47 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.010 | 13/47 (A-172, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.30×** | +3.6 | 0.014 | 14/47 (KATO III, NCI-H2030, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.30×** | +3.6 | 0.014 | 14/47 (A-172, LS 180, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.017 | 10/47 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Decitabine (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.050 | 9/47 (AN3 CA, SHP-77, …) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 5 µM |  | **1.52×** | +3.0 | 0.089 | 3/43 (A498, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.089 | 13/47 (HEC-1-A, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13232.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.641×** | -6.1 | 5e-07 | 25/47 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.738×** | -4.2 | 0.008 | 17/48 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.575×** | -4.0 | 0.012 | 14/46 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.597×** | -3.7 | 0.026 | 12/48 (NCI-H23, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.783× | -3.2 | 0.16 | 15/48 (SK-MEL-2, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.797× | -3.1 | 0.16 | 7/48 (NCI-H1792, SK-MEL-2, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.802× | -3.0 | 0.19 | 17/47 (SNU-1, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13232. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 23.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.65× (z +12.3) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 21.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.07× (z +10.8) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -10.1) ⚠ cell-cycle shift, explains ~22% of this change |
| [[A549 (line)]] | wt | 34.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 10.6 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0984× (z -8.6) |
| [[HOP62 (line)]] | alt | 23.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.51× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 11.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.170× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.111× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~3% of this change |
| [[NCI-H2030 (line)]] | alt | 19.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 22.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 80.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 17.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0457× (z -13.2) |
| [[SW480 (line)]] | alt | 18.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.357× (z -8.5) |
| [[A-172 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13232), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF354A]] | +0.61 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[TLCD5]] | +0.55 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[MDM4]] | +0.54 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[TRMT10B]] | +0.54 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[CHURC1]] | +0.54 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[TYW5]] | +0.53 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[THEM4]] | +0.52 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[ZNF555]] | +0.51 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[VPS8]] | +0.51 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[AIMP2]] | +0.50 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[GEMIN8]] | +0.50 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[IAH1]] | +0.50 | +0.26 / +0.47 | both halves | 4e-04 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPI1]] | -0.54 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[GUCD1]] | -0.51 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[SERPINH1]] | -0.49 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[LIN54]] | -0.49 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[CENPO]] | -0.48 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[PGRMC1]] | -0.48 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[MTFR2]] | -0.47 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[SAR1A]] | -0.47 | -0.60 / -0.46 | both halves | 2e-05 |  |
| [[TOPBP1]] | -0.47 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[CHAF1B]] | -0.47 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[HSPA14]] | -0.46 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[KLHL3]] | -0.46 | -0.28 / -0.47 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.368). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-28.9, 4.6); signed map (4.9, -23.6). **Vector** length 70.2, 12.6% of its response variance represented; |z| ≥ 3 in 744 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +3.0 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +5.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +2.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +3.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | +0.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -1.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -3.4 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.4 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Arbutin (drug)]] 0.5 µM |  | -1.2 | -1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger SWIM-type containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p12 — chr17:15,976,560-15,999,717 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SWS1 |
| Gene groups (HGNC) | Zinc fingers SWIM-type; Shu complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q19AV6](https://www.uniprot.org/uniprotkb/Q19AV6) (Zinc finger SWIM domain-containing protein 7):

> Involved in early stages DNA double-strand break (DSB) repair via homologous recombination (HR). Forms a heterodimeric complex with ZSWIM7/SWS1 that promotes HR by regulating replication protein-A (RPA) dynamics on single-stranded DNA, thereby stabilizing RAD51 and DMC1 filaments on DNA. The SWSAP1-ZSWIM7/SWS1 heterodimer is essential during meiosis by stabilizing DMC1 filaments. In contrast, it is critical for only certain types of homologous-directed DNA repair, such as inter-homolog …

**Summary**, from NCBI Gene [125150](https://www.ncbi.nlm.nih.gov/gene/125150):

> Predicted to enable zinc ion binding activity. Involved in double-strand break repair via homologous recombination and protein stabilization. Part of Shu complex. Implicated in ovarian dysgenesis 10 and spermatogenic failure 71. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26993](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26993) · Entrez [125150](https://www.ncbi.nlm.nih.gov/gene/125150) · UniProt [Q19AV6](https://www.uniprot.org/uniprotkb/Q19AV6) · Ensembl [ENSG00000214941](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214941)

## Data

Gene col 13232: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13232); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13232, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13232]; `tensor/DDL_lfc|DDL_z.npy` [13232]; `embed/gene_vectors.npy` [13232]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13232 or target_col == 13232). Every well: [[ZSWIM7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSWIM7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
