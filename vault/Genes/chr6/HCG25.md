---
symbol: "HCG25"
type: "gene"
col: 13877
ensembl_id: "ENSG00000232940"
name: "HLA complex group 25"
location: "6p21.32"
module: 21
arm: "+"
pooled_cpm: 2.28
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# HCG25

*HLA complex group 25* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.20× (z +11.3, q 9e-27, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 2.08× (z +7.4, q 2e-11, up in 20 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.846× (z -5.9, q 3e-06, down in 22 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.568× (z -5.7, q 3e-06, down in 20 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.0556×, SNU-423 0.0818×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LOX-IMVI 0.0630×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM182B]] (+0.58, fdr 5e-05), [[FLYWCH1]] (+0.57, fdr 2e-05), [[CDC26]] (+0.57, fdr 7e-05); moves opposite to [[NUP188]] (-0.53, fdr 4e-05), [[FAM111A]] (-0.53, fdr 2e-04), [[IPO9]] (-0.51, fdr 3e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13877.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.20×** | +11.3 | 9e-27 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.12×** | +7.6 | 1e-11 | 3/11 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.24×** | +7.5 | 1e-11 | 1/5 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.08×** | +7.4 | 2e-11 | 20/43 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.05×** | +7.2 | 5e-11 | 17/45 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.60×** | +6.7 | 3e-09 | 6/45 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.88×** | +6.4 | 2e-08 | 20/42 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.86×** | +6.2 | 3e-08 | 12/44 (LOX-IMVI, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.84×** | +6.1 | 5e-08 | 14/31 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.5 | 3e-06 | 12/32 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +5.3 | 7e-06 | 14/40 (HOP62, SW 900, …) | top dose only |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | **1.52×** | +4.2 | 0.001 | 6/31 (NCI-H1792, NCI-H460, …) | two highest doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.53×** | +4.1 | 0.002 | 6/34 (HS-578T, HOP62, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.007 | 5/45 (A-427, NCI-H2347, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.023 | 6/44 (C32, LS 180, …) | rises with dose |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.032 | 4/44 (SW480, HEC-1-A, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13877.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.0556×, SNU-423 0.0818×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LOX-IMVI 0.0630×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.846× | -5.9 | 3e-06 | 22/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.568×** | -5.7 | 3e-06 | 20/41 (SNU-423, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.665×** | -4.1 | 0.006 | 10/46 (LOX-IMVI, SNU-423, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | 0.730× | -3.2 | 0.19 | 6/23 (PANC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.727× | -3.1 | 0.20 | 11/40 (RPMI-7951, KATO III, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.741× | -3.1 | 0.21 | 9/31 (SNU-423, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13877. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 2.74 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0630× (z -9.0) |
| [[PANC-1 (line)]] | alt | 2.82 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0556× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SNU-423 (line)]] | alt | 5.94 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0818× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.870 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.973 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.970 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.886 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13877), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM182B]] | +0.58 | +0.40 / +0.66 | both halves | 5e-05 |  |
| [[FLYWCH1]] | +0.57 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[CDC26]] | +0.57 | +0.38 / +0.64 | both halves | 7e-05 |  |
| [[EFCAB14-AS1]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[RHOQ-AS1]] | +0.56 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[KIZ-AS1]] ⚠ | +0.56 | +0.57 / +0.52 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MME-AS1]] | +0.55 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[DEDD2]] | +0.54 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[NDRG1]] | +0.54 | +0.39 / +0.53 | both halves | 6e-05 |  |
| [[UBOX5-AS1]] | +0.54 | +0.43 / +0.57 | both halves | 4e-05 |  |
| [[RN7SL2]] | +0.54 | +0.52 / +0.54 | both halves | 1e-05 | same gene group |
| [[PRMT5-DT]] | +0.54 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[TPT1]] | +0.54 | +0.48 / +0.56 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP188]] | -0.53 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[FAM111A]] | -0.53 | -0.30 / -0.54 | both halves | 2e-04 |  |
| [[IPO9]] | -0.51 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[POGLUT1]] | -0.51 | -0.23 / -0.57 | both halves | 5e-04 |  |
| [[SRCAP]] | -0.50 | -0.29 / -0.56 | both halves | 3e-04 |  |
| [[ZNF644]] | -0.49 | -0.26 / -0.52 | both halves | 4e-04 |  |
| [[CRYBG1]] | -0.49 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[DNMT1]] | -0.49 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[CHRAC1]] | -0.49 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[SNX5]] | -0.48 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[TMPO]] | -0.47 | -0.34 / -0.54 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.508). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.7, 30.1); signed map (-32.2, -2.2). **Vector** length 35.0, 3.16% of its response variance represented; |z| ≥ 3 in 1,008 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +2.6 | +5.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | -0.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +4.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +1.3 | +6.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.3 | +6.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.9 | -0.2 |
|  | [[Infigratinib (drug)]] 5 µM |  | +0.8 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.8 | +0.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -1.6 | -3.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -1.3 | -3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -5.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -0.9 | -0.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -2.0 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -0.9 | -2.6 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | -0.8 | -1.3 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -0.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | HLA complex group 25 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6p21.32 — chr6:33,249,534-33,255,167 (+) |
| Ensembl biotype | lncRNA |
| Also known as | dJ1033B10.16 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:20196](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20196) · Entrez [414765](https://www.ncbi.nlm.nih.gov/gene/414765) · Ensembl [ENSG00000232940](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232940)

## Data

Gene col 13877: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13877); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13877, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13877]; `tensor/DDL_lfc|DDL_z.npy` [13877]; `embed/gene_vectors.npy` [13877]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13877 or target_col == 13877). Every well: [[HCG25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HCG25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
