---
symbol: "MUTYH"
type: "gene"
col: 5371
ensembl_id: "ENSG00000132781"
name: "mutY DNA glycosylase"
location: "1p34.1"
module: 35
arm: "+"
pooled_cpm: 6.39
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# MUTYH

*mutY DNA glycosylase* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.51× (z +30.5, q 0e+00, up in 12 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.74× (z +12.3, q 9e-33, up in 26 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.661× (z -6.5, q 4e-08, down in 20 of 47 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZCWPW1]] (+0.66, fdr 1e-05), [[CYB5D2]] (+0.64, fdr 7e-06), [[CROCC]] (+0.64, fdr 1e-05); moves opposite to [[COX6A1]] (-0.57, fdr 4e-05), [[SDHAF1]] (-0.55, fdr 3e-05), [[UQCR10]] (-0.53, fdr 4e-05, ⚠ UQCR10 in the vector space only through flagged drug-doses), [[PDCD10]] (-0.51, fdr 2e-04).
> It sits in the **+** arm of [[Module 035]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5371.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.51×** | +30.5 | 0e+00 | 12/12 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.15×** | +28.6 | 0e+00 | 29/30 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.58×** | +22.1 | 0e+00 | 17/18 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +12.3 | 9e-33 | 26/40 (C32, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +9.2 | 3e-18 | 26/42 (AsPC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +6.3 | 2e-08 | 13/32 (HOP62, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +6.0 | 2e-07 | 11/38 (C32, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.32×** | +4.4 | 9e-04 | 12/47 (A498, A549, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.003 | 4/44 (SW 900, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.29×** | +3.9 | 0.006 | 9/39 (A-427, SNU-423, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.031 | 2/44 (Panc 03.27, NCI-H1792) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.24×** | +3.4 | 0.036 | 6/47 (J82, MIA PaCa-2, …) | rises with dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.036 | 3/44 (NCI-H2347, LS 180, …) | top dose only |  |
| [[Neratinib (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.080 | 4/45 (HOP62, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5371.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.661×** | -6.5 | 4e-08 | 20/47 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.707×** | -5.5 | 1e-05 | 16/42 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.707×** | -5.4 | 1e-05 | 15/45 (SW48, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.733×** | -4.9 | 2e-04 | 14/45 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.805×** | -3.4 | 0.074 | 12/45 (RPMI-7951, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5371. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 6.42 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.16× (z +11.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 13.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.6× (z +18.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 11.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.72× (z +10.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 6.24 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.75× (z +12.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 6.85 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.50× (z +10.2) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 5.99 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0927× (z -9.2) |
| [[SW480 (line)]] | alt | 8.02 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 13.5× (z +16.9) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 11.0 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0965× (z -8.9) |
| [[C32 (line)]] | wt | 6.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 5.00 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.88× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 6.47 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.37× (z +8.9) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 5.39 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.0× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 5.00 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0658× (z -10.5) |
| [[J82 (line)]] | alt | 6.58 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.4× (z +10.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 6.90 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.5× (z +11.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 4.60 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.28× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 4.19 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 19.1× (z +13.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 4.17 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 14.7× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 5.07 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.5× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 8.12 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.10× (z +10.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.28 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5371), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCWPW1]] | +0.66 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[CYB5D2]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[CROCC]] | +0.64 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[ALDH16A1]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SUMO2P17]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[DNAJC27-AS1]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[MSTO1]] | +0.56 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[MROH8]] | +0.56 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[OXCT1]] | +0.56 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[QTRT1]] | +0.56 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[PRDM11]] | +0.55 | +0.56 / +0.36 | both halves | 1e-04 |  |
| [[LMNB1-DT]] | +0.55 | +0.65 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX6A1]] | -0.57 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[SDHAF1]] | -0.55 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[UQCR10]] ⚠ | -0.53 | -0.41 / -0.41 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[UQCRQ]] ⚠ | -0.51 | -0.49 / -0.41 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PDCD10]] | -0.51 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[ELOB]] | -0.51 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[UBL5]] | -0.51 | -0.59 / -0.29 | both halves | 2e-04 |  |
| [[NEDD8]] | -0.51 | -0.65 / -0.36 | both halves | 1e-04 |  |
| [[TRAPPC1]] | -0.50 | -0.68 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[PGRMC2]] | -0.50 | -0.52 / -0.30 | both halves | 2e-04 |  |
| [[COX6C]] | -0.49 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[RAB5IF]] | -0.49 | -0.48 / -0.28 | both halves | 3e-04 |  |
| [[RPS5]] | -0.48 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[ATP5MK]] | -0.48 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[SEC61G]] | -0.48 | -0.44 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.492). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (0.1, 23.0); signed map (33.2, -19.2). **Vector** length 52.9, 6.70% of its response variance represented; |z| ≥ 3 in 836 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.9 | +28.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.8 | +30.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.3 | +22.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +12.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +9.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +1.2 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | +0.9 | +2.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.7 | -5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.5 | -6.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.1 | -5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -0.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.1 | -0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | +0.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | mutY DNA glycosylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:45,329,163-45,340,893 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MYH |
| Gene groups (HGNC) | DNA glycosylases |
| Reactome | 10 pathways, smallest: Diseases of Base Excision Repair; Displacement of DNA glycosylase by APEX1; Cleavage of the damaged purine |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UIF7](https://www.uniprot.org/uniprotkb/Q9UIF7) (Adenine DNA glycosylase):

> Involved in oxidative DNA damage repair. Initiates repair of A*oxoG to C*G by removing the inappropriately paired adenine base from the DNA backbone. Possesses both adenine and 2-OH-A DNA glycosylase activities.

**Summary**, from NCBI Gene [4595](https://www.ncbi.nlm.nih.gov/gene/4595):

> This gene encodes a DNA glycosylase involved in oxidative DNA damage repair. The enzyme excises adenine bases from the DNA backbone at sites where adenine is inappropriately paired with guanine, cytosine, or 8-oxo-7,8-dihydroguanine, a major oxidatively damaged DNA lesion. The protein is localized to the nucleus and mitochondria. This gene product is thought to play a role in signaling apoptosis by the introduction of single-strand breaks following oxidative damage. Mutations in this gene …

**Accessions** — [HGNC:7527](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7527) · Entrez [4595](https://www.ncbi.nlm.nih.gov/gene/4595) · UniProt [Q9UIF7](https://www.uniprot.org/uniprotkb/Q9UIF7) · Ensembl [ENSG00000132781](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132781)

## Data

Gene col 5371: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5371); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5371, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5371]; `tensor/DDL_lfc|DDL_z.npy` [5371]; `embed/gene_vectors.npy` [5371]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5371 or target_col == 5371). Every well: [[MUTYH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MUTYH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
