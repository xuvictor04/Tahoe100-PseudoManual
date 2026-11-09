---
symbol: "CAPRIN2"
type: "gene"
col: 3176
ensembl_id: "ENSG00000110888"
name: "caprin family member 2"
location: "12p11.21"
module: 147
arm: "+"
pooled_cpm: 135.63
n_lines_expressing: 47
n_dd_up: 1
n_dd_down: 33
n_dd_up_clean: 1
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# CAPRIN2

*caprin family member 2* — 12p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.32× (z +6.1, q 6e-07, up in 25 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (A498 2.63×, SW480 2.36×, LOX-IMVI 1.93×, A-172 1.90×, …); [[Tucidinostat (drug)]] 5 µM in 3 lines (SW480 1.90×, NCI-H460 1.79×, SW1417 1.75×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW1417 1.90×; ⚠ cell-cycle shift, explains ~57% of this change); [[Dexamethasone (drug)]] 0.5 µM in 1 line (NCI-H1573 3.68×).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (9 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.5 µM: 0.686× (z -6.9, q 3e-09, down in 33 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00941]] (+0.80, fdr 7e-06, ⚠ same locus), [[SPRY4]] (+0.71, fdr 7e-06), [[PTPN12]] (+0.71, fdr 7e-06), [[SPRY4-AS1]] (+0.70, fdr 7e-06); moves opposite to [[GBP2]] (-0.56, fdr 1e-05), [[ZSCAN31]] (-0.56, fdr 1e-05), [[FRK]] (-0.54, fdr 1e-05).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC00941]] → it (grade B ⚠); 1 goes from it, the strongest it → [[GCNT2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3176.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (A498 2.63×, SW480 2.36×, LOX-IMVI 1.93×, A-172 1.90×, …); [[Tucidinostat (drug)]] 5 µM in 3 lines (SW480 1.90×, NCI-H460 1.79×, SW1417 1.75×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW1417 1.90×; ⚠ cell-cycle shift, explains ~57% of this change); [[Dexamethasone (drug)]] 0.5 µM in 1 line (NCI-H1573 3.68×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +6.1 | 6e-07 | 25/46 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~1% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3176.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.5 µM |  | **0.686×** | -6.9 | 3e-09 | 33/45 (AsPC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.688×** | -5.9 | 9e-07 | 30/46 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.729×** | -5.7 | 2e-06 | 32/45 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.715×** | -5.7 | 2e-06 | 28/47 (AsPC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.697×** | -5.6 | 3e-06 | 28/46 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.687×** | -5.5 | 3e-06 | 28/45 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.700×** | -5.5 | 3e-06 | 33/45 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.700×** | -5.3 | 9e-06 | 26/44 (AsPC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.710×** | -5.3 | 9e-06 | 25/44 (AsPC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.787×** | -5.2 | 1e-05 | 27/45 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.708×** | -5.1 | 2e-05 | 28/44 (LoVo, J82, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.714×** | -5.0 | 3e-05 | 28/45 (LoVo, AsPC-1, …) | rises with dose | composition shift |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.706×** | -4.9 | 3e-05 | 25/44 (AsPC-1, SW48, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.722×** | -4.7 | 9e-05 | 28/45 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.722×** | -4.7 | 9e-05 | 27/45 (NCI-H23, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.802×** | -4.7 | 9e-05 | 26/45 (AsPC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **0.560×** | -4.6 | 1e-04 | 27/45 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.813×** | -4.4 | 4e-04 | 25/46 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3176. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 802 | 0 | 25 (9 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.337× (z -35.0) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.203× (z -17.3) |
| [[AsPC-1 (line)]] | alt | 368 | 1 (1 ⚠) | 18 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +10.0) ⚠ cell-cycle shift, explains ~51% of this change | [[Trametinib (drug)]] 5 µM 0.155× (z -17.6) |
| [[LoVo (line)]] | wt | 167 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -11.5) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 0.458× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 206 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -18.7) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.436× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 83.6 | 8 | 0 | [[Dexamethasone (drug)]] 0.5 µM 3.68× (z +10.1) | — |
| [[RKO (line)]] | wt | 382 | 0 | 8 (1 ⚠) | — | [[Binimetinib (drug)]] 5 µM 0.282× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 121 | 0 | 5 | — | [[Trametinib (drug)]] 0.5 µM 0.312× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 132 | 0 | 5 | — | [[Binimetinib (drug)]] 0.5 µM 0.280× (z -11.8) |
| [[J82 (line)]] | alt | 87.2 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.342× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.509× (z -8.5) |
| [[HOP62 (line)]] | alt | 335 | 0 | 3 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.611× (z -13.9) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 0.5 µM 0.373× (z -9.6) |
| [[SW1417 (line)]] | alt | 63.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +10.2) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.75× (z +8.8) | — |
| [[SW480 (line)]] | alt | 63.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +15.1) | — |
| [[A-172 (line)]] | wt | 95.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +10.4) | — |
| [[A-427 (line)]] | wt | 82.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A498 (line)]] | wt | 56.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +15.3) | — |
| [[A549 (line)]] | wt | 204 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -12.3) ⚠ cell-cycle shift, explains ~57% of this change |
| [[H4 (line)]] | wt | 76.6 | 0 | 1 | — | [[NG25 (drug)]] 5 µM 0.0506× (z -12.1) |
| [[HCT15 (line)]] | alt | 84.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -9.4) ⚠ cell-cycle shift, explains ~57% of this change |
| [[HEC-1-A (line)]] | alt | 43.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +10.1) | — |
| [[Hs 766T (line)]] | wt | 310 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -9.1) ⚠ cell-cycle shift, explains ~57% of this change |
| [[LOX-IMVI (line)]] | wt | 98.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +10.5) | — |
| [[NCI-H1792 (line)]] | alt | 182 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.663× (z -12.4) ⚠ position not correctable |
| [[NCI-H460 (line)]] | wt | 80.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.79× (z +8.9) | — |
| [[NCI-H661 (line)]] | alt | 49.7 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.105× (z -8.9) |
| [[SHP-77 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.429× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[SW 1088 (line)]] | alt | 118 | 0 | 1 | — | [[Esmolol (hydrochloride) (drug)]] 0.5 µM 0.0641× (z -11.3) |
| [[SW 900 (line)]] | alt | 123 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.383× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[SW48 (line)]] | wt | 70.2 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.216× (z -9.4) |
| [[AN3 CA (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.9 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 76.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.0 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 132 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 71.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 84.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 84.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 387 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3176), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00941]] | +0.80 | +0.83 / +0.79 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[SPRY4]] | +0.71 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[PTPN12]] | +0.71 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[SPRY4-AS1]] | +0.70 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[ITGB5]] | +0.69 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[SEPTIN10]] | +0.69 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[NIBAN2]] | +0.68 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[S100A16]] | +0.67 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[NT5E]] | +0.67 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[THSD4]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[HMGA2]] | +0.66 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[ABTB3]] | +0.66 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[PXN]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GBP2]] | -0.56 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[ZSCAN31]] | -0.56 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[FRK]] | -0.54 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ABCC6]] | -0.53 | -0.46 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00941]] | B | LINC00941 activity raises CAPRIN2's level | lines that do not express LINC00941 (9) vs lines expressing it (41) | 3.01× lower at baseline in the lines without LINC00941 | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000285517, KLF12, PGM5P2-1; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises CAPRIN2's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 6.2% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds |
| [[RASA3]] | B | RASA3 activity raises CAPRIN2's level | lines that do not express RASA3 (9) vs lines expressing it (41) | 1.81× lower at baseline in the lines without RASA3 | 0.067 | ⚠ within organs, on part of the lines; also absent: C13orf46, PRR5L, LINC02100; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GCNT2]] | C | CAPRIN2 activity lowers GCNT2's level | lines that do not express CAPRIN2 (3) vs lines expressing it (47) | 2.13× higher at baseline in the lines without CAPRIN2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PALS2, STX2, POLR3G; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.773). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.0, 5.8); signed map (7.4, 46.9). **Vector** length 139, 45.4% of its response variance represented; |z| ≥ 3 in 1,567 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +6.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +1.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | -0.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +3.2 | +2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.0 | +1.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.6 | +0.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.6 | +2.9 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -9.4 | -6.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -8.7 | -5.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -8.6 | -5.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -8.4 | -5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -8.4 | -5.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -8.2 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | caprin family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.21 — chr12:30,709,552-30,823,302 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EEG1, FLJ22569, FLJ11391, caprin-2, RNG140; previously C1QDC1 |
| Gene groups (HGNC) | C1q domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IMN6](https://www.uniprot.org/uniprotkb/Q6IMN6) (Caprin-2):

> Promotes phosphorylation of the Wnt coreceptor LRP6, leading to increased activity of the canonical Wnt signaling pathway. Facilitates constitutive LRP6 phosphorylation by CDK14/CCNY during G2/M stage of the cell cycle, which may potentiate cells for Wnt signaling. May regulate the transport and translation of mRNAs, modulating for instance the expression of proteins involved in synaptic plasticity in neurons (By similarity). Involved in regulation of growth as erythroblasts shift from a highly …

**Summary**, from NCBI Gene [65981](https://www.ncbi.nlm.nih.gov/gene/65981):

> The protein encoded by this gene may regulate the transport of mRNA. It may play a role in the differentiation of erythroblasts. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:21259](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21259) · Entrez [65981](https://www.ncbi.nlm.nih.gov/gene/65981) · UniProt [Q6IMN6](https://www.uniprot.org/uniprotkb/Q6IMN6) · Ensembl [ENSG00000110888](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110888)

## Data

Gene col 3176: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3176); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3176, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3176]; `tensor/DDL_lfc|DDL_z.npy` [3176]; `embed/gene_vectors.npy` [3176]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3176 or target_col == 3176). Every well: [[CAPRIN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAPRIN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
