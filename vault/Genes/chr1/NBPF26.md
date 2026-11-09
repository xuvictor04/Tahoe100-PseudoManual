---
symbol: "NBPF26"
type: "gene"
col: 15764
ensembl_id: "ENSG00000273136"
name: "NBPF member 26"
location: "1p11.2"
module: 226
arm: "+"
pooled_cpm: 16.6
n_lines_expressing: 46
n_dd_up: 13
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/226"]
generated_by: "tahoemap"
---

# NBPF26

*NBPF member 26* — 1p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.99× (z +27.6, q 0e+00, up in 42 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.579× (z -7.4, q 9e-11, down in 20 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.681× (z -5.4, q 2e-05, down in 21 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1792 0.117×, hTERT-HPNE 0.180×, HEC-1-A 0.335×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 0.177×, SNU-423 0.192×, SK-MEL-2 0.258×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (NCI-H2030 0.101×, NCI-H23 0.199×); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (SNU-1 0.0834×); [[Silodosin (drug)]] 5 µM in 1 line (HCT15 0.0773×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOTCH2NLR]] (+0.72, fdr 7e-06, ⚠ same locus), [[NOTCH2NLA]] (+0.71, fdr 7e-06), [[NBPF19]] (+0.71, fdr 7e-06), [[NBPF10]] (+0.70, fdr 7e-06); moves opposite to [[TMEM248]] (-0.59, fdr 1e-05), [[CTDP1]] (-0.55, fdr 1e-05), [[ILRUN]] (-0.54, fdr 3e-05).
> It is in [[Module 226]], a single-armed module (NOTCH2 Activation and Transmission of Signal to the Nucleus).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NOTCH2NLR]] → it (grade B ⚠); 2 go from it, the strongest it → [[NOTCH2NLR]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15764.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.99×** | +27.6 | 0e+00 | 42/42 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.47×** | +12.3 | 4e-32 | 38/43 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.01×** | +9.8 | 2e-20 | 32/42 (HEC-1-A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.59×** | +6.6 | 8e-09 | 27/43 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.96×** | +4.9 | 8e-05 | 22/43 (SK-MEL-2, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +4.8 | 1e-04 | 21/43 (Hs 766T, NCI-H2347, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.78×** | +4.3 | 0.002 | 16/43 (SK-MEL-2, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +4.2 | 0.002 | 16/40 (BT-474, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +4.0 | 0.003 | 18/43 (BT-474, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +4.0 | 0.003 | 16/43 (HOP62, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.9 | 0.006 | 17/39 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +3.6 | 0.013 | 10/41 (RKO, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.4 | 0.026 | 11/43 (HT-29, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.044 | 15/43 (A-427, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15764.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1792 0.117×, hTERT-HPNE 0.180×, HEC-1-A 0.335×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 0.177×, SNU-423 0.192×, SK-MEL-2 0.258×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (NCI-H2030 0.101×, NCI-H23 0.199×); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (SNU-1 0.0834×); [[Silodosin (drug)]] 5 µM in 1 line (HCT15 0.0773×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.579×** | -7.4 | 9e-11 | 20/26 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.681×** | -5.4 | 2e-05 | 21/43 (NCI-H2030, NCI-H23, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.695×** | -5.1 | 6e-05 | 21/32 (NCI-H1792, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.712×** | -4.4 | 0.002 | 16/29 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Arbutin (drug)]] 5 µM |  | 0.784× | -3.3 | 0.11 | 9/43 (BT-474, NCI-H2030, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.855× | -3.1 | 0.17 | 9/43 (SW 900, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15764. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 26.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +20.2) | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -9.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 24.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -10.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 13.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +19.4) | — |
| [[A-427 (line)]] | wt | 34.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +16.2) | — |
| [[hTERT-HPNE (line)]] | wt | 26.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -9.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 12.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +13.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 13.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +9.8) | [[HI-TOPK-032 (drug)]] 0.05 µM 0.174× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 24.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +13.5) | [[Dinaciclib (drug)]] 0.05 µM 0.284× (z -8.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 49.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.258× (z -9.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 30.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.192× (z -10.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 7.69 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +10.2) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.146× (z -9.3) |
| [[SW480 (line)]] | alt | 13.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.177× (z -12.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +14.6) | — |
| [[AN3 CA (line)]] | alt | 27.2 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0895× (z -9.0) |
| [[BT-474 (line)]] | alt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +8.7) | — |
| [[C32 (line)]] | wt | 16.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +12.7) | — |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0773× (z -9.8) |
| [[HOP62 (line)]] | alt | 29.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +16.4) | — |
| [[Hs 766T (line)]] | wt | 19.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 28.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 10.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.86× (z +13.9) | — |
| [[J82 (line)]] | alt | 25.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +16.2) | — |
| [[KATO III (line)]] | alt | 4.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +12.4) | — |
| [[NCI-H1573 (line)]] | alt | 6.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 38.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -15.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 7.43 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.101× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 12.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.199× (z -8.5) |
| [[RKO (line)]] | wt | 27.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +13.4) | — |
| [[SNU-1 (line)]] | wt | 15.0 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0834× (z -10.4) |
| [[SW48 (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0775× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.84 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15764), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOTCH2NLR]] | +0.72 | +0.66 / +0.74 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[NOTCH2NLA]] | +0.71 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[NBPF19]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 | same gene group |
| [[NBPF10]] | +0.70 | +0.68 / +0.65 | both halves | 7e-06 | same gene group; STRING 456 |
| [[NOTCH2NLB]] | +0.67 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[NBPF14]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 | same gene group |
| [[NOTCH2NLC]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[NOTCH2]] | +0.65 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[PRR14]] | +0.48 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[ZC3H6]] | +0.48 | +0.54 / +0.37 | both halves | 9e-05 |  |
| [[TIFA]] | +0.48 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[SYNGAP1]] | +0.48 | +0.51 / +0.40 | both halves | 4e-05 |  |
| [[UST]] | +0.47 | +0.48 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM248]] | -0.59 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[CTDP1]] | -0.55 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[ILRUN]] | -0.54 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[STRAP]] | -0.53 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[DNAJB11]] | -0.53 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[NIPA2]] | -0.50 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[TRAPPC10]] | -0.50 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[ATG5]] | -0.50 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[PARN]] | -0.50 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[UFD1]] | -0.50 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ADPGK]] | -0.49 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[TYW1]] | -0.49 | -0.46 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOTCH2NLR]] | B | NOTCH2NLR activity raises NBPF26's level | lines that do not express NOTCH2NLR (9) vs lines expressing it (41) | 3.34× lower at baseline in the lines without NOTCH2NLR | 2e-04 | ⚠ within organs, on part of the lines |
| [[FMNL3]] | B | FMNL3 activity raises NBPF26's level | lines that do not express FMNL3 (8) vs lines expressing it (42) | 2.41× lower at baseline in the lines without FMNL3 | 0.012 | ⚠ within organs, on part of the lines; also absent: STARD9, CERCAM, ASAP3 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOTCH2NLR]] | C | NBPF26 activity raises NOTCH2NLR's level | lines that do not express NBPF26 (4) vs lines expressing it (46) | 2.69× lower at baseline in the lines without NBPF26 | 0.015 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent |
| [[TRAPPC10]] | C | NBPF26 activity raises TRAPPC10's level | lines that do not express NBPF26 (4) vs lines expressing it (46) | 1.35× lower at baseline in the lines without NBPF26 | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 226]] — NOTCH2 Activation and Transmission of Signal to the Nucleus; 9 genes; every member is in the + arm (projection on the module's main direction 0.844). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.5, -29.5); signed map (44.5, -15.5). **Vector** length 58.4, 9.04% of its response variance represented; |z| ≥ 3 in 852 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NOTCH2 Activation and Transmission of Signal to the Nucleus* (reactome, mean cos +0.67 to 4); *Signaling by NOTCH2* (reactome, mean cos +0.67 to 4); *Pre-NOTCH Transcription and Translation* (reactome, mean cos +0.67 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +27.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.6 | +12.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.3 | +9.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.1 | +1.3 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.1 | +0.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.0 | -0.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | +1.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.6 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.6 | -2.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | +0.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.0 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.9 | +3.6 |

## What is on record

|  |  |
|---|---|
| Name | NBPF member 26 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p11.2 — chr1:120,723,945-120,842,229 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | NBPF members |
| Matched by | ensembl_id |

UniProt [B4DH59](https://www.uniprot.org/uniprotkb/B4DH59) carries no function annotation.

**Summary**, from NCBI Gene [101060684](https://www.ncbi.nlm.nih.gov/gene/101060684):

> Predicted to enable calcium ion binding activity. Predicted to be involved in animal organ development; positive regulation of signal transduction; and system development. Predicted to be located in cytoplasm and extracellular region. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:49571](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49571) · Entrez [101060684](https://www.ncbi.nlm.nih.gov/gene/101060684) · UniProt [B4DH59](https://www.uniprot.org/uniprotkb/B4DH59) · Ensembl [ENSG00000273136](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000273136)

## Data

Gene col 15764: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15764); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15764, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15764]; `tensor/DDL_lfc|DDL_z.npy` [15764]; `embed/gene_vectors.npy` [15764]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15764 or target_col == 15764). Every well: [[NBPF26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NBPF26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
