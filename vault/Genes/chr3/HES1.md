---
symbol: "HES1"
type: "gene"
col: 3538
ensembl_id: "ENSG00000114315"
name: "hes family bHLH transcription factor 1"
location: "3q29"
module: 109
arm: "+"
pooled_cpm: 218.1
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# HES1

*hes family bHLH transcription factor 1* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.71× (z +11.4, q 3e-27, up in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~68% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 8.84× (z +7.0, q 5e-10, up in 47 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (C32 17.6×, NCI-H2347 8.61×, SK-MEL-2 11.4×, HepG2/C3A 12.1×, …; ⚠ cell-cycle shift, explains ~68% of this change); [[Harringtonine (drug)]] 5 µM in 4 lines (C32 26.9×, PANC-1 12.0×, NCI-H460 21.0×, SK-MEL-2 19.6×; ⚠ cell-cycle shift, explains ~45% of this change); [[TAK-901 (drug)]] 5 µM in 4 lines (C32 190×, SK-MEL-2 56.2×, Hs 766T 36.5×, H4 42.0×); [[Gefitinib (drug)]] 5 µM in 1 line (NCI-H460 7.07×); [[PH-797804 (drug)]] 5 µM in 1 line (C32 23.8×).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.472× (z -4.6, q 0.002, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOS]] (+0.71, fdr 7e-06), [[NR4A1]] (+0.71, fdr 7e-06), [[NR4A3]] (+0.70, fdr 7e-06); moves opposite to [[NAPB]] (-0.68, fdr 7e-06), [[CLCC1]] (-0.68, fdr 7e-06), [[METTL3]] (-0.67, fdr 1e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[RASD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3538.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (C32 17.6×, NCI-H2347 8.61×, SK-MEL-2 11.4×, HepG2/C3A 12.1×, …; ⚠ cell-cycle shift, explains ~68% of this change); [[Harringtonine (drug)]] 5 µM in 4 lines (C32 26.9×, PANC-1 12.0×, NCI-H460 21.0×, SK-MEL-2 19.6×; ⚠ cell-cycle shift, explains ~45% of this change); [[TAK-901 (drug)]] 5 µM in 4 lines (C32 190×, SK-MEL-2 56.2×, Hs 766T 36.5×, H4 42.0×); [[Gefitinib (drug)]] 5 µM in 1 line (NCI-H460 7.07×); [[PH-797804 (drug)]] 5 µM in 1 line (C32 23.8×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **3.71×** | +11.4 | 3e-27 | 43/47 (C32, NCI-H2347, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **5.36×** | +9.9 | 1e-20 | 45/47 (C32, PANC-1, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **8.84×** | +7.0 | 5e-10 | 47/48 (C32, SK-MEL-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **2.37×** | +5.3 | 2e-05 | 41/47 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.96×** | +4.1 | 0.004 | 34/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **2.00×** | +4.1 | 0.004 | 36/46 (C32, SK-MEL-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~80% of this change | 1.64× | +3.0 | 0.20 | 33/47 (NCI-H460, H4, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3538.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.472×** | -4.6 | 0.002 | 37/47 (A-427, HT-29, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.502×** | -3.9 | 0.026 | 41/47 (SW480, SW48, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.645×** | -3.8 | 0.031 | 37/47 (SW480, SNU-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.535×** | -3.7 | 0.031 | 35/47 (SW48, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.572×** | -3.4 | 0.067 | 34/47 (SW48, NCI-H2030, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~93% of this change | 0.572× | -3.2 | 0.11 | 31/47 (HT-29, SW48, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.583× | -3.2 | 0.12 | 32/49 (SNU-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.604× | -3.1 | 0.13 | 36/47 (SW480, KATO III, …) | inconsistent across doses | position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 0.701× | -3.1 | 0.13 | 35/47 (H4, HOP62, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.609× | -3.0 | 0.13 | 26/47 (NCI-H1573, LS 180, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +1.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3538. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 132 | 10 (9 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 21.0× (z +14.1) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Gefitinib (drug)]] 5 µM 7.07× (z +9.4) | — |
| [[C32 (line)]] | wt | 307 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.6× (z +20.7) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 190× (z +14.0) | — |
| [[PANC-1 (line)]] | alt | 228 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +14.8) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 111 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +16.6) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 56.2× (z +10.2) | — |
| [[A498 (line)]] | wt | 174 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +12.3) ⚠ cell-cycle shift, explains ~68% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -9.4) ⚠ cell-cycle shift, explains ~8% of this change |
| [[H4 (line)]] | wt | 137 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +10.4) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 42.0× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 110 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.60× (z +15.3) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 36.5× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 138 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.45× (z +13.8) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[J82 (line)]] | alt | 134 | 3 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 11.8× (z +11.8) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H2347 (line)]] | alt | 185 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.61× (z +17.4) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[SW48 (line)]] | wt | 488 | 1 (1 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 7.99× (z +10.8) ⚠ cell-cycle shift, explains ~45% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -10.8) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -9.7) |
| [[A-172 (line)]] | wt | 118 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 8.83× (z +10.4) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[AN3 CA (line)]] | alt | 146 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +10.0) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[AsPC-1 (line)]] | alt | 117 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.74× (z +15.3) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[HEC-1-A (line)]] | alt | 143 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 15.1× (z +13.2) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[HepG2_C3A (line)]] | wt | 70.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +16.0) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 135 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 7.57× (z +9.9) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[KATO III (line)]] | alt | 364 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.93× (z +15.2) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[NCI-H1573 (line)]] | alt | 174 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 11.4× (z +12.4) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[A549 (line)]] | wt | 114 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 7.48× (z +9.8) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[CFPAC-1 (line)]] | alt | 291 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +10.3) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 139 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 10.8× (z +11.0) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H1792 (line)]] | alt | 188 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 9.64× (z +9.2) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[Panc 03.27 (line)]] | alt | 415 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +9.2) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[RPMI-7951 (line)]] | alt | 231 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 9.79× (z +9.8) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[SNU-1 (line)]] | wt | 183 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.36× (z +9.2) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[SNU-423 (line)]] | alt | 168 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +10.8) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[SW 1088 (line)]] | alt | 148 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.15× (z +10.0) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[SW1417 (line)]] | alt | 491 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +12.4) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[A-427 (line)]] | wt | 187 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 273 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 143 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 340 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 567 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 221 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 191 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 352 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 302 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 103 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.8 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 306 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 323 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3538), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOS]] | +0.71 | +0.72 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY; STRING 454 |
| [[NR4A1]] | +0.71 | +0.70 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[NR4A3]] | +0.70 | +0.69 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[IER2]] | +0.69 | +0.72 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[PER2]] | +0.67 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[MIR23AHG]] | +0.67 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[NR4A2]] | +0.66 | +0.55 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[FOSB]] | +0.66 | +0.64 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[EGR2]] | +0.65 | +0.65 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[TIPARP]] | +0.65 | +0.59 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[JUNB]] | +0.63 | +0.73 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[KLF10]] | +0.62 | +0.63 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAPB]] | -0.68 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[CLCC1]] | -0.68 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[METTL3]] | -0.67 | -0.57 / -0.65 | both halves | 1e-05 |  |
| [[CCNY-AS1]] | -0.66 | -0.63 / -0.61 | both halves | 7e-06 |  |
| [[RTCA]] | -0.60 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[C1orf198]] | -0.59 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[C8orf76]] | -0.58 | -0.70 / -0.45 | both halves | 3e-05 |  |
| [[ABCB10]] | -0.58 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[RAB18]] | -0.57 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[CIZ1]] | -0.57 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[PAQR3]] | -0.57 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[ZDHHC6]] | -0.56 | -0.45 / -0.60 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASD1]] | B | RASD1 activity raises HES1's level | lines that do not express RASD1 (21) vs lines expressing it (29) | 1.21× lower at baseline in the lines without RASD1 | 0.072 | ⚠ within organs, on part of the lines; also absent: MTSS1, TREM1, APOE |
| [[PLK2]] | B | PLK2 activity raises HES1's level | lines that do not express PLK2 (6) vs lines expressing it (44) | 1.62× lower at baseline in the lines without PLK2 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with ZFHX3, POLE |
| [[PMEPA1]] | B | PMEPA1 activity raises HES1's level | lines that do not express PMEPA1 (6) vs lines expressing it (44) | 1.50× lower at baseline in the lines without PMEPA1 | 0.087 | ⚠ within organs, on part of the lines; also absent: SOX4, SLC2A1-DT, ENSG00000285253 |
| [[MAML2]] | B | MAML2 activity raises HES1's level | lines that do not express MAML2 (8) vs lines expressing it (42) | 1.54× lower at baseline in the lines without MAML2 | 0.093 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| [[PDGFRA]] | B | PDGFRA activity raises HES1's level | compounds that target PDGFRA: 2 of 3 lower it (Ponatinib, c-Kit-IN-1) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.701). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.4, -0.2); signed map (6.6, 27.3). **Vector** length 139, 54.2% of its response variance represented; |z| ≥ 3 in 887 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *immediate early* (control, mean cos +0.63 to 9); *NGF-stimulated transcription* (reactome, mean cos +0.56 to 9); *Nuclear Events (kinase and transcription factor activation)* (reactome, mean cos +0.56 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +8.0 | +11.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +7.0 | +9.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.2 | +7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +1.1 |
|  | [[Thymol (drug)]] 5 µM |  | +2.8 | +2.8 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.5 | +2.5 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -7.6 | -2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.9 | +0.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.7 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -6.7 | -3.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~93% of this change | -6.7 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.6 | -0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.3 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | hes family bHLH transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:194,136,148-194,138,732 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20408, HES-1, bHLHb39; previously HRY |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Hallmark sets | NOTCH_SIGNALING, ESTROGEN_RESPONSE_EARLY, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 24 pathways, smallest: NOTCH2 intracellular domain regulates transcription; RUNX3 regulates NOTCH signaling; Regulation of gene expression in late stage (branching morphogenesis) pancreatic bud precursor cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14469](https://www.uniprot.org/uniprotkb/Q14469) (Transcription factor HES-1):

> Transcriptional repressor of genes that require a bHLH protein for their transcription. May act as a negative regulator of myogenesis by inhibiting the functions of MYOD1 and ASH1. Binds DNA on N-box motifs: 5'-CACNAG-3' with high affinity and on E-box motifs: 5'-CANNTG-3' with low affinity (By similarity). May play a role in a functional FA core complex response to DNA cross-link damage, being required for the stability and nuclear localization of FA core complex proteins, as well as for …

**Summary**, from NCBI Gene [3280](https://www.ncbi.nlm.nih.gov/gene/3280):

> This protein belongs to the basic helix-loop-helix family of transcription factors. It is a transcriptional repressor of genes that require a bHLH protein for their transcription. The protein has a particular type of basic domain that contains a helix interrupting protein that binds to the N-box rather than the canonical E-box. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5192](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5192) · Entrez [3280](https://www.ncbi.nlm.nih.gov/gene/3280) · UniProt [Q14469](https://www.uniprot.org/uniprotkb/Q14469) · Ensembl [ENSG00000114315](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114315)

## Data

Gene col 3538: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3538); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3538, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3538]; `tensor/DDL_lfc|DDL_z.npy` [3538]; `embed/gene_vectors.npy` [3538]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3538 or target_col == 3538). Every well: [[HES1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HES1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
