---
symbol: "CFAP53"
type: "gene"
col: 10246
ensembl_id: "ENSG00000172361"
name: "cilia and flagella associated protein 53"
location: "18q21.1"
module: 37
arm: "+"
pooled_cpm: 9.36
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 1
n_dd_up_clean: 24
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# CFAP53

*cilia and flagella associated protein 53* — 18q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.91× (z +36.5, q 0e+00, up in 41 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Belumosudil (drug)]] 5 µM: 0.737× (z -3.9, q 0.055, down in 15 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 0.125×, COLO 205 0.252×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Belumosudil (drug)]] 5 µM in 2 lines (C32 0.0840×, NCI-H1573 0.205×); [[Simotinib (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0931×; ⚠ toxic); [[Ralimetinib dimesylate (drug)]] 0.5 µM in 1 line (SNU-1 0.0494×); [[Ligustrazine (drug)]] 5 µM in 1 line (NCI-H2030 0.147×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02936]] (+0.87, fdr 7e-06), [[PIWIL2]] (+0.83, fdr 7e-06), [[CASS4]] (+0.83, fdr 7e-06).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10246.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.91×** | +36.5 | 0e+00 | 41/41 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.40×** | +28.0 | 0e+00 | 44/44 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.67×** | +23.1 | 0e+00 | 42/42 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.02×** | +14.7 | 0e+00 | 40/45 (SW480, LoVo, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.70×** | +12.8 | 4e-35 | 34/41 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +11.5 | 8e-29 | 31/44 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.22×** | +10.2 | 1e-22 | 22/37 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.11×** | +9.6 | 8e-20 | 34/45 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.62×** | +9.2 | 3e-18 | 24/47 (NCI-H2347, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.88×** | +8.3 | 4e-15 | 30/45 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.83×** | +8.1 | 4e-14 | 29/47 (SW48, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.86×** | +7.5 | 4e-12 | 22/45 (NCI-H460, C-33 A, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +5.9 | 1e-07 | 21/47 (SNU-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.53×** | +5.7 | 5e-07 | 20/47 (C-33 A, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +5.2 | 6e-06 | 17/46 (LoVo, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +4.8 | 5e-05 | 12/46 (C-33 A, MIA PaCa-2, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10246.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 0.125×, COLO 205 0.252×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Belumosudil (drug)]] 5 µM in 2 lines (C32 0.0840×, NCI-H1573 0.205×); [[Simotinib (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0931×; ⚠ toxic); [[Ralimetinib dimesylate (drug)]] 0.5 µM in 1 line (SNU-1 0.0494×); [[Ligustrazine (drug)]] 5 µM in 1 line (NCI-H2030 0.147×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **0.737×** | -3.9 | 0.055 | 15/45 (C32, NCI-H1573, …) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.778× | -3.3 | 0.18 | 4/47 (NCI-H1792, COLO 205, …) | inconsistent across doses |  |
| [[Posaconazole (drug)]] 5 µM |  | 0.776× | -3.2 | 0.18 | 3/46 (NCI-H661, RPMI-7951, …) | top dose only | plate-row cell shift |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.842× | -3.2 | 0.18 | 8/48 (NCI-H1573, SW 1271, …) | all doses, stronger at high dose |  |
| [[Megestrol (drug)]] 0.05 µM |  | 0.776× | -3.0 | 0.23 | 9/47 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10246. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 33.3 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.14× (z +20.1) | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[LoVo (line)]] | wt | 17.6 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +22.7) | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H1573 (line)]] | alt | 20.4 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +21.6) | [[Belumosudil (drug)]] 5 µM 0.205× (z -8.5) |
| [[C32 (line)]] | wt | 7.26 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.41× (z +10.1) | [[Belumosudil (drug)]] 5 µM 0.0840× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 10.0 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +18.0) | [[Ligustrazine (drug)]] 5 µM 0.147× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 5.61 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +17.4) | — |
| [[SW48 (line)]] | wt | 11.5 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.22× (z +11.5) | [[Rucaparib (phosphate) (drug)]] 0.05 µM 0.0833× (z -8.5) |
| [[SW480 (line)]] | alt | 7.79 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +14.9) | — |
| [[HS-578T (line)]] | alt | 6.52 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.35× (z +11.9) | — |
| [[hTERT-HPNE (line)]] | wt | 22.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.00× (z +12.4) | [[Simotinib (drug)]] 5 µM 0.0931× (z -10.4) ⚠ toxic |
| [[KATO III (line)]] | alt | 21.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -9.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 6.04 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.40× (z +12.4) | — |
| [[NCI-H23 (line)]] | alt | 9.31 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.6× (z +20.2) | — |
| [[NCI-H2347 (line)]] | alt | 5.09 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.23× (z +12.8) | — |
| [[SHP-77 (line)]] | alt | 6.77 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.85× (z +11.0) | — |
| [[A498 (line)]] | wt | 10.2 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.67× (z +10.3) | — |
| [[AsPC-1 (line)]] | alt | 3.30 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.5× (z +12.4) | — |
| [[C-33 A (line)]] | alt | 17.8 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 9.09× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 7.18 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.33× (z +12.2) | — |
| [[HCT15 (line)]] | alt | 19.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.94× (z +12.0) | — |
| [[HOP62 (line)]] | alt | 4.48 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +13.8) | — |
| [[J82 (line)]] | alt | 3.70 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.65× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 6.72 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.57× (z +11.4) | — |
| [[LS 180 (line)]] | wt | 15.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 3.18 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.09× (z +12.9) | — |
| [[RKO (line)]] | wt | 17.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 5.36 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.97× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 32.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 5.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.18× (z +10.7) | — |
| [[Panc 03.27 (line)]] | alt | 4.92 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.55× (z +11.3) | — |
| [[RPMI-7951 (line)]] | alt | 7.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.53× (z +10.6) | — |
| [[SK-MEL-2 (line)]] | alt | 9.67 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +14.6) | — |
| [[SNU-1 (line)]] | wt | 15.8 | 0 | 1 | — | [[Ralimetinib dimesylate (drug)]] 0.5 µM 0.0494× (z -8.7) |
| [[SW1417 (line)]] | alt | 4.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.88× (z +9.6) | — |
| [[A-172 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10246), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02936]] | +0.87 | +0.81 / +0.81 | both halves | 7e-06 |  |
| [[PIWIL2]] | +0.83 | +0.82 / +0.74 | both halves | 7e-06 |  |
| [[CASS4]] | +0.83 | +0.82 / +0.76 | both halves | 7e-06 |  |
| [[SNX31]] | +0.79 | +0.81 / +0.73 | both halves | 7e-06 |  |
| [[TMEM269]] | +0.79 | +0.83 / +0.71 | both halves | 7e-06 |  |
| [[THAP2]] | +0.78 | +0.82 / +0.61 | both halves | 7e-06 |  |
| [[CDKL3]] | +0.78 | +0.79 / +0.62 | both halves | 7e-06 |  |
| [[C1S]] | +0.77 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[TMEM225B]] | +0.76 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[CCNP]] | +0.76 | +0.75 / +0.79 | both halves | 7e-06 |  |
| [[LRP2BP]] | +0.76 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[TAS2R4]] | +0.76 | +0.76 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CFAP53's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[IGSF11]] | B | IGSF11 activity raises CFAP53's level | lines that do not express IGSF11 (10) vs lines expressing it (40) | 1.43× lower at baseline in the lines without IGSF11 | 0.047 | ⚠ within organs, on part of the lines; also absent: LINC02398, ANKRD7; maybe low, not absent |
| [[ST8SIA5]] | B | ST8SIA5 activity raises CFAP53's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 1.65× lower at baseline in the lines without ST8SIA5 | 0.060 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.809). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.9, -16.2); signed map (12.5, 5.0). **Vector** length 89.0, 19.3% of its response variance represented; |z| ≥ 3 in 1,100 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +28.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.0 | +14.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.3 | +23.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +36.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +12.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +9.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +7.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +3.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.5 | +5.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.0 | +8.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.4 | +8.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | +1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -3.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | cilia and flagella associated protein 53 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.1 — chr18:50,227,193-50,266,495 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32743; previously CCDC11 |
| Gene groups (HGNC) | Cilia and flagella associated; Centriolar satellite proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96M91](https://www.uniprot.org/uniprotkb/Q96M91) (Cilia- and flagella-associated protein 53):

> Microtubule inner protein (MIP) part of the dynein-decorated doublet microtubules (DMTs) in cilia axoneme, which is required for motile cilia beating. Regulates motility patterns of both 9+0 and 9+2 motile cilia through differential localization and recruitment of axonemal dynein components (By similarity). Required for centriolar satellite integrity and non-motile cilium assembly. Required for motile cilium formation. Through its role in the beating of primary cilia, involved in the …

**Summary**, from NCBI Gene [220136](https://www.ncbi.nlm.nih.gov/gene/220136):

> This gene belongs to the CFAP53 family. It was found to be differentially expressed by the ciliated cells of frog epidermis and in skin fibroblasts from human. Mutations in this gene are associated with visceral heterotaxy-6, which implicates this gene in determination of left-right asymmetric patterning. [provided by RefSeq, Aug 2015]

**Accessions** — [HGNC:26530](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26530) · Entrez [220136](https://www.ncbi.nlm.nih.gov/gene/220136) · UniProt [Q96M91](https://www.uniprot.org/uniprotkb/Q96M91) · Ensembl [ENSG00000172361](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172361)

## Data

Gene col 10246: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10246); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10246, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10246]; `tensor/DDL_lfc|DDL_z.npy` [10246]; `embed/gene_vectors.npy` [10246]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10246 or target_col == 10246). Every well: [[CFAP53 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP53.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
