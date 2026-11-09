---
symbol: "NAB1"
type: "gene"
col: 6167
ensembl_id: "ENSG00000138386"
name: "NGFI-A binding protein 1"
location: "2q32.2"
module: 197
arm: "+"
pooled_cpm: 103.34
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 27
n_dd_up_clean: 5
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/197"]
generated_by: "tahoemap"
---

# NAB1

*NGFI-A binding protein 1* — 2q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 3.36× (z +19.4, q 0e+00, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.525× (z -10.7, q 3e-24, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JUNB]] (+0.65, fdr 1e-05), [[BAHCC1]] (+0.65, fdr 7e-06), [[FAT1]] (+0.64, fdr 7e-06); moves opposite to [[NDUFAF7]] (-0.68, fdr 7e-06), [[ZNF500]] (-0.62, fdr 1e-05), [[CCDC32]] (-0.62, fdr 1e-05).
> It is in [[Module 197]], a single-armed module (Nervous system development).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SLC22A3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6167.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **3.36×** | +19.4 | 0e+00 | 40/48 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.20×** | +18.6 | 0e+00 | 39/47 (HOP62, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.04×** | +11.8 | 4e-30 | 39/49 (NCI-H1573, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.00×** | +11.5 | 1e-28 | 31/47 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +9.8 | 2e-20 | 34/42 (NCI-H1573, HOP62, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +9.0 | 1e-17 | 34/45 (HOP62, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +8.6 | 6e-16 | 10/50 (LoVo, NCI-H23, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +4.5 | 4e-04 | 24/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.023 | 20/48 (SNU-423, C32, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~9% of this change | **1.23×** | +3.3 | 0.054 | 22/47 (SNU-423, HepG2/C3A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6167.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.525×** | -10.7 | 3e-24 | 42/48 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.582×** | -8.5 | 5e-15 | 40/48 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.663×** | -6.8 | 1e-09 | 34/48 (LoVo, SNU-1, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.755×** | -6.6 | 5e-09 | 28/49 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.690×** | -6.2 | 7e-08 | 36/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.493×** | -6.2 | 7e-08 | 34/44 (LoVo, RKO, …) | all doses, flat | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.718×** | -5.5 | 2e-06 | 30/48 (AsPC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.737×** | -5.1 | 2e-05 | 31/48 (AsPC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.568×** | -4.9 | 5e-05 | 33/48 (LoVo, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.823×** | -4.6 | 2e-04 | 22/49 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.595×** | -4.5 | 3e-04 | 32/48 (LoVo, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.762×** | -4.4 | 6e-04 | 23/48 (Hs 766T, LS 180, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.775×** | -4.3 | 9e-04 | 28/48 (LoVo, Hs 766T, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.786×** | -4.0 | 0.002 | 27/48 (SNU-1, KATO III, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.731×** | -3.7 | 0.007 | 26/49 (MIA PaCa-2, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.803×** | -3.7 | 0.009 | 23/48 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.659×** | -3.6 | 0.009 | 24/48 (Hs 766T, LoVo, …) | rises with dose | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6167. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 292 | 0 | 26 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -18.1) |
| [[Hs 766T (line)]] | wt | 330 | 0 | 12 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.235× (z -14.6) |
| [[LS 180 (line)]] | wt | 310 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -17.3) |
| [[NCI-H460 (line)]] | wt | 75.6 | 7 (2 ⚠) | 2 | [[Harringtonine (drug)]] 5 µM 5.76× (z +18.7) | [[Ixazomib citrate (drug)]] 5 µM 0.435× (z -9.3) |
| [[KATO III (line)]] | alt | 175 | 0 | 8 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -14.1) |
| [[SW480 (line)]] | alt | 157 | 0 | 8 | — | [[Panobinostat (drug)]] 5 µM 0.271× (z -12.4) |
| [[BT-474 (line)]] | alt | 45.1 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.34× (z +17.9) | — |
| [[HOP62 (line)]] | alt | 68.5 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.40× (z +26.9) | — |
| [[PANC-1 (line)]] | alt | 72.3 | 5 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 4.15× (z +17.2) | [[Ixazomib citrate (drug)]] 5 µM 0.462× (z -9.3) |
| [[SNU-1 (line)]] | wt | 178 | 0 | 6 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.182× (z -13.4) |
| [[HEC-1-A (line)]] | alt | 79.3 | 5 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.78× (z +13.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 70.5 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 5.39× (z +15.4) | [[Ixazomib citrate (drug)]] 5 µM 0.385× (z -8.7) |
| [[SW 900 (line)]] | alt | 65.1 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +15.9) | [[Ixazomib citrate (drug)]] 5 µM 0.347× (z -9.1) |
| [[A-172 (line)]] | wt | 96.1 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.83× (z +17.9) | — |
| [[A498 (line)]] | wt | 113 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.33× (z +15.2) | — |
| [[A549 (line)]] | wt | 85.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +16.8) | — |
| [[AsPC-1 (line)]] | alt | 269 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.137× (z -17.5) |
| [[C32 (line)]] | wt | 34.1 | 4 | 0 | [[Harringtonine (drug)]] 0.5 µM 5.80× (z +12.7) | — |
| [[HS-578T (line)]] | alt | 54.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +15.9) | — |
| [[NCI-H1573 (line)]] | alt | 83.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +22.0) | — |
| [[NCI-H2030 (line)]] | alt | 72.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +18.3) | — |
| [[RPMI-7951 (line)]] | alt | 83.0 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +16.7) | [[Auranofin (drug)]] 5 µM 0.374× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 81.6 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.17× (z +10.5) | — |
| [[J82 (line)]] | alt | 67.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +19.3) | — |
| [[NCI-H1792 (line)]] | alt | 81.0 | 1 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.50× (z +11.4) | [[Digitoxin (drug)]] 5 µM 0.381× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 50.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.84× (z +23.5) | — |
| [[NCI-H2347 (line)]] | alt | 45.6 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.73× (z +14.3) | — |
| [[SNU-423 (line)]] | alt | 50.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.96× (z +22.5) | — |
| [[A-427 (line)]] | wt | 79.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.431× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 74.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +15.9) | — |
| [[COLO 205 (line)]] | alt | 72.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.59× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 61.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +17.0) | — |
| [[LOX-IMVI (line)]] | wt | 66.8 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 3.53× (z +12.5) | — |
| [[RKO (line)]] | wt | 104 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.312× (z -9.4) |
| [[SHP-77 (line)]] | alt | 71.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.6) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0907× (z -12.3) ⚠ toxic |
| [[C-33 A (line)]] | alt | 88.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.48× (z +8.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 44.9 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM 0.126× (z -9.3) |
| [[H4 (line)]] | wt | 57.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 38.9 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.90× (z +10.3) | — |
| [[SW 1088 (line)]] | alt | 92.6 | 0 | 1 (1 ⚠) | — | [[olaparib (drug)]] 0.05 µM 0.0454× (z -11.6) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 97.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6167), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*35 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUNB]] | +0.65 | +0.55 / +0.70 | both halves | 1e-05 | pathway: NGF-stimulated transcription |
| [[BAHCC1]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[FAT1]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[MYO1C]] | +0.64 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[SKIL]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[KRT8]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[HR]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[CDK6]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[INPP1]] | +0.59 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[SFR1]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[EXTL2]] | +0.57 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[JAG1]] | +0.57 | +0.60 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*65 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFAF7]] | -0.68 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[ZNF500]] | -0.62 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[CCDC32]] | -0.62 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[RAB6A]] | -0.61 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[QPCTL]] | -0.60 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[CRYZL1]] | -0.59 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[FLYWCH1]] | -0.59 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[ELMOD3]] | -0.58 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[MED31]] | -0.58 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[RNF149]] | -0.58 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[C8orf76]] | -0.58 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[IL17RA]] | -0.58 | -0.44 / -0.61 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC22A3]] | B | SLC22A3 activity raises NAB1's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 1.72× lower at baseline in the lines without SLC22A3 | 0.045 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |
| [[SERPINE2]] | B | SERPINE2 activity raises NAB1's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 1.17× lower at baseline in the lines without SERPINE2 | 0.086 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[IL2RG]] | B | IL2RG activity raises NAB1's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 1.50× lower at baseline in the lines without IL2RG | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 197]] — Nervous system development; 16 genes; every member is in the + arm (projection on the module's main direction 0.678). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.7, 1.7); signed map (22.6, 34.6). **Vector** length 148, 48.0% of its response variance represented; |z| ≥ 3 in 1,399 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +12.8 | +19.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +11.5 | +18.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.9 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.7 | +11.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.5 | +11.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.8 | +2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.5 | +1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +3.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -9.4 | -10.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -8.9 | -8.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -7.5 | -6.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.3 | -4.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.1 | -4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.0 | -6.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.6 | -4.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.4 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | NGFI-A binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.2 — chr2:190,646,746-190,692,766 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | NGFI-A binding protein family |
| Reactome | 7 pathways, smallest: EGR2 and SOX10-mediated initiation of Schwann cell myelination; NGF-stimulated transcription; Nuclear Events (kinase and transcription factor activation) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13506](https://www.uniprot.org/uniprotkb/Q13506) (NGFI-A-binding protein 1):

> Acts as a transcriptional repressor for zinc finger transcription factors EGR1 and EGR2.

**Summary**, from NCBI Gene [4664](https://www.ncbi.nlm.nih.gov/gene/4664):

> Predicted to enable transcription coregulator activity. Predicted to be involved in regulation of DNA-templated transcription. Predicted to act upstream of or within endochondral ossification; nervous system development; and regulation of epidermis development. Predicted to be located in nucleoplasm. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7626](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7626) · Entrez [4664](https://www.ncbi.nlm.nih.gov/gene/4664) · UniProt [Q13506](https://www.uniprot.org/uniprotkb/Q13506) · Ensembl [ENSG00000138386](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138386)

## Data

Gene col 6167: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6167); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6167, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6167]; `tensor/DDL_lfc|DDL_z.npy` [6167]; `embed/gene_vectors.npy` [6167]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6167 or target_col == 6167). Every well: [[NAB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
