---
symbol: "TBCE-1"
type: "gene"
col: 16086
ensembl_id: "ENSG00000285053"
name: ""
location: ""
module: 23
arm: "+"
pooled_cpm: 8.79
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# TBCE-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.32× (z +30.1, q 0e+00, up in 43 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Flutamide (drug)]] 0.5 µM in 1 line (SHP-77 0.0457×); [[Menadione (drug)]] 5 µM in 1 line (C-33 A 0.0744×); [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (COLO 205 0.0533×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM184B]] (+0.81, fdr 7e-06), [[GGPS1]] (+0.79, fdr 1e-05, ⚠ same locus), [[PPP1R12A-AS2]] (+0.79, fdr 2e-05), [[CDKL3]] (+0.78, fdr 7e-06); moves opposite to [[WRAP73]] (-0.68, fdr 3e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16086.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.32×** | +30.1 | 0e+00 | 43/43 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.34×** | +24.8 | 0e+00 | 37/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.76×** | +21.0 | 0e+00 | 17/18 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.24×** | +17.1 | 0e+00 | 26/32 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.75×** | +13.0 | 9e-37 | 22/26 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.39×** | +12.6 | 1e-34 | 35/45 (SW480, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.05×** | +10.4 | 2e-23 | 29/42 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +9.9 | 2e-21 | 26/43 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +9.5 | 2e-19 | 27/43 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +8.9 | 4e-17 | 26/37 (CFPAC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.72×** | +7.3 | 1e-11 | 27/46 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +6.8 | 6e-10 | 20/48 (A-172, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +6.6 | 2e-09 | 23/48 (NCI-H2347, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +4.7 | 8e-05 | 12/46 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.5 | 2e-04 | 16/39 (NCI-H460, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.71×** | +4.1 | 0.002 | 8/46 (A-172, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.002 | 18/47 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.016 | 8/47 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.016 | 9/46 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.023 | 5/47 (hTERT-HPNE, NCI-H1573, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16086.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Flutamide (drug)]] 0.5 µM in 1 line (SHP-77 0.0457×); [[Menadione (drug)]] 5 µM in 1 line (C-33 A 0.0744×); [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (COLO 205 0.0533×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -4.3 | 0.010 | 6/48 (NCI-H2347, J82, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.798× | -3.0 | 0.58 | 10/45 (SNU-423, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16086. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.26 | 13 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.15× (z +18.6) | — |
| [[SW480 (line)]] | alt | 10.1 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.39× (z +21.2) | — |
| [[A-172 (line)]] | wt | 15.0 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.85× (z +16.5) | — |
| [[A498 (line)]] | wt | 10.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +16.1) | — |
| [[COLO 205 (line)]] | alt | 10.6 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +13.3) | [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM 0.0533× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 6.20 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.74× (z +13.5) | — |
| [[SW 900 (line)]] | alt | 13.1 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.86× (z +13.8) | — |
| [[SW1417 (line)]] | alt | 7.28 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.87× (z +13.5) | — |
| [[C32 (line)]] | wt | 6.44 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.8× (z +14.8) | — |
| [[CFPAC-1 (line)]] | alt | 5.73 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.26× (z +13.3) | — |
| [[HOP62 (line)]] | alt | 8.20 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.91× (z +12.7) | — |
| [[Hs 766T (line)]] | wt | 10.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 7.04 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.72× (z +10.4) | — |
| [[LoVo (line)]] | wt | 9.57 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +15.4) | — |
| [[LOX-IMVI (line)]] | wt | 5.57 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +14.7) | — |
| [[NCI-H1573 (line)]] | alt | 13.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +15.7) | — |
| [[NCI-H2347 (line)]] | alt | 4.88 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.39× (z +14.5) | — |
| [[PANC-1 (line)]] | alt | 13.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +15.0) | — |
| [[RPMI-7951 (line)]] | alt | 8.23 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +12.1) | — |
| [[AsPC-1 (line)]] | alt | 5.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.1× (z +15.7) | — |
| [[BT-474 (line)]] | alt | 13.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.26× (z +12.7) | — |
| [[C-33 A (line)]] | alt | 13.8 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0744× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 7.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.27× (z +12.7) | — |
| [[J82 (line)]] | alt | 5.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +8.9) | — |
| [[KATO III (line)]] | alt | 5.38 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0721× (z -10.0) ⚠ transcription drop |
| [[LS 180 (line)]] | wt | 10.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 4.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.12× (z +10.6) | — |
| [[RKO (line)]] | wt | 9.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.78× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 8.92 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.0457× (z -13.4) |
| [[SNU-423 (line)]] | alt | 7.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.34× (z +11.8) | — |
| [[A-427 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16086), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM184B]] | +0.81 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[GGPS1]] | +0.79 | +0.87 / +0.50 | both halves | 1e-05 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[PPP1R12A-AS2]] | +0.79 | +0.79 / +0.48 | both halves | 2e-05 |  |
| [[CDKL3]] | +0.78 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[CPEB2-DT]] | +0.78 | +0.73 / +0.47 | both halves | 2e-05 |  |
| [[LINC01090]] | +0.78 | +0.76 / +0.56 | both halves | 1e-05 |  |
| [[PSMD7-DT]] | +0.77 | +0.79 / +0.46 | both halves | 3e-05 |  |
| [[CHD1-DT]] | +0.77 | +0.78 / +0.45 | both halves | 3e-05 |  |
| [[TMEM202-AS1]] | +0.77 | +0.78 / +0.42 | both halves | 4e-05 |  |
| [[CCDC90B-AS1]] | +0.77 | +0.76 / +0.39 | both halves | 5e-05 |  |
| [[PPP1R3F]] | +0.76 | +0.75 / +0.48 | both halves | 2e-05 |  |
| [[THAP2]] | +0.76 | +0.77 / +0.44 | both halves | 3e-05 |  |
| [[LINC02955]] | +0.76 | +0.72 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WRAP73]] | -0.68 | -0.47 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TBCE-1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CBX2]] | B | CBX2 activity raises TBCE-1's level | lines that do not express CBX2 (6) vs lines expressing it (44) | 1.43× lower at baseline in the lines without CBX2 | 0.043 | ⚠ within organs, on part of the lines; also absent: CCNP, CTXN1, ADGRL1; maybe low, not absent |
| [[IGSF11]] | B | IGSF11 activity raises TBCE-1's level | lines that do not express IGSF11 (10) vs lines expressing it (40) | 1.27× lower at baseline in the lines without IGSF11 | 0.059 | ⚠ within organs, on part of the lines; also absent: LINC02398, ANKRD7; maybe low, not absent |
| [[MGC4859]] | B | MGC4859 activity raises TBCE-1's level | lines that do not express MGC4859 (8) vs lines expressing it (42) | 1.40× lower at baseline in the lines without MGC4859 | 0.079 | ⚠ within organs, on part of the lines; also absent: LINC00922, LINC01811, LINC00276; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.830). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (9.7, 20.7); signed map (27.7, -2.7). **Vector** length 82.4, 15.7% of its response variance represented; |z| ≥ 3 in 1,043 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +30.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +24.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.5 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +21.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +13.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +6.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.1 | +4.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +2.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.7 | +0.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | +0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.4 | +3.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | -1.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -0.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | +1.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.3 | -1.7 |

## What is on record

> [!warning] No registry record
> TBCE-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16086: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16086); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16086, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16086]; `tensor/DDL_lfc|DDL_z.npy` [16086]; `embed/gene_vectors.npy` [16086]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16086 or target_col == 16086). Every well: [[TBCE-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBCE-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
