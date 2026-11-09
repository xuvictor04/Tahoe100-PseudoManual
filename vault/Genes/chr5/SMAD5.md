---
symbol: "SMAD5"
type: "gene"
col: 3491
ensembl_id: "ENSG00000113658"
name: "SMAD family member 5"
location: "5q31.1"
module: 186
arm: "+"
pooled_cpm: 134.42
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/186"]
generated_by: "tahoemap"
---

# SMAD5

*SMAD family member 5* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.97× (z +9.7, q 2e-19, up in 42 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (J82 0.579×, COLO 205 0.500×, LOX-IMVI 0.608×, AN3 CA 0.464×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.381×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A549 0.358×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RYK]] (+0.67, fdr 7e-06), [[HOXB5]] (+0.63, fdr 2e-05), [[TMEM68]] (+0.59, fdr 1e-05); moves opposite to [[SLC35C2]] (-0.61, fdr 1e-05), [[BCL7B]] (-0.56, fdr 2e-05), [[SETX]] (-0.54, fdr 1e-05).
> It is in [[Module 186]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HOXB5]], [[HOXB6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 20 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3491.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.97×** | +9.7 | 2e-19 | 42/49 (LoVo, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.22×** | +7.6 | 9e-12 | 26/49 (LS 180, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.30×** | +7.2 | 9e-11 | 29/48 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.63×** | +7.0 | 3e-10 | 35/48 (A-172, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +7.0 | 3e-10 | 24/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.26×** | +6.1 | 8e-08 | 30/48 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.23×** | +5.6 | 2e-06 | 25/48 (LoVo, HOP62, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.45×** | +5.3 | 8e-06 | 23/38 (A549, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.21×** | +5.2 | 1e-05 | 27/48 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.42×** | +5.1 | 2e-05 | 30/49 (NCI-H23, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.20× | +4.9 | 4e-05 | 21/48 (HS-578T, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.20× | +4.8 | 9e-05 | 22/50 (NCI-H460, A-427, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~5% of this change | 1.19× | +4.7 | 1e-04 | 22/47 (A-172, LS 180, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.18× | +4.5 | 2e-04 | 21/48 (SNU-423, CFPAC-1, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +4.5 | 2e-04 | 10/48 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +4.5 | 2e-04 | 21/48 (NCI-H23, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.15× | +3.7 | 0.005 | 15/48 (C32, SW48, …) | top dose only |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.09× | +3.3 | 0.022 | 1/49 (Hs 766T) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.12× | +3.1 | 0.037 | 14/48 (C-33 A, A-427, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.12× | +3.1 | 0.046 | 10/48 (CFPAC-1, BT-474, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.12× | +2.9 | 0.067 | 9/48 (MIA PaCa-2, HS-578T, …) | top dose only |  |
| [[Terfenadine (drug)]] 0.5 µM |  | 1.11× | +2.9 | 0.072 | 6/48 (HCT15, MIA PaCa-2, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3491.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (J82 0.579×, COLO 205 0.500×, LOX-IMVI 0.608×, AN3 CA 0.464×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.381×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A549 0.358×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.852× | -4.3 | 0.011 | 19/48 (NCI-H1573, NCI-H1792, …) | rises with dose | position effect removed |
| [[Demeclocycline (drug)]] 5 µM |  | 0.916× | -3.5 | 0.16 | 2/48 (NCI-H661, SW 1088) | top dose only |  |
| [[Pexidartinib (hydrochloride) (drug)]] 0.5 µM |  | 0.895× | -3.1 | 0.25 | 8/48 (SW 1088, NCI-H1792, …) | rises with dose | position effect removed |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 0.895× | -3.1 | 0.25 | 6/48 (NCI-H1573, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3491. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 171 | 8 (6 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.34× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.70× (z +11.9) | — |
| [[LS 180 (line)]] | wt | 125 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +12.5) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 4.02× (z +8.7) | — |
| [[A-172 (line)]] | wt | 164 | 3 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 3.44× (z +10.6) | — |
| [[NCI-H460 (line)]] | wt | 161 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.52× (z +11.4) ⚠ cell-cycle shift, explains ~9% of this change | — |
| [[PANC-1 (line)]] | alt | 162 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.77× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.88× (z +8.6) | — |
| [[A498 (line)]] | wt | 151 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.92× (z +9.1) | — |
| [[A549 (line)]] | wt | 137 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.358× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 185 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 88.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.583× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 166 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.438× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~60% of this change |
| [[C32 (line)]] | wt | 143 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 3.77× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.579× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 87.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.48× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 156 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.608× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 145 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.59× (z +9.4) ⚠ cell-cycle shift, explains ~9% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 160 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 124 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.44× (z +8.8) | — |
| [[SW480 (line)]] | alt | 116 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.12× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 145 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 182 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 151 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 176 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 207 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 125 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 159 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 110 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 125 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 151 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 102 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3491), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RYK]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[HOXB5]] | +0.63 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[TMEM68]] | +0.59 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[ALG9]] | +0.58 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[VGLL4]] | +0.57 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[FBXO9]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[FHIP2A]] | +0.57 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[SEC24B]] | +0.57 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[ASB7]] | +0.57 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[PPP2R5E]] | +0.56 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[SNX4]] | +0.55 | +0.61 / +0.38 | both halves | 6e-05 |  |
| [[CNIH4]] | +0.54 | +0.49 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35C2]] | -0.61 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[BCL7B]] | -0.56 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[SETX]] | -0.54 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[ZNF674]] | -0.52 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[PPP1R10]] | -0.51 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[THOC6]] | -0.51 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[BLOC1S3]] | -0.50 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[PNKP]] | -0.50 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[SRCAP]] | -0.49 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[UBXN11]] | -0.47 | -0.39 / -0.45 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXB5]], [[HOXB6]] | B | HOXB5, HOXB6 activity lowers SMAD5's level | lines that do not express HOXB5, HOXB6 (11) vs lines expressing them (39) | 1.31× higher at baseline in the lines without HOXB5, HOXB6 | 0.063 | ⚠ within organs, on part of the lines; also absent: HOXB3, HOXB8; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 186]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.669). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.6, -5.7); signed map (-34.1, -11.4). **Vector** length 99.4, 24.5% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.7 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.8 | +3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.4 | +4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +4.4 | +6.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +4.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | +0.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.8 | -1.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.6 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | +2.5 |
|  | [[Posaconazole (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -1.6 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.7 | -3.5 |
|  | [[Rimonabant (drug)]] 5 µM |  | -1.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | SMAD family member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:136,132,845-136,188,747 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Dwfc, JV5-1; previously MADH5 |
| Gene groups (HGNC) | SMAD family |
| Hallmark sets | DNA_REPAIR |
| Reactome | 2 pathways, smallest: Signaling by BMP; Signaling by TGFB family members |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99717](https://www.uniprot.org/uniprotkb/Q99717) (SMAD family member 5):

> Transcriptional regulator that plays a role in various cellular processes including embryonic development, cell differentiation, angiogenesis and tissue homeostasis. Upon BMP ligand binding to their receptors at the cell surface, is phosphorylated by activated type I BMP receptors (BMPRIs) and associates with SMAD4 to form a heteromeric complex which translocates into the nucleus acting as transcription factor. In turn, the hetero-trimeric complex recognizes cis-regulatory elements containing …

**Summary**, from NCBI Gene [4090](https://www.ncbi.nlm.nih.gov/gene/4090):

> The protein encoded by this gene is involved in the transforming growth factor beta signaling pathway that results in an inhibition of the proliferation of hematopoietic progenitor cells. The encoded protein is activated by bone morphogenetic proteins type 1 receptor kinase, and may be involved in cancer. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2014]

**Accessions** — [HGNC:6771](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6771) · Entrez [4090](https://www.ncbi.nlm.nih.gov/gene/4090) · UniProt [Q99717](https://www.uniprot.org/uniprotkb/Q99717) · Ensembl [ENSG00000113658](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113658)

## Data

Gene col 3491: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3491); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3491, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3491]; `tensor/DDL_lfc|DDL_z.npy` [3491]; `embed/gene_vectors.npy` [3491]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3491 or target_col == 3491). Every well: [[SMAD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMAD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
