---
symbol: "C3orf62"
type: "gene"
col: 12002
ensembl_id: "ENSG00000188315"
name: "chromosome 3 open reading frame 62"
location: "3p21.31"
module: 39
arm: "+"
pooled_cpm: 7.14
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# C3orf62

*chromosome 3 open reading frame 62* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.56× (z +5.8, q 4e-06, up in 17 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.591× (z -7.0, q 2e-09, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C3orf20]] (+0.75, fdr 7e-06), [[CDKL4]] (+0.73, fdr 1e-05), [[EPHX3]] (+0.73, fdr 7e-06); moves opposite to [[KDM1A]] (-0.61, fdr 1e-05), [[DCUN1D4]] (-0.58, fdr 1e-05), [[GSTA4]] (-0.58, fdr 7e-05).
> It is in [[Module 039]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12002.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +5.8 | 4e-06 | 17/41 (HS-578T, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +5.0 | 2e-04 | 13/45 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +4.9 | 2e-04 | 13/34 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +4.7 | 3e-04 | 6/14 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +4.3 | 0.002 | 10/47 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.004 | 15/42 (SHP-77, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +3.9 | 0.009 | 7/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.013 | 4/47 (HOP62, SW1417, …) | inconsistent across doses |  |
| [[Tetracycline (hydrochloride) (drug)]] 0.05 µM |  | 1.30× | +3.1 | 0.10 | 3/44 (NCI-H2030, A-427, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.27× | +3.1 | 0.11 | 8/46 (NCI-H2030, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12002.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.591×** | -7.0 | 2e-09 | 22/47 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.645×** | -5.8 | 2e-06 | 20/45 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.666×** | -5.4 | 1e-05 | 19/45 (NCI-H460, KATO III, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.722×** | -4.3 | 0.002 | 19/41 (NCI-H1573, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.737×** | -3.9 | 0.009 | 15/44 (NCI-H2030, C-33 A, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.569×** | -3.9 | 0.009 | 11/44 (A549, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.757×** | -3.6 | 0.030 | 16/38 (AsPC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -3.3 | 0.058 | 4/47 (SW480, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Allopurinol (drug)]] 0.5 µM |  | **0.780×** | -3.3 | 0.058 | 5/46 (HepG2/C3A, NCI-H460, …) | inconsistent across doses |  |
| [[Bexarotene (drug)]] 5 µM |  | **0.781×** | -3.3 | 0.058 | 6/47 (A-427, J82, …) | top dose only |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **0.767×** | -3.3 | 0.058 | 7/39 (A-172, BT-474, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.846× | -3.2 | 0.076 | 14/41 (SW1417, SW48, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.636×** | -3.1 | 0.076 | 6/39 (HOP62, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12002. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 10.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0683× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 0.05 µM 0.106× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 3.55 | 0 | 2 (1 ⚠) | — | [[Pemetrexed (drug)]] 5 µM 0.101× (z -8.5) |
| [[SNU-423 (line)]] | alt | 6.76 | 0 | 2 | — | [[Mifepristone (drug)]] 0.05 µM 0.0659× (z -10.8) |
| [[A-427 (line)]] | wt | 10.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -8.9) ⚠ cell-cycle shift, explains ~20% of this change |
| [[BT-474 (line)]] | alt | 7.77 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0988× (z -8.9) ⚠ cell-cycle shift, explains ~20% of this change |
| [[HepG2_C3A (line)]] | wt | 6.34 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 0.5 µM 0.0600× (z -8.8) |
| [[HOP62 (line)]] | alt | 6.73 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0690× (z -12.2) |
| [[HS-578T (line)]] | alt | 6.79 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.105× (z -8.9) ⚠ cell-cycle shift, explains ~20% of this change |
| [[LoVo (line)]] | wt | 10.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.162× (z -11.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 4.64 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.100× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 8.86 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0491× (z -14.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 4.05 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.139× (z -9.5) ⚠ cell-cycle shift, explains ~13% of this change |
| [[RKO (line)]] | wt | 9.95 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.150× (z -9.3) |
| [[A-172 (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12002), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C3orf20]] | +0.75 | +0.79 / +0.69 | both halves | 7e-06 |  |
| [[CDKL4]] | +0.73 | +0.77 / +0.57 | both halves | 1e-05 |  |
| [[EPHX3]] | +0.73 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[PILRA]] | +0.72 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[IDI2-AS1]] | +0.70 | +0.79 / +0.64 | both halves | 7e-06 |  |
| [[RFPL3S]] | +0.69 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[CFAP251]] | +0.69 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[LINC02803]] | +0.68 | +0.76 / +0.52 | both halves | 1e-05 |  |
| [[SCUBE2]] | +0.67 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.67 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[GARIN1A]] | +0.67 | +0.73 / +0.58 | both halves | 8e-06 |  |
| [[FLACC1]] | +0.67 | +0.73 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM1A]] | -0.61 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[DCUN1D4]] | -0.58 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[GSTA4]] | -0.58 | -0.58 / -0.38 | both halves | 7e-05 |  |
| [[GGA2]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.694). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.6, -15.6); signed map (15.9, 8.9). **Vector** length 64.3, 9.14% of its response variance represented; |z| ≥ 3 in 956 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +4.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.4 | +4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +2.4 |
| fall | [[NG25 (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -2.4 | -3.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.3 | -2.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.9 | -4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 3 open reading frame 62 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:49,268,596-49,277,232 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ43654, MAPS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZUJ4](https://www.uniprot.org/uniprotkb/Q6ZUJ4) (Uncharacterized protein C3orf62):

> Essential for normal spermatogenesis and male fertility.

**Summary**, from NCBI Gene [375341](https://www.ncbi.nlm.nih.gov/gene/375341):

> Predicted to be involved in spermatogenesis. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24771](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24771) · Entrez [375341](https://www.ncbi.nlm.nih.gov/gene/375341) · UniProt [Q6ZUJ4](https://www.uniprot.org/uniprotkb/Q6ZUJ4) · Ensembl [ENSG00000188315](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188315)

## Data

Gene col 12002: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12002); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12002, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12002]; `tensor/DDL_lfc|DDL_z.npy` [12002]; `embed/gene_vectors.npy` [12002]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12002 or target_col == 12002). Every well: [[C3orf62 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C3orf62.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
