---
symbol: "RRP36"
type: "gene"
col: 4539
ensembl_id: "ENSG00000124541"
name: "ribosomal RNA processing 36"
location: "6p21.1"
module: 7
arm: "+"
pooled_cpm: 24.01
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# RRP36

*ribosomal RNA processing 36* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (13 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.28× (z +15.3, q 0e+00, up in 45 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.134×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (Hs 766T 0.187×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[LY-2584702 (tosylate salt) (drug)]] 5 µM in 1 line (KATO III 0.0746×; ⚠ toxic); [[Crizotinib (hydrochloride) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.210×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL20]] (+0.76, fdr 7e-06), [[GTF2E1]] (+0.67, fdr 7e-06), [[SCO1]] (+0.64, fdr 9e-06); moves opposite to [[MLF1]] (-0.59, fdr 1e-05), [[FAM53C]] (-0.57, fdr 1e-05), [[MYLIP]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 17 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4539.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.28×** | +15.3 | 0e+00 | 45/48 (SW480, LS 180, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.04×** | +12.8 | 4e-35 | 39/48 (LS 180, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.88×** | +11.1 | 2e-26 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.89×** | +10.8 | 8e-25 | 41/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.81×** | +10.0 | 1e-21 | 26/36 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.75×** | +9.9 | 6e-21 | 29/43 (SNU-423, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.38×** | +8.0 | 9e-14 | 30/47 (A-427, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +8.0 | 9e-14 | 34/47 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +7.0 | 2e-10 | 27/45 (SW480, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.48×** | +6.4 | 1e-08 | 23/40 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +6.1 | 4e-08 | 29/48 (HT-29, HOP62, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +6.0 | 8e-08 | 27/47 (SW480, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +5.8 | 3e-07 | 29/48 (PANC-1, A549, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.41×** | +5.8 | 3e-07 | 24/47 (LoVo, NCI-H2030, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +5.0 | 2e-05 | 25/47 (PANC-1, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.4 | 4e-04 | 18/48 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +4.2 | 7e-04 | 20/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +4.2 | 7e-04 | 15/48 (CFPAC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.5 | 0.010 | 9/48 (Panc 03.27, CFPAC-1, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.014 | 10/47 (CFPAC-1, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.017 | 10/47 (NCI-H23, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4539.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.134×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (Hs 766T 0.187×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[LY-2584702 (tosylate salt) (drug)]] 5 µM in 1 line (KATO III 0.0746×; ⚠ toxic); [[Crizotinib (hydrochloride) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.210×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.838× | -3.1 | 0.53 | 5/48 (J82, SW1417, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.843× | -3.0 | 0.53 | 8/48 (CFPAC-1, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4539. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 24.0 | 5 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.14× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 31.1 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.38× (z +10.0) | — |
| [[KATO III (line)]] | alt | 20.9 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.4× (z +9.0) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0746× (z -9.5) ⚠ toxic |
| [[LoVo (line)]] | wt | 19.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.62× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 20.2 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 12.6× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 21.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[A-427 (line)]] | wt | 29.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +9.9) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[A498 (line)]] | wt | 18.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[C-33 A (line)]] | alt | 35.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[HepG2_C3A (line)]] | wt | 25.3 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.210× (z -8.8) |
| [[Hs 766T (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HT-29 (line)]] | alt | 23.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.98× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 18.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H23 (line)]] | alt | 32.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.83× (z +8.7) | — |
| [[RKO (line)]] | wt | 30.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.28× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -9.1) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A-172 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4539), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL20]] | +0.76 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[GTF2E1]] | +0.67 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[SCO1]] | +0.64 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[MRM2]] | +0.63 | +0.67 / +0.56 | both halves | 1e-05 | pathway: rRNA processing |
| [[CIAPIN1]] | +0.63 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[TXNDC9]] | +0.63 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[FAM118B]] | +0.63 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[ZNF623]] | +0.62 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[MRPS11]] | +0.61 | +0.74 / +0.46 | both halves | 3e-05 |  |
| [[NDUFAF5]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[RNF25]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[C5orf22]] | +0.59 | +0.67 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLF1]] | -0.59 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[FAM53C]] | -0.57 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[MYLIP]] | -0.55 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[PEAK1]] | -0.55 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[RFX2]] | -0.54 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[LGMN]] | -0.54 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[KLHL15]] | -0.53 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[PIM2]] | -0.53 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[TENT5C]] | -0.52 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[VASN]] | -0.51 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[GTF2B]] | -0.50 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[TESK2]] | -0.49 | -0.51 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.526). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-48.0, 2.8); signed map (-8.5, -26.0). **Vector** length 86.4, 18.6% of its response variance represented; |z| ≥ 3 in 882 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.0 | +15.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.7 | +12.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.2 | +11.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.3 | +10.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +5.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +4.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +2.7 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | -2.4 | +3.0 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.8 | -1.1 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.7 | -3.1 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | -1.7 | -3.0 |
|  | [[Artemether (drug)]] 0.05 µM |  | -1.6 | -2.1 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal RNA processing 36 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:43,021,623-43,034,156 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ20C7.4; previously C6orf153 |
| Gene groups (HGNC) | Ribosome biogenesis factors |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EU6](https://www.uniprot.org/uniprotkb/Q96EU6) (Ribosomal RNA processing protein 36 homolog):

> Involved in the early processing steps of the pre-rRNA in the maturation pathway leading to the 18S rRNA.

**Summary**, from NCBI Gene [88745](https://www.ncbi.nlm.nih.gov/gene/88745):

> RRP36 functions at an early stage in the processing of 35S preribosomal RNA into the mature 18S species (Gerus et al., 2010 [PubMed 20038530]).[supplied by OMIM, Jul 2010]

**Accessions** — [HGNC:21374](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21374) · Entrez [88745](https://www.ncbi.nlm.nih.gov/gene/88745) · UniProt [Q96EU6](https://www.uniprot.org/uniprotkb/Q96EU6) · Ensembl [ENSG00000124541](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124541)

## Data

Gene col 4539: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4539); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4539, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4539]; `tensor/DDL_lfc|DDL_z.npy` [4539]; `embed/gene_vectors.npy` [4539]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4539 or target_col == 4539). Every well: [[RRP36 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRP36.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
