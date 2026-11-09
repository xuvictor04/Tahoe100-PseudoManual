---
symbol: "CLASP1-AS1"
type: "gene"
col: 15457
ensembl_id: "ENSG00000265451"
name: "CLASP1 antisense RNA 1"
location: "2q14.2"
module: 54
arm: "-"
pooled_cpm: 2.89
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# CLASP1-AS1

*CLASP1 antisense RNA 1* — 2q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 94.1× (z +29.7, q 0e+00, up in 19 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 5.93× (z +16.4, q 0e+00, up in 31 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[OTS514 (drug)]] 0.05 µM: 0.480× (z -4.5, q 0.003, down in 13 of 39 measured lines) ⚠ transcription drop.
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TEX14]] (+0.68, fdr 7e-06), [[CCDC200]] (+0.67, fdr 7e-06), [[GRIK5]] (+0.59, fdr 3e-05); moves opposite to [[SDHAF1]] (-0.64, fdr 1e-05), [[POP7]] (-0.60, fdr 3e-05), [[CCZ1]] (-0.56, fdr 4e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15457.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **94.1×** | +29.7 | 0e+00 | 19/19 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **85.8×** | +28.0 | 0e+00 | 6/6 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **54.2×** | +24.1 | 0e+00 | 9/9 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **5.93×** | +16.4 | 0e+00 | 31/34 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **13.6×** | +8.9 | 5e-17 | 7/8 (PANC-1, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.53×** | +8.2 | 2e-14 | 26/32 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.28×** | +7.7 | 8e-13 | 32/45 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.38×** | +7.6 | 1e-12 | 28/40 (HEC-1-A, SW 900, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.77×** | +6.5 | 4e-09 | 30/44 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.72×** | +6.5 | 4e-09 | 14/30 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.53×** | +6.1 | 7e-08 | 24/46 (SK-MEL-2, SW480, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +5.3 | 6e-06 | 16/33 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.25×** | +5.2 | 8e-06 | 18/43 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.07×** | +4.5 | 3e-04 | 18/43 (LOX-IMVI, SW480, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.82×** | +3.8 | 0.005 | 13/40 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.72×** | +3.5 | 0.012 | 13/46 (HEC-1-A, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Cytarabine (drug)]] 5 µM |  | **1.76×** | +3.5 | 0.012 | 6/40 (LoVo, HS-578T, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.73×** | +3.5 | 0.012 | 9/43 (HEC-1-A, SW1417, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.71×** | +3.3 | 0.025 | 7/40 (HEC-1-A, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Flutamide (drug)]] 0.05 µM |  | **1.61×** | +3.1 | 0.050 | 10/45 (NCI-H460, LoVo, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.068 | 7/44 (HEC-1-A, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15457.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.480×** | -4.5 | 0.003 | 13/39 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | 0.580× | -3.5 | 0.13 | 11/45 (HCT15, LoVo, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.602× | -3.3 | 0.18 | 8/45 (A498, HT-29, …) | two highest doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.608× | -3.2 | 0.18 | 10/41 (HEC-1-A, SW 900, …) | inconsistent across doses | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.711× | -3.2 | 0.18 | 9/46 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.05 µM |  | 0.609× | -3.1 | 0.20 | 9/40 (HCT15, PANC-1, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.05 µM |  | 0.614× | -3.0 | 0.20 | 5/41 (RPMI-7951, NCI-H2030, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15457. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.49 | 5 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 401× (z +17.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 27.7× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 2.77 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 183× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 12.8× (z +9.7) | — |
| [[A498 (line)]] | wt | 2.32 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 78.2× (z +12.4) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 5.83 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 364× (z +13.6) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 4.50 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 87.1× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 23.0× (z +11.8) | — |
| [[J82 (line)]] | alt | 4.45 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 31.2× (z +9.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 5.99 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 134× (z +12.8) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 1.66 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 154× (z +14.3) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 6.18 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 130× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 22.9× (z +10.7) | — |
| [[SW 900 (line)]] | alt | 4.05 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 192× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 11.7× (z +8.6) | — |
| [[SW480 (line)]] | alt | 2.26 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 170× (z +17.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 6.17× (z +8.5) | — |
| [[C32 (line)]] | wt | 3.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 39.0× (z +10.8) | — |
| [[CFPAC-1 (line)]] | alt | 3.11 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 52.1× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 2.28 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 136× (z +11.0) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 3.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.6× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.61 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 198× (z +11.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 5.11 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 32.8× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 2.36 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 66.7× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.748 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.999 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15457), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEX14]] | +0.68 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[CCDC200]] | +0.67 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[GRIK5]] | +0.59 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[LINC00641]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[FSIP1]] | +0.58 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[IQCN]] | +0.57 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[CROCC]] | +0.57 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[AXDND1]] | +0.56 | +0.66 / +0.39 | both halves | 5e-05 |  |
| [[RYR2]] | +0.56 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[GALC]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[MYOSLID]] | +0.55 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[UBE2D3-AS1]] | +0.55 | +0.65 / +0.47 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*39 of its nearest partners move opposite, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAF1]] | -0.64 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[POP7]] | -0.60 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[CCZ1]] | -0.56 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[CDK5RAP1]] | -0.55 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[MALSU1]] | -0.54 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[NCBP2AS2]] | -0.54 | -0.30 / -0.58 | both halves | 2e-04 |  |
| [[NSFP1]] | -0.54 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[C1orf35]] | -0.54 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[BFAR]] | -0.53 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[C8orf76]] | -0.53 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[CCZ1B]] | -0.53 | -0.61 / -0.35 | both halves | 1e-04 |  |
| [[TMEM11]] | -0.53 | -0.32 / -0.60 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.595). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (27.3, -26.1); signed map (17.4, -1.7). **Vector** length 53.1, 7.14% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.6 | +28.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.5 | +29.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.0 | +24.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +16.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +0.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.2 | +4.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +2.7 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | +1.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | +0.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.0 | +0.3 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | CLASP1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q14.2 — chr2:121,530,422-121,532,705 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55328](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55328) · Entrez [107985942](https://www.ncbi.nlm.nih.gov/gene/107985942) · Ensembl [ENSG00000265451](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000265451)

## Data

Gene col 15457: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15457); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15457, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15457]; `tensor/DDL_lfc|DDL_z.npy` [15457]; `embed/gene_vectors.npy` [15457]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15457 or target_col == 15457). Every well: [[CLASP1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLASP1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
