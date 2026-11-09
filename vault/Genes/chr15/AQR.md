---
symbol: "AQR"
type: "gene"
col: 330
ensembl_id: "ENSG00000021776"
name: "aquarius intron-binding spliceosomal factor"
location: "15q14"
module: 49
arm: "+"
pooled_cpm: 124.17
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# AQR

*aquarius intron-binding spliceosomal factor* — 15q14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 4.15× (z +14.0, q 6e-42, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.763× (z -8.1, q 4e-13, down in 30 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (KATO III 0.476×, A549 0.514×, LoVo 0.603×, HT-29 0.560×, …); [[Dinaciclib (drug)]] 5 µM in 5 lines (Panc 03.27 0.298×, A-172 0.416×, HEC-1-A 0.469×, CFPAC-1 0.447×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (J82 0.442×, CFPAC-1 0.448×; ⚠ toxic; transcription drop); [[Omeprazole (drug)]] 0.5 µM in 1 line (SW 1088 0.0656×); [[XRK3F2 (drug)]] 0.5 µM in 1 line (SW 1271 0.0948×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UTP6]] (+0.64, fdr 1e-05), [[PRPF3]] (+0.63, fdr 7e-06), [[TMEM161B]] (+0.60, fdr 1e-05); moves opposite to [[DENND5B]] (-0.55, fdr 6e-05), [[MAFG]] (-0.52, fdr 3e-05), [[HIVEP1]] (-0.50, fdr 8e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 330.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.15×** | +14.0 | 6e-42 | 47/49 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.31×** | +11.8 | 1e-29 | 47/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +8.7 | 6e-16 | 34/48 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +8.2 | 3e-14 | 41/48 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +5.8 | 9e-07 | 32/48 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.28×** | +5.2 | 2e-05 | 29/48 (A-172, LoVo, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.26×** | +4.9 | 7e-05 | 26/48 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.52×** | +4.2 | 0.002 | 37/49 (A498, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.18× | +3.5 | 0.028 | 21/48 (LoVo, SNU-1, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.5 | 0.029 | 20/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.4 | 0.034 | 19/48 (LoVo, AsPC-1, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.18× | +3.3 | 0.048 | 22/47 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.074 | 17/49 (HEC-1-A, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 330.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (KATO III 0.476×, A549 0.514×, LoVo 0.603×, HT-29 0.560×, …); [[Dinaciclib (drug)]] 5 µM in 5 lines (Panc 03.27 0.298×, A-172 0.416×, HEC-1-A 0.469×, CFPAC-1 0.447×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (J82 0.442×, CFPAC-1 0.448×; ⚠ toxic; transcription drop); [[Omeprazole (drug)]] 0.5 µM in 1 line (SW 1088 0.0656×); [[XRK3F2 (drug)]] 0.5 µM in 1 line (SW 1271 0.0948×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.763×** | -8.1 | 4e-13 | 30/49 (KATO III, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.713×** | -6.6 | 1e-08 | 27/45 (J82, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.746×** | -5.9 | 5e-07 | 28/44 (Panc 03.27, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.758×** | -5.8 | 8e-07 | 28/49 (SW1417, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~9% of this change | **0.818×** | -4.2 | 0.003 | 25/48 (NCI-H661, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.773×** | -3.9 | 0.010 | 27/48 (CHP-212, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -3.7 | 0.020 | 21/48 (AN3 CA, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 330. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 194 | 4 (1 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.98× (z +14.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 130 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.51× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.469× (z -10.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 79.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.29× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.416× (z -11.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 87.7 | 3 | 1 | [[TAK-901 (drug)]] 0.05 µM 2.30× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.597× (z -8.5) |
| [[HT-29 (line)]] | alt | 139 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -11.0) |
| [[SW1417 (line)]] | alt | 153 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.34× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.451× (z -10.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 133 | 3 | 1 | [[TAK-901 (drug)]] 5 µM 6.90× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.658× (z -9.9) |
| [[C-33 A (line)]] | alt | 148 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.50× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.419× (z -9.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 145 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.92× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.447× (z -10.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 155 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 6.75× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -14.2) |
| [[RKO (line)]] | wt | 134 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +14.2) | — |
| [[A549 (line)]] | wt | 182 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 5.96× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -13.1) |
| [[COLO 205 (line)]] | alt | 141 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 15.8× (z +14.4) | — |
| [[HOP62 (line)]] | alt | 107 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.16× (z +10.9) | — |
| [[Hs 766T (line)]] | wt | 92.2 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.91× (z +11.1) | — |
| [[LOX-IMVI (line)]] | wt | 130 | 2 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.72× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 133 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 9.17× (z +11.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 109 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.24× (z +10.7) | — |
| [[Panc 03.27 (line)]] | alt | 119 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.86× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -14.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 141 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 4.55× (z +10.6) | — |
| [[SW 1271 (line)]] | alt | 120 | 0 | 2 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0948× (z -8.9) |
| [[A-427 (line)]] | wt | 84.6 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 5.19× (z +8.7) | — |
| [[A498 (line)]] | wt | 95.2 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 1.79× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 133 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -8.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 184 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -8.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 145 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.97× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 122 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -9.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.442× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 145 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.491× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 138 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.17× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 113 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.20× (z +10.9) | — |
| [[NCI-H661 (line)]] | alt | 146 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.182× (z -10.2) ⚠ transcription drop; cell-cycle shift, explains ~9% of this change |
| [[SHP-77 (line)]] | alt | 138 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.38× (z +10.6) | — |
| [[SW 1088 (line)]] | alt | 85.5 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0656× (z -9.8) |
| [[SW48 (line)]] | wt | 141 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -9.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 95.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 121 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 330), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP6]] | +0.64 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[PRPF3]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[TMEM161B]] | +0.60 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[LONP2]] | +0.59 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[NUP214]] | +0.57 | +0.59 / +0.44 | both halves | 3e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[AGK]] | +0.57 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[CNOT7]] | +0.56 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[MED23]] | +0.56 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[MRPL3]] | +0.56 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[NOL10]] | +0.55 | +0.49 / +0.51 | both halves | 2e-05 |  |
| [[NUP160]] | +0.55 | +0.48 / +0.57 | both halves | 2e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 442 |
| [[SMARCAD1]] | +0.54 | +0.56 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND5B]] | -0.55 | -0.57 / -0.38 | both halves | 6e-05 |  |
| [[MAFG]] | -0.52 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[HIVEP1]] | -0.50 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[B3GALNT2]] | -0.48 | -0.51 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[UPK2]] | -0.48 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[KLHL21]] | -0.46 | -0.37 / -0.46 | both halves | 7e-05 |  |
| [[GLIS2]] | -0.46 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[ERF]] | -0.45 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[RNASEK]] | -0.45 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[STX11]] | -0.45 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[DEGS1]] | -0.45 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers AQR's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.378). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-30.4, -7.9); signed map (-34.6, -24.6). **Vector** length 88.0, 23.5% of its response variance represented; |z| ≥ 3 in 923 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.1 | +14.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +11.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.5 | +8.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +5.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +3.3 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +1.7 | +3.1 |
|  | [[EX229 (drug)]] 5 µM |  | +1.6 | +1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.6 | +4.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -8.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.2 | -0.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | +2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | +1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | +0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | +0.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[Neratinib (drug)]] 5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | aquarius intron-binding spliceosomal factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q14 — chr15:34,851,782-34,969,742 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0560, fSAP164, IBP160 |
| Gene groups (HGNC) | UPF1 like RNA helicases; Spliceosomal B complex; Spliceosomal Bact complex; Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 13 pathways, smallest: Formation of TC-NER Pre-Incision Complex; Gap-filling DNA repair synthesis and ligation in TC-NER; Dual incision in TC-NER |
| Matched by | ensembl_id |

**Function**, from UniProt [O60306](https://www.uniprot.org/uniprotkb/O60306) (RNA helicase aquarius):

> Involved in pre-mRNA splicing as component of the spliceosome. Intron-binding spliceosomal protein required to link pre-mRNA splicing and snoRNP (small nucleolar ribonucleoprotein) biogenesis. Plays a key role in position-dependent assembly of intron-encoded box C/D small snoRNP, splicing being required for snoRNP assembly. May act by helping the folding of the snoRNA sequence. Binds to intron of pre-mRNAs in a sequence-independent manner, contacting the region between snoRNA and the …

**Summary**, from NCBI Gene [9716](https://www.ncbi.nlm.nih.gov/gene/9716):

> Enables 3'-5' RNA helicase activity and single-stranded RNA binding activity. Involved in mRNA splicing, via spliceosome. Located in nucleoplasm. Part of U2-type catalytic step 2 spliceosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29513](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29513) · Entrez [9716](https://www.ncbi.nlm.nih.gov/gene/9716) · UniProt [O60306](https://www.uniprot.org/uniprotkb/O60306) · Ensembl [ENSG00000021776](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000021776)

## Data

Gene col 330: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 330); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 330, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 330]; `tensor/DDL_lfc|DDL_z.npy` [330]; `embed/gene_vectors.npy` [330]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 330 or target_col == 330). Every well: [[AQR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AQR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
