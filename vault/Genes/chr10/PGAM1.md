---
symbol: "PGAM1"
type: "gene"
col: 10091
ensembl_id: "ENSG00000171314"
name: "phosphoglycerate mutase 1"
location: "10q24.1"
module: 29
arm: "+"
pooled_cpm: 25.32
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# PGAM1

*phosphoglycerate mutase 1* — 10q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 13.1× (z +11.7, q 4e-29, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.472× (z -9.0, q 2e-16, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRKL]] (+0.78, fdr 7e-06), [[CIPC]] (+0.69, fdr 7e-06), [[BPNT2]] (+0.69, fdr 7e-06); moves opposite to [[CROCCP2-1]] (-0.74, fdr 7e-06), [[WASHC1]] (-0.66, fdr 7e-06), [[OFD1]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10091.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **13.1×** | +11.7 | 4e-29 | 48/48 (SW480, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **11.5×** | +11.1 | 2e-26 | 45/46 (SW480, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +5.7 | 2e-06 | 29/40 (SW480, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +3.9 | 0.012 | 26/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.56×** | +3.8 | 0.014 | 28/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.018 | 26/47 (LoVo, SW480, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +3.6 | 0.021 | 23/46 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +3.6 | 0.021 | 24/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Roxadustat (drug)]] 5 µM |  | **1.54×** | +3.6 | 0.022 | 28/47 (C-33 A, A-172, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.45×** | +3.2 | 0.079 | 20/43 (A498, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.99×** | +3.1 | 0.089 | 17/46 (SW480, HOP62, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10091.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.472×** | -9.0 | 2e-16 | 40/47 (RPMI-7951, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.807×** | -6.6 | 1e-08 | 36/48 (SW 900, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.596×** | -4.4 | 0.002 | 29/48 (SNU-1, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.694×** | -4.4 | 0.002 | 29/48 (SW480, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.657×** | -3.7 | 0.024 | 27/47 (A-427, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.668×** | -3.4 | 0.059 | 25/47 (BT-474, NCI-H2030, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.692×** | -3.3 | 0.092 | 19/48 (HepG2/C3A, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ivabradine (hydrochloride) (drug)]] 5 µM | ⚠ unreliable plate only | 0.698× | -3.2 | 0.11 | 20/47 (SHP-77, SW1417, …) | top dose only | position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.546× | -3.1 | 0.14 | 22/48 (SW48, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10091. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 24.4 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.77× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 5.35× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 35.9 | 2 | 1 | [[PH-797804 (drug)]] 5 µM 29.3× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -10.6) |
| [[SW480 (line)]] | alt | 21.0 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 25.7× (z +11.6) | — |
| [[HEC-1-A (line)]] | alt | 22.8 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 24.2× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 22.0 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.97× (z +8.9) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 27.3× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 28.7 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 24.5× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -9.6) |
| [[A-172 (line)]] | wt | 27.4 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 16.0× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -9.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 44.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -9.3) |
| [[C32 (line)]] | wt | 21.3 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 31.8× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 35.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -11.9) |
| [[LoVo (line)]] | wt | 15.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 22.1× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 30.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 16.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 31.8× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 28.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 21.5× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 31.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0931× (z -15.3) |
| [[SW 900 (line)]] | alt | 33.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -8.7) |
| [[A-427 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10091), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRKL]] | +0.78 | +0.80 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[CIPC]] | +0.69 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[BPNT2]] | +0.69 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[PPT1]] | +0.68 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[TMED7]] | +0.68 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[SCARB2]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[TMX1]] | +0.67 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[RPE]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[RAD23B]] | +0.66 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[TMEM30A]] | +0.66 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[TMEM106C]] | +0.65 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[PRDX3]] | +0.65 | +0.65 / +0.62 | both halves | 7e-06 | STRING 749 |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP2-1]] | -0.74 | -0.76 / -0.72 | both halves | 7e-06 |  |
| [[WASHC1]] | -0.66 | -0.66 / -0.70 | both halves | 7e-06 |  |
| [[OFD1]] | -0.65 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[ATF4]] | -0.64 | -0.69 / -0.59 | both halves | 7e-06 |  |
| [[EIF1B]] | -0.63 | -0.59 / -0.69 | both halves | 7e-06 |  |
| [[PQBP1]] | -0.63 | -0.70 / -0.57 | both halves | 1e-05 |  |
| [[GATAD1]] | -0.62 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[GGNBP2]] | -0.62 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[CYP20A1]] | -0.62 | -0.73 / -0.58 | both halves | 7e-06 |  |
| [[CDK3]] | -0.61 | -0.71 / -0.54 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.61 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[LIME1]] | -0.60 | -0.62 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.763). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-26.0, -23.0); signed map (-22.9, -40.1). **Vector** length 112, 31.0% of its response variance represented; |z| ≥ 3 in 752 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.1 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.2 | +5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.5 | +11.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.1 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.1 | +2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.5 | -9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -3.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.4 | -2.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | -0.6 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.6 | -3.1 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -2.6 | -2.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.3 | -2.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | phosphoglycerate mutase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.1 — chr10:97,426,191-97,433,444 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PGAM-B; previously PGAMA |
| Gene groups (HGNC) | Phosphoglycerate mutases; Bisphosphoglycerate phosphatases |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 6 pathways, smallest: Gluconeogenesis; Glycolysis; Glucose metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P18669](https://www.uniprot.org/uniprotkb/P18669) (Phosphoglycerate mutase 1):

> Catalyzes the interconversion of 2-phosphoglycerate and 3-phosphoglycerate, a crucial step in glycolysis, by using 2,3-bisphosphoglycerate. Also catalyzes the interconversion of (2R)-2,3-bisphosphoglycerate and (2R)-3-phospho-glyceroyl phosphate.

**Summary**, from NCBI Gene [5223](https://www.ncbi.nlm.nih.gov/gene/5223):

> The protein encoded by this gene is a mutase that catalyzes the reversible reaction of 3-phosphoglycerate (3-PGA) to 2-phosphoglycerate (2-PGA) in the glycolytic pathway. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2015]

**Accessions** — [HGNC:8888](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8888) · Entrez [5223](https://www.ncbi.nlm.nih.gov/gene/5223) · UniProt [P18669](https://www.uniprot.org/uniprotkb/P18669) · Ensembl [ENSG00000171314](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171314)

## Data

Gene col 10091: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10091); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10091, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10091]; `tensor/DDL_lfc|DDL_z.npy` [10091]; `embed/gene_vectors.npy` [10091]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10091 or target_col == 10091). Every well: [[PGAM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGAM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
