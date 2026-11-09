---
symbol: "KCTD2"
type: "gene"
col: 11145
ensembl_id: "ENSG00000180901"
name: "potassium channel tetramerization domain containing 2"
location: "17q25.1"
module: 30
arm: "+"
pooled_cpm: 18.77
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# KCTD2

*potassium channel tetramerization domain containing 2* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.36× (z +24.1, q 0e+00, up in 29 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.61× (z +9.8, q 2e-20, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.714× (z -6.7, q 1e-08, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.312×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-172 0.276×; ⚠ cell-cycle shift, explains ~13% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.282×).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTC1]] (+0.59, fdr 3e-04), [[TMEM219]] (+0.58, fdr 4e-05), [[ZC3H3]] (+0.57, fdr 6e-05); moves opposite to [[GSTCD]] (-0.50, fdr 4e-05), [[THRB]] (-0.45, fdr 1e-04), [[MYCBP2]] (-0.44, fdr 3e-04).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11145.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.36×** | +24.1 | 0e+00 | 29/35 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +17.8 | 0e+00 | 34/41 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +12.3 | 2e-32 | 29/38 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.61×** | +9.8 | 2e-20 | 33/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +8.9 | 5e-17 | 29/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +5.5 | 3e-06 | 23/47 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.61×** | +5.1 | 2e-05 | 22/48 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.41×** | +5.1 | 3e-05 | 21/46 (SK-MEL-2, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.27×** | +4.8 | 9e-05 | 15/45 (HOP62, H4, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.4 | 6e-04 | 8/35 (A549, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.20× | +3.5 | 0.020 | 14/44 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.5 | 0.023 | 13/47 (H4, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.025 | 16/48 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.13× | +3.4 | 0.025 | 7/48 (MIA PaCa-2, RKO, …) | top dose only | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +3.3 | 0.035 | 8/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.053 | 5/48 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.16× | +3.1 | 0.068 | 10/47 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.16× | +2.9 | 0.095 | 5/46 (KATO III, H4, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11145.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.312×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-172 0.276×; ⚠ cell-cycle shift, explains ~13% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.282×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.714×** | -6.7 | 1e-08 | 21/48 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.805×** | -4.4 | 0.004 | 18/46 (A-172, HEC-1-A, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.839× | -3.5 | 0.078 | 8/47 (NCI-H460, A-172, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.849× | -3.3 | 0.13 | 12/47 (COLO 205, CHP-212, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.851× | -3.3 | 0.13 | 8/47 (A-172, A-427, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.861× | -3.1 | 0.17 | 13/47 (A-172, RPMI-7951, …) | rises with dose |  |
| [[Pyridoxine (drug)]] 5 µM |  | 0.903× | -3.0 | 0.20 | 5/48 (Hs 766T, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11145. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 29.8 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -10.3) |
| [[LoVo (line)]] | wt | 13.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 7.33× (z +13.2) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 26.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.45× (z +15.0) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 21.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.45× (z +12.2) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 13.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.90× (z +11.1) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 22.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.14× (z +14.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 15.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.60× (z +11.4) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 20.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.37× (z +18.2) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 30.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.03× (z +12.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 20.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AsPC-1 (line)]] | alt | 14.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.3× (z +12.1) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 16.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.98× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 20.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.32× (z +10.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 22.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.88× (z +11.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 12.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.13× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 12.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.32× (z +9.1) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 20.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +9.1) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 18.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.40× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -9.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 16.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.25× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 19.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +9.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 65.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11145), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 12 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTC1]] | +0.59 | +0.28 / +0.63 | both halves | 3e-04 |  |
| [[TMEM219]] | +0.58 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[ZC3H3]] | +0.57 | +0.39 / +0.63 | both halves | 6e-05 |  |
| [[IFT52]] | +0.56 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[DNAL1]] | +0.54 | +0.33 / +0.51 | both halves | 1e-04 |  |
| [[MAPK3]] | +0.54 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[PPP1R12C]] | +0.53 | +0.29 / +0.52 | both halves | 2e-04 |  |
| [[EXOC3]] | +0.53 | +0.44 / +0.40 | both halves | 5e-05 |  |
| [[VPS16]] | +0.53 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[E4F1]] | +0.53 | +0.43 / +0.53 | both halves | 4e-05 |  |
| [[TCEA2]] | +0.52 | +0.36 / +0.53 | both halves | 9e-05 |  |
| [[ABHD8]] | +0.52 | +0.50 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSTCD]] | -0.50 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[THRB]] | -0.45 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[MYCBP2]] | -0.44 | -0.29 / -0.42 | both halves | 3e-04 |  |
| [[E2F3]] | -0.43 | -0.33 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KCTD2's level | compounds that target TOP2A: 2 of 5 lower it (Doxorubicin, Epirubicin) | 40% of the class's compounds vs 0.6% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[THRB]] | B | THRB activity lowers KCTD2's level | lines that do not express THRB (21) vs lines expressing it (29) | 1.09× higher at baseline in the lines without THRB | 0.097 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.404). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-4.6, 27.6); signed map (-30.5, -2.7). **Vector** length 69.7, 10.8% of its response variance represented; |z| ≥ 3 in 823 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.0 | +17.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.7 | +24.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +12.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.3 | +5.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +0.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +3.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.5 | +2.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | -3.9 | -3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -3.8 | -4.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -6.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -2.5 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | +0.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | -1.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.4 | -1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | potassium channel tetramerization domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,032,575-75,065,889 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0176 |
| Gene groups (HGNC) | BTB domain containing; KCTD family |
| Matched by | ensembl_id |

UniProt [Q14681](https://www.uniprot.org/uniprotkb/Q14681) carries no function annotation.

**Summary**, from NCBI Gene [23510](https://www.ncbi.nlm.nih.gov/gene/23510):

> Predicted to enable cullin family protein binding activity. Predicted to be involved in proteasome-mediated ubiquitin-dependent protein catabolic process. Predicted to be part of Cul3-RING ubiquitin ligase complex. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21294](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21294) · Entrez [23510](https://www.ncbi.nlm.nih.gov/gene/23510) · UniProt [Q14681](https://www.uniprot.org/uniprotkb/Q14681) · Ensembl [ENSG00000180901](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180901)

## Data

Gene col 11145: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11145); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11145, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11145]; `tensor/DDL_lfc|DDL_z.npy` [11145]; `embed/gene_vectors.npy` [11145]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11145 or target_col == 11145). Every well: [[KCTD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCTD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
