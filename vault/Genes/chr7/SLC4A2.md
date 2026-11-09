---
symbol: "SLC4A2"
type: "gene"
col: 9021
ensembl_id: "ENSG00000164889"
name: "solute carrier family 4 member 2"
location: "7q36.1"
module: 138
arm: "+"
pooled_cpm: 26.09
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 5
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# SLC4A2

*solute carrier family 4 member 2* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.87× (z +9.1, q 5e-17, up in 35 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.43× (z +7.3, q 3e-11, up in 26 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.650× (z -6.3, q 2e-07, down in 32 of 48 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (Hs 766T 0.278×, LS 180 0.365×; ⚠ cell-cycle shift, explains ~29% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.158×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.105×); [[Loperamide (hydrochloride) (drug)]] 0.05 µM in 1 line (AN3 CA 0.0961×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRTC2]] (+0.64, fdr 9e-06), [[RIPOR1]] (+0.63, fdr 7e-06), [[MBD6]] (+0.62, fdr 7e-06); moves opposite to [[SPCS1]] (-0.63, fdr 1e-05), [[BBLN]] (-0.55, fdr 2e-05), [[SENP5]] (-0.53, fdr 1e-05).
> It is in [[Module 138]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9021.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +9.1 | 5e-17 | 35/43 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +8.5 | 5e-15 | 27/34 (J82, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +7.7 | 2e-12 | 30/40 (KATO III, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.67×** | +7.5 | 1e-11 | 35/48 (NCI-H460, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +7.3 | 3e-11 | 26/47 (A498, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.64×** | +6.9 | 5e-10 | 34/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.35×** | +6.1 | 9e-08 | 27/48 (RKO, C32, …) | top dose only | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +5.3 | 1e-05 | 26/47 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.84×** | +4.6 | 2e-04 | 22/48 (NCI-H460, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.39×** | +4.6 | 3e-04 | 22/48 (PANC-1, C32, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +4.5 | 4e-04 | 24/46 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.52×** | +4.3 | 7e-04 | 20/46 (RKO, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.73×** | +4.2 | 0.001 | 21/48 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +4.1 | 0.001 | 19/48 (PANC-1, LoVo, …) | inconsistent across doses | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.71×** | +4.1 | 0.002 | 21/46 (Hs 766T, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.015 | 19/45 (NCI-H460, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.017 | 11/48 (HOP62, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.58×** | +3.5 | 0.017 | 18/48 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.019 | 15/48 (SW480, HCT15, …) | inconsistent across doses | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.019 | 11/48 (LoVo, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.022 | 10/48 (BT-474, KATO III, …) | inconsistent across doses | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.039 | 11/48 (HS-578T, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Carbamazepine (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.041 | 7/48 (SNU-423, A-172, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9021.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (Hs 766T 0.278×, LS 180 0.365×; ⚠ cell-cycle shift, explains ~29% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.158×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.105×); [[Loperamide (hydrochloride) (drug)]] 0.05 µM in 1 line (AN3 CA 0.0961×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.650×** | -6.3 | 2e-07 | 32/48 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.705×** | -5.1 | 1e-04 | 29/48 (NCI-H23, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.789×** | -4.9 | 2e-04 | 23/47 (Hs 766T, LS 180, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.764×** | -3.9 | 0.012 | 22/48 (NCI-H23, A-427, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.784×** | -3.4 | 0.073 | 19/47 (Hs 766T, C-33 A, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9021. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 36.3 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.5) | — |
| [[A498 (line)]] | wt | 46.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +14.1) | — |
| [[HepG2_C3A (line)]] | wt | 15.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +10.0) | [[Canagliflozin (drug)]] 0.05 µM 0.105× (z -9.1) |
| [[Hs 766T (line)]] | wt | 37.4 | 0 | 2 (1 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.158× (z -12.9) |
| [[J82 (line)]] | alt | 20.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.82× (z +11.1) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 22.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.04× (z +11.0) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 20.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.90× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 23.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +8.5) | — |
| [[A-427 (line)]] | wt | 24.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 20.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +11.5) | — |
| [[AN3 CA (line)]] | alt | 31.6 | 0 | 1 | — | [[Loperamide (hydrochloride) (drug)]] 0.05 µM 0.0961× (z -8.8) |
| [[LS 180 (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -9.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H1573 (line)]] | alt | 9.42 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.20× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 17.4 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.63× (z +11.9) ⚠ unreliable plate only | — |
| [[SNU-423 (line)]] | alt | 28.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +10.5) | — |
| [[SW 900 (line)]] | alt | 26.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +9.2) | — |
| [[SW48 (line)]] | wt | 26.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -8.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 90.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9021), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRTC2]] | +0.64 | +0.72 / +0.57 | both halves | 9e-06 |  |
| [[RIPOR1]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[MBD6]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[PRR14]] | +0.62 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[SYNGAP1]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[WIZ]] | +0.60 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[MTSS2]] | +0.59 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[MED16]] | +0.59 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[ATXN2L]] | +0.58 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[DVL2]] | +0.58 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[PLXNB2]] | +0.57 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[VARS2]] | +0.57 | +0.51 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPCS1]] | -0.63 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[BBLN]] | -0.55 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[SENP5]] | -0.53 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[UQCRQ]] ⚠ | -0.53 | -0.47 / -0.51 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ROMO1]] | -0.53 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[ARPC1B]] | -0.51 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[RABGEF1P1]] | -0.51 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[COX6A1]] | -0.51 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[SH3BGRL3]] | -0.51 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[SEC61G]] | -0.51 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[MAP2K1]] | -0.50 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[CHIC2]] | -0.50 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[LINC03009-1]] | -0.49 | -0.56 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SLC4A2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.604). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.4, -26.4); signed map (4.9, -7.7). **Vector** length 102, 24.1% of its response variance represented; |z| ≥ 3 in 817 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.3 | +7.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.0 | +6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +7.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +5.0 | +0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +4.9 | +6.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.1 | +4.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.9 | +4.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.5 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +4.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.3 | -4.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -2.1 | -6.3 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.2 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -2.0 | -1.3 |
|  | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | -1.9 | -1.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.9 | -2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 4 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:151,057,210-151,076,526 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HKB3, BND3L, NBND3; previously EPB3L1, AE2 |
| Gene groups (HGNC) | Solute carrier family 4 |
| Reactome | 4 pathways, smallest: Bicarbonate transporters; SLC-mediated transport of inorganic anions; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P04920](https://www.uniprot.org/uniprotkb/P04920) (Anion exchange protein 2):

> Sodium-independent anion exchanger which mediates the electroneutral exchange of chloride for bicarbonate ions across the cell membrane. Plays an important role in osteoclast differentiation and function. Regulates bone resorption and calpain-dependent actin cytoskeleton organization in osteoclasts via anion exchange-dependent control of pH (By similarity). Essential for intracellular pH regulation in CD8(+) T-cells upon CD3 stimulation, modulating CD8(+) T-cell responses (By similarity).

**Summary**, from NCBI Gene [6522](https://www.ncbi.nlm.nih.gov/gene/6522):

> This gene encodes a member of the anion exchanger family of membrane transport proteins. The encoded protein regulates intracellular pH, biliary bicarbonate secretion, and chloride uptake. Reduced expression of this gene may be associated with primary biliary cirrhosis (PBC) in human patients, while differential expression of this gene may be associated with malignant hepatocellular carcinoma, colon and gastric cancers. [provided by RefSeq, Nov 2016]

**Accessions** — [HGNC:11028](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11028) · Entrez [6522](https://www.ncbi.nlm.nih.gov/gene/6522) · UniProt [P04920](https://www.uniprot.org/uniprotkb/P04920) · Ensembl [ENSG00000164889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164889)

## Data

Gene col 9021: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9021); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9021, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9021]; `tensor/DDL_lfc|DDL_z.npy` [9021]; `embed/gene_vectors.npy` [9021]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9021 or target_col == 9021). Every well: [[SLC4A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC4A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
