---
symbol: "PGLS"
type: "gene"
col: 5052
ensembl_id: "ENSG00000130313"
name: "6-phosphogluconolactonase"
location: "19p13.11"
module: 24
arm: "+"
pooled_cpm: 14.21
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 16
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# PGLS

*6-phosphogluconolactonase* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.54× (z +8.3, q 6e-14, up in 33 of 37 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 4.78×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 4.40×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.425× (z -10.7, q 4e-24, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IP6K1]] (+0.61, fdr 3e-05), [[BTBD7]] (+0.61, fdr 1e-05), [[COMTD1]] (+0.60, fdr 3e-05); moves opposite to [[TMX1]] (-0.57, fdr 6e-05), [[PAICS]] (-0.54, fdr 2e-04), [[SRP9]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5052.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 4.78×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 4.40×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.54×** | +8.3 | 6e-14 | 33/37 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +6.0 | 7e-07 | 19/28 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +4.7 | 5e-04 | 23/32 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +3.4 | 0.080 | 22/44 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.43× | +3.0 | 0.26 | 19/40 (HT-29, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5052.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.425×** | -10.7 | 4e-24 | 41/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.444×** | -7.2 | 2e-10 | 37/48 (BT-474, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.494×** | -6.3 | 7e-08 | 37/47 (BT-474, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.570×** | -5.0 | 9e-05 | 33/47 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.586×** | -4.7 | 2e-04 | 32/47 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.605×** | -4.4 | 8e-04 | 31/48 (NCI-H23, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.619×** | -4.3 | 0.002 | 22/48 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.420×** | -4.0 | 0.004 | 26/48 (Panc 03.27, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.425×** | -4.0 | 0.004 | 22/43 (KATO III, NCI-H23, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.671×** | -3.5 | 0.023 | 23/46 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.681×** | -3.4 | 0.034 | 21/46 (RPMI-7951, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.686×** | -3.3 | 0.040 | 20/46 (LS 180, SNU-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.767×** | -3.3 | 0.040 | 20/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.695×** | -3.1 | 0.079 | 19/46 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.707×** | -3.1 | 0.080 | 19/48 (BT-474, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.694×** | -3.0 | 0.100 | 11/48 (SW 1088, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5052. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 25.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -11.8) |
| [[BT-474 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 16.3 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0728× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 18.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -8.9) |
| [[J82 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -10.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 8.10 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.1000× (z -17.5) |
| [[NCI-H460 (line)]] | wt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 35.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -8.8) |
| [[PANC-1 (line)]] | alt | 9.98 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -8.5) |
| [[SW480 (line)]] | alt | 14.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.40× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.97 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5052), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 9 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IP6K1]] | +0.61 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[BTBD7]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[COMTD1]] | +0.60 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[ANKRD49]] | +0.60 | +0.37 / +0.71 | both halves | 8e-05 |  |
| [[MAP3K10]] | +0.59 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[SMIM26]] ⚠ | +0.59 | +0.35 / +0.66 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[USP42]] | +0.58 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[SSNA1]] | +0.58 | +0.41 / +0.66 | both halves | 4e-05 |  |
| [[LINC00685]] | +0.57 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[OXLD1]] | +0.57 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[SCAND1]] | +0.56 | +0.30 / +0.61 | both halves | 2e-04 |  |
| [[FBXW5]] | +0.56 | +0.36 / +0.67 | both halves | 1e-04 |  |
| [[C1orf122]] | +0.56 | +0.38 / +0.57 | both halves | 7e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMX1]] | -0.57 | -0.38 / -0.61 | both halves | 6e-05 |  |
| [[PAICS]] | -0.54 | -0.32 / -0.62 | both halves | 2e-04 |  |
| [[SRP9]] | -0.53 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[PRPS2]] | -0.52 | -0.40 / -0.52 | both halves | 4e-05 | pathway: Metabolism of carbohydrates and carbohydrate derivatives; STRING 487 |
| [[FKBP1A]] | -0.52 | -0.24 / -0.62 | both halves | 5e-04 |  |
| [[TMEM123]] | -0.51 | -0.36 / -0.55 | both halves | 9e-05 |  |
| [[RBBP7]] | -0.49 | -0.32 / -0.56 | both halves | 2e-04 |  |
| [[HELLS]] | -0.49 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[TFRC]] | -0.48 | -0.31 / -0.61 | both halves | 2e-04 | pathway: HALLMARK_HEME_METABOLISM |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.573). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-44.6, -15.7); signed map (-22.3, -2.0). **Vector** length 46.6, 7.57% of its response variance represented; |z| ≥ 3 in 633 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +1.3 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +1.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.4 | +0.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.2 | +1.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.1 | +1.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -0.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -6.3 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -0.9 | -1.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | 6-phosphogluconolactonase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:17,511,636-17,521,288 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 6PGL |
| Hallmark sets | HEME_METABOLISM, GLYCOLYSIS |
| Reactome | 2 pathways, smallest: Pentose phosphate pathway; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [O95336](https://www.uniprot.org/uniprotkb/O95336) (6-phosphogluconolactonase):

> Hydrolysis of 6-phosphogluconolactone to 6-phosphogluconate.

**Summary**, from NCBI Gene [25796](https://www.ncbi.nlm.nih.gov/gene/25796):

> Enables 6-phosphogluconolactonase activity. Involved in pentose-phosphate shunt. Acts upstream of or within pentose-phosphate shunt, oxidative branch. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:8903](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8903) · Entrez [25796](https://www.ncbi.nlm.nih.gov/gene/25796) · UniProt [O95336](https://www.uniprot.org/uniprotkb/O95336) · Ensembl [ENSG00000130313](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130313)

## Data

Gene col 5052: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5052); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5052, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5052]; `tensor/DDL_lfc|DDL_z.npy` [5052]; `embed/gene_vectors.npy` [5052]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5052 or target_col == 5052). Every well: [[PGLS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGLS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
