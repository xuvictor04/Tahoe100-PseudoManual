---
symbol: "RNF11"
type: "gene"
col: 4397
ensembl_id: "ENSG00000123091"
name: "ring finger protein 11"
location: "1p32.3"
module: 5
arm: "-"
pooled_cpm: 87.91
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# RNF11

*ring finger protein 11* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.56× (z +10.8, q 1e-24, up in 37 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF10]] (+0.62, fdr 7e-06), [[TCTA]] (+0.55, fdr 4e-05), [[CCPG1]] (+0.54, fdr 1e-05); moves opposite to [[POLR3K]] (-0.59, fdr 1e-05), [[POLR1G]] (-0.58, fdr 1e-05), [[SPOUT1]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4397.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +10.8 | 1e-24 | 37/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.26×** | +10.4 | 5e-23 | 43/49 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +10.0 | 3e-21 | 32/48 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +8.8 | 1e-16 | 29/44 (PANC-1, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +8.4 | 4e-15 | 32/45 (NCI-H23, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +7.8 | 5e-13 | 36/48 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.33×** | +7.0 | 2e-10 | 33/49 (HS-578T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +6.6 | 2e-09 | 28/48 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +6.6 | 2e-09 | 28/48 (LoVo, HT-29, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.20×** | +6.3 | 2e-08 | 21/48 (HOP62, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +5.4 | 3e-06 | 25/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +5.4 | 3e-06 | 30/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +5.2 | 1e-05 | 17/49 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +5.2 | 1e-05 | 25/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.24×** | +4.9 | 4e-05 | 25/48 (HT-29, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.40×** | +4.3 | 6e-04 | 23/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.18× | +4.0 | 0.002 | 17/48 (A498, SW480, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.17× | +3.8 | 0.004 | 22/48 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.009 | 9/49 (HT-29, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.16× | +3.4 | 0.015 | 19/47 (BT-474, LS 180, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4397.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 0.5 µM |  | 0.852× | -4.0 | 0.032 | 17/48 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.898× | -3.8 | 0.032 | 14/48 (SNU-1, BT-474, …) | top dose only |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.856× | -3.7 | 0.032 | 10/49 (LoVo, NCI-H1792, …) | top dose only | plate-row cell shift |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.863× | -3.7 | 0.032 | 15/48 (SW480, LS 180, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 5 µM |  | 0.868× | -3.5 | 0.048 | 13/48 (LoVo, Panc 03.27, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.871× | -3.5 | 0.052 | 16/48 (LS 180, HEC-1-A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.866× | -3.3 | 0.059 | 12/47 (A-427, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | 0.871× | -3.3 | 0.059 | 18/48 (NCI-H2347, LS 180, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.877× | -3.3 | 0.059 | 14/48 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.871× | -3.3 | 0.059 | 13/48 (HT-29, NCI-H1792, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 0.05 µM |  | 0.870× | -3.2 | 0.060 | 16/48 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 0.5 µM |  | 0.879× | -3.2 | 0.060 | 5/48 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.917× | -3.1 | 0.088 | 3/48 (Panc 03.27, KATO III, …) | top dose only |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.885× | -3.0 | 0.093 | 12/48 (SW48, LS 180, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 0.886× | -3.0 | 0.095 | 5/48 (SW480, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4397. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 76.5 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 68.6 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.12× (z +18.7) | — |
| [[HOP62 (line)]] | alt | 84.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.60× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 119 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +13.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 112 | 3 | 0 | [[Auranofin (drug)]] 5 µM 2.26× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 97.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.28× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +10.7) | — |
| [[A-172 (line)]] | wt | 81.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.2) | — |
| [[A498 (line)]] | wt | 74.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +11.2) | — |
| [[AsPC-1 (line)]] | alt | 95.8 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +12.1) | — |
| [[NCI-H1573 (line)]] | alt | 82.7 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +10.2) | — |
| [[A549 (line)]] | wt | 52.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +8.9) | — |
| [[C32 (line)]] | wt | 90.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 72.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 117 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +10.8) | — |
| [[NCI-H23 (line)]] | alt | 86.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.53× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 66.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.95× (z +12.7) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 75.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 83.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +11.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 60.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.26× (z +10.2) | — |
| [[A-427 (line)]] | wt | 98.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 110 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 104 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 97.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 115 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 79.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 96.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 93.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 93.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 94.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 75.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4397), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*38 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF10]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 | same gene group |
| [[TCTA]] | +0.55 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[CCPG1]] | +0.54 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[RTN3]] | +0.54 | +0.50 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[KIAA1191]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[YPEL5]] | +0.53 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[MAP1LC3B]] | +0.53 | +0.38 / +0.58 | both halves | 7e-05 |  |
| [[BLOC1S6]] | +0.52 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[PSAP]] | +0.51 | +0.39 / +0.61 | both halves | 5e-05 |  |
| [[CHP1]] | +0.51 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[SNX3]] | +0.51 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[SLC12A6]] | +0.51 | +0.46 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*62 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR3K]] | -0.59 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[POLR1G]] | -0.58 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[SPOUT1]] | -0.57 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[DHODH]] | -0.56 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[PPRC1]] | -0.56 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[URB2]] | -0.56 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[PWP2]] | -0.55 | -0.37 / -0.65 | both halves | 8e-05 |  |
| [[HAUS7]] | -0.54 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[MRPL12]] | -0.54 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[BRIX1]] | -0.54 | -0.39 / -0.65 | both halves | 5e-05 |  |
| [[NAT10]] | -0.54 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[NOP2]] | -0.53 | -0.47 / -0.60 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.455). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.7, -43.1); signed map (-13.1, 15.4). **Vector** length 99.7, 26.7% of its response variance represented; |z| ≥ 3 in 989 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +8.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.0 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +8.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +5.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.8 | +2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.7 | +0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.6 | +1.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | +4.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.5 | +5.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.5 | -3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -1.4 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -1.6 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:51,236,273-51,273,447 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-123, Sid1669p, MGC51169 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | ADIPOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3C5](https://www.uniprot.org/uniprotkb/Q9Y3C5) (RING finger protein 11):

> Essential component of a ubiquitin-editing protein complex, comprising also TNFAIP3, ITCH and TAX1BP1, that ensures the transient nature of inflammatory signaling pathways. Promotes the association of TNFAIP3 to RIPK1 after TNF stimulation. TNFAIP3 deubiquitinates 'Lys-63' polyubiquitin chains on RIPK1 and catalyzes the formation of 'Lys-48'-polyubiquitin chains. This leads to RIPK1 proteasomal degradation and consequently termination of the TNF- or LPS-mediated activation of NF-kappa-B. …

**Summary**, from NCBI Gene [26994](https://www.ncbi.nlm.nih.gov/gene/26994):

> The protein encoded by this gene contains a RING-H2 finger motif, which is known to be important for protein-protein interactions. The expression of this gene has been shown to be induced by mutant RET proteins (MEN2A/MEN2B). The germline mutations in RET gene are known to be responsible for the development of multiple endocrine neoplasia (MEN). [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10056](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10056) · Entrez [26994](https://www.ncbi.nlm.nih.gov/gene/26994) · UniProt [Q9Y3C5](https://www.uniprot.org/uniprotkb/Q9Y3C5) · Ensembl [ENSG00000123091](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123091)

## Data

Gene col 4397: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4397); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4397, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4397]; `tensor/DDL_lfc|DDL_z.npy` [4397]; `embed/gene_vectors.npy` [4397]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4397 or target_col == 4397). Every well: [[RNF11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
