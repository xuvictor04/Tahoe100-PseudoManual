---
symbol: "DDAH2"
type: "gene"
col: 13131
ensembl_id: "ENSG00000213722"
name: "DDAH family member 2, ADMA-independent"
location: "6p21.33"
module: 5
arm: "-"
pooled_cpm: 22.2
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 22
n_dd_up_clean: 2
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# DDAH2

*DDAH family member 2, ADMA-independent* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.27× (z +10.7, q 6e-24, up in 33 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.44× (z +4.6, q 4e-04, up in 19 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW1417 3.35×, A-172 3.05×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 5.97×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (KATO III 6.43×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.658× (z -7.7, q 8e-12, down in 28 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRIP2]] (+0.66, fdr 1e-05), [[HDAC5]] (+0.64, fdr 1e-05), [[DLGAP4]] (+0.64, fdr 1e-05); moves opposite to [[ALG8]] (-0.63, fdr 3e-05), [[TLCD3A]] (-0.59, fdr 6e-05), [[PRMT3]] (-0.59, fdr 1e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13131.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW1417 3.35×, A-172 3.05×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 5.97×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (KATO III 6.43×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.27×** | +10.7 | 6e-24 | 33/39 (SW1417, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +8.5 | 6e-15 | 25/31 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +6.0 | 3e-07 | 26/43 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +4.7 | 4e-04 | 17/35 (SW1417, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.44×** | +4.6 | 4e-04 | 19/45 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.37×** | +4.1 | 0.004 | 19/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | 1.26× | +3.0 | 0.19 | 9/45 (NCI-H2030, Panc 03.27, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13131.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.658×** | -7.7 | 8e-12 | 28/44 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.582×** | -6.8 | 3e-09 | 24/44 (H4, HT-29, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.596×** | -6.7 | 3e-09 | 33/45 (A498, SW480, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.411×** | -6.1 | 2e-07 | 26/43 (SW 900, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.659×** | -5.4 | 7e-06 | 28/45 (SW48, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.690×** | -4.8 | 1e-04 | 23/45 (Panc 03.27, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.784×** | -4.5 | 7e-04 | 26/46 (NCI-H661, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.715×** | -4.4 | 9e-04 | 22/45 (H4, HOP62, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.717×** | -4.3 | 1e-03 | 22/46 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.708×** | -4.2 | 0.001 | 21/46 (NCI-H2347, H4, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.550×** | -4.1 | 0.002 | 20/46 (A-427, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.747×** | -3.8 | 0.007 | 21/45 (Panc 03.27, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.751×** | -3.6 | 0.016 | 22/45 (SK-MEL-2, HT-29, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.766×** | -3.5 | 0.021 | 16/45 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.756×** | -3.4 | 0.023 | 16/45 (BT-474, SW1417, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.606×** | -3.4 | 0.023 | 14/44 (MIA PaCa-2, PANC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.785×** | -3.1 | 0.056 | 10/45 (BT-474, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.634×** | -3.1 | 0.059 | 10/44 (SW48, PANC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13131. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 22.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 28.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -15.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 52.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -13.0) |
| [[HT-29 (line)]] | alt | 30.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -11.7) |
| [[A-172 (line)]] | wt | 34.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 26.3 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0564× (z -9.4) |
| [[A498 (line)]] | wt | 18.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.260× (z -9.2) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 74.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -9.7) |
| [[BT-474 (line)]] | alt | 22.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 35.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 20.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.97× (z +11.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 20.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -10.2) |
| [[KATO III (line)]] | alt | 15.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.43× (z +10.1) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 22.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -14.5) |
| [[NCI-H2347 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 38.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.99 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13131), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRIP2]] | +0.66 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[HDAC5]] | +0.64 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[DLGAP4]] | +0.64 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[OPTN]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[MAPK8IP1]] | +0.61 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[TPPP]] | +0.60 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[PNPLA2]] | +0.60 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[RAP1GAP]] | +0.59 | +0.51 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[TBC1D17]] | +0.58 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[GNAI2]] | +0.58 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[SPAG9]] | +0.58 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[NBEAL1]] | +0.58 | +0.59 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG8]] | -0.63 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[TLCD3A]] | -0.59 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[PRMT3]] | -0.59 | -0.51 / -0.55 | both halves | 1e-05 | STRING 511 |
| [[TSR1]] | -0.59 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[L3HYPDH]] | -0.58 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[PTPRG]] | -0.58 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[ATR]] | -0.57 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[DHX33]] | -0.56 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[SPOPL-DT]] | -0.55 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[ANAPC1]] | -0.55 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[NSMAF]] | -0.54 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[TRNT1]] | -0.54 | -0.48 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DDAH2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DUSP8]] | C | DUSP8 activity raises DDAH2's level | lines that do not express DUSP8 (4) vs lines expressing it (46) | 2.07× lower at baseline in the lines without DUSP8 | 0.013 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FAM241B, BTG3-AS1; maybe low, not absent; co-absent with the target |
| [[TBC1D17]] | C | TBC1D17's natural level strengthens DDAH2's drug response | TBC1D17's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.12; direction not clear | 0.029 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.594). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (0.8, -36.4); signed map (-10.2, 15.7). **Vector** length 78.9, 16.4% of its response variance represented; |z| ≥ 3 in 818 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +3.7 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +10.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +8.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.3 | -2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.3 | +4.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.9 | +2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +1.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | +1.5 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.2 | -6.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -3.4 | -5.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.1 | -3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -4.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.2 | -3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -6.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | DDAH family member 2, ADMA-independent |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,727,038-31,730,617 (-) |
| Ensembl biotype | protein_coding |
| Also known as | G6A, DDAHII |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [O95865](https://www.uniprot.org/uniprotkb/O95865) (Putative hydrolase DDAH2):

> Putative hydrolase with unknown substrate (Probable). Does not hydrolyze N(G),N(G)-dimethyl-L-arginine (ADMA) which acts as an inhibitor of NOS. In endothelial cells, induces expression of vascular endothelial growth factor (VEGF) via phosphorylation of the transcription factor SP1 by PKA in a process that is independent of NO and NO synthase (By similarity). Similarly, enhances pancreatic insulin secretion through SP1-mediated transcriptional up-regulation of secretagogin/SCGN, an insulin …

**Summary**, from NCBI Gene [23564](https://www.ncbi.nlm.nih.gov/gene/23564):

> This gene encodes a dimethylarginine dimethylaminohydrolase. The encoded enzyme functions in nitric oxide generation by regulating the cellular concentrations of methylarginines, which in turn inhibit nitric oxide synthase activity. The protein may be localized to the mitochondria. Alternative splicing resulting in multiple transcript variants. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:2716](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2716) · Entrez [23564](https://www.ncbi.nlm.nih.gov/gene/23564) · UniProt [O95865](https://www.uniprot.org/uniprotkb/O95865) · Ensembl [ENSG00000213722](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213722)

## Data

Gene col 13131: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13131); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13131, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13131]; `tensor/DDL_lfc|DDL_z.npy` [13131]; `embed/gene_vectors.npy` [13131]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13131 or target_col == 13131). Every well: [[DDAH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDAH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
