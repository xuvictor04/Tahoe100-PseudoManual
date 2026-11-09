---
symbol: "SLC13A3"
type: "gene"
col: 8151
ensembl_id: "ENSG00000158296"
name: "solute carrier family 13 member 3"
location: "20q13.12"
module: 23
arm: "+"
pooled_cpm: 14.91
n_lines_expressing: 40
n_dd_up: 40
n_dd_down: 1
n_dd_up_clean: 32
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# SLC13A3

*solute carrier family 13 member 3* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.67× (z +30.2, q 0e+00, up in 31 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Dimethyl fumarate (drug)]] 5 µM: 0.767× (z -3.6, q 0.100, down in 9 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SK-MEL-2 0.0892×, KATO III 0.342×, NCI-H2030 0.238×, SNU-423 0.309×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 0.0464×, SK-MEL-2 0.260×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SHP-77 0.113×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (KATO III 0.267×); [[Malotilate (drug)]] 0.05 µM in 1 line (C-33 A 0.0953×); [[Crizotinib (hydrochloride) (drug)]] 0.5 µM in 1 line (C-33 A 0.0964×).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01004]] (+0.75, fdr 1e-04), [[SMIM15-AS1]] (+0.75, fdr 3e-05), [[MIRLET7IHG]] (+0.75, fdr 6e-05); moves opposite to [[MPP1]] (-0.65, fdr 2e-04), [[SPATA6]] (-0.63, fdr 2e-04), [[HACE1]] (-0.61, fdr 0.001, ⚠ one half only (not replicated)).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[C21orf91-OT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8151.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.67×** | +30.2 | 0e+00 | 31/33 (AsPC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.26×** | +23.1 | 0e+00 | 29/33 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.77×** | +17.7 | 0e+00 | 20/28 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.14×** | +15.3 | 0e+00 | 27/29 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.17×** | +14.8 | 0e+00 | 26/32 (C32, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.82×** | +13.8 | 2e-41 | 7/18 (LOX-IMVI, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.99×** | +13.4 | 3e-39 | 30/38 (BT-474, A-172, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.67×** | +13.1 | 3e-37 | 26/33 (RKO, C32, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.71×** | +12.8 | 2e-35 | 10/20 (LOX-IMVI, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.27×** | +11.3 | 5e-28 | 26/37 (A-172, SHP-77, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.13×** | +10.4 | 9e-24 | 10/24 (Hs 766T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.63×** | +9.5 | 1e-19 | 21/37 (SK-MEL-2, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.03×** | +9.4 | 2e-19 | 21/37 (C32, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.81×** | +8.2 | 1e-14 | 22/38 (KATO III, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +8.1 | 3e-14 | 20/38 (C32, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +6.6 | 1e-09 | 20/38 (KATO III, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +5.6 | 6e-07 | 14/36 (AsPC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +5.6 | 7e-07 | 16/36 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +5.3 | 4e-06 | 17/38 (SHP-77, KATO III, …) | top dose only | cell-cycle shift (explains ~19% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8151.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SK-MEL-2 0.0892×, KATO III 0.342×, NCI-H2030 0.238×, SNU-423 0.309×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 0.0464×, SK-MEL-2 0.260×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SHP-77 0.113×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (KATO III 0.267×); [[Malotilate (drug)]] 0.05 µM in 1 line (C-33 A 0.0953×); [[Crizotinib (hydrochloride) (drug)]] 0.5 µM in 1 line (C-33 A 0.0964×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.767×** | -3.6 | 0.100 | 9/38 (RPMI-7951, NCI-H2030, …) | top dose only | plate-row cell shift |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.837× | -3.6 | 0.100 | 7/38 (Hs 766T, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 0.849× | -3.3 | 0.19 | 10/37 (LOX-IMVI, NCI-H661, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8151. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 104 | 3 | 7 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.0464× (z -25.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.267× (z -11.5) |
| [[C32 (line)]] | wt | 40.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.31× (z +17.8) | — |
| [[SHP-77 (line)]] | alt | 58.1 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.05× (z +10.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.113× (z -15.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 9.33 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.36× (z +8.7) | [[Malotilate (drug)]] 0.05 µM 0.0953× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 9.28 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.93× (z +12.8) | — |
| [[HOP62 (line)]] | alt | 10.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +11.1) | — |
| [[SK-MEL-2 (line)]] | alt | 54.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0892× (z -17.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 6.86 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.84× (z +10.5) | — |
| [[A498 (line)]] | wt | 23.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +13.2) | — |
| [[AsPC-1 (line)]] | alt | 28.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.53× (z +15.7) | — |
| [[BT-474 (line)]] | alt | 27.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.35× (z +13.2) | — |
| [[LOX-IMVI (line)]] | wt | 12.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.53× (z +11.0) | — |
| [[NCI-H1573 (line)]] | alt | 4.56 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.93× (z +11.5) | — |
| [[NCI-H2030 (line)]] | alt | 18.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 5.51 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.43× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 76.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -8.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 18.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.98× (z +11.9) | — |
| [[HCT15 (line)]] | alt | 6.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.49× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 4.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.94× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 5.56 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.8× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 4.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.48× (z +10.1) | — |
| [[LoVo (line)]] | wt | 4.34 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.65× (z +12.1) | — |
| [[Panc 03.27 (line)]] | alt | 4.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.05× (z +9.5) | — |
| [[RPMI-7951 (line)]] | alt | 29.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +11.9) | — |
| [[SW1417 (line)]] | alt | 5.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.09× (z +11.1) | — |
| [[SW480 (line)]] | alt | 25.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +9.9) | — |
| [[A-427 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8151), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01004]] | +0.75 | +0.77 / +0.35 | both halves | 1e-04 |  |
| [[SMIM15-AS1]] | +0.75 | +0.75 / +0.46 | both halves | 3e-05 |  |
| [[MIRLET7IHG]] | +0.75 | +0.78 / +0.39 | both halves | 6e-05 |  |
| [[MSH4]] | +0.75 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[ANKRD17-DT]] | +0.71 | +0.77 / +0.33 | both halves | 1e-04 |  |
| [[RFX3-DT]] | +0.71 | +0.79 / +0.28 | both halves | 3e-04 |  |
| [[HCG17]] | +0.70 | +0.75 / +0.37 | both halves | 8e-05 |  |
| [[ZFHX2-AS1]] | +0.70 | +0.70 / +0.35 | both halves | 1e-04 |  |
| [[C1S]] | +0.70 | +0.69 / +0.44 | both halves | 3e-05 |  |
| [[PPP1R12A-AS2]] | +0.70 | +0.75 / +0.39 | both halves | 5e-05 |  |
| [[CHD1-DT]] | +0.70 | +0.77 / +0.35 | both halves | 1e-04 |  |
| [[ST8SIA5]] | +0.69 | +0.73 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPP1]] | -0.65 | -0.49 / -0.29 | both halves | 2e-04 |  |
| [[SPATA6]] | -0.63 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[HACE1]] | -0.61 | -0.70 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC13A3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SOCS2-AS1]] | B | SOCS2-AS1 activity weakens SLC13A3's drug response | lines that do not express SOCS2-AS1 (7) vs lines expressing it (31) | the lines without SOCS2-AS1 respond 1.17× as strongly (z diff -0.32); strongest at Epirubicin (hydrochloride) 5 µM: 3.66x vs 2.25x (z diff -2.8) | 0.075 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2; target measured in part of the lines; artifact flags |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C21orf91-OT1]] | B | SLC13A3 activity raises C21orf91-OT1's level | lines that do not express SLC13A3 (10) vs lines expressing it (40) | 1.76× lower at baseline in the lines without SLC13A3 | 0.070 | ⚠ within organs, on part of the lines; also absent: TLN2; maybe low, not absent |
| [[DNAH10]] | B | SLC13A3 activity raises DNAH10's level | lines that do not express SLC13A3 (10) vs lines expressing it (40) | 1.42× lower at baseline in the lines without SLC13A3 | 0.087 | ⚠ within organs, on part of the lines; also absent: TLN2; maybe low, not absent |
| [[RNF32-DT]] | B | SLC13A3 activity lowers RNF32-DT's level | lines that do not express SLC13A3 (10) vs lines expressing it (40) | 1.92× higher at baseline in the lines without SLC13A3 | 0.089 | ⚠ within organs, on part of the lines; also absent: TLN2; maybe low, not absent |
| [[ZNF460-AS1]] | B | SLC13A3 activity lowers ZNF460-AS1's level | lines that do not express SLC13A3 (10) vs lines expressing it (40) | 1.09× higher at baseline in the lines without SLC13A3 | 0.096 | ⚠ within organs, on part of the lines; also absent: TLN2; maybe low, not absent |
| [[HEXIM2-AS1]] | B | SLC13A3 activity weakens HEXIM2-AS1's drug response | lines that do not express SLC13A3 (10) vs lines expressing it (38) | the lines without SLC13A3 respond 1.51× as strongly (z diff -0.93); strongest at Panobinostat 0.5 µM: 0.35x vs 0.50x (z diff -1.8) | 0.099 | ⚠ within organs, on part of the lines; also absent: TLN2; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.688). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (27.6, -12.1); signed map (17.5, 1.6). **Vector** length 66.6, 11.5% of its response variance represented; |z| ≥ 3 in 964 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +30.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +11.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +13.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +15.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +13.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +8.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +4.1 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | +1.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.9 | +5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.8 | +6.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.6 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -3.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -2.9 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.3 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 13 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:46,557,823-46,684,467 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NADC3, SDCT2 |
| Gene groups (HGNC) | Solute carrier family 13 |
| Reactome | 3 pathways, smallest: SLC-mediated transport of organic anions; SLC-mediated transmembrane transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWT9](https://www.uniprot.org/uniprotkb/Q8WWT9) (Na(+)/dicarboxylate cotransporter 3):

> High-affinity sodium-dicarboxylate cotransporter that accepts a range of substrates with 4-6 carbon atoms, such as the citric acid cycle intermediates succinate and alpha-ketoglutarate (2-oxoglutarate), as well as other compounds including N-acetyl-L-aspartate. Transports the dicarboxylate into the cell with a probable stoichiometry of 3 Na(+) for 1 divalent dicarboxylate, rendering the process electrogenic. Can transport citrate in a Na(+)-dependent manner, recognizing the divalent form of …

**Summary**, from NCBI Gene [64849](https://www.ncbi.nlm.nih.gov/gene/64849):

> Mammalian sodium-dicarboxylate cotransporters transport succinate and other Krebs cycle intermediates. They fall into 2 categories based on their substrate affinity: low affinity and high affinity. Both the low- and high-affinity transporters play an important role in the handling of citrate by the kidneys. The protein encoded by this gene represents the high-affinity form. Alternatively spliced transcript variants encoding different isoforms have been found for this gene, although the …

**Accessions** — [HGNC:14430](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14430) · Entrez [64849](https://www.ncbi.nlm.nih.gov/gene/64849) · UniProt [Q8WWT9](https://www.uniprot.org/uniprotkb/Q8WWT9) · Ensembl [ENSG00000158296](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158296)

## Data

Gene col 8151: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8151); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8151, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8151]; `tensor/DDL_lfc|DDL_z.npy` [8151]; `embed/gene_vectors.npy` [8151]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8151 or target_col == 8151). Every well: [[SLC13A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC13A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
