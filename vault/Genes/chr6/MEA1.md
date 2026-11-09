---
symbol: "MEA1"
type: "gene"
col: 4561
ensembl_id: "ENSG00000124733"
name: "male-enhanced antigen 1"
location: "6p21.1"
module: 3
arm: "+"
pooled_cpm: 26.9
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 3
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# MEA1

*male-enhanced antigen 1* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.65× (z +8.1, q 3e-13, up in 42 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (PANC-1 3.64×, A498 4.76×, HEC-1-A 3.87×, SW480 4.05×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW 900 5.46×, Panc 03.27 3.88×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.574× (z -6.6, q 3e-08, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRPT1]] (+0.74, fdr 7e-06), [[MRPL17]] (+0.68, fdr 7e-06), [[SLC25A11]] (+0.65, fdr 2e-05); moves opposite to [[IQCH-AS1]] (-0.61, fdr 1e-04), [[FUBP1]] (-0.60, fdr 8e-05), [[SPTY2D1OS]] (-0.58, fdr 2e-04).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4561.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (PANC-1 3.64×, A498 4.76×, HEC-1-A 3.87×, SW480 4.05×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW 900 5.46×, Panc 03.27 3.88×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **2.65×** | +8.1 | 3e-13 | 42/43 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **2.42×** | +7.1 | 4e-10 | 33/37 (SW 900, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.87×** | +5.2 | 4e-05 | 39/45 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.72×** | +4.5 | 8e-04 | 37/48 (SW480, KATO III, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.59×** | +3.9 | 0.012 | 26/48 (KATO III, SW480, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +3.6 | 0.033 | 1/48 (Hs 766T) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4561.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.574×** | -6.6 | 3e-08 | 40/47 (NCI-H2030, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.323×** | -4.4 | 0.004 | 35/47 (LoVo, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.401×** | -3.5 | 0.077 | 27/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.685× | -3.2 | 0.15 | 25/48 (SW 900, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.669× | -3.1 | 0.15 | 27/47 (C32, Panc 03.27, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.687× | -3.1 | 0.15 | 27/48 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.690× | -3.1 | 0.15 | 23/47 (SW 900, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.697× | -3.0 | 0.18 | 23/47 (A549, NCI-H23, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4561. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 41.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0632× (z -16.4) |
| [[A498 (line)]] | wt | 14.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[BT-474 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.107× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 21.0 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.134× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 31.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[NCI-H2030 (line)]] | alt | 49.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 41.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.88× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[PANC-1 (line)]] | alt | 35.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[SW 900 (line)]] | alt | 22.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.46× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[SW480 (line)]] | alt | 18.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[A-172 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4561), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRPT1]] | +0.74 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[MRPL17]] | +0.68 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[SLC25A11]] | +0.65 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[VKORC1]] | +0.64 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[WDR54]] | +0.64 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[AKR7A2]] | +0.63 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[TXNDC17]] | +0.63 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[CIB1]] | +0.62 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[ALDOA]] | +0.61 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[MPG]] | +0.61 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[UBA6]] | +0.60 | +0.58 / +0.34 | both halves | 1e-04 |  |
| [[MYO9B]] | +0.60 | +0.58 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQCH-AS1]] | -0.61 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[FUBP1]] | -0.60 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[SPTY2D1OS]] | -0.58 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[CC2D2A]] | -0.57 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[CCNT2]] | -0.56 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[ANKRD10]] | -0.56 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[GALNT7-DT]] | -0.55 | -0.51 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[GAS2]] | -0.55 | -0.54 / -0.25 | both halves | 4e-04 |  |
| [[ARGLU1]] | -0.55 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[CYB5D2]] | -0.53 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[SRSF1]] | -0.53 | -0.29 / -0.47 | both halves | 3e-04 |  |
| [[KRBA2]] | -0.52 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[EWSR1]] | -0.52 | -0.32 / -0.49 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.512). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (9.8, -13.4); signed map (-36.5, 18.0). **Vector** length 66.4, 18.0% of its response variance represented; |z| ≥ 3 in 583 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +4.4 | +4.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +3.9 | +3.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +2.1 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +1.3 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +1.9 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +1.1 | +2.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -3.9 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.3 | +2.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -6.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | +0.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.8 | -0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | male-enhanced antigen 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:43,011,143-43,016,868 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MEA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16626](https://www.uniprot.org/uniprotkb/Q16626) (Male-enhanced antigen 1):

> May play an important role in spermatogenesis and/or testis development.

**Summary**, from NCBI Gene [4201](https://www.ncbi.nlm.nih.gov/gene/4201):

> Predicted to be involved in male gonad development and spermatogenesis. Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:6986](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6986) · Entrez [4201](https://www.ncbi.nlm.nih.gov/gene/4201) · UniProt [Q16626](https://www.uniprot.org/uniprotkb/Q16626) · Ensembl [ENSG00000124733](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124733)

## Data

Gene col 4561: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4561); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4561, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4561]; `tensor/DDL_lfc|DDL_z.npy` [4561]; `embed/gene_vectors.npy` [4561]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4561 or target_col == 4561). Every well: [[MEA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
