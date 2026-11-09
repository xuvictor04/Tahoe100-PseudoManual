---
symbol: "HSBP1"
type: "gene"
col: 13774
ensembl_id: "ENSG00000230989"
name: "heat shock factor binding protein 1"
location: "16q23.3"
module: 48
arm: "+"
pooled_cpm: 38.99
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# HSBP1

*heat shock factor binding protein 1* — 16q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.38× (z +12.8, q 5e-35, up in 45 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.57× (z +3.9, q 0.008, up in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (HOP62 6.00×, NCI-H460 6.21×, C32 7.09×, NCI-H1573 9.16×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (LoVo 7.02×, HOP62 5.19×, SW480 5.29×, C32 5.96×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.711× (z -4.2, q 0.014, down in 27 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SHP-77 0.393×, MIA PaCa-2 0.321×, A-427 0.356×); [[Bestatin (drug)]] 5 µM in 1 line (NCI-H661 0.0497×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEDD8]] (+0.68, fdr 7e-06), [[ATP5PF]] (+0.61, fdr 1e-05), [[EMC4]] (+0.60, fdr 1e-05); moves opposite to [[TIMM44]] (-0.54, fdr 2e-05), [[CIRBP]] (-0.53, fdr 2e-04), [[EXOSC8]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13774.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (HOP62 6.00×, NCI-H460 6.21×, C32 7.09×, NCI-H1573 9.16×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (LoVo 7.02×, HOP62 5.19×, SW480 5.29×, C32 5.96×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **4.38×** | +12.8 | 5e-35 | 45/45 (HOP62, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **4.25×** | +12.1 | 3e-31 | 37/37 (LoVo, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.67×** | +7.9 | 6e-13 | 39/43 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.81×** | +5.2 | 3e-05 | 38/48 (NCI-H460, PANC-1, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +5.0 | 6e-05 | 38/45 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **1.59×** | +4.0 | 0.005 | 28/47 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +3.9 | 0.008 | 34/48 (HOP62, A-172, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.36×** | +3.8 | 0.011 | 28/47 (A549, NCI-H2347, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.52×** | +3.5 | 0.034 | 31/48 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +3.4 | 0.040 | 0/48 | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.49×** | +3.3 | 0.047 | 30/48 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | 1.44× | +3.0 | 0.11 | 28/48 (SNU-423, AN3 CA, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13774.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SHP-77 0.393×, MIA PaCa-2 0.321×, A-427 0.356×); [[Bestatin (drug)]] 5 µM in 1 line (NCI-H661 0.0497×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.711×** | -4.2 | 0.014 | 27/47 (SHP-77, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.643× | -3.3 | 0.25 | 30/48 (C32, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13774. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 45.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.33× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -8.8) |
| [[HOP62 (line)]] | alt | 45.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 32.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.62× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -9.8) |
| [[SHP-77 (line)]] | alt | 70.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -9.9) |
| [[A-172 (line)]] | wt | 56.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A549 (line)]] | wt | 32.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.92× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[C32 (line)]] | wt | 35.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.09× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[Hs 766T (line)]] | wt | 33.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 32.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.26× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[KATO III (line)]] | alt | 61.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LoVo (line)]] | wt | 30.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.02× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LOX-IMVI (line)]] | wt | 33.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.91× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1573 (line)]] | alt | 27.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.16× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1792 (line)]] | alt | 39.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.77× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H460 (line)]] | wt | 29.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.21× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[Panc 03.27 (line)]] | alt | 26.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.83× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[PANC-1 (line)]] | alt | 28.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.91× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SNU-423 (line)]] | alt | 31.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.41× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW480 (line)]] | alt | 32.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.29× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A498 (line)]] | wt | 58.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[C-33 A (line)]] | alt | 37.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[CFPAC-1 (line)]] | alt | 33.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HCT15 (line)]] | alt | 35.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.27× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HEC-1-A (line)]] | alt | 42.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HS-578T (line)]] | alt | 58.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 41.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.53× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[J82 (line)]] | alt | 30.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LS 180 (line)]] | wt | 35.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2030 (line)]] | alt | 87.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H661 (line)]] | alt | 32.5 | 0 | 1 | — | [[Bestatin (drug)]] 5 µM 0.0497× (z -9.5) |
| [[RKO (line)]] | wt | 47.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[RPMI-7951 (line)]] | alt | 49.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.57× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW 900 (line)]] | alt | 36.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[AN3 CA (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13774), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 8 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEDD8]] | +0.68 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[ATP5PF]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[EMC4]] | +0.60 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[NDUFA4]] | +0.56 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[UBL5]] | +0.55 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[TIMP1]] | +0.54 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[PRDX1]] | +0.54 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[POLR2K]] | +0.53 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[SRP14]] | +0.53 | +0.41 / +0.65 | both halves | 4e-05 |  |
| [[ITM2C]] | +0.52 | +0.48 / +0.35 | both halves | 1e-04 |  |
| [[UQCRQ]] ⚠ | +0.51 | +0.53 / +0.49 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MTPN]] | +0.51 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[CD59]] | +0.51 | +0.52 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM44]] | -0.54 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[CIRBP]] | -0.53 | -0.55 / -0.30 | both halves | 2e-04 |  |
| [[EXOSC8]] | -0.51 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[CCT6P3]] | -0.51 | -0.51 / -0.28 | both halves | 3e-04 |  |
| [[RNF214]] | -0.50 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[RSL1D1]] | -0.50 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[SAFB]] | -0.48 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[AAAS]] | -0.47 | -0.53 / -0.36 | both halves | 9e-05 | pathway: Cellular response to heat stress |
| [[PRPF39]] | -0.47 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[LARS1]] | -0.47 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[GLOD4]] | -0.46 | -0.31 / -0.34 | both halves | 2e-04 |  |
| [[DXO]] | -0.46 | -0.43 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HSBP1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.505). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-22.0, -47.5); signed map (-36.3, 10.7). **Vector** length 51.0, 12.0% of its response variance represented; |z| ≥ 3 in 585 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +1.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | +2.9 | +5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | +2.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.1 | +1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +0.9 | -0.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +0.9 | +0.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -2.9 | -4.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -0.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -2.3 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -2.3 | +7.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.9 | -0.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.7 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | +0.4 |
|  | [[EX229 (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.6 | +1.2 |

## What is on record

|  |  |
|---|---|
| Name | heat shock factor binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.3 — chr16:83,719,311-83,819,737 (+) |
| Ensembl biotype | protein_coding |
| Reactome | 6 pathways, smallest: Attenuation phase; HSF1 activation; HSF1-dependent transactivation |
| Matched by | ensembl_id |

**Function**, from UniProt [O75506](https://www.uniprot.org/uniprotkb/O75506) (Heat shock factor-binding protein 1):

> Negative regulator of the heat shock response. Negatively affects HSF1 DNA-binding activity. May have a role in the suppression of the activation of the stress response during the aging process.

**Summary**, from NCBI Gene [3281](https://www.ncbi.nlm.nih.gov/gene/3281):

> The heat-shock response is elicited by exposure of cells to thermal and chemical stress and through the activation of HSFs (heat shock factors) results in the elevated expression of heat-shock induced genes. Heat shock factor binding protein 1 (HSBP1), is a 76-amino-acid protein that binds to heat shock factor 1(HSF1), which is a transcription factor involved in the HS response. During HS response, HSF1 undergoes conformational transition from an inert non-DNA-binding monomer to active …

**Accessions** — [HGNC:5203](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5203) · Entrez [3281](https://www.ncbi.nlm.nih.gov/gene/3281) · UniProt [O75506](https://www.uniprot.org/uniprotkb/O75506) · Ensembl [ENSG00000230989](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000230989)

## Data

Gene col 13774: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13774); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13774, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13774]; `tensor/DDL_lfc|DDL_z.npy` [13774]; `embed/gene_vectors.npy` [13774]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13774 or target_col == 13774). Every well: [[HSBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
