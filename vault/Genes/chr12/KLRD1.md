---
symbol: "KLRD1"
type: "gene"
col: 5576
ensembl_id: "ENSG00000134539"
name: "killer cell lectin like receptor D1"
location: "12p13.2"
module: 37
arm: "+"
pooled_cpm: 11.24
n_lines_expressing: 42
n_dd_up: 42
n_dd_down: 20
n_dd_up_clean: 37
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 6
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# KLRD1

*killer cell lectin like receptor D1* — 12p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 11.9× (z +28.1, q 0e+00, up in 37 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.218× (z -12.2, q 1e-31, down in 36 of 39 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.238× (z -6.0, q 5e-07, down in 22 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADCY10]] (+0.78, fdr 7e-06), [[SNX31]] (+0.76, fdr 7e-06), [[KLRK1-AS1]] (+0.74, fdr 7e-06, ⚠ same locus), [[ECT2L]] (+0.74, fdr 7e-06); moves opposite to [[EIF2B3]] (-0.60, fdr 6e-05), [[MPHOSPH6]] (-0.60, fdr 2e-05), [[AGK]] (-0.59, fdr 2e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[KLRK1-AS1]] → it (grade B ⚠); 6 go from it, the strongest it → [[VPS13B-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5576.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **11.9×** | +28.1 | 0e+00 | 37/37 (SW 900, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **8.51×** | +16.5 | 0e+00 | 32/36 (SW 900, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **7.51×** | +15.6 | 0e+00 | 34/37 (SW 900, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.16×** | +13.0 | 1e-36 | 30/38 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.29×** | +9.4 | 9e-19 | 26/40 (HOP62, NCI-H2030, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **8.29×** | +8.9 | 6e-17 | 35/38 (A-427, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.85×** | +8.4 | 4e-15 | 27/40 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.91×** | +8.2 | 1e-14 | 23/30 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.74×** | +8.1 | 3e-14 | 24/37 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.03×** | +8.0 | 6e-14 | 27/40 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.40×** | +7.0 | 1e-10 | 28/39 (SW 900, HOP62, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **2.37×** | +6.9 | 2e-10 | 24/39 (C32, A-427, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.31×** | +6.7 | 8e-10 | 25/39 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +6.6 | 1e-09 | 23/36 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.09×** | +5.9 | 1e-07 | 22/39 (BT-474, A-427, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.03×** | +5.7 | 4e-07 | 19/40 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.02×** | +5.7 | 5e-07 | 22/39 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +5.2 | 7e-06 | 17/40 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5576.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.218×** | -12.2 | 1e-31 | 36/39 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.238×** | -6.0 | 5e-07 | 22/36 (SW 900, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.283×** | -5.3 | 2e-05 | 21/35 (NCI-H1792, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.364×** | -4.2 | 0.003 | 16/39 (NCI-H1792, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.371×** | -4.2 | 0.003 | 13/30 (NCI-H2030, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.615×** | -3.9 | 0.009 | 17/40 (NCI-H1573, COLO 205, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.621×** | -3.8 | 0.011 | 17/40 (NCI-H1573, SHP-77, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.409×** | -3.8 | 0.012 | 15/36 (NCI-H460, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.636×** | -3.6 | 0.017 | 15/40 (COLO 205, NCI-H1573, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.648×** | -3.5 | 0.027 | 10/40 (HT-29, NCI-H1573, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.738×** | -3.4 | 0.030 | 14/40 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.566×** | -3.3 | 0.052 | 10/40 (SW 900, SW 1271, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.668×** | -3.2 | 0.052 | 9/40 (NCI-H1573, hTERT-HPNE, …) | top dose only |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | **0.674×** | -3.2 | 0.062 | 11/39 (RPMI-7951, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.658×** | -3.1 | 0.070 | 11/37 (A549, H4, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.675×** | -3.0 | 0.083 | 14/39 (NCI-H1573, MIA PaCa-2, …) | top dose only |  |
| [[Furosemide (drug)]] 5 µM |  | **0.767×** | -3.0 | 0.083 | 8/40 (C32, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5576. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 6.74 | 13 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 29.9× (z +18.5) | [[Gemfibrozil (drug)]] 0.5 µM 0.102× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 72.7 | 4 (1 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.05× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 15.6 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +14.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.136× (z -8.8) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 76.4 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0828× (z -11.0) ⚠ unreliable plate only · without an alert: [[Belumosudil (drug)]] 5 µM 0.116× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 25.3 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.01× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.0892× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 10.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.6× (z +13.9) | — |
| [[HOP62 (line)]] | alt | 10.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 29.6× (z +16.2) | — |
| [[Panc 03.27 (line)]] | alt | 10.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.0× (z +14.3) | — |
| [[SW 900 (line)]] | alt | 11.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.7× (z +16.3) | — |
| [[BT-474 (line)]] | alt | 9.17 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +12.0) | — |
| [[HCT15 (line)]] | alt | 32.1 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.128× (z -8.7) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 5.22 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +10.9) | — |
| [[LOX-IMVI (line)]] | wt | 4.18 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.4× (z +13.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.94 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.2× (z +13.2) | — |
| [[NCI-H2030 (line)]] | alt | 32.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.87× (z +12.0) | — |
| [[SNU-423 (line)]] | alt | 11.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +12.4) | — |
| [[A-172 (line)]] | wt | 7.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.3× (z +12.1) | — |
| [[A549 (line)]] | wt | 3.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +10.5) | — |
| [[AN3 CA (line)]] | alt | 10.3 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.0670× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 2.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.1× (z +12.3) | — |
| [[CFPAC-1 (line)]] | alt | 3.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.3× (z +12.7) | — |
| [[CHP-212 (line)]] | wt | 23.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0135× (z -10.9) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 8.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.4× (z +9.9) | — |
| [[H4 (line)]] | wt | 32.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.42× (z +10.2) | — |
| [[HepG2_C3A (line)]] | wt | 16.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.98× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 4.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.4× (z +11.2) | — |
| [[HT-29 (line)]] | alt | 3.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.4× (z +11.8) | — |
| [[J82 (line)]] | alt | 2.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.4× (z +10.6) | — |
| [[LS 180 (line)]] | wt | 3.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 7.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.33× (z +9.6) | — |
| [[SW48 (line)]] | wt | 5.82 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.3× (z +9.5) | — |
| [[A-427 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.993 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.47 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5576), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADCY10]] | +0.78 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[SNX31]] | +0.76 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[KLRK1-AS1]] | +0.74 | +0.69 / +0.65 | both halves | 7e-06 | ⚠ same locus (34.0 kb, same strand: neighbours can correlate without regulation) |
| [[ECT2L]] | +0.74 | +0.73 / +0.85 | both halves | 7e-06 |  |
| [[CASS4]] | +0.73 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[UPP2]] | +0.72 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[MAP7D2]] | +0.71 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[LINC02680]] | +0.71 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[ZNNT1]] | +0.70 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[TMEM269]] | +0.70 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[WDR49]] | +0.70 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[N4BP2L1]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[LINC00640]] | +0.68 | +0.71 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2B3]] | -0.60 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[MPHOSPH6]] | -0.60 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[AGK]] | -0.59 | -0.47 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLRK1-AS1]] | B | KLRK1-AS1 activity raises KLRD1's level | lines that do not express KLRK1-AS1 (11) vs lines expressing it (39) | 3.02× lower at baseline in the lines without KLRK1-AS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: BACH2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers KLRD1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VPS13B-DT]] | B | KLRD1 activity lowers VPS13B-DT's level | lines that do not express KLRD1 (8) vs lines expressing it (42) | 1.40× higher at baseline in the lines without KLRD1 | 0.014 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[DPF1]] | B | KLRD1 activity lowers DPF1's level | lines that do not express KLRD1 (8) vs lines expressing it (42) | 1.46× higher at baseline in the lines without KLRD1 | 0.018 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[OOEP]] | B | KLRD1 activity lowers OOEP's level | lines that do not express KLRD1 (8) vs lines expressing it (42) | 1.80× higher at baseline in the lines without KLRD1 | 0.020 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SLC23A1]] | B | KLRD1 activity raises SLC23A1's level | lines that do not express KLRD1 (8) vs lines expressing it (42) | 1.10× lower at baseline in the lines without KLRD1 | 0.072 | ⚠ within organs, on part of the lines; maybe low, not absent |
| cells under [[Isocorydine (drug)]] 5 µM | B | KLRD1 activity raises the cells' numbers under Isocorydine 5 µM (protects the cells) | lines that do not express KLRD1 (8) vs lines expressing it (40) | the lines without KLRD1: 0.92× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; maybe low, not absent |
| cells under [[HI-TOPK-032 (drug)]] 0.05 µM | B | KLRD1 activity raises the cells' numbers under HI-TOPK-032 0.05 µM (protects the cells) | lines that do not express KLRD1 (8) vs lines expressing it (40) | the lines without KLRD1: 0.87× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.772). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.8, -17.9); signed map (10.4, 4.3). **Vector** length 106, 26.7% of its response variance represented; |z| ≥ 3 in 1,219 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +28.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +16.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +15.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +6.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +9.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.3 | +8.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.1 | -12.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | -2.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +2.5 |
|  | [[EX229 (drug)]] 5 µM |  | -4.1 | -5.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.8 | -6.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.4 | -4.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.4 | -3.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.2 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | killer cell lectin like receptor D1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.2 — chr12:10,226,058-10,329,608 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CD94 |
| Gene groups (HGNC) | CD molecules; Killer cell lectin like receptors; C-type lectin domain containing |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 5 pathways, smallest: DAP12 signaling; DAP12 interactions; Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13241](https://www.uniprot.org/uniprotkb/Q13241) (Natural killer cells antigen CD94):

> Immune receptor involved in self-nonself discrimination. In complex with KLRC1 or KLRC2 on cytotoxic and regulatory lymphocyte subsets, recognizes non-classical major histocompatibility (MHC) class Ib molecule HLA-E loaded with self-peptides derived from the signal sequence of classical MHC class Ia and non-classical MHC class Ib molecules. Enables cytotoxic cells to monitor the expression of MHC class I molecules in healthy cells and to tolerate self. Primarily functions as a ligand binding …

**Summary**, from NCBI Gene [3824](https://www.ncbi.nlm.nih.gov/gene/3824):

> Natural killer (NK) cells are a distinct lineage of lymphocytes that mediate cytotoxic activity and secrete cytokines upon immune stimulation. Several genes of the C-type lectin superfamily, including members of the NKG2 family, are expressed by NK cells and may be involved in the regulation of NK cell function. KLRD1 (CD94) is an antigen preferentially expressed on NK cells and is classified as a type II membrane protein because it has an external C terminus. Several transcript variants …

**Accessions** — [HGNC:6378](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6378) · Entrez [3824](https://www.ncbi.nlm.nih.gov/gene/3824) · UniProt [Q13241](https://www.uniprot.org/uniprotkb/Q13241) · Ensembl [ENSG00000134539](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134539)

## Data

Gene col 5576: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5576); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5576, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5576]; `tensor/DDL_lfc|DDL_z.npy` [5576]; `embed/gene_vectors.npy` [5576]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5576 or target_col == 5576). Every well: [[KLRD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLRD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
