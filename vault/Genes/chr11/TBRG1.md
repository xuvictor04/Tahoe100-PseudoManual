---
symbol: "TBRG1"
type: "gene"
col: 7777
ensembl_id: "ENSG00000154144"
name: "FYRN and FYRC domains INO80 complex interactor 1"
location: "11q24.2"
module: 29
arm: "-"
pooled_cpm: 44.2
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# TBRG1

*FYRN and FYRC domains INO80 complex interactor 1* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.60× (z +10.9, q 8e-25, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.577× (z -4.7, q 0.001, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBXN4]] (+0.61, fdr 1e-05), [[TSG101]] (+0.59, fdr 1e-05), [[NSRP1]] (+0.58, fdr 1e-05); moves opposite to [[SMAD6]] (-0.60, fdr 3e-05), [[TMEM123]] (-0.57, fdr 1e-05), [[ATP5F1B]] (-0.57, fdr 2e-05).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7777.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +10.9 | 8e-25 | 39/47 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.85×** | +10.0 | 3e-21 | 43/48 (HOP62, SW480, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.67×** | +8.1 | 1e-13 | 27/38 (LOX-IMVI, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.63×** | +7.9 | 3e-13 | 39/48 (HOP62, Hs 766T, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.62×** | +7.9 | 4e-13 | 31/48 (A-427, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +7.5 | 8e-12 | 37/47 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +7.0 | 3e-10 | 33/47 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.51×** | +6.7 | 1e-09 | 35/48 (HOP62, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.49×** | +6.5 | 6e-09 | 34/48 (NCI-H1573, HOP62, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +5.8 | 3e-07 | 33/48 (HOP62, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +5.7 | 5e-07 | 35/48 (LOX-IMVI, NCI-H23, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +5.5 | 1e-06 | 32/48 (HOP62, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.37×** | +4.9 | 4e-05 | 29/48 (LS 180, SW480, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.32×** | +4.3 | 7e-04 | 24/47 (RPMI-7951, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.27×** | +3.5 | 0.015 | 19/42 (Hs 766T, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.023 | 18/48 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.045 | 14/48 (SW 900, NCI-H460, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.048 | 14/48 (NCI-H2347, HT-29, …) | top dose only | position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.048 | 14/48 (NCI-H460, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.43×** | +3.0 | 0.064 | 11/48 (NCI-H1792, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.064 | 19/47 (J82, SW1417, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.087 | 10/47 (AsPC-1, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7777.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.577×** | -4.7 | 0.001 | 26/48 (RKO, BT-474, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.612×** | -4.2 | 0.007 | 20/49 (PANC-1, AsPC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.810×** | -3.5 | 0.095 | 19/48 (SW480, HS-578T, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7777. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 31.7 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.88× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 47.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 83.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +12.6) | — |
| [[A-427 (line)]] | wt | 31.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[COLO 205 (line)]] | alt | 31.9 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.226× (z -9.2) |
| [[Hs 766T (line)]] | wt | 45.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[LOX-IMVI (line)]] | wt | 40.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SW480 (line)]] | alt | 63.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.9) | — |
| [[A-172 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 60.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 55.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7777), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBXN4]] | +0.61 | +0.77 / +0.49 | both halves | 1e-05 |  |
| [[TSG101]] | +0.59 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[NSRP1]] | +0.58 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[ATF4]] | +0.57 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[DDX27]] | +0.56 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[RALGAPA1]] | +0.56 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[RBMX2]] | +0.56 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | +0.56 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[TIPRL]] | +0.56 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[MMADHC]] | +0.55 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[PRMT2]] | +0.54 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[ZNF761]] | +0.54 | +0.51 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMAD6]] | -0.60 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[TMEM123]] | -0.57 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[ATP5F1B]] | -0.57 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[H3-3A]] | -0.57 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[ILF2]] | -0.57 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[ANP32A]] | -0.56 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[C4orf46]] | -0.56 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[PGAM1]] | -0.56 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.54 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[FKBP1A]] | -0.53 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[STT3B]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[RANBP1]] | -0.53 | -0.51 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.553). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-38.8, -0.3); signed map (1.4, -13.5). **Vector** length 79.6, 18.7% of its response variance represented; |z| ≥ 3 in 726 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +4.6 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.1 | +5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +10.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.5 | +7.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.0 | +2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.0 | +1.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.3 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | -3.8 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -4.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -3.2 | +8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | +0.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.0 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | +0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | FYRN and FYRC domains INO80 complex interactor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:124,622,836-124,635,926 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14621, TB-5, NIAM; previously TBRG1 |
| Gene groups (HGNC) | INO80 complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3YBR2](https://www.uniprot.org/uniprotkb/Q3YBR2) (Transforming growth factor beta regulator 1):

> Acts as a growth inhibitor. Can activate p53/TP53, causes G1 arrest and collaborates with CDKN2A to restrict proliferation, but does not require either protein to inhibit DNA synthesis. Redistributes CDKN2A into the nucleoplasm. Involved in maintaining chromosomal stability.

**Summary**, from NCBI Gene [84897](https://www.ncbi.nlm.nih.gov/gene/84897):

> Involved in several processes, including DNA replication; protein localization to nucleoplasm; and protein stabilization. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29551](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29551) · Entrez [84897](https://www.ncbi.nlm.nih.gov/gene/84897) · UniProt [Q3YBR2](https://www.uniprot.org/uniprotkb/Q3YBR2) · Ensembl [ENSG00000154144](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154144)

## Data

Gene col 7777: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7777); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7777, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7777]; `tensor/DDL_lfc|DDL_z.npy` [7777]; `embed/gene_vectors.npy` [7777]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7777 or target_col == 7777). Every well: [[TBRG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBRG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
