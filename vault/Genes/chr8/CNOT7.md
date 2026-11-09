---
symbol: "CNOT7"
type: "gene"
col: 12677
ensembl_id: "ENSG00000198791"
name: "CCR4-NOT transcription complex subunit 7"
location: "8p22"
module: 57
arm: "+"
pooled_cpm: 67.04
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# CNOT7

*CCR4-NOT transcription complex subunit 7* — 8p22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.75× (z +11.3, q 1e-26, up in 41 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.26× (z +4.7, q 6e-04, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.703× (z -10.0, q 7e-21, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GFM2]] (+0.62, fdr 1e-05), [[SNRNP200]] (+0.62, fdr 3e-05), [[NAA20]] (+0.62, fdr 1e-05); moves opposite to [[HES4]] (-0.58, fdr 1e-05), [[PHLDA2]] (-0.52, fdr 3e-05), [[NFKBIB]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12677.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.75×** | +11.3 | 1e-26 | 41/48 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +11.2 | 2e-26 | 31/44 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +4.7 | 6e-04 | 26/48 (HS-578T, MIA PaCa-2, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.54×** | +4.5 | 9e-04 | 32/47 (KATO III, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.52×** | +4.4 | 0.001 | 26/49 (HS-578T, A498, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.26×** | +4.3 | 0.002 | 25/45 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.32×** | +3.9 | 0.007 | 23/46 (SK-MEL-2, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.22×** | +3.9 | 0.007 | 22/46 (NCI-H1573, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **1.21×** | +3.8 | 0.008 | 22/47 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.14× | +3.7 | 0.010 | 11/48 (LOX-IMVI, NCI-H2030, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.021 | 21/48 (CFPAC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.042 | 19/48 (A-172, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.047 | 18/48 (NCI-H23, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.16× | +3.0 | 0.10 | 19/48 (HS-578T, SNU-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12677.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.703×** | -10.0 | 7e-21 | 35/48 (NCI-H460, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.749×** | -5.6 | 7e-06 | 33/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pemetrexed (drug)]] 0.5 µM |  | **0.803×** | -4.4 | 0.002 | 26/47 (SW480, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -4.0 | 0.009 | 0/49 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12677. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 89.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.597× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 51.8 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -15.5) |
| [[A498 (line)]] | wt | 74.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +10.8) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 76.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -9.4) |
| [[PANC-1 (line)]] | alt | 31.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.35× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 70.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +9.0) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 78.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -9.0) |
| [[HS-578T (line)]] | alt | 80.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +8.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 64.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 54.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 47.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +9.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 81.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 133 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 70.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -9.5) |
| [[SNU-423 (line)]] | alt | 44.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.95× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 32.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 98.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.91× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 73.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 96.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 92.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 83.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 94.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 77.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 61.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 110 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 72.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 85.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 73.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12677), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GFM2]] | +0.62 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[SNRNP200]] | +0.62 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[NAA20]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[TMEM161B]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[VTA1]] | +0.59 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[SDHB]] | +0.59 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[TSN]] | +0.57 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[RTF2]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[MIGA1]] | +0.57 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[COMMD9]] | +0.57 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[UBE4A]] | +0.56 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[AQR]] | +0.56 | +0.51 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HES4]] | -0.58 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[PHLDA2]] | -0.52 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[NFKBIB]] | -0.50 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[MEMO1]] | -0.50 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[FLT3LG]] | -0.50 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[NPHS1]] | -0.49 | -0.43 / -0.37 | both halves | 9e-05 |  |
| [[ELOVL7]] | -0.48 | -0.40 / -0.46 | both halves | 4e-05 |  |
| [[TRAF3]] | -0.48 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[GCNT4]] | -0.47 | -0.37 / -0.38 | both halves | 7e-05 |  |
| [[USP43]] | -0.46 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[DNMT3A]] | -0.46 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[PSME2]] | -0.46 | -0.40 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.541). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-21.3, -14.9); signed map (-34.2, -25.6). **Vector** length 78.1, 16.5% of its response variance represented; |z| ≥ 3 in 693 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.7 | +4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.5 | +3.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.2 | +4.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +4.7 |
|  | [[Sulfatinib (drug)]] 5 µM |  | +1.5 | +2.6 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | +1.4 | +1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.3 | +0.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.7 | -5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.9 | -10.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.3 | -1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.7 | -0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.4 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | CCR4-NOT transcription complex subunit 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p22 — chr8:17,224,966-17,246,878 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CAF1 |
| Gene groups (HGNC) | CCR4-NOT transcription complex |
| Reactome | 8 pathways, smallest: TP53 regulates transcription of additional cell cycle genes whose exact role in the p53 pathway remain uncertain; Deadenylation of mRNA; M-decay: degradation of maternal mRNAs by maternally stored factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UIV1](https://www.uniprot.org/uniprotkb/Q9UIV1) (CCR4-NOT transcription complex subunit 7):

> Has 3'-5' poly(A) exoribonuclease activity for synthetic poly(A) RNA substrate. Its function seems to be partially redundant with that of CNOT8. Catalytic component of the CCR4-NOT complex which is one of the major cellular mRNA deadenylases and is linked to various cellular processes including bulk mRNA degradation, miRNA-mediated repression, translational repression during translational initiation and general transcription regulation. During miRNA-mediated repression the complex also seems to …

**Summary**, from NCBI Gene [29883](https://www.ncbi.nlm.nih.gov/gene/29883):

> The protein encoded by this gene binds to an anti-proliferative protein, B-cell translocation protein 1, which negatively regulates cell proliferation. Binding of the two proteins, which is driven by phosphorylation of the anti-proliferative protein, causes signaling events in cell division that lead to changes in cell proliferation associated with cell-cell contact. The encoded protein downregulates the innate immune response and therefore provides a therapeutic target for enhancing its …

**Accessions** — [HGNC:14101](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14101) · Entrez [29883](https://www.ncbi.nlm.nih.gov/gene/29883) · UniProt [Q9UIV1](https://www.uniprot.org/uniprotkb/Q9UIV1) · Ensembl [ENSG00000198791](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198791)

## Data

Gene col 12677: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12677); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12677, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12677]; `tensor/DDL_lfc|DDL_z.npy` [12677]; `embed/gene_vectors.npy` [12677]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12677 or target_col == 12677). Every well: [[CNOT7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNOT7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
