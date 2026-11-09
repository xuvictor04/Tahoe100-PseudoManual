---
symbol: "FMO4"
type: "gene"
col: 1148
ensembl_id: "ENSG00000076258"
name: "flavin containing dimethylaniline monoxygenase 4"
location: "1q24.3"
module: 10
arm: "+"
pooled_cpm: 2.44
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# FMO4

*flavin containing dimethylaniline monoxygenase 4* — 1q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 2.21× (z +10.5, q 6e-23, up in 24 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.533× (z -5.9, q 2e-06, down in 20 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLIC2]] (+0.66, fdr 1e-05), [[FNBP1P1]] (+0.63, fdr 7e-06), [[LINC00240]] (+0.61, fdr 1e-05); moves opposite to [[GNB1L]] (-0.62, fdr 3e-05), [[LPCAT1]] (-0.61, fdr 1e-04), [[TTC13]] (-0.59, fdr 6e-05).
> It sits in the **+** arm of [[Module 010]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1148.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **2.21×** | +10.5 | 6e-23 | 24/43 (A-172, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.98×** | +9.8 | 2e-20 | 1/3 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.91×** | +6.1 | 2e-07 | 3/11 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +5.8 | 8e-07 | 3/11 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.79×** | +5.1 | 5e-05 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +4.8 | 2e-04 | 13/36 (LoVo, RKO, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.6 | 4e-04 | 6/42 (A498, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +4.3 | 0.001 | 8/34 (Hs 766T, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +3.8 | 0.010 | 3/36 (NCI-H1573, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.48×** | +3.7 | 0.014 | 9/41 (LS 180, KATO III, …) | rises with dose |  |
| [[Clotrimazole (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.037 | 1/32 (Panc 03.27) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +3.3 | 0.046 | 1/11 (A498) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.061 | 6/37 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.061 | 9/32 (H4, LOX-IMVI, …) | rises with dose |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.44×** | +3.2 | 0.061 | 0/22 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1148.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.533×** | -5.9 | 2e-06 | 20/38 (NCI-H460, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.614×** | -4.6 | 0.002 | 14/44 (COLO 205, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.672×** | -3.7 | 0.024 | 10/41 (SNU-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.757×** | -3.7 | 0.024 | 10/41 (RKO, NCI-H1573, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.473×** | -3.7 | 0.024 | 7/34 (NCI-H1573, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Ranolazine (drug)]] 0.5 µM |  | **0.676×** | -3.7 | 0.024 | 7/39 (SW 900, NCI-H2030, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.702×** | -3.3 | 0.078 | 12/36 (CFPAC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.709×** | -3.2 | 0.092 | 4/44 (SW48, A-172, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.521×** | -3.2 | 0.092 | 7/27 (NCI-H1573, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.710× | -3.1 | 0.12 | 8/41 (A549, C32, …) | top dose only |  |
| [[Flumatinib (mesylate) (drug)]] 0.5 µM |  | 0.724× | -3.0 | 0.13 | 3/40 (HEC-1-A, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1148. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 3.35 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0485× (z -9.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0689× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.685 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.831 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.828 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.746 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.657 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.712 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.70 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1148), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLIC2]] | +0.66 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[FNBP1P1]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[LINC00240]] | +0.61 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[PATL2]] | +0.61 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[KCNMB3]] | +0.60 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[STAT6]] | +0.60 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[FBXO38-DT]] | +0.60 | +0.63 / +0.40 | both halves | 4e-05 |  |
| [[LYRM2]] | +0.59 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | +0.59 | +0.59 / +0.40 | both halves | 4e-05 |  |
| [[LINC01725]] | +0.59 | +0.65 / +0.41 | both halves | 4e-05 |  |
| [[THBS4]] | +0.59 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[GDAP1]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNB1L]] | -0.62 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[LPCAT1]] | -0.61 | -0.66 / -0.34 | both halves | 1e-04 |  |
| [[TTC13]] | -0.59 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[POC1A]] | -0.58 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[GNA12]] | -0.58 | -0.61 / -0.37 | both halves | 9e-05 |  |
| [[SETD3]] | -0.58 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[ATP7B]] | -0.58 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[SOCS7]] | -0.58 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[TENT4A]] | -0.57 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[TRAP1]] | -0.57 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[SRD5A1]] | -0.57 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[NPHP4]] | -0.56 | -0.46 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.581). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (11.4, 7.2); signed map (15.1, -20.5). **Vector** length 40.4, 4.49% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.6 | +10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +4.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.7 | +3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +9.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.1 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.1 | +2.3 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +0.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | +2.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -2.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | +0.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | +1.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.9 | -3.2 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | -0.7 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -0.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | flavin containing dimethylaniline monoxygenase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.3 — chr1:171,314,183-171,342,084 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously FMO2 |
| Gene groups (HGNC) | Flavin containing monooxygenases; Flavoproteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P31512](https://www.uniprot.org/uniprotkb/P31512) (Flavin-containing monooxygenase 4):

> Is likely involved in the oxidative metabolism of a variety of xenobiotics such as drugs and pesticides. Is able to use methimazole as substrate.

**Summary**, from NCBI Gene [2329](https://www.ncbi.nlm.nih.gov/gene/2329):

> Metabolic N-oxidation of diet-derived amino-trimethylamine (TMA) is mediated by flavin-containing monooxygenase and is subject to an inherited FMO3 polymorphism in man. This results in a small subpopulation with reduced TMA N-oxidation capacity and causes fish odor syndrome (Trimethylaminuria). Three forms of the enzyme are encoded by genes clustered in the 1q23-q25 region. Flavin-containing monooxygenases are NADPH-dependent flavoenzymes that catalyzes the oxidation of soft nucleophilic …

**Accessions** — [HGNC:3772](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3772) · Entrez [2329](https://www.ncbi.nlm.nih.gov/gene/2329) · UniProt [P31512](https://www.uniprot.org/uniprotkb/P31512) · Ensembl [ENSG00000076258](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076258)

## Data

Gene col 1148: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1148); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1148, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1148]; `tensor/DDL_lfc|DDL_z.npy` [1148]; `embed/gene_vectors.npy` [1148]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1148 or target_col == 1148). Every well: [[FMO4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FMO4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
