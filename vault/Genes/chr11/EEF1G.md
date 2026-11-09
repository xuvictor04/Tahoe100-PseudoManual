---
symbol: "EEF1G"
type: "gene"
col: 14896
ensembl_id: "ENSG00000254772"
name: "eukaryotic translation elongation factor 1 gamma"
location: "11q12.3"
module: 43
arm: "+"
pooled_cpm: 248.84
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# EEF1G

*eukaryotic translation elongation factor 1 gamma* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.37× (z +12.6, q 2e-33, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.84× (z +6.3, q 4e-08, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.589× (z -7.8, q 4e-12, down in 41 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 14 lines (SNU-1 0.264×, C-33 A 0.319×, LS 180 0.352×, NCI-H23 0.356×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LS 180 0.411×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL29]] (+0.87, fdr 7e-06), [[RPL7]] (+0.85, fdr 7e-06), [[RPS4X]] (+0.84, fdr 7e-06); moves opposite to [[ZNF518A]] (-0.57, fdr 2e-05), [[MIS12]] (-0.56, fdr 1e-05), [[SLC35A4]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → [[NPM1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14896.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.37×** | +12.6 | 2e-33 | 49/49 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.81×** | +10.3 | 3e-22 | 43/44 (SHP-77, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.12×** | +7.2 | 1e-10 | 44/45 (KATO III, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.84×** | +6.3 | 4e-08 | 48/48 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.79×** | +6.0 | 2e-07 | 48/48 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +5.2 | 2e-05 | 0/50 | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.64×** | +5.1 | 2e-05 | 45/48 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.65×** | +4.9 | 7e-05 | 46/48 (KATO III, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.56×** | +4.4 | 7e-04 | 38/47 (SHP-77, COLO 205, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.007 | 35/48 (C32, KATO III, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.010 | 28/49 (NCI-H2347, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.99×** | +3.7 | 0.010 | 39/45 (HT-29, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.53×** | +3.2 | 0.071 | 34/47 (SNU-1, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.52×** | +3.1 | 0.071 | 37/48 (RKO, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.071 | 26/50 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14896.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 14 lines (SNU-1 0.264×, C-33 A 0.319×, LS 180 0.352×, NCI-H23 0.356×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LS 180 0.411×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.589×** | -7.8 | 4e-12 | 41/48 (SNU-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14896. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 296 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -15.5) |
| [[AsPC-1 (line)]] | alt | 203 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 241 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 331 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +12.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -11.0) |
| [[KATO III (line)]] | alt | 225 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +12.4) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 359 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -11.5) |
| [[LS 180 (line)]] | wt | 300 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -14.2) |
| [[NCI-H460 (line)]] | wt | 241 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -9.4) |
| [[SHP-77 (line)]] | alt | 177 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.02× (z +12.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -10.6) |
| [[SW480 (line)]] | alt | 302 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -12.0) |
| [[A-427 (line)]] | wt | 330 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.89× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -10.3) |
| [[A498 (line)]] | wt | 147 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +10.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 284 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.66× (z +12.0) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 195 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 213 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 261 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +10.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 251 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +10.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 168 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.12× (z +10.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 353 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +13.1) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 291 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 177 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.77× (z +12.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 160 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +10.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 275 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.19× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -13.1) |
| [[Panc 03.27 (line)]] | alt | 308 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +12.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 415 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -10.6) |
| [[SNU-423 (line)]] | alt | 332 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +11.4) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 163 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +10.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 128 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +10.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 342 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -9.3) |
| [[BT-474 (line)]] | alt | 145 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -9.3) |
| [[C32 (line)]] | wt | 136 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +9.0) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 226 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +9.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 253 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +8.5) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 100.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.54× (z +11.6) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 229 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +10.0) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 205 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +9.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 195 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 341 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +11.0) | — |
| [[PANC-1 (line)]] | alt | 250 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +9.6) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 115 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 85.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 364 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -17.4) |
| [[SW1417 (line)]] | alt | 277 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 454 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 302 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 249 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 176 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14896), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 14 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL29]] | +0.87 | +0.89 / +0.82 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 889 |
| [[RPL7]] | +0.85 | +0.85 / +0.82 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 950 |
| [[RPS4X]] | +0.84 | +0.84 / +0.82 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 982 |
| [[RPL14]] | +0.84 | +0.78 / +0.83 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 939 |
| [[RACK1]] | +0.83 | +0.85 / +0.80 | both halves | 7e-06 | STRING 994 |
| [[SLC25A6]] | +0.82 | +0.81 / +0.80 | both halves | 7e-06 | STRING 495 |
| [[RPLP0]] | +0.81 | +0.78 / +0.80 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 996 |
| [[RPL13A]] | +0.80 | +0.84 / +0.74 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 969 |
| [[RPS20]] | +0.79 | +0.76 / +0.78 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 949 |
| [[RPL11]] | +0.77 | +0.77 / +0.76 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 987 |
| [[RPL3]] | +0.76 | +0.82 / +0.68 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 968 |
| [[RPL27A]] | +0.76 | +0.73 / +0.72 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 870 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF518A]] | -0.57 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[MIS12]] | -0.56 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[SLC35A4]] | -0.54 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[ZC3H7B]] | -0.54 | -0.56 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPM1]] | C | EEF1G's natural level weakens NPM1's drug response | EEF1G's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.15; direction not clear | 0.043 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[EEF2]] | C | EEF1G's natural level weakens EEF2's drug response | EEF1G's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.64, reverse -0.04; direction not clear | 0.048 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[RPL27A]] | C | EEF1G's natural level strengthens RPL27A's drug response | EEF1G's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse -0.28; direction not clear | 0.089 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.722). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-46.2, -30.0); signed map (-61.0, -6.7). **Vector** length 105, 50.0% of its response variance represented; |z| ≥ 3 in 736 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Peptide chain elongation* (reactome, mean cos +0.66 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.66 to 53); *Nonsense Mediated Decay (NMD) independent of the Exon Junction Complex (EJC)* (reactome, mean cos +0.66 to 52).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.4 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.9 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.5 | +6.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.0 | +3.7 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +1.2 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.9 | -0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +0.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.6 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.8 | -7.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.3 | -2.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.0 | -2.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -0.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.2 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -1.4 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -2.7 | -0.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.4 | -0.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.4 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation elongation factor 1 gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,559,596-62,574,086 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EF1G |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Reactome | 5 pathways, smallest: Signaling by ALK fusions and activated point mutants; Signaling by ALK in cancer; Eukaryotic Translation Elongation |
| Matched by | ensembl_id |

**Function**, from UniProt [P26641](https://www.uniprot.org/uniprotkb/P26641) (Elongation factor 1-gamma):

> Probably plays a role in anchoring the complex to other cellular components.

**Summary**, from NCBI Gene [1937](https://www.ncbi.nlm.nih.gov/gene/1937):

> This gene encodes a subunit of the elongation factor-1 complex, which is responsible for the enzymatic delivery of aminoacyl tRNAs to the ribosome. This subunit contains an N-terminal glutathione transferase domain, which may be involved in regulating the assembly of multisubunit complexes containing this elongation factor and aminoacyl-tRNA synthetases. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3213](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3213) · Entrez [1937](https://www.ncbi.nlm.nih.gov/gene/1937) · UniProt [P26641](https://www.uniprot.org/uniprotkb/P26641) · Ensembl [ENSG00000254772](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254772)

## Data

Gene col 14896: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14896); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14896, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14896]; `tensor/DDL_lfc|DDL_z.npy` [14896]; `embed/gene_vectors.npy` [14896]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14896 or target_col == 14896). Every well: [[EEF1G — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EEF1G.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
