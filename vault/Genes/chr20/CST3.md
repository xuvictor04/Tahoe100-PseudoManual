---
symbol: "CST3"
type: "gene"
col: 2136
ensembl_id: "ENSG00000101439"
name: "cystatin C"
location: "20p11.21"
module: 48
arm: "+"
pooled_cpm: 81.27
n_lines_expressing: 48
n_dd_up: 8
n_dd_down: 6
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# CST3

*cystatin C* — 20p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.01× (z +11.3, q 7e-27, up in 46 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.96× (z +6.7, q 4e-09, up in 41 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (NCI-H1573 9.41×, SW480 5.98×, HEC-1-A 5.40×, PANC-1 5.73×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 4.91×, HCT15 11.2×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (AsPC-1 3.20×, LS 180 2.98×).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.364× (z -10.0, q 5e-21, down in 43 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPX1]] (+0.63, fdr 3e-05), [[SSR4]] (+0.63, fdr 7e-06), [[UBL5]] (+0.60, fdr 1e-05); moves opposite to [[MATR3-1]] (-0.56, fdr 1e-05), [[TATDN1]] (-0.56, fdr 2e-05), [[DNAJC2]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[HLA-DRA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2136.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (NCI-H1573 9.41×, SW480 5.98×, HEC-1-A 5.40×, PANC-1 5.73×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 4.91×, HCT15 11.2×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (AsPC-1 3.20×, LS 180 2.98×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **5.01×** | +11.3 | 7e-27 | 46/46 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **3.67×** | +8.8 | 5e-16 | 39/39 (SW480, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.14×** | +7.4 | 2e-11 | 41/41 (SW480, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +6.7 | 4e-09 | 41/47 (AsPC-1, LS 180, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +4.8 | 2e-04 | 42/45 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.74×** | +3.7 | 0.019 | 33/48 (HEC-1-A, SK-MEL-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.031 | 32/46 (SW1417, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~65% of this change | **1.59×** | +3.2 | 0.084 | 29/46 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2136.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.364×** | -10.0 | 5e-21 | 43/46 (RKO, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.514×** | -4.4 | 0.003 | 37/46 (HT-29, COLO 205, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.542×** | -4.3 | 0.003 | 39/46 (RPMI-7951, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.588×** | -3.7 | 0.026 | 31/46 (COLO 205, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.396×** | -3.4 | 0.076 | 37/47 (NCI-H661, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.406×** | -3.3 | 0.086 | 33/47 (BT-474, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Baicalin (drug)]] 5 µM |  | 0.738× | -3.0 | 0.20 | 39/47 (hTERT-HPNE, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2136. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 328 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 9.41× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -8.7) |
| [[SW480 (line)]] | alt | 78.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.98× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 61.4 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -9.3) |
| [[KATO III (line)]] | alt | 154 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -13.2) |
| [[LoVo (line)]] | wt | 39.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.42× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -10.2) |
| [[A549 (line)]] | wt | 58.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.10× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HCT15 (line)]] | alt | 29.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.6× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HS-578T (line)]] | alt | 148 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -9.0) |
| [[HT-29 (line)]] | alt | 65.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -11.0) |
| [[LS 180 (line)]] | wt | 91.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 41.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.79× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 97.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.09× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 42.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.17× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -9.2) |
| [[RKO (line)]] | wt | 49.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.96× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -13.5) |
| [[RPMI-7951 (line)]] | alt | 160 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -12.1) |
| [[SHP-77 (line)]] | alt | 88.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -12.2) |
| [[A-427 (line)]] | wt | 26.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -10.2) |
| [[A498 (line)]] | wt | 90.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[BT-474 (line)]] | alt | 55.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 64.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.58× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[COLO 205 (line)]] | alt | 163 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 47.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HepG2_C3A (line)]] | wt | 128 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -9.1) |
| [[HOP62 (line)]] | alt | 59.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.82× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[Hs 766T (line)]] | wt | 117 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 67.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.92× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1792 (line)]] | alt | 58.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.90× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2347 (line)]] | alt | 74.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -11.1) |
| [[PANC-1 (line)]] | alt | 33.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.73× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 66.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.62× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SNU-1 (line)]] | wt | 55.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.45× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SNU-423 (line)]] | alt | 78.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.60× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW 900 (line)]] | alt | 107 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -10.9) |
| [[SW1417 (line)]] | alt | 294 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW48 (line)]] | wt | 41.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.98× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.5 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.4 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2136), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPX1]] | +0.63 | +0.44 / +0.71 | both halves | 3e-05 |  |
| [[SSR4]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[UBL5]] | +0.60 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[TMSB10]] | +0.59 | +0.57 / +0.68 | both halves | 9e-06 |  |
| [[APRT]] | +0.58 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[NDUFA2]] | +0.58 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[FUCA1]] | +0.57 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[SLPI]] | +0.57 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[SIAE]] | +0.56 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[S100A6]] | +0.56 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[PRDX4]] | +0.55 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[ATP1A1]] | +0.55 | +0.66 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MATR3-1]] | -0.56 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[TATDN1]] | -0.56 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[DNAJC2]] | -0.55 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[GTF2H3]] | -0.54 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[GLRX2]] | -0.54 | -0.61 / -0.31 | both halves | 2e-04 |  |
| [[CHMP6]] | -0.53 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[POGK]] | -0.53 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[PSMC5]] | -0.53 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[DRG2]] | -0.53 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[PPID]] | -0.51 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[UBXN4]] | -0.50 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[DNAJA3]] | -0.50 | -0.47 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-DRA]] | B | HLA-DRA activity raises CST3's level | lines that do not express HLA-DRA (39) vs lines expressing it (11) | 1.87× lower at baseline in the lines without HLA-DRA | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530 |
| [[AQP3]] | B | AQP3 activity raises CST3's level | lines that do not express AQP3 (19) vs lines expressing it (31) | 1.72× lower at baseline in the lines without AQP3 | 0.036 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CST3's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CD74]] | B | CD74 activity raises CST3's level | lines that do not express CD74 (31) vs lines expressing it (19) | 1.65× lower at baseline in the lines without CD74 | 0.039 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5 |
| [[PSMB5]] | B | PSMB5 activity raises CST3's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HAPLN3]] | B | HAPLN3 activity weakens CST3's drug response | lines that do not express HAPLN3 (7) vs lines expressing it (41) | the lines without HAPLN3 respond 1.19× as strongly (z diff -1.08); strongest at Homoharringtonine 5 µM: 0.27x vs 0.42x (z diff -2.6) | 0.086 | ⚠ within organs, on part of the lines; also absent: GLIPR2, MFGE8, GLI2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[HLA-DRB1]] | B | HLA-DRB1 activity raises CST3's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 1.54× lower at baseline in the lines without HLA-DRB1 | 0.091 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP |
| [[S100A13]] | C | S100A13 activity raises CST3's level | lines that do not express S100A13 (4) vs lines expressing it (46) | 2.77× lower at baseline in the lines without S100A13 | 0.061 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CASP4, SP100, KIFC3; maybe low, not absent |
| [[SSBP2]] | C | SSBP2 activity lowers CST3's level | lines that do not express SSBP2 (4) vs lines expressing it (46) | 2.85× higher at baseline in the lines without SSBP2 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENAH, AGPAT4, ANKRD44; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.560). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-49.0, -21.5); signed map (-35.1, 11.4). **Vector** length 80.2, 31.0% of its response variance represented; |z| ≥ 3 in 647 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +6.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.7 | +3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | -0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | -1.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +1.6 | +0.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.3 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.2 | -4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.6 | -10.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.9 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -0.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -0.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | cystatin C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.21 — chr20:23,626,706-23,638,473 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cystatins, type 2 |
| Reactome | 5 pathways, smallest: Amyloid fiber formation; Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [P01034](https://www.uniprot.org/uniprotkb/P01034) (Cystatin-C):

> As an inhibitor of cysteine proteinases, this protein is thought to serve an important physiological role as a local regulator of this enzyme activity.

**Summary**, from NCBI Gene [1471](https://www.ncbi.nlm.nih.gov/gene/1471):

> The cystatin superfamily encompasses proteins that contain multiple cystatin-like sequences. Some of the members are active cysteine protease inhibitors, while others have lost or perhaps never acquired this inhibitory activity. There are three inhibitory families in the superfamily, including the type 1 cystatins (stefins), type 2 cystatins and the kininogens. The type 2 cystatin proteins are a class of cysteine proteinase inhibitors found in a variety of human fluids and secretions, where …

**Accessions** — [HGNC:2475](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2475) · Entrez [1471](https://www.ncbi.nlm.nih.gov/gene/1471) · UniProt [P01034](https://www.uniprot.org/uniprotkb/P01034) · Ensembl [ENSG00000101439](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101439)

## Data

Gene col 2136: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2136); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2136, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2136]; `tensor/DDL_lfc|DDL_z.npy` [2136]; `embed/gene_vectors.npy` [2136]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2136 or target_col == 2136). Every well: [[CST3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CST3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
