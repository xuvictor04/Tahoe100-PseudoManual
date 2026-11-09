---
symbol: "CNTN5"
type: "gene"
col: 7423
ensembl_id: "ENSG00000149972"
name: "contactin 5"
location: "11q22.1"
module: 140
arm: "+"
pooled_cpm: 13.69
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# CNTN5

*contactin 5* — 11q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.24× (z +23.5, q 0e+00, up in 37 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Dihydroartemisinin (drug)]] 5 µM: 0.716× (z -3.8, q 0.070, down in 14 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.0942×; ⚠ toxic); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0761×); [[Irinotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (A549 0.0724×); [[Canagliflozin (drug)]] 5 µM in 1 line (NCI-H2030 0.101×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNTNAP5]] (+0.86, fdr 7e-06), [[USH2A]] (+0.85, fdr 7e-06), [[CNTNAP4]] (+0.82, fdr 7e-06).
> It is in [[Module 140]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7423.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.24×** | +23.5 | 0e+00 | 37/42 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.54×** | +15.2 | 0e+00 | 35/41 (NCI-H2030, SW 900, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.70×** | +15.0 | 0e+00 | 24/27 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.76×** | +14.7 | 0e+00 | 10/11 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.24×** | +13.5 | 1e-39 | 36/44 (BT-474, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.85×** | +11.1 | 8e-27 | 14/16 (J82, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.77×** | +9.2 | 2e-18 | 29/45 (J82, NCI-H460, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +6.8 | 7e-10 | 21/39 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +6.5 | 5e-09 | 20/38 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +6.3 | 2e-08 | 20/40 (AsPC-1, J82, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.66×** | +5.8 | 3e-07 | 22/47 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.57×** | +5.0 | 2e-05 | 17/45 (SK-MEL-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +4.7 | 1e-04 | 15/41 (SW 900, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.48×** | +4.5 | 3e-04 | 20/45 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +4.5 | 3e-04 | 15/44 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Allantoin (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.007 | 10/46 (PANC-1, HS-578T, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.042 | 7/47 (KATO III, BT-474, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.083 | 6/43 (SNU-423, NCI-H23, …) | rises with dose | position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | 1.20× | +2.9 | 0.083 | 6/46 (SW480, A-172, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +2.9 | 0.083 | 8/43 (CFPAC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7423.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.0942×; ⚠ toxic); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0761×); [[Irinotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (A549 0.0724×); [[Canagliflozin (drug)]] 5 µM in 1 line (NCI-H2030 0.101×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.716×** | -3.8 | 0.070 | 14/46 (NCI-H2030, C-33 A, …) | top dose only |  |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 0.808× | -3.5 | 0.15 | 4/48 (BT-474, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7423. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.74 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.21× (z +11.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.47× (z +10.6) | — |
| [[J82 (line)]] | alt | 6.21 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 4.44 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +13.1) | [[Canagliflozin (drug)]] 5 µM 0.101× (z -8.7) |
| [[PANC-1 (line)]] | alt | 3.57 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.79× (z +13.8) | — |
| [[A-172 (line)]] | wt | 4.42 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.69× (z +11.4) | — |
| [[A498 (line)]] | wt | 5.04 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 17.8× (z +13.2) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LoVo (line)]] | wt | 4.09 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.20× (z +11.9) | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0942× (z -10.0) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 3.65 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +9.5) | — |
| [[SW480 (line)]] | alt | 4.13 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.12× (z +12.2) | — |
| [[A549 (line)]] | wt | 4.03 | 0 | 1 | — | [[Irinotecan (hydrochloride) (drug)]] 0.05 µM 0.0724× (z -8.8) |
| [[BT-474 (line)]] | alt | 4.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.4× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 4.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.70× (z +11.1) | — |
| [[HOP62 (line)]] | alt | 4.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.14× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 4.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.10× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 6.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.73× (z +8.5) | — |
| [[KATO III (line)]] | alt | 4.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.59× (z +11.7) | — |
| [[LOX-IMVI (line)]] | wt | 5.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.25× (z +10.2) | — |
| [[LS 180 (line)]] | wt | 3.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.90× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 6.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.23× (z +12.6) | — |
| [[NCI-H23 (line)]] | alt | 4.97 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 16.8× (z +9.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[RKO (line)]] | wt | 4.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.09× (z +10.6) | — |
| [[SK-MEL-2 (line)]] | alt | 5.91 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0761× (z -8.9) |
| [[SW 900 (line)]] | alt | 5.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +12.0) | — |
| [[A-427 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 362 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7423), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNTNAP5]] | +0.86 | +0.76 / +0.84 | both halves | 7e-06 | STRING 573 |
| [[USH2A]] | +0.85 | +0.77 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[CNTNAP4]] | +0.82 | +0.73 / +0.76 | both halves | 7e-06 | STRING 964 |
| [[PTPRT]] | +0.82 | +0.71 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[SGCZ]] | +0.81 | +0.78 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[GRIA4]] | +0.80 | +0.79 / +0.74 | both halves | 7e-06 |  |
| [[CSMD1]] | +0.80 | +0.65 / +0.83 | both halves | 7e-06 | STRING 480 |
| [[CNBD1]] | +0.80 | +0.74 / +0.81 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.80 | +0.76 / +0.79 | both halves | 7e-06 | same gene group |
| [[SCHLAP1]] | +0.79 | +0.71 / +0.82 | both halves | 7e-06 |  |
| [[LUZP2]] | +0.79 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[SLC27A6]] | +0.78 | +0.56 / +0.80 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.843). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.5, 29.1); signed map (32.9, 14.8). **Vector** length 64.0, 9.70% of its response variance represented; |z| ≥ 3 in 920 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.8 | +23.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.2 | +15.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.5 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.8 | +11.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.7 | +15.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +9.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.8 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.5 | +2.7 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.6 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.3 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -0.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -0.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.8 | -1.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.6 | -1.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | contactin 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.1 — chr11:99,020,949-100,358,885 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NB-2, hNB-2 |
| Gene groups (HGNC) | I-set domain containing; Contactins |
| Reactome | 1 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [O94779](https://www.uniprot.org/uniprotkb/O94779) (Contactin-5):

> Contactins mediate cell surface interactions during nervous system development. Has some neurite outgrowth-promoting activity in the cerebral cortical neurons but not in hippocampal neurons. Probably involved in neuronal activity in the auditory system (By similarity).

**Summary**, from NCBI Gene [53942](https://www.ncbi.nlm.nih.gov/gene/53942):

> The protein encoded by this gene is a member of the immunoglobulin superfamily, and contactin family, which mediate cell surface interactions during nervous system development. This protein is a glycosylphosphatidylinositol (GPI)-anchored neuronal membrane protein that functions as a cell adhesion molecule. It may play a role in the formation of axon connections in the developing nervous system. Alternatively spliced transcript variants encoding different isoforms have been described for this …

**Accessions** — [HGNC:2175](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2175) · Entrez [53942](https://www.ncbi.nlm.nih.gov/gene/53942) · UniProt [O94779](https://www.uniprot.org/uniprotkb/O94779) · Ensembl [ENSG00000149972](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149972)

## Data

Gene col 7423: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7423); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7423, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7423]; `tensor/DDL_lfc|DDL_z.npy` [7423]; `embed/gene_vectors.npy` [7423]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7423 or target_col == 7423). Every well: [[CNTN5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNTN5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
