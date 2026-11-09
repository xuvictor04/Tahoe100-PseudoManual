---
symbol: "SCAF1"
type: "gene"
col: 4739
ensembl_id: "ENSG00000126461"
name: "SR-related CTD associated factor 1"
location: "19q13.3-q13.4"
module: 173
arm: "+"
pooled_cpm: 26.44
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 9
n_dd_up_clean: 16
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/173"]
generated_by: "tahoemap"
---

# SCAF1

*SR-related CTD associated factor 1* — 19q13.3-q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.60× (z +24.2, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.643× (z -8.1, q 2e-13, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MEPCE]] (+0.80, fdr 7e-06), [[ZNF543]] (+0.79, fdr 7e-06), [[ZNF646]] (+0.79, fdr 7e-06); moves opposite to [[NME2]] (-0.67, fdr 2e-05), [[RPS5]] (-0.64, fdr 1e-05), [[RPS25]] (-0.64, fdr 1e-05).
> It is in [[Module 173]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4739.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.60×** | +24.2 | 0e+00 | 47/47 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.01×** | +12.9 | 2e-35 | 40/47 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.88×** | +11.2 | 7e-27 | 38/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.96×** | +6.5 | 2e-08 | 29/48 (LS 180, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +5.5 | 4e-06 | 27/47 (BT-474, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +5.4 | 7e-06 | 25/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +5.2 | 2e-05 | 22/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +5.1 | 2e-05 | 19/47 (LS 180, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.28×** | +4.5 | 4e-04 | 17/45 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.4 | 7e-04 | 0/48 | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.001 | 16/47 (HOP62, HS-578T, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.003 | 16/48 (NCI-H2347, HT-29, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.003 | 15/48 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.9 | 0.003 | 15/47 (AsPC-1, PANC-1, …) | rises with dose |  |
| [[Pentoxifylline (drug)]] 0.5 µM |  | **1.22×** | +3.7 | 0.009 | 11/48 (A498, Hs 766T, …) | rises with dose | position effect removed |
| [[Pentoxifylline (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.012 | 9/48 (J82, A498, …) | rises with dose | position effect removed |
| [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.017 | 15/47 (SNU-1, A549, …) | inconsistent across doses | position effect removed |
| [[Captopril (drug)]] 0.05 µM |  | **1.20×** | +3.4 | 0.025 | 13/47 (A549, NCI-H2347, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4739.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.643×** | -8.1 | 2e-13 | 38/48 (A-172, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~1% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.681×** | -7.1 | 3e-10 | 30/48 (SW1417, A-172, …) | all doses, flat | cell-cycle shift (explains ~1% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.682×** | -7.1 | 3e-10 | 31/48 (HS-578T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.809×** | -5.4 | 7e-06 | 25/48 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.746×** | -5.4 | 7e-06 | 24/48 (NCI-H1573, BT-474, …) | all doses, flat | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.749×** | -5.3 | 9e-06 | 24/47 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.789×** | -4.2 | 0.002 | 14/47 (CHP-212, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.801×** | -4.1 | 0.003 | 15/47 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.658×** | -4.0 | 0.003 | 14/48 (LoVo, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 0.5 µM |  | 0.845× | -3.1 | 0.099 | 12/46 (HepG2/C3A, MIA PaCa-2, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.846× | -3.1 | 0.10 | 5/48 (LoVo, SW1417, …) | inconsistent across doses | position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | 0.838× | -3.0 | 0.12 | 4/48 (A-172, Hs 766T, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4739. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +17.6) | — |
| [[A-427 (line)]] | wt | 27.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +8.9) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -10.2) ⚠ cell-cycle shift, explains ~20% of this change |
| [[AN3 CA (line)]] | alt | 34.5 | 0 | 2 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0908× (z -9.8) |
| [[C-33 A (line)]] | alt | 44.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 29.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.14× (z +21.5) | — |
| [[LS 180 (line)]] | wt | 17.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.236× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[PANC-1 (line)]] | alt | 18.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +13.5) | — |
| [[A-172 (line)]] | wt | 34.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.4) | — |
| [[A498 (line)]] | wt | 26.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.0) | — |
| [[AsPC-1 (line)]] | alt | 23.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +12.5) | — |
| [[C32 (line)]] | wt | 16.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 23.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.7) | — |
| [[CHP-212 (line)]] | wt | 23.7 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0754× (z -8.7) |
| [[COLO 205 (line)]] | alt | 23.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 43.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 16.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +13.4) | — |
| [[Hs 766T (line)]] | wt | 20.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 27.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +14.0) | — |
| [[HT-29 (line)]] | alt | 44.1 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.135× (z -9.5) ⚠ toxic |
| [[KATO III (line)]] | alt | 31.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.0) | — |
| [[LoVo (line)]] | wt | 31.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +19.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 29.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +13.0) | — |
| [[NCI-H1573 (line)]] | alt | 22.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +14.2) | — |
| [[NCI-H1792 (line)]] | alt | 26.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +15.6) | — |
| [[NCI-H2030 (line)]] | alt | 28.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +16.2) | — |
| [[NCI-H23 (line)]] | alt | 25.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +13.8) | — |
| [[RKO (line)]] | wt | 23.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +10.5) | — |
| [[RPMI-7951 (line)]] | alt | 37.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +12.0) | — |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 17.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +10.9) | — |
| [[SW 900 (line)]] | alt | 26.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +9.3) | — |
| [[SW480 (line)]] | alt | 23.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +11.6) | — |
| [[A549 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4739), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEPCE]] | +0.80 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[ZNF543]] | +0.79 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[ZNF646]] | +0.79 | +0.84 / +0.61 | both halves | 7e-06 |  |
| [[ZC3H4]] | +0.78 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[CELSR3]] | +0.74 | +0.84 / +0.65 | both halves | 7e-06 |  |
| [[C19orf54]] | +0.74 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[FIZ1]] | +0.74 | +0.76 / +0.50 | both halves | 1e-05 |  |
| [[NAIF1]] | +0.73 | +0.77 / +0.42 | both halves | 4e-05 |  |
| [[BRPF3]] | +0.73 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[PEF1]] | +0.72 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[SP2]] | +0.71 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[SRCAP]] | +0.71 | +0.68 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NME2]] | -0.67 | -0.69 / -0.46 | both halves | 2e-05 |  |
| [[RPS5]] | -0.64 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[RPS25]] | -0.64 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[SEC11A]] | -0.64 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[RPS24]] | -0.64 | -0.70 / -0.52 | both halves | 1e-05 |  |
| [[STRN]] | -0.63 | -0.67 / -0.27 | both halves | 3e-04 |  |
| [[UQCRH]] | -0.63 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[RPS21]] | -0.62 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[ATP8A1]] | -0.61 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[PALS2]] | -0.61 | -0.70 / -0.46 | both halves | 2e-05 |  |
| [[METAP1]] | -0.61 | -0.64 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises SCAF1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises SCAF1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 173]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.856). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-10.4, 5.2); signed map (15.0, -22.8). **Vector** length 99.3, 21.7% of its response variance represented; |z| ≥ 3 in 917 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.9 | +24.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.7 | +12.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.6 | +11.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +5.3 | +4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +5.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +0.0 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.3 | -7.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.9 | -8.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.7 | -4.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.4 | -7.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.4 | -5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -5.4 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.3 | -3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | SR-related CTD associated factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.3-q13.4 — chr19:49,642,209-49,658,642 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SR-A1, FLJ00034 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H7N4](https://www.uniprot.org/uniprotkb/Q9H7N4) (Splicing factor, arginine/serine-rich 19):

> May function in pre-mRNA splicing.

**Summary**, from NCBI Gene [58506](https://www.ncbi.nlm.nih.gov/gene/58506):

> Enables RNA polymerase II C-terminal domain binding activity. Predicted to be involved in RNA splicing; mRNA processing; and transcription by RNA polymerase II. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30403](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30403) · Entrez [58506](https://www.ncbi.nlm.nih.gov/gene/58506) · UniProt [Q9H7N4](https://www.uniprot.org/uniprotkb/Q9H7N4) · Ensembl [ENSG00000126461](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126461)

## Data

Gene col 4739: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4739); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4739, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4739]; `tensor/DDL_lfc|DDL_z.npy` [4739]; `embed/gene_vectors.npy` [4739]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4739 or target_col == 4739). Every well: [[SCAF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCAF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
