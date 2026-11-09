---
symbol: "LIX1-AS1"
type: "gene"
col: 14770
ensembl_id: "ENSG00000251513"
name: "LIX1 and RIOK2 antisense RNA 1"
location: "5q15"
module: 26
arm: "+"
pooled_cpm: 14.08
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 14
n_dd_up_clean: 16
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# LIX1-AS1

*LIX1 and RIOK2 antisense RNA 1* — 5q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.97× (z +15.5, q 0e+00, up in 40 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.374× (z -9.9, q 3e-20, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01340]] (+0.90, fdr 7e-06), [[PKN2-AS1]] (+0.78, fdr 1e-05), [[MAMDC2-AS1]] (+0.76, fdr 7e-06); moves opposite to [[ARRB2]] (-0.62, fdr 2e-04), [[CABLES2]] (-0.62, fdr 4e-04), [[CEP131]] (-0.61, fdr 3e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14770.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.97×** | +15.5 | 0e+00 | 40/44 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.01×** | +11.1 | 6e-26 | 44/47 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.45×** | +8.6 | 1e-15 | 33/46 (HS-578T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.32×** | +8.1 | 8e-14 | 33/45 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.76×** | +8.0 | 1e-13 | 34/47 (A-172, HOP62, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.70×** | +5.1 | 3e-05 | 24/46 (NCI-H23, RKO, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +4.8 | 1e-04 | 11/26 (RPMI-7951, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +4.6 | 4e-04 | 19/46 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +4.4 | 6e-04 | 19/44 (LoVo, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.58×** | +4.4 | 6e-04 | 19/46 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.51×** | +4.1 | 0.002 | 19/46 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.002 | 19/47 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.45×** | +3.7 | 0.008 | 13/33 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Demeclocycline (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.011 | 14/47 (RKO, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.46×** | +3.5 | 0.018 | 10/31 (SW 900, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +3.5 | 0.018 | 15/47 (LoVo, A-427, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.39×** | +3.3 | 0.030 | 10/46 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.37×** | +3.1 | 0.051 | 7/47 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14770.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.374×** | -9.9 | 3e-20 | 38/47 (C32, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.444×** | -8.2 | 1e-13 | 37/47 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.454×** | -7.9 | 4e-13 | 32/46 (MIA PaCa-2, C32, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.531×** | -6.4 | 3e-08 | 29/46 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.636×** | -4.6 | 6e-04 | 16/47 (C32, A498, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.630×** | -4.5 | 7e-04 | 22/46 (RKO, A498, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.648×** | -4.4 | 0.001 | 21/44 (SNU-423, SW480, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.666×** | -4.1 | 0.003 | 21/46 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.672×** | -4.0 | 0.004 | 20/47 (SW480, SNU-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.699×** | -3.6 | 0.018 | 17/47 (RKO, SW480, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.784×** | -3.5 | 0.027 | 18/47 (CFPAC-1, HepG2/C3A, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.638×** | -3.2 | 0.058 | 12/47 (NCI-H23, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.726×** | -3.1 | 0.084 | 15/43 (SW480, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **0.729×** | -3.1 | 0.090 | 17/41 (HepG2/C3A, NCI-H23, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14770. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 80.0 | 0 | 10 (7 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.0252× (z -18.4) |
| [[SW480 (line)]] | alt | 16.3 | 3 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +12.0) | [[Belinostat (drug)]] 5 µM 0.215× (z -10.3) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -9.4) |
| [[C32 (line)]] | wt | 28.6 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0592× (z -13.9) |
| [[LoVo (line)]] | wt | 9.32 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +10.8) | — |
| [[RKO (line)]] | wt | 30.9 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.173× (z -9.5) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[venetoclax (drug)]] 5 µM 0.0404× (z -9.1) |
| [[SNU-423 (line)]] | alt | 5.76 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.04× (z +9.5) | [[Belinostat (drug)]] 0.5 µM 0.0781× (z -9.5) |
| [[A-172 (line)]] | wt | 18.1 | 1 | 1 (1 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 3.35× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.183× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A549 (line)]] | wt | 3.87 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.14× (z +10.0) | [[Procainamide (hydrochloride) (drug)]] 0.5 µM 0.0592× (z -9.5) |
| [[KATO III (line)]] | alt | 19.0 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 19.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.23× (z +13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 9.20× (z +10.7) | — |
| [[A-427 (line)]] | wt | 6.14 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.109× (z -8.8) |
| [[A498 (line)]] | wt | 21.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 6.23 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0892× (z -9.4) |
| [[HOP62 (line)]] | alt | 7.33 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.96× (z +10.5) | — |
| [[HS-578T (line)]] | alt | 11.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.48× (z +10.2) | — |
| [[HT-29 (line)]] | alt | 5.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.54× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0684× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1573 (line)]] | alt | 43.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.216× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 19.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.137× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 6.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.66× (z +12.8) | — |
| [[Panc 03.27 (line)]] | alt | 4.43 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM 0.0745× (z -8.7) |
| [[SNU-1 (line)]] | wt | 19.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0960× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[AN3 CA (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 11.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14770), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01340]] | +0.90 | +0.88 / +0.76 | both halves | 7e-06 |  |
| [[PKN2-AS1]] | +0.78 | +0.77 / +0.54 | both halves | 1e-05 | same gene group |
| [[MAMDC2-AS1]] | +0.76 | +0.68 / +0.65 | both halves | 7e-06 | same gene group |
| [[HCG17]] | +0.76 | +0.75 / +0.58 | both halves | 7e-06 |  |
| [[PSMD7-DT]] | +0.75 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[MMADHC-DT]] | +0.75 | +0.73 / +0.46 | both halves | 3e-05 |  |
| [[ST8SIA5]] | +0.74 | +0.76 / +0.56 | both halves | 1e-05 |  |
| [[MYLK4]] | +0.74 | +0.69 / +0.41 | both halves | 4e-05 |  |
| [[UBA6-DT]] | +0.74 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[ALG1L9P]] | +0.74 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[NEB]] | +0.74 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | +0.74 | +0.69 / +0.56 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARRB2]] | -0.62 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[CABLES2]] | -0.62 | -0.52 / -0.26 | both halves | 4e-04 |  |
| [[CEP131]] | -0.61 | -0.59 / -0.26 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LIX1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.800). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (10.7, 15.7); signed map (24.5, -2.7). **Vector** length 95.8, 22.2% of its response variance represented; |z| ≥ 3 in 1,201 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.9 | +11.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +15.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.9 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.4 | +4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +8.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.7 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +3.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.2 | +4.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -5.0 | -3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~94% of this change | -4.9 | -1.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.6 | -4.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.9 | -0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.7 | -0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.7 | -2.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.1 | -4.6 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -1.9 | -1.6 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | LIX1 and RIOK2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q15 — chr5:97,089,075-97,437,217 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52976](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52976) · Entrez [101926893](https://www.ncbi.nlm.nih.gov/gene/101926893) · Ensembl [ENSG00000251513](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000251513)

## Data

Gene col 14770: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14770); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14770, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14770]; `tensor/DDL_lfc|DDL_z.npy` [14770]; `embed/gene_vectors.npy` [14770]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14770 or target_col == 14770). Every well: [[LIX1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIX1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
