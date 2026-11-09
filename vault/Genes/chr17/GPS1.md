---
symbol: "GPS1"
type: "gene"
col: 9844
ensembl_id: "ENSG00000169727"
name: "G protein pathway suppressor 1"
location: "17q25.3"
module: 50
arm: "+"
pooled_cpm: 9.51
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# GPS1

*G protein pathway suppressor 1* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.90× (z +15.5, q 0e+00, up in 32 of 34 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.72× (z +5.3, q 8e-06, up in 27 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (NCI-H2030 0.0858×); [[Carbamazepine (drug)]] 0.05 µM in 1 line (AsPC-1 0.0575×); [[AZD-8055 (drug)]] 5 µM in 1 line (SHP-77 0.0518×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AP2M1]] (+0.71, fdr 1e-05), [[COPS6]] (+0.70, fdr 9e-06), [[DPM2]] (+0.70, fdr 1e-05); moves opposite to [[PABPN1]] (-0.65, fdr 1e-05), [[MRPL33]] (-0.64, fdr 1e-05), [[UBE2CP5]] (-0.57, fdr 2e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9844.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **4.90×** | +15.5 | 0e+00 | 32/34 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **4.28×** | +13.7 | 5e-40 | 14/16 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **3.13×** | +10.3 | 1e-22 | 26/26 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.21×** | +7.8 | 1e-12 | 43/47 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **2.09×** | +7.2 | 7e-11 | 37/47 (SW480, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **2.02×** | +6.9 | 6e-10 | 40/47 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.75×** | +5.5 | 4e-06 | 26/39 (HOP62, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.72×** | +5.3 | 8e-06 | 27/46 (SW480, HOP62, …) | two highest doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.68×** | +4.9 | 6e-05 | 22/38 (KATO III, SW1417, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.64×** | +4.8 | 8e-05 | 22/45 (KATO III, A498, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **1.55×** | +4.1 | 0.002 | 15/41 (LOX-IMVI, A549, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.52×** | +4.1 | 0.002 | 20/47 (HEC-1-A, SK-MEL-2, …) | two highest doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.43×** | +3.5 | 0.019 | 10/47 (SW480, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +3.3 | 0.041 | 13/46 (KATO III, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.056 | 13/46 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.056 | 17/47 (HEC-1-A, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9844.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (NCI-H2030 0.0858×); [[Carbamazepine (drug)]] 0.05 µM in 1 line (AsPC-1 0.0575×); [[AZD-8055 (drug)]] 5 µM in 1 line (SHP-77 0.0518×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.697× | -3.5 | 0.25 | 19/47 (SW1417, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.720× | -3.2 | 0.40 | 16/46 (SW48, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9844. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 16.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.19× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[HOP62 (line)]] | alt | 8.01 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.94× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H460 (line)]] | wt | 8.57 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.27× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[PANC-1 (line)]] | alt | 12.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.17× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SW480 (line)]] | alt | 9.32 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.82× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A498 (line)]] | wt | 10.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[AsPC-1 (line)]] | alt | 2.99 | 0 | 1 | — | [[Carbamazepine (drug)]] 0.05 µM 0.0575× (z -8.9) |
| [[HT-29 (line)]] | alt | 8.77 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.58× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[LoVo (line)]] | wt | 5.13 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.34× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H2030 (line)]] | alt | 4.50 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0858× (z -9.4) |
| [[SHP-77 (line)]] | alt | 21.9 | 0 | 1 | — | [[AZD-8055 (drug)]] 5 µM 0.0518× (z -8.9) |
| [[SNU-423 (line)]] | alt | 9.97 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.94× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A-172 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.83 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9844), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP2M1]] | +0.71 | +0.75 / +0.56 | both halves | 1e-05 | pathway: Cargo recognition for clathrin-mediated endocytosis |
| [[COPS6]] | +0.70 | +0.74 / +0.57 | both halves | 9e-06 | same gene group; pathway: Cargo recognition for clathrin-mediated endocytosis; STRING 999 |
| [[DPM2]] | +0.70 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[SNX17]] | +0.67 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[MLX]] | +0.66 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[TAF6]] | +0.64 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[PHB1]] | +0.64 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[ECHS1]] | +0.64 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[BCKDK]] | +0.63 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[TTLL12]] | +0.62 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[APEH]] | +0.61 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[PRPS1]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PABPN1]] | -0.65 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[MRPL33]] | -0.64 | -0.64 / -0.57 | both halves | 1e-05 |  |
| [[UBE2CP5]] | -0.57 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[PNISR]] | -0.55 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[NDUFA1]] | -0.54 | -0.69 / -0.41 | both halves | 4e-05 |  |
| [[MIA]] | -0.54 | -0.47 / -0.37 | both halves | 9e-05 |  |
| [[ZBTB7A]] | -0.54 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[TERF2IP]] | -0.53 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[CD63]] | -0.53 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[EIF3J-DT]] | -0.52 | -0.41 / -0.32 | both halves | 1e-04 |  |
| [[LINC01772]] | -0.52 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[CCDC65]] | -0.51 | -0.53 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.425). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-26.8, -18.4); signed map (-26.5, -44.0). **Vector** length 60.9, 10.4% of its response variance represented; |z| ≥ 3 in 791 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +3.2 | +15.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +2.9 | +13.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +4.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +2.7 | +6.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +2.6 | +7.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.5 | +3.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +0.0 |
| fall | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.6 | -3.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.6 | -1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.1 | -2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -2.7 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -1.3 | -1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.3 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | G protein pathway suppressor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:82,050,691-82,057,470 (+) |
| Ensembl biotype | protein_coding |
| Also known as | COPS1, CSN1 |
| Gene groups (HGNC) | COP9 signalosome |
| Reactome | 16 pathways, smallest: RHOBTB1 GTPase cycle; RHOBTB GTPase Cycle; DNA Damage Recognition in GG-NER |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13098](https://www.uniprot.org/uniprotkb/Q13098) (COP9 signalosome complex subunit 1):

> Component of the COP9 signalosome (CSN), a master regulator of the ubiquitin conjugation pathway. CSN mediates the deneddylation of the cullin subunits of all cullin-RING ligases. By reversing the activating neddylation on the cullin-RING ligase, the COP9 signalosome restores the ligase to its inactive state and resets it for substrate recognition. CSN is also involved in phosphorylation of p53/TP53, c-jun/JUN, IkappaBalpha/NFKBIA, ITPK1 and IRF8/ICSBP, possibly via its association with CK2 and …

**Summary**, from NCBI Gene [2873](https://www.ncbi.nlm.nih.gov/gene/2873):

> This gene is known to suppress G-protein and mitogen-activated signal transduction in mammalian cells. The encoded protein shares significant similarity with Arabidopsis FUS6, which is a regulator of light-mediated signal transduction in plant cells. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:4549](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4549) · Entrez [2873](https://www.ncbi.nlm.nih.gov/gene/2873) · UniProt [Q13098](https://www.uniprot.org/uniprotkb/Q13098) · Ensembl [ENSG00000169727](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169727)

## Data

Gene col 9844: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9844); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9844, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9844]; `tensor/DDL_lfc|DDL_z.npy` [9844]; `embed/gene_vectors.npy` [9844]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9844 or target_col == 9844). Every well: [[GPS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
