---
symbol: "IQCJ"
type: "gene"
col: 13187
ensembl_id: "ENSG00000214216"
name: "IQ motif containing J"
location: "3q25.32"
module: 37
arm: "+"
pooled_cpm: 15.27
n_lines_expressing: 44
n_dd_up: 23
n_dd_down: 11
n_dd_up_clean: 21
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 6
direction_downstream: 8
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# IQCJ

*IQ motif containing J* — 3q25.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.15× (z +26.2, q 0e+00, up in 33 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.396× (z -10.0, q 6e-21, down in 30 of 34 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.527× (z -7.2, q 1e-10, down in 26 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST8SIA5]] (+0.63, fdr 7e-06), [[LINC01422]] (+0.61, fdr 1e-05), [[ALOX12-AS1]] (+0.61, fdr 7e-06); moves opposite to [[LCLAT1]] (-0.53, fdr 1e-05), [[SAAL1]] (-0.51, fdr 4e-05), [[SCAP]] (-0.50, fdr 5e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LINC02360]] → it (grade B ⚠); 8 go from it, the strongest it → [[PELO-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13187.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.15×** | +26.2 | 0e+00 | 33/38 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **5.05×** | +18.3 | 0e+00 | 36/39 (NCI-H460, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.80×** | +16.5 | 0e+00 | 31/39 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.30×** | +13.0 | 2e-36 | 30/38 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.09×** | +12.3 | 1e-32 | 26/37 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.93×** | +12.2 | 4e-32 | 30/41 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.62×** | +10.9 | 8e-26 | 23/38 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.87×** | +10.1 | 6e-22 | 24/41 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.29×** | +9.4 | 4e-19 | 28/40 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.29×** | +9.4 | 4e-19 | 30/41 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.77×** | +6.5 | 6e-09 | 22/41 (J82, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.78×** | +6.3 | 1e-08 | 23/39 (C32, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.66×** | +5.2 | 9e-06 | 19/41 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.36×** | +5.1 | 2e-05 | 22/40 (A-427, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.27×** | +4.9 | 4e-05 | 12/41 (LoVo, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13187.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.396×** | -10.0 | 6e-21 | 30/34 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.527×** | -7.2 | 1e-10 | 26/41 (HepG2/C3A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.551×** | -6.3 | 4e-08 | 22/40 (LOX-IMVI, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.583×** | -6.1 | 2e-07 | 21/29 (SNU-423, A498, …) | inconsistent across doses | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.378×** | -5.7 | 1e-06 | 23/37 (NCI-H1792, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.641×** | -4.8 | 1e-04 | 19/39 (NCI-H1792, HepG2/C3A, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.451×** | -4.7 | 2e-04 | 16/35 (NCI-H1792, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.457×** | -4.6 | 3e-04 | 19/41 (NCI-H1792, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.472×** | -4.4 | 6e-04 | 17/36 (COLO 205, C32, …) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **0.699×** | -4.0 | 0.003 | 14/42 (A-427, NCI-H23, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~83% of this change | **0.742×** | -3.4 | 0.040 | 18/37 (HS-578T, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | 0.765× | -3.0 | 0.12 | 6/42 (HepG2/C3A, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13187. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.52 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +19.0) | — |
| [[A498 (line)]] | wt | 33.8 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.310× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 44.6 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0618× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.158× (z -10.9) |
| [[SNU-423 (line)]] | alt | 122 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.257× (z -10.7) |
| [[HOP62 (line)]] | alt | 28.8 | 3 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.80× (z +10.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.125× (z -12.8) ⚠ toxic |
| [[SW480 (line)]] | alt | 5.78 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.92× (z +12.6) | — |
| [[COLO 205 (line)]] | alt | 28.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.31× (z +10.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0497× (z -11.9) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 11.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.17× (z +12.8) | — |
| [[LoVo (line)]] | wt | 12.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +14.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0603× (z -10.9) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 19.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 9.64 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.57× (z +11.7) | — |
| [[NCI-H2030 (line)]] | alt | 7.74 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +13.8) | [[Simotinib (drug)]] 5 µM 0.0906× (z -9.5) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 9.62 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.80× (z +12.4) | — |
| [[RKO (line)]] | wt | 73.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -12.8) |
| [[SHP-77 (line)]] | alt | 8.40 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.45× (z +11.9) | — |
| [[SW 900 (line)]] | alt | 13.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.95× (z +11.1) | — |
| [[A-172 (line)]] | wt | 10.8 | 2 | 0 | [[Auranofin (drug)]] 5 µM 17.7× (z +13.3) | — |
| [[Hs 766T (line)]] | wt | 7.00 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +12.4) | — |
| [[J82 (line)]] | alt | 6.31 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.7× (z +14.9) | — |
| [[NCI-H2347 (line)]] | alt | 3.99 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.85× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 37.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +11.0) | — |
| [[BT-474 (line)]] | alt | 6.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +10.0) | — |
| [[C-33 A (line)]] | alt | 7.56 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.21× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 6.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.9× (z +14.0) | — |
| [[H4 (line)]] | wt | 35.4 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.103× (z -9.7) |
| [[HCT15 (line)]] | alt | 5.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +11.7) | — |
| [[HepG2_C3A (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0916× (z -8.5) ⚠ toxic; unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 7.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.77× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 7.79 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +8.5) | — |
| [[A-427 (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.49 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13187), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST8SIA5]] | +0.63 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[LINC01422]] | +0.61 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[ALOX12-AS1]] | +0.61 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[DNHD1]] | +0.60 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[ESR2]] | +0.59 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[LINC02646]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[LINC00310]] | +0.58 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[LINC01358]] | +0.57 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[TMEM225B]] | +0.57 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[LINC02641]] | +0.56 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[CCDC146]] | +0.56 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[TPTE2]] | +0.56 | +0.56 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCLAT1]] | -0.53 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[SAAL1]] | -0.51 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[SCAP]] | -0.50 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[GNPTAB]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[ALDH7A1]] | -0.48 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[AGK]] | -0.48 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[PEX7]] | -0.48 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[PPP5C]] | -0.48 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[ZDHHC13]] | -0.47 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[COPG2]] | -0.47 | -0.47 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02360]] | B | LINC02360 activity raises IQCJ's level | lines that do not express LINC02360 (33) vs lines expressing it (17) | 2.14× lower at baseline in the lines without LINC02360 | 0.019 | ⚠ within organs, on part of the lines; also absent: MAGEB2, LINC01905, AJAP1 |
| [[TOP2A]] | B | TOP2A activity lowers IQCJ's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[APCDD1L-DT]] | B | APCDD1L-DT activity raises IQCJ's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 2.02× lower at baseline in the lines without APCDD1L-DT | 0.036 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[CASC20]] | B | CASC20 activity raises IQCJ's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 2.32× lower at baseline in the lines without CASC20 | 0.044 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |
| [[LINC02112]] | B | LINC02112 activity raises IQCJ's level | lines that do not express LINC02112 (6) vs lines expressing it (44) | 2.46× lower at baseline in the lines without LINC02112 | 0.060 | ⚠ within organs, on part of the lines; also absent: DNAH6, IQCM, LINC02932; maybe low, not absent |
| [[LINC01358]] | B | LINC01358 activity raises IQCJ's level | lines that do not express LINC01358 (14) vs lines expressing it (36) | 1.79× lower at baseline in the lines without LINC01358 | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, BMPER, FRMD4A; maybe low, not absent |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PELO-AS1]] | B | IQCJ activity raises PELO-AS1's level | lines that do not express IQCJ (6) vs lines expressing it (44) | 1.54× lower at baseline in the lines without IQCJ | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000222042, MR1, HECTD2; maybe low, not absent |
| [[FAM184B]] | B | IQCJ activity raises FAM184B's level | lines that do not express IQCJ (6) vs lines expressing it (44) | 1.36× lower at baseline in the lines without IQCJ | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000222042, MR1, HECTD2; maybe low, not absent |
| [[RPL34-DT]] | B | IQCJ activity raises RPL34-DT's level | lines that do not express IQCJ (6) vs lines expressing it (44) | 2.27× lower at baseline in the lines without IQCJ | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000222042, MR1, HECTD2; maybe low, not absent |
| [[ALDH7A1]] | B | IQCJ activity raises ALDH7A1's level | lines that do not express IQCJ (6) vs lines expressing it (44) | 1.89× lower at baseline in the lines without IQCJ | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000222042, MR1, HECTD2; maybe low, not absent |
| [[LINC01618]] | B | IQCJ activity raises LINC01618's level | lines that do not express IQCJ (6) vs lines expressing it (44) | 1.49× lower at baseline in the lines without IQCJ | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000222042, MR1, HECTD2; maybe low, not absent |
| [[PSMD7-DT]] | B | IQCJ activity raises PSMD7-DT's level | lines that do not express IQCJ (6) vs lines expressing it (44) | 1.49× lower at baseline in the lines without IQCJ | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000222042, MR1, HECTD2; maybe low, not absent |
| [[UBA6-DT]] | B | IQCJ activity raises UBA6-DT's level | lines that do not express IQCJ (6) vs lines expressing it (44) | 2.71× lower at baseline in the lines without IQCJ | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000222042, MR1, HECTD2; maybe low, not absent |
| [[WDR49]] | C | IQCJ activity raises WDR49's level | lines that do not express IQCJ (6) vs lines expressing it (44) | 2.70× lower at baseline in the lines without IQCJ | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000222042, MR1, HECTD2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.592). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.1, -18.2); signed map (8.6, 8.0). **Vector** length 96.7, 22.3% of its response variance represented; |z| ≥ 3 in 1,226 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.4 | +18.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +26.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +13.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +12.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +16.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +10.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +6.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | +1.6 | +2.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.7 | -7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.4 | -10.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -5.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +0.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.7 | -4.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | +0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -4.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.2 | +0.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | IQ motif containing J |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.32 — chr3:158,962,928-159,266,307 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [Q1A5X6](https://www.uniprot.org/uniprotkb/Q1A5X6) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:32406](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32406) · Entrez [654502](https://www.ncbi.nlm.nih.gov/gene/654502) · UniProt [Q1A5X6](https://www.uniprot.org/uniprotkb/Q1A5X6) · Ensembl [ENSG00000214216](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214216)

## Data

Gene col 13187: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13187); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13187, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13187]; `tensor/DDL_lfc|DDL_z.npy` [13187]; `embed/gene_vectors.npy` [13187]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13187 or target_col == 13187). Every well: [[IQCJ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IQCJ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
