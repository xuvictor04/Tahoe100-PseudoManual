---
symbol: "GSK3B-DT"
type: "gene"
col: 14325
ensembl_id: "ENSG00000242622"
name: "GSK3B divergent transcript"
location: "3q13.33"
module: 35
arm: "+"
pooled_cpm: 9.77
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 11
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# GSK3B-DT

*GSK3B divergent transcript* — 3q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.70× (z +31.6, q 0e+00, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.444× (z -9.5, q 8e-19, down in 33 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.469× (z -8.9, q 1e-16, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00863]] (+0.80, fdr 1e-05), [[ACTR3-AS1]] (+0.80, fdr 7e-06), [[UBE2D3-AS1]] (+0.78, fdr 1e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14325.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.70×** | +31.6 | 0e+00 | 44/45 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.00×** | +12.4 | 5e-33 | 36/41 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.04×** | +11.9 | 3e-30 | 31/44 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.85×** | +10.3 | 1e-22 | 30/48 (SW1417, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +9.9 | 4e-21 | 34/43 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.22×** | +9.0 | 2e-17 | 25/35 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.59×** | +7.7 | 1e-12 | 28/47 (Panc 03.27, J82, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +6.8 | 1e-09 | 27/46 (A-172, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +4.0 | 0.004 | 10/47 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.005 | 7/48 (AsPC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.007 | 13/46 (CFPAC-1, NCI-H23, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.7 | 0.010 | 2/48 (NCI-H23, Hs 766T) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.75×** | +3.4 | 0.026 | 7/36 (C32, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +3.3 | 0.038 | 9/25 (NCI-H2030, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.29×** | +3.0 | 0.088 | 12/44 (J82, LS 180, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14325.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.444×** | -9.5 | 8e-19 | 33/42 (NCI-H1573, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.469×** | -8.9 | 1e-16 | 39/47 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.524×** | -7.6 | 6e-12 | 32/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.576×** | -6.5 | 1e-08 | 28/46 (NCI-H1573, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.598×** | -5.8 | 7e-07 | 25/43 (CFPAC-1, LoVo, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.420×** | -5.3 | 9e-06 | 20/37 (HT-29, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.697×** | -4.1 | 0.004 | 19/37 (J82, BT-474, …) | top dose only |  |
| [[Erlotinib (drug)]] 5 µM |  | **0.705×** | -3.9 | 0.006 | 20/45 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.729×** | -3.7 | 0.013 | 15/43 (C32, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.733×** | -3.6 | 0.015 | 9/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.571×** | -3.4 | 0.030 | 8/41 (HOP62, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.770× | -3.1 | 0.10 | 14/47 (NCI-H1573, MIA PaCa-2, …) | two highest doses | position effect removed |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | 0.773× | -3.0 | 0.11 | 8/47 (HS-578T, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14325. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 39.9 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0753× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.182× (z -10.1) |
| [[SW480 (line)]] | alt | 7.12 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.72× (z +14.8) | [[Digitoxin (drug)]] 5 µM 0.241× (z -8.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 24.0 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -10.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 8.91 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.96× (z +12.0) | — |
| [[LoVo (line)]] | wt | 7.13 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.47× (z +14.5) | [[Bosentan (hydrate) (drug)]] 5 µM 0.155× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 12.6 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 7.26 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.57× (z +15.5) | — |
| [[A549 (line)]] | wt | 7.53 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.39× (z +12.0) | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0901× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 6.38 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.18× (z +11.5) | [[Digitoxin (drug)]] 5 µM 0.104× (z -8.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 24.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.36× (z +14.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.175× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~31% of this change |
| [[CFPAC-1 (line)]] | alt | 12.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.13× (z +15.1) | [[Bosentan (hydrate) (drug)]] 5 µM 0.173× (z -9.3) |
| [[H4 (line)]] | wt | 13.3 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 9.16 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.95× (z +13.5) | — |
| [[J82 (line)]] | alt | 10.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.30× (z +11.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0947× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~31% of this change |
| [[Panc 03.27 (line)]] | alt | 9.14 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +15.0) | [[Digitoxin (drug)]] 5 µM 0.123× (z -9.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 6.27 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.07× (z +14.0) | [[Digitoxin (drug)]] 0.5 µM 0.200× (z -8.8) |
| [[A-172 (line)]] | wt | 10.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.49× (z +13.9) | — |
| [[A498 (line)]] | wt | 6.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.66× (z +14.3) | — |
| [[C32 (line)]] | wt | 6.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.56× (z +9.0) | — |
| [[HCT15 (line)]] | alt | 4.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 8.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.85× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 5.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.49× (z +10.7) | — |
| [[HT-29 (line)]] | alt | 11.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.12× (z +13.1) | — |
| [[hTERT-HPNE (line)]] | wt | 4.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +11.0) | — |
| [[KATO III (line)]] | alt | 8.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.12× (z +12.2) | — |
| [[LOX-IMVI (line)]] | wt | 5.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +13.1) | — |
| [[LS 180 (line)]] | wt | 4.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.26× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 4.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.54× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 9.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 12.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.47× (z +11.1) | — |
| [[NCI-H2347 (line)]] | alt | 7.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.84× (z +12.6) | — |
| [[RKO (line)]] | wt | 6.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.06× (z +11.6) | — |
| [[SK-MEL-2 (line)]] | alt | 13.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 7.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.89× (z +13.0) | — |
| [[SW 900 (line)]] | alt | 4.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.46× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 9.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +15.3) | — |
| [[A-427 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14325), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00863]] | +0.80 | +0.79 / +0.51 | both halves | 1e-05 |  |
| [[ACTR3-AS1]] | +0.80 | +0.80 / +0.59 | both halves | 7e-06 |  |
| [[UBE2D3-AS1]] | +0.78 | +0.79 / +0.49 | both halves | 1e-05 |  |
| [[MSH4]] | +0.77 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[CCT6B]] | +0.77 | +0.74 / +0.50 | both halves | 1e-05 |  |
| [[SMIM15-AS1]] | +0.77 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[PBLD]] | +0.76 | +0.73 / +0.47 | both halves | 2e-05 |  |
| [[LRP2BP]] | +0.74 | +0.70 / +0.46 | both halves | 2e-05 |  |
| [[LINC00393]] | +0.74 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[THUMPD3-AS1]] | +0.73 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[ZFHX2-AS1]] | +0.73 | +0.68 / +0.37 | both halves | 8e-05 |  |
| [[CPEB2-DT]] | +0.73 | +0.72 / +0.38 | both halves | 6e-05 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GSK3B-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[BTG3-AS1]] | B | BTG3-AS1 activity raises GSK3B-DT's level | lines that do not express BTG3-AS1 (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without BTG3-AS1 | 0.033 | ⚠ within organs, on part of the lines; also absent: DUSP8, USP43, EFNA2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.762). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (10.7, 10.9); signed map (22.1, -4.0). **Vector** length 97.6, 21.8% of its response variance represented; |z| ≥ 3 in 1,109 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.8 | +31.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +12.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.9 | +10.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +11.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +6.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | -0.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.3 | +1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.2 | +2.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -6.1 | -3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | -2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -2.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.7 | -0.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.1 | -3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.0 | +0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.8 | -5.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.8 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | GSK3B divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q13.33 — chr3:120,094,895-120,136,783 (+) |
| Ensembl biotype | lncRNA |
| Also known as | GPNCA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55635](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55635) · Entrez [107986119](https://www.ncbi.nlm.nih.gov/gene/107986119) · Ensembl [ENSG00000242622](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242622)

## Data

Gene col 14325: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14325); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14325, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14325]; `tensor/DDL_lfc|DDL_z.npy` [14325]; `embed/gene_vectors.npy` [14325]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14325 or target_col == 14325). Every well: [[GSK3B-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSK3B-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
