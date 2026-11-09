---
symbol: "PPIL6"
type: "gene"
col: 11646
ensembl_id: "ENSG00000185250"
name: "peptidylprolyl isomerase like 6"
location: "6q21"
module: 15
arm: "+"
pooled_cpm: 7.05
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 8
n_dd_up_clean: 14
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# PPIL6

*peptidylprolyl isomerase like 6* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.69× (z +15.2, q 0e+00, up in 38 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.436× (z -9.0, q 1e-16, down in 30 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC40]] (+0.58, fdr 3e-05), [[PPP1CB-DT]] (+0.55, fdr 1e-05), [[KIF9]] (+0.52, fdr 3e-05); moves opposite to [[ATP5MF]] (-0.41, fdr 2e-04), [[SLC25A4]] (-0.37, fdr 0.001, ⚠ not reproduced), [[VPS16]] (-0.37, fdr 2e-04).
> It sits in the **+** arm of [[Module 015]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11646.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.69×** | +15.2 | 0e+00 | 38/40 (NCI-H1792, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.91×** | +11.1 | 2e-26 | 9/10 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.27×** | +8.9 | 1e-16 | 33/46 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.12×** | +8.1 | 5e-14 | 19/28 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.12×** | +8.1 | 5e-14 | 26/45 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.97×** | +7.4 | 2e-11 | 27/45 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.00×** | +6.9 | 3e-10 | 9/18 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +5.4 | 6e-06 | 22/45 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.56×** | +4.8 | 1e-04 | 16/46 (C-33 A, A-172, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.54×** | +3.9 | 0.005 | 13/44 (A-172, A498, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +3.6 | 0.013 | 12/39 (A-172, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.013 | 8/44 (NCI-H460, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.88×** | +3.6 | 0.016 | 8/43 (HOP62, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.024 | 5/39 (NCI-H23, SW480, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.024 | 8/39 (LOX-IMVI, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.036 | 7/45 (A-427, HS-578T, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.089 | 4/43 (NCI-H1573, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11646.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.436×** | -9.0 | 1e-16 | 30/45 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.520×** | -7.1 | 4e-10 | 21/45 (PANC-1, RKO, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.545×** | -6.6 | 9e-09 | 25/45 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.583×** | -5.9 | 7e-07 | 21/39 (PANC-1, LoVo, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.664×** | -4.4 | 1e-03 | 18/45 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cytarabine (drug)]] 5 µM |  | **0.691×** | -3.9 | 0.011 | 12/44 (NCI-H2347, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.646×** | -3.4 | 0.058 | 8/46 (MIA PaCa-2, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.738×** | -3.3 | 0.067 | 9/44 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.750× | -3.1 | 0.11 | 13/44 (PANC-1, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11646. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 15.8 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -12.7) |
| [[HS-578T (line)]] | alt | 5.68 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 16.4× (z +9.7) ⚠ toxic; transcription drop | [[Pyridoxine (drug)]] 0.5 µM 0.0823× (z -9.0) |
| [[HT-29 (line)]] | alt | 6.75 | 0 | 2 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0785× (z -9.5) |
| [[BT-474 (line)]] | alt | 6.34 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.0816× (z -8.7) |
| [[C-33 A (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.129× (z -8.8) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 12.4 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.207× (z -8.6) |
| [[LoVo (line)]] | wt | 9.18 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.164× (z -9.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 6.88 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0982× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 13.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.106× (z -11.3) |
| [[SHP-77 (line)]] | alt | 9.72 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.114× (z -8.8) |
| [[A-172 (line)]] | wt | 7.14 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11646), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC40]] | +0.58 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[PPP1CB-DT]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[KIF9]] | +0.52 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[COPB2-DT]] | +0.51 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[NEK5]] | +0.51 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[UGDH-AS1]] | +0.51 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[RSL24D1]] | +0.50 | +0.38 / +0.52 | both halves | 7e-05 |  |
| [[RNF32]] | +0.50 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[AK8]] | +0.48 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[CDNF]] | +0.48 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[TMEM9B-AS1]] | +0.48 | +0.66 / +0.36 | both halves | 9e-05 |  |
| [[BRPF3-AS1]] | +0.47 | +0.57 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5MF]] | -0.41 | -0.32 / -0.29 | both halves | 2e-04 |  |
| [[SLC25A4]] | -0.37 | -0.17 / -0.28 | ⚠ not reproduced | 0.001 |  |
| [[VPS16]] | -0.37 | -0.35 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.243). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (3.7, 22.3); signed map (32.9, -7.9). **Vector** length 61.4, 9.55% of its response variance represented; |z| ≥ 3 in 985 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +8.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.1 | +3.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +4.8 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | +1.3 | +2.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.3 | +0.7 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -9.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.1 | -4.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -7.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -0.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.8 | -6.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -2.1 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.3 | -1.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -3.1 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | peptidylprolyl isomerase like 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:109,390,215-109,441,171 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA425D10.6, MGC41939, dJ919F19.1, RSPH12 |
| Gene groups (HGNC) | Cyclophilin peptidylprolyl isomerases |
| Reactome | 3 pathways, smallest: Dengue Virus-Host Interactions; Dengue Virus Infection; Viral Infection Pathways |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IXY8](https://www.uniprot.org/uniprotkb/Q8IXY8) (Probable inactive peptidyl-prolyl cis-trans isomerase-like 6):

> Probable inactive PPIase with no peptidyl-prolyl cis-trans isomerase activity.

**Summary**, from NCBI Gene [285755](https://www.ncbi.nlm.nih.gov/gene/285755):

> Predicted to enable peptidyl-prolyl cis-trans isomerase activity. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21557](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21557) · Entrez [285755](https://www.ncbi.nlm.nih.gov/gene/285755) · UniProt [Q8IXY8](https://www.uniprot.org/uniprotkb/Q8IXY8) · Ensembl [ENSG00000185250](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185250)

## Data

Gene col 11646: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11646); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11646, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11646]; `tensor/DDL_lfc|DDL_z.npy` [11646]; `embed/gene_vectors.npy` [11646]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11646 or target_col == 11646). Every well: [[PPIL6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPIL6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
