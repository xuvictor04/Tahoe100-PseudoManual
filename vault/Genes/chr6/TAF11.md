---
symbol: "TAF11"
type: "gene"
col: 766
ensembl_id: "ENSG00000064995"
name: "TATA-box binding protein associated factor 11"
location: "6p21.31"
module: 15
arm: "+"
pooled_cpm: 27.45
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# TAF11

*TATA-box binding protein associated factor 11* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.42× (z +10.5, q 7e-23, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.698× (z -10.7, q 7e-24, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAPN10-DT]] (+0.74, fdr 7e-06), [[ANKRD42-DT]] (+0.73, fdr 7e-06), [[MIR762HG]] (+0.73, fdr 1e-05); moves opposite to [[TJP1]] (-0.57, fdr 6e-05), [[CELSR3]] (-0.55, fdr 1e-05), [[NAB1]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 015]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 766.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +10.5 | 7e-23 | 31/48 (PANC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +7.3 | 7e-11 | 26/48 (CFPAC-1, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.29×** | +5.3 | 2e-05 | 21/48 (CFPAC-1, C32, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +5.1 | 4e-05 | 21/48 (SW48, RKO, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +5.1 | 4e-05 | 23/46 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.003 | 18/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +4.0 | 0.006 | 20/47 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.13× | +3.5 | 0.030 | 6/48 (SK-MEL-2, SW 900, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.18× | +3.4 | 0.036 | 17/47 (HOP62, AsPC-1, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.036 | 7/47 (HT-29, A-172, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.061 | 8/48 (SW480, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.097 | 6/48 (MIA PaCa-2, PANC-1, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.097 | 8/46 (AsPC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.097 | 2/46 (LoVo, NCI-H1792) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.35×** | +3.0 | 0.097 | 4/47 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | 1.11× | +3.0 | 0.097 | 4/48 (Hs 766T, BT-474, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.16× | +3.0 | 0.097 | 12/47 (HepG2/C3A, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 766.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.698×** | -10.7 | 7e-24 | 31/48 (RKO, SNU-423, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.612×** | -9.9 | 1e-20 | 36/48 (HCT15, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.821×** | -5.8 | 9e-07 | 23/48 (LS 180, SNU-423, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.759×** | -5.8 | 9e-07 | 23/48 (RPMI-7951, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.951× | -3.9 | 0.011 | 1/48 (AN3 CA) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.857× | -3.2 | 0.11 | 4/48 (HCT15, RPMI-7951, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.850× | -3.2 | 0.11 | 12/47 (SW480, H4, …) | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.864× | -3.1 | 0.15 | 3/48 (SW 1088, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 766. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 49.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0932× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change |
| [[AsPC-1 (line)]] | alt | 21.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 32.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -9.1) |
| [[PANC-1 (line)]] | alt | 30.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +9.3) | — |
| [[RKO (line)]] | wt | 28.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -11.7) |
| [[SNU-423 (line)]] | alt | 41.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -9.9) |
| [[SW480 (line)]] | alt | 41.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.464× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change |
| [[A-427 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 766), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPN10-DT]] | +0.74 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[ANKRD42-DT]] | +0.73 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[MIR762HG]] | +0.73 | +0.52 / +0.74 | both halves | 1e-05 |  |
| [[NDUFAF7]] | +0.72 | +0.63 / +0.77 | both halves | 7e-06 |  |
| [[URM1]] | +0.70 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[NUDT2]] | +0.69 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[C8orf76]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[ZBTB8OS]] | +0.66 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[ZNF500]] | +0.65 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[WDR20]] | +0.65 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[TM2D1]] | +0.64 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[PCF11-AS1]] | +0.64 | +0.42 / +0.66 | both halves | 4e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TJP1]] | -0.57 | -0.38 / -0.60 | both halves | 6e-05 |  |
| [[CELSR3]] | -0.55 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[NAB1]] | -0.55 | -0.46 / -0.60 | both halves | 2e-05 |  |
| [[CSRP1]] | -0.55 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[PLCB4]] | -0.53 | -0.39 / -0.62 | both halves | 5e-05 |  |
| [[MTNR1A]] | -0.53 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[SPTAN1]] | -0.53 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[VEZF1]] | -0.53 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[PCNX2]] | -0.52 | -0.36 / -0.58 | both halves | 9e-05 |  |
| [[SRSF3]] | -0.52 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[GALNT10]] | -0.52 | -0.56 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.590). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.6, 23.5); signed map (-0.1, -1.3). **Vector** length 85.5, 17.4% of its response variance represented; |z| ≥ 3 in 664 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.2 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +10.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.1 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +5.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | +3.0 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +3.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.0 | +3.2 |
|  | [[EX229 (drug)]] 0.5 µM |  | +2.0 | +3.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.0 | -9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -10.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -5.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.1 | -2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -3.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | TATA-box binding protein associated factor 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:34,877,462-34,889,192 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TAFII28; previously TAF2I |
| Gene groups (HGNC) | General transcription factor IID complex subunits |
| Reactome | 20 pathways, smallest: HIV Transcription Initiation; RNA Polymerase II HIV Promoter Escape; RNA Polymerase II Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15544](https://www.uniprot.org/uniprotkb/Q15544) (Transcription initiation factor TFIID subunit 11):

> The TFIID basal transcription factor complex plays a major role in the initiation of RNA polymerase II (Pol II)-dependent transcription. TFIID recognizes and binds promoters with or without a TATA box via its subunit TBP, a TATA-box-binding protein, and promotes assembly of the pre-initiation complex (PIC). The TFIID complex consists of TBP and TBP-associated factors (TAFs), including TAF1, TAF2, TAF3, TAF4, TAF5, TAF6, TAF7, TAF8, TAF9, TAF10, TAF11, TAF12 and TAF13. TAF11, together with TAF13 …

**Summary**, from NCBI Gene [6882](https://www.ncbi.nlm.nih.gov/gene/6882):

> Initiation of transcription by RNA polymerase II requires the activities of more than 70 polypeptides. The protein that coordinates these activities is transcription factor IID (TFIID), which binds to the core promoter to position the polymerase properly, serves as the scaffold for assembly of the remainder of the transcription complex, and acts as a channel for regulatory signals. TFIID is composed of the TATA-binding protein (TBP) and a group of evolutionarily conserved proteins known as …

**Accessions** — [HGNC:11544](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11544) · Entrez [6882](https://www.ncbi.nlm.nih.gov/gene/6882) · UniProt [Q15544](https://www.uniprot.org/uniprotkb/Q15544) · Ensembl [ENSG00000064995](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064995)

## Data

Gene col 766: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 766); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 766, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 766]; `tensor/DDL_lfc|DDL_z.npy` [766]; `embed/gene_vectors.npy` [766]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 766 or target_col == 766). Every well: [[TAF11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAF11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
