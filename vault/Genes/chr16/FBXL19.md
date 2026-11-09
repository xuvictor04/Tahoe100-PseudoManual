---
symbol: "FBXL19"
type: "gene"
col: 1799
ensembl_id: "ENSG00000099364"
name: "F-box and leucine rich repeat protein 19"
location: "16p11.2"
module: 7
arm: "+"
pooled_cpm: 16.9
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 27
n_dd_up_clean: 0
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# FBXL19

*F-box and leucine rich repeat protein 19* — 16p11.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.315× (z -25.3, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1orf159]] (+0.64, fdr 7e-06), [[ZNF444]] (+0.57, fdr 1e-05), [[ZNF513]] (+0.56, fdr 2e-05); moves opposite to [[GTF3A]] (-0.56, fdr 1e-05, ⚠ GTF3A in the vector space only through flagged drug-doses), [[ARHGAP12]] (-0.49, fdr 9e-05), [[ARL2BP]] (-0.46, fdr 5e-05), [[TRIM36]] (-0.45, fdr 4e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1799.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.7 | 0.14 | 1/48 (C32) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 1.23× | +3.2 | 0.36 | 11/45 (LoVo, C-33 A, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.38 | 7/47 (HOP62, LOX-IMVI, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1799.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.315×** | -25.3 | 0e+00 | 44/47 (MIA PaCa-2, BT-474, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.354×** | -16.1 | 0e+00 | 47/48 (KATO III, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.376×** | -15.1 | 0e+00 | 45/48 (BT-474, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.396×** | -14.3 | 2e-44 | 44/47 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.435×** | -12.9 | 5e-36 | 38/47 (MIA PaCa-2, BT-474, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.560×** | -12.7 | 6e-35 | 41/47 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.402×** | -12.5 | 5e-34 | 39/47 (MIA PaCa-2, COLO 205, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.571×** | -8.7 | 3e-16 | 32/48 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.596×** | -8.0 | 8e-14 | 31/46 (LS 180, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.384×** | -7.7 | 6e-13 | 35/48 (A-427, hTERT-HPNE, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.619×** | -7.4 | 6e-12 | 29/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.750×** | -6.3 | 1e-08 | 26/48 (NCI-H460, C32, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.677×** | -6.0 | 7e-08 | 26/48 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.680×** | -6.0 | 1e-07 | 27/47 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **0.650×** | -5.9 | 1e-07 | 23/44 (LoVo, HCT15, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.530×** | -5.1 | 9e-06 | 18/44 (HOP62, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.556×** | -4.8 | 6e-05 | 16/48 (SK-MEL-2, CHP-212, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.840× | -3.8 | 0.004 | 15/48 (A-427, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.789×** | -3.7 | 0.006 | 11/47 (J82, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.791×** | -3.6 | 0.006 | 13/47 (C32, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1799. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 13.0 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -12.5) |
| [[BT-474 (line)]] | alt | 19.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0880× (z -21.0) |
| [[MIA PaCa-2 (line)]] | alt | 27.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -21.2) |
| [[A-427 (line)]] | wt | 17.7 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.164× (z -12.4) |
| [[HT-29 (line)]] | alt | 15.6 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.321× (z -10.2) |
| [[KATO III (line)]] | alt | 19.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -14.8) |
| [[LOX-IMVI (line)]] | wt | 22.0 | 0 | 4 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -13.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.299× (z -11.9) |
| [[COLO 205 (line)]] | alt | 24.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -15.0) |
| [[SW480 (line)]] | alt | 13.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -16.4) |
| [[A-172 (line)]] | wt | 24.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -12.6) |
| [[C-33 A (line)]] | alt | 29.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -11.6) |
| [[C32 (line)]] | wt | 15.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.184× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 18.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -13.4) |
| [[Hs 766T (line)]] | wt | 18.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -10.8) |
| [[J82 (line)]] | alt | 14.5 | 0 | 2 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0879× (z -10.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.379× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 23.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.201× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 14.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -9.1) |
| [[SNU-423 (line)]] | alt | 14.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -12.2) |
| [[SW1417 (line)]] | alt | 13.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -11.7) |
| [[A498 (line)]] | wt | 24.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 18.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 15.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -12.6) |
| [[CHP-212 (line)]] | wt | 19.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -10.8) |
| [[HCT15 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 19.3 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.169× (z -9.0) |
| [[LoVo (line)]] | wt | 14.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -15.1) |
| [[LS 180 (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.160× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[NCI-H23 (line)]] | alt | 22.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 14.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -17.1) |
| [[RKO (line)]] | wt | 14.8 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.122× (z -10.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 16.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -9.1) |
| [[SW48 (line)]] | wt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -9.9) |
| [[A549 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1799), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1orf159]] | +0.64 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[ZNF444]] | +0.57 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[ZNF513]] | +0.56 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[PCGF3]] | +0.56 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[SMG5]] | +0.56 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[CD2BP2]] | +0.56 | +0.37 / +0.58 | both halves | 8e-05 |  |
| [[KMT2D]] | +0.54 | +0.58 / +0.51 | both halves | 1e-05 | same gene group |
| [[NACC1]] | +0.54 | +0.50 / +0.50 | both halves | 1e-05 | STRING 778 |
| [[PSMD3]] | +0.54 | +0.50 / +0.53 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[PRCC]] | +0.52 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[IKBKG]] | +0.52 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[AHSA2P]] | +0.51 | +0.45 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF3A]] ⚠ | -0.56 | -0.56 / -0.56 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ARHGAP12]] | -0.49 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[ARL2BP]] | -0.46 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[TRIM36]] | -0.45 | -0.41 / -0.55 | both halves | 4e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[CEP63]] | -0.45 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[LGALS1]] | -0.44 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[NR1D1]] | -0.44 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[UACA]] | -0.44 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[LNX2]] | -0.44 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[GADD45B]] | -0.44 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[MLF1]] | -0.44 | -0.37 / -0.45 | both halves | 7e-05 |  |
| [[TMEM14C]] | -0.44 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[ARSK]] | -0.44 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.343). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-33.6, -7.3); signed map (-12.9, -20.0). **Vector** length 75.4, 15.5% of its response variance represented; |z| ≥ 3 in 1,087 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +2.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.4 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +1.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.5 | +0.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -6.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.1 | -3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.2 | -3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.1 | -2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -8.7 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -2.0 | -1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | F-box and leucine rich repeat protein 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:30,923,055-30,948,783 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434K0410, Fbl19, JHDM1C, CXXC11 |
| Gene groups (HGNC) | PHD finger proteins; Zinc fingers CXXC-type; F-box and leucine rich repeat proteins |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PCT2](https://www.uniprot.org/uniprotkb/Q6PCT2) (F-box/LRR-repeat protein 19):

> Substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex that plays a role in different processes including cell migration, cell proliferation or cytoskeletal reorganization. Mediates RHOA ubiquitination and degradation in a ERK2-dependent manner. Induces RAC1 and RAC3 degradation by the proteasome system and thereby regulates TGFB1-induced E-cadherin down-regulation and cell migration. Also mediates ubiquitination and degradation of IL-33-induced …

**Summary**, from NCBI Gene [54620](https://www.ncbi.nlm.nih.gov/gene/54620):

> This gene encodes a member of the Skp1-Cullin-F-box family of E3 ubiquitin ligases. The encoded protein is reported to bind to the transmembrane receptor interleukin 1 receptor-like 1 and regulate its ubiquitination and degradation. This protein has been linked to the regulation of pulmonary inflammation and psoriasis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:25300](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25300) · Entrez [54620](https://www.ncbi.nlm.nih.gov/gene/54620) · UniProt [Q6PCT2](https://www.uniprot.org/uniprotkb/Q6PCT2) · Ensembl [ENSG00000099364](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099364)

## Data

Gene col 1799: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1799); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1799, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1799]; `tensor/DDL_lfc|DDL_z.npy` [1799]; `embed/gene_vectors.npy` [1799]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1799 or target_col == 1799). Every well: [[FBXL19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXL19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
