---
symbol: "NSUN5P1"
type: "gene"
col: 13355
ensembl_id: "ENSG00000223705"
name: "NSUN5 pseudogene 1"
location: "7q11.23"
module: 168
arm: "+"
pooled_cpm: 2.7
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/168"]
generated_by: "tahoemap"
---

# NSUN5P1

*NSUN5 pseudogene 1* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 2.93× (z +9.8, q 4e-20, up in 2 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.69× (z +5.2, q 2e-05, up in 13 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.558× (z -5.6, q 2e-05, down in 17 of 40 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Pentamidine (isethionate) (drug)]] 0.5 µM: 0.667× (z -4.0, q 0.019, down in 12 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PMS2P3-1]] (+0.69, fdr 1e-05), [[ADAT2]] (+0.64, fdr 8e-06), [[ACTR5]] (+0.62, fdr 1e-05); moves opposite to [[C6orf62]] (-0.59, fdr 3e-05), [[XRN1]] (-0.58, fdr 3e-05), [[SHOC2]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 168]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13355.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.93×** | +9.8 | 4e-20 | 2/4 (SW480, PANC-1) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.42×** | +8.4 | 1e-14 | 4/10 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +8.1 | 1e-13 | 1/3 (SW480) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.86×** | +6.1 | 1e-07 | 3/11 (SW480, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.20× | +6.0 | 2e-07 | 14/47 (HEC-1-A, Hs 766T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +5.2 | 2e-05 | 13/45 (NCI-H661, HS-578T, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.44×** | +5.1 | 2e-05 | 3/43 (A-172, A498, …) | rises with dose | low cells (technical?); position effect removed |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.55×** | +4.3 | 0.001 | 6/28 (HEC-1-A, LS 180, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Pasireotide (acetate) (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.012 | 6/39 (SW480, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.019 | 2/42 (SW 900, NCI-H1573) | top dose only | cell-cycle shift (explains ~14% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +3.4 | 0.029 | 0/3 | top dose only | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.032 | 7/42 (KATO III, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.032 | 6/44 (NCI-H1573, C32, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.035 | 3/27 (C-33 A, RKO, …) | top dose only | position effect removed |
| [[Pemetrexed (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.048 | 3/41 (SW 900, KATO III, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13355.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.558×** | -5.6 | 2e-05 | 17/40 (A-172, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Pentamidine (isethionate) (drug)]] 0.5 µM |  | **0.667×** | -4.0 | 0.019 | 12/42 (A549, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Busulfan (drug)]] 0.5 µM |  | **0.676×** | -3.8 | 0.019 | 15/37 (C-33 A, KATO III, …) | two highest doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **0.761×** | -3.8 | 0.019 | 13/30 (PANC-1, NCI-H460, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.712×** | -3.4 | 0.081 | 9/44 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[5-Fluorouracil (drug)]] 0.5 µM |  | **0.714×** | -3.3 | 0.081 | 3/40 (Panc 03.27, Hs 766T, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13355. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.67 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0766× (z -9.4) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Tofacitinib (drug)]] 0.5 µM 0.0857× (z -8.9) |
| [[A-172 (line)]] | wt | 3.31 | 0 | 1 | — | [[Phenytoin (sodium) (drug)]] 0.05 µM 0.0695× (z -8.7) |
| [[PANC-1 (line)]] | alt | 3.94 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0787× (z -12.2) |
| [[A-427 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.997 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13355), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS2P3-1]] | +0.69 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[ADAT2]] | +0.64 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[ACTR5]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[RFT1]] | +0.62 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ZNF512]] | +0.62 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[CGREF1]] | +0.61 | +0.46 / +0.68 | both halves | 2e-05 |  |
| [[PMS2P1]] | +0.60 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[PMS2P3]] | +0.59 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[CRYBB2P1]] | +0.59 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[FAM86DP]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[OTUD6B]] | +0.58 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[ABHD17A]] | +0.57 | +0.41 / +0.61 | both halves | 4e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C6orf62]] | -0.59 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[XRN1]] | -0.58 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[SHOC2]] | -0.54 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[PDPK1]] | -0.53 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[FBXO48]] | -0.53 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[CEP350]] | -0.53 | -0.37 / -0.58 | both halves | 9e-05 |  |
| [[MED29]] | -0.52 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[PHACTR4]] | -0.52 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[ELF1]] | -0.51 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[BPTF]] | -0.51 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[TOR1AIP1]] | -0.50 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[GOLGB1]] | -0.49 | -0.39 / -0.57 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 168]]; 25 genes; this gene is in the **+** arm (projection on the module's main direction 0.639). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-10.9, -29.5); signed map (-36.9, -23.2). **Vector** length 35.9, 3.20% of its response variance represented; |z| ≥ 3 in 1,043 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +8.1 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.9 | +3.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +1.9 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +3.4 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +0.9 | +3.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +0.8 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.7 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.3 | -5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | -2.1 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.2 | -3.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -0.9 | -3.0 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -0.9 | -0.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -0.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | NSUN5 pseudogene 1 |
| Locus type | pseudogene |
| Location | 7q11.23 — chr7:75,410,368-75,416,597 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | WBSCR20B; previously NSUN5B |
| Matched by | ensembl_id |

UniProt [Q3KNT7](https://www.uniprot.org/uniprotkb/Q3KNT7) carries no function annotation.

**Summary**, from NCBI Gene [155400](https://www.ncbi.nlm.nih.gov/gene/155400):

> This locus represents a transcribed pseudogene of a nearby locus on chromosome 7, which encodes a putative methyltransferase. There is also a third closely related pseudogene locus in this region. Alternative splicing results in multiple transcript variants of this gene. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:19146](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19146) · Entrez [155400](https://www.ncbi.nlm.nih.gov/gene/155400) · UniProt [Q3KNT7](https://www.uniprot.org/uniprotkb/Q3KNT7) · Ensembl [ENSG00000223705](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000223705)

## Data

Gene col 13355: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13355); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13355, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13355]; `tensor/DDL_lfc|DDL_z.npy` [13355]; `embed/gene_vectors.npy` [13355]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13355 or target_col == 13355). Every well: [[NSUN5P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSUN5P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
