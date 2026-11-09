---
symbol: "NOTCH1"
type: "gene"
col: 7279
ensembl_id: "ENSG00000148400"
name: "notch receptor 1"
location: "9q34.3"
module: 2
arm: "+"
pooled_cpm: 22.25
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 4
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# NOTCH1

*notch receptor 1* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.71× (z +15.7, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.343× (z -8.9, q 5e-16, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFPM1]] (+0.70, fdr 7e-06), [[PLEKHO2]] (+0.58, fdr 1e-05), [[FOXP4]] (+0.57, fdr 1e-05); moves opposite to [[ANKRD13C]] (-0.54, fdr 4e-05), [[NHLRC3]] (-0.54, fdr 1e-05), [[MFF]] (-0.45, fdr 3e-04).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7279.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.71×** | +15.7 | 0e+00 | 44/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +14.9 | 0e+00 | 34/46 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +13.3 | 8e-38 | 33/47 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.22×** | +12.5 | 6e-34 | 41/47 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.11×** | +11.8 | 7e-30 | 37/46 (BT-474, HOP62, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.91×** | +10.2 | 3e-22 | 35/46 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +6.3 | 2e-08 | 27/47 (MIA PaCa-2, KATO III, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.0 | 3e-05 | 24/45 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.74×** | +4.6 | 3e-04 | 14/45 (Panc 03.27, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 0.003 | 16/45 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.018 | 11/47 (Hs 766T, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +3.6 | 0.018 | 15/47 (A498, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.31×** | +3.4 | 0.032 | 15/46 (NCI-H460, RKO, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.22×** | +3.1 | 0.068 | 9/42 (A549, SNU-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.070 | 7/47 (A498, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.093 | 13/46 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7279.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.343×** | -8.9 | 5e-16 | 31/47 (RKO, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.556×** | -4.9 | 3e-04 | 19/44 (HOP62, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.724×** | -4.1 | 0.008 | 16/39 (LS 180, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.779×** | -3.8 | 0.018 | 19/46 (HS-578T, RKO, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.813× | -3.2 | 0.16 | 7/46 (AsPC-1, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7279. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.6 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.92× (z +13.6) | — |
| [[LoVo (line)]] | wt | 17.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +11.8) | — |
| [[A549 (line)]] | wt | 13.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +12.4) | — |
| [[AsPC-1 (line)]] | alt | 28.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.94× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 21.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.277× (z -8.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 26.0 | 1 | 1 | [[Auranofin (drug)]] 5 µM 4.03× (z +10.2) | [[PH-797804 (drug)]] 5 µM 0.110× (z -8.6) |
| [[KATO III (line)]] | alt | 24.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.42× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 39.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.54× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 5.81 | 0 | 2 | — | [[Mozavaptan (drug)]] 5 µM 0.0929× (z -10.5) |
| [[PANC-1 (line)]] | alt | 9.24 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.72× (z +11.0) | — |
| [[RKO (line)]] | wt | 45.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +11.5) | — |
| [[SW480 (line)]] | alt | 31.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.06× (z +9.5) | — |
| [[A498 (line)]] | wt | 22.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +9.8) | — |
| [[BT-474 (line)]] | alt | 18.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.9× (z +12.6) | — |
| [[C32 (line)]] | wt | 50.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +10.3) | — |
| [[CHP-212 (line)]] | wt | 82.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -8.6) |
| [[Hs 766T (line)]] | wt | 25.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.11× (z +8.9) | — |
| [[J82 (line)]] | alt | 21.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.94× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 34.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 5.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 23.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +11.2) | — |
| [[SW1417 (line)]] | alt | 25.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.66× (z +8.8) | — |
| [[A-172 (line)]] | wt | 64.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7279), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFPM1]] | +0.70 | +0.59 / +0.68 | both halves | 7e-06 | same gene group |
| [[PLEKHO2]] | +0.58 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[FOXP4]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 | same gene group |
| [[CEP170B]] | +0.57 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[RELT]] | +0.57 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[ABCD1]] | +0.56 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[NSMF]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 | same gene group |
| [[INPP5A]] | +0.56 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[IGSF9B]] | +0.55 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[SMTN]] | +0.55 | +0.52 / +0.46 | both halves | 3e-05 | pathway: HALLMARK_MYOGENESIS |
| [[TTYH3]] | +0.54 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[CDKN1A]] | +0.54 | +0.58 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_MYOGENESIS; STRING 680 |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD13C]] | -0.54 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[NHLRC3]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[MFF]] | -0.45 | -0.27 / -0.57 | both halves | 3e-04 |  |
| [[FBXO9]] | -0.44 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[DUT]] | -0.44 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[WBP11]] | -0.44 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[FIGN]] | -0.44 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[TTC23]] | -0.43 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[SRBD1]] | -0.43 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[NDUFB6]] | -0.43 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[SCRN3]] | -0.43 | -0.24 / -0.49 | both halves | 5e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.489). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (15.8, -6.5); signed map (-9.6, 30.6). **Vector** length 94.8, 21.1% of its response variance represented; |z| ≥ 3 in 1,074 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.7 | +11.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.7 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +6.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.1 | +2.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.7 | +14.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.5 | +2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.8 | +4.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -7.3 | -8.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.9 | -4.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -1.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.5 | -3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -1.9 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | notch receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:136,494,433-136,546,048 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously TAN1 |
| Gene groups (HGNC) | Notch receptors; MicroRNA protein coding host genes |
| Hallmark sets | NOTCH_SIGNALING, WNT_BETA_CATENIN_SIGNALING, MYOGENESIS, P53_PATHWAY |
| Reactome | 56 pathways, smallest: Defective LFNG causes SCDO3; FBXW7 Mutants and NOTCH1 in Cancer; Loss of Function of FBXW7 in Cancer and NOTCH1 Signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P46531](https://www.uniprot.org/uniprotkb/P46531) (Neurogenic locus notch homolog protein 1):

> Functions as a receptor for membrane-bound ligands Jagged-1 (JAG1), Jagged-2 (JAG2) and Delta-1 (DLL1) to regulate cell-fate determination. Upon ligand activation through the released notch intracellular domain (NICD) it forms a transcriptional activator complex with RBPJ/RBPSUH and activates genes of the enhancer of split locus. Affects the implementation of differentiation, proliferation and apoptotic programs. Involved in angiogenesis; negatively regulates endothelial cell proliferation and …

**Summary**, from NCBI Gene [4851](https://www.ncbi.nlm.nih.gov/gene/4851):

> This gene encodes a member of the NOTCH family of proteins. Members of this Type I transmembrane protein family share structural characteristics including an extracellular domain consisting of multiple epidermal growth factor-like (EGF) repeats, and an intracellular domain consisting of multiple different domain types. Notch signaling is an evolutionarily conserved intercellular signaling pathway that regulates interactions between physically adjacent cells through binding of Notch family …

**Accessions** — [HGNC:7881](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7881) · Entrez [4851](https://www.ncbi.nlm.nih.gov/gene/4851) · UniProt [P46531](https://www.uniprot.org/uniprotkb/P46531) · Ensembl [ENSG00000148400](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148400)

## Data

Gene col 7279: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7279); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7279, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7279]; `tensor/DDL_lfc|DDL_z.npy` [7279]; `embed/gene_vectors.npy` [7279]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7279 or target_col == 7279). Every well: [[NOTCH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOTCH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
