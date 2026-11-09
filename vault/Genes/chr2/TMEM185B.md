---
symbol: "TMEM185B"
type: "gene"
col: 13538
ensembl_id: "ENSG00000226479"
name: "transmembrane protein 185B"
location: "2q14.2"
module: 16
arm: "+"
pooled_cpm: 10.0
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# TMEM185B

*transmembrane protein 185B* — 2q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.96× (z +6.8, q 7e-09, up in 15 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.58× (z +4.8, q 4e-04, up in 23 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.449× (z -11.9, q 5e-30, down in 38 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MGA]] (+0.77, fdr 7e-06), [[TTPAL]] (+0.75, fdr 7e-06), [[PUF60]] (+0.75, fdr 7e-06); moves opposite to [[APTR]] (-0.78, fdr 7e-06), [[SRP54-AS1]] (-0.74, fdr 7e-06), [[COG7]] (-0.73, fdr 7e-06).
> It sits in the **+** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13538.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +6.8 | 7e-09 | 15/20 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +4.8 | 4e-04 | 23/44 (CFPAC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.58×** | +4.6 | 7e-04 | 22/45 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +4.2 | 0.004 | 15/25 (RPMI-7951, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.2 | 0.004 | 2/47 (SW48, HCT15) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +3.9 | 0.010 | 11/45 (HS-578T, BT-474, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +3.6 | 0.022 | 14/32 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +3.6 | 0.022 | 13/46 (CFPAC-1, SW480, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.026 | 14/47 (SW480, SW1417, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.42×** | +3.4 | 0.032 | 11/46 (HEC-1-A, HS-578T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.24×** | +3.2 | 0.064 | 18/45 (A-172, NCI-H2347, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +3.2 | 0.070 | 16/46 (HS-578T, HOP62, …) | all doses, flat |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.38×** | +3.2 | 0.070 | 8/46 (PANC-1, A498, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.085 | 10/47 (A498, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13538.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.449×** | -11.9 | 5e-30 | 38/45 (LOX-IMVI, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.503×** | -7.2 | 2e-10 | 28/45 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.587×** | -5.6 | 4e-06 | 25/46 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.609×** | -5.2 | 2e-05 | 24/46 (AN3 CA, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.614×** | -5.1 | 3e-05 | 25/45 (C-33 A, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.620×** | -4.8 | 1e-04 | 23/44 (A-427, H4, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.633×** | -4.5 | 4e-04 | 19/43 (PANC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.646×** | -4.4 | 7e-04 | 22/43 (LoVo, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.666×** | -4.3 | 0.001 | 20/42 (HT-29, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.701×** | -3.7 | 0.010 | 15/46 (COLO 205, SW48, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.725×** | -3.4 | 0.036 | 19/46 (C32, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.651×** | -3.2 | 0.061 | 9/46 (AN3 CA, SW 1271, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.742× | -3.0 | 0.11 | 20/45 (A-427, RKO, …) | top dose only | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13538. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 16.8 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0961× (z -13.3) |
| [[NCI-H23 (line)]] | alt | 14.8 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0501× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 10.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -15.9) |
| [[SW480 (line)]] | alt | 10.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.217× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -8.6) |
| [[BT-474 (line)]] | alt | 6.74 | 0 | 1 | — | [[Belumosudil (drug)]] 0.05 µM 0.0590× (z -9.9) |
| [[COLO 205 (line)]] | alt | 6.86 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0622× (z -8.5) |
| [[H4 (line)]] | wt | 12.0 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0539× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 12.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -12.1) |
| [[HOP62 (line)]] | alt | 9.03 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -10.9) |
| [[HS-578T (line)]] | alt | 6.52 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -8.8) |
| [[HT-29 (line)]] | alt | 9.56 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0547× (z -13.9) |
| [[hTERT-HPNE (line)]] | wt | 5.71 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.121× (z -8.6) |
| [[PANC-1 (line)]] | alt | 14.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -9.5) |
| [[RKO (line)]] | wt | 23.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.101× (z -8.9) |
| [[SHP-77 (line)]] | alt | 6.58 | 0 | 1 | — | [[Tofacitinib (drug)]] 0.05 µM 0.0829× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -8.6) |
| [[SNU-423 (line)]] | alt | 5.89 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0931× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 6.56 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0654× (z -8.9) |
| [[A-172 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.677 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13538), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGA]] | +0.77 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[TTPAL]] | +0.75 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[PUF60]] | +0.75 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[ZKSCAN2]] | +0.74 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[SLC35A4]] | +0.73 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[COA7]] | +0.73 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[N6AMT1]] | +0.73 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[SAYSD1]] | +0.72 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[RTL6]] | +0.71 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[ZFP41]] | +0.70 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[BBS10]] | +0.70 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[EIF4G1]] | +0.70 | +0.74 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APTR]] | -0.78 | -0.64 / -0.76 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | -0.74 | -0.76 / -0.68 | both halves | 7e-06 |  |
| [[COG7]] | -0.73 | -0.68 / -0.75 | both halves | 7e-06 |  |
| [[RAB6A]] | -0.73 | -0.75 / -0.67 | both halves | 7e-06 |  |
| [[KDELR1]] | -0.72 | -0.65 / -0.73 | both halves | 7e-06 |  |
| [[PMS2P4-1]] | -0.70 | -0.62 / -0.73 | both halves | 7e-06 |  |
| [[PIK3C2A]] | -0.68 | -0.71 / -0.62 | both halves | 7e-06 |  |
| [[KLHL7]] | -0.68 | -0.74 / -0.63 | both halves | 7e-06 |  |
| [[MFSD8]] | -0.67 | -0.61 / -0.69 | both halves | 7e-06 |  |
| [[GNRH1]] | -0.67 | -0.65 / -0.68 | both halves | 7e-06 |  |
| [[TULP3]] | -0.66 | -0.67 / -0.66 | both halves | 7e-06 |  |
| [[MAX]] | -0.66 | -0.64 / -0.67 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.713). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-3.1, -18.7); signed map (0.7, -32.1). **Vector** length 90.3, 20.1% of its response variance represented; |z| ≥ 3 in 822 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.1 | +3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +4.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.0 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +3.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.3 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -11.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -3.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.8 | -5.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.7 | -7.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -3.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 185B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.2 — chr2:120,217,479-120,223,400 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20979; previously FAM11B |
| Matched by | ensembl_id |

UniProt [Q9H7F4](https://www.uniprot.org/uniprotkb/Q9H7F4) carries no function annotation.

**Summary**, from NCBI Gene [79134](https://www.ncbi.nlm.nih.gov/gene/79134):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18896](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18896) · Entrez [79134](https://www.ncbi.nlm.nih.gov/gene/79134) · UniProt [Q9H7F4](https://www.uniprot.org/uniprotkb/Q9H7F4) · Ensembl [ENSG00000226479](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226479)

## Data

Gene col 13538: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13538); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13538, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13538]; `tensor/DDL_lfc|DDL_z.npy` [13538]; `embed/gene_vectors.npy` [13538]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13538 or target_col == 13538). Every well: [[TMEM185B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM185B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
