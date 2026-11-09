---
symbol: "NORAD"
type: "gene"
col: 15257
ensembl_id: "ENSG00000260032"
name: "non-coding RNA activated by DNA damage"
location: "20q11.23"
module: 25
arm: "+"
pooled_cpm: 197.46
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# NORAD

*non-coding RNA activated by DNA damage* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.26× (z +12.1, q 5e-31, up in 47 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.95× (z +10.1, q 1e-21, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.678× (z -8.3, q 5e-14, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK9]] (+0.66, fdr 7e-06), [[PURB]] (+0.65, fdr 1e-05), [[NRAS]] (+0.63, fdr 7e-06); moves opposite to [[SNHG9]] (-0.62, fdr 1e-05), [[MZT2A]] (-0.59, fdr 4e-05), [[TRIM52-AS1]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15257.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.26×** | +12.1 | 5e-31 | 47/50 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.95×** | +10.1 | 1e-21 | 45/48 (C32, RKO, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.06×** | +5.7 | 2e-06 | 42/49 (A498, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.86×** | +4.9 | 1e-04 | 36/48 (NCI-H2347, hTERT-HPNE, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.30×** | +3.7 | 0.025 | 25/45 (NCI-H2347, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | 1.23× | +3.1 | 0.16 | 23/48 (NCI-H1792, HS-578T, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 1.24× | +3.1 | 0.17 | 29/48 (LOX-IMVI, J82, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.23× | +3.0 | 0.18 | 24/48 (A-427, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15257.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.678×** | -8.3 | 5e-14 | 40/49 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.675×** | -5.7 | 3e-06 | 34/48 (SW480, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.714×** | -5.1 | 5e-05 | 44/49 (NCI-H2347, HCT15, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.526×** | -5.1 | 5e-05 | 36/45 (NCI-H2030, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.757×** | -4.1 | 0.006 | 26/47 (C-33 A, SW 900, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.759×** | -4.0 | 0.006 | 32/49 (COLO 205, HepG2/C3A, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.841× | -3.7 | 0.018 | 24/48 (NCI-H1573, SW480, …) | top dose only | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.788×** | -3.6 | 0.022 | 27/48 (COLO 205, A549, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.792×** | -3.4 | 0.043 | 25/48 (BT-474, NCI-H23, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.856× | -3.3 | 0.051 | 14/48 (RKO, HT-29, …) | rises with dose |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | 0.789× | -3.1 | 0.11 | 23/48 (HT-29, SNU-423, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15257. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 252 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.07× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -10.7) |
| [[A-172 (line)]] | wt | 183 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.38× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 126 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.25× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.587× (z -9.4) |
| [[LoVo (line)]] | wt | 241 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.378× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 241 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -15.4) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.351× (z -12.0) |
| [[NCI-H2347 (line)]] | alt | 154 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.33× (z +9.0) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 280 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.26× (z +9.7) | [[Harringtonine (drug)]] 5 µM 0.454× (z -9.1) |
| [[SW480 (line)]] | alt | 298 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.370× (z -12.0) |
| [[A498 (line)]] | wt | 111 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.07× (z +9.8) | — |
| [[BT-474 (line)]] | alt | 178 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.57× (z +9.9) | — |
| [[C-33 A (line)]] | alt | 123 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.352× (z -10.1) ⚠ toxic |
| [[C32 (line)]] | wt | 124 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.72× (z +16.7) | — |
| [[HepG2_C3A (line)]] | wt | 223 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -8.8) |
| [[Hs 766T (line)]] | wt | 511 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -10.5) |
| [[HT-29 (line)]] | alt | 265 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.71× (z +10.5) | — |
| [[KATO III (line)]] | alt | 387 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.429× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 228 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 125 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 242 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.88× (z +11.4) | — |
| [[RKO (line)]] | wt | 202 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.36× (z +13.0) | — |
| [[SHP-77 (line)]] | alt | 82.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.10× (z +11.2) | — |
| [[SK-MEL-2 (line)]] | alt | 242 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.05× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 168 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.380× (z -8.7) ⚠ cell-cycle shift, explains ~20% of this change |
| [[SW 900 (line)]] | alt | 153 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -8.8) |
| [[A-427 (line)]] | wt | 166 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 147 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 129 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 194 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 159 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 163 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 136 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 268 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 116 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 152 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 275 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 438 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 437 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 166 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15257), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK9]] | +0.66 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[PURB]] | +0.65 | +0.49 / +0.74 | both halves | 1e-05 |  |
| [[NRAS]] | +0.63 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[ZNF460]] | +0.63 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[HAPSTR1]] | +0.61 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[TARDBP]] | +0.60 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[BBS10]] | +0.60 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[TGOLN2]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[G6PD]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[CLTC]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[PRELID3B]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[SF3B4]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG9]] | -0.62 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[MZT2A]] | -0.59 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[TRIM52-AS1]] | -0.59 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[SNHG12]] | -0.57 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[NDUFC1]] | -0.57 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[COX5A]] ⚠ | -0.55 | -0.47 / -0.64 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG6]] | -0.55 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[TBC1D12]] | -0.54 | -0.39 / -0.61 | both halves | 6e-05 |  |
| [[CNIH4]] | -0.53 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[LONRF1]] | -0.53 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[SNHG8]] | -0.53 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[LSM8]] | -0.53 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[SNHG32]] | -0.52 | -0.47 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.463). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-32.8, -20.9); signed map (-15.4, -36.0). **Vector** length 131, 39.7% of its response variance represented; |z| ≥ 3 in 804 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +12.6 | +10.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.6 | +5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.3 | +4.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.3 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +3.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.9 | +2.1 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +2.9 | +3.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.9 | -8.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.9 | -4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -4.4 | -3.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | -4.3 | -3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.3 | -3.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.4 | -2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -2.5 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -2.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | non-coding RNA activated by DNA damage |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20q11.23 — chr20:36,045,618-36,051,018 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously LINC00657 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [647979](https://www.ncbi.nlm.nih.gov/gene/647979):

> Predicted to enable protein sequestering activity. Predicted to be involved in regulation of mRNA stability. Biomarker of lung non-small cell carcinoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:44311](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44311) · Entrez [647979](https://www.ncbi.nlm.nih.gov/gene/647979) · Ensembl [ENSG00000260032](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000260032)

## Data

Gene col 15257: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15257); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15257, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15257]; `tensor/DDL_lfc|DDL_z.npy` [15257]; `embed/gene_vectors.npy` [15257]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15257 or target_col == 15257). Every well: [[NORAD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NORAD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
