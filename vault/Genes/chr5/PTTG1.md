---
symbol: "PTTG1"
type: "gene"
col: 8971
ensembl_id: "ENSG00000164611"
name: "PTTG1 regulator of sister chromatid separation, securin"
location: "5q33.3"
module: 22
arm: "+"
pooled_cpm: 41.65
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 1
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# PTTG1

*PTTG1 regulator of sister chromatid separation, securin* — 5q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.46× (z +6.5, q 6e-08, up in 36 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.48× (z +4.0, q 0.006, up in 29 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (hTERT-HPNE 5.22×, NCI-H1792 5.69×, AsPC-1 4.63×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H460 4.78×, PANC-1 4.25×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 3.47×).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.552× (z -4.0, q 0.029, down in 28 of 48 measured lines) ⚠ cell-cycle shift, explains ~99% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 3 lines (A-427 0.268×, H4 0.187×, SNU-1 0.231×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (H4 0.108×; ⚠ cell-cycle shift, would explain all of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM in 1 line (H4 0.122×; ⚠ cell-cycle shift, explains ~84% of this change); [[Amsacrine (drug)]] 5 µM in 1 line (H4 0.218×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDKN3]] (+0.88, fdr 7e-06), [[CKAP2]] (+0.87, fdr 7e-06), [[NEK2]] (+0.87, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CDC25C]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 13 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8971.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (hTERT-HPNE 5.22×, NCI-H1792 5.69×, AsPC-1 4.63×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H460 4.78×, PANC-1 4.25×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 3.47×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **2.46×** | +6.5 | 6e-08 | 36/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **2.30×** | +5.8 | 2e-06 | 33/38 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **2.17×** | +5.6 | 5e-06 | 43/47 (NCI-H23, KATO III, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~91% of this change | **2.13×** | +5.4 | 8e-06 | 44/47 (SW 900, HOP62, …) | all doses, flat | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.76×** | +4.1 | 0.005 | 34/48 (KATO III, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.76×** | +4.1 | 0.005 | 29/48 (NCI-H1792, SW1417, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.0 | 0.006 | 29/47 (A549, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.48×** | +3.9 | 0.008 | 36/48 (KATO III, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.70×** | +3.8 | 0.009 | 31/48 (KATO III, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.69×** | +3.8 | 0.009 | 32/48 (KATO III, A549, …) | all doses, stronger at high dose | position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **2.78×** | +3.6 | 0.014 | 35/47 (J82, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~88% of this change | **1.61×** | +3.3 | 0.044 | 28/47 (A-172, H4, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **1.67×** | +3.1 | 0.092 | 25/41 (C-33 A, A-172, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | 1.52× | +3.0 | 0.10 | 25/48 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8971.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 3 lines (A-427 0.268×, H4 0.187×, SNU-1 0.231×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (H4 0.108×; ⚠ cell-cycle shift, would explain all of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM in 1 line (H4 0.122×; ⚠ cell-cycle shift, explains ~84% of this change); [[Amsacrine (drug)]] 5 µM in 1 line (H4 0.218×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~99% of this change | **0.552×** | -4.0 | 0.029 | 28/48 (SW 1271, LOX-IMVI, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.581×** | -3.9 | 0.029 | 34/48 (HS-578T, NCI-H23, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | 0.624× | -3.2 | 0.15 | 26/48 (LoVo, HOP62, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.640× | -3.2 | 0.15 | 29/48 (H4, A-427, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.643× | -3.2 | 0.15 | 25/48 (NCI-H2030, NCI-H2347, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.650× | -3.1 | 0.15 | 31/48 (NCI-H661, NCI-H2030, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.733× | -3.1 | 0.15 | 29/48 (A-427, HCT15, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | 0.735× | -3.0 | 0.15 | 29/48 (KATO III, PANC-1, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | 0.653× | -3.0 | 0.15 | 24/48 (H4, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +1.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8971. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 57.5 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.187× (z -10.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.218× (z -9.0) |
| [[A-427 (line)]] | wt | 62.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.268× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 32.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +8.6) | — |
| [[AsPC-1 (line)]] | alt | 13.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[hTERT-HPNE (line)]] | wt | 33.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1792 (line)]] | alt | 15.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.69× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 34.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | — |
| [[PANC-1 (line)]] | alt | 41.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | — |
| [[SNU-1 (line)]] | wt | 37.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.231× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 71.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 86.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 95.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 50.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8971), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN3]] | +0.88 | +0.83 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 840 |
| [[CKAP2]] | +0.87 | +0.87 / +0.85 | both halves | 7e-06 | STRING 413 |
| [[NEK2]] | +0.87 | +0.88 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 890 |
| [[CDCA2]] | +0.87 | +0.85 / +0.84 | both halves | 7e-06 | STRING 555 |
| [[DLGAP5]] | +0.87 | +0.90 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 913 |
| [[PIF1]] | +0.86 | +0.89 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[FAM72D]] | +0.86 | +0.84 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[CDCA8]] | +0.86 | +0.89 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 893 |
| [[KIF20A]] | +0.85 | +0.86 / +0.83 | both halves | 7e-06 | STRING 900 |
| [[CCNB2]] | +0.85 | +0.86 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 970 |
| [[CCNF]] | +0.84 | +0.84 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 515 |
| [[KIF2C]] | +0.84 | +0.85 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 875 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises PTTG1's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.30× lower at baseline in the lines without PIMREG | 0.001 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NEURL1B]] | B | NEURL1B activity raises PTTG1's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.88× lower at baseline in the lines without NEURL1B | 0.013 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[FAM72B]] | B | FAM72B activity raises PTTG1's level | lines that do not express FAM72B (6) vs lines expressing it (44) | 1.71× lower at baseline in the lines without FAM72B | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC02798, SRGAP2C, ZNF512B; its own permutation p |
| [[AURKB]] | C | AURKB activity raises PTTG1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.53× lower at baseline in the lines without AURKB | 0.005 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[CDC20]] | C | CDC20 activity raises PTTG1's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.33× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[ACBD7]] | C | ACBD7 activity raises PTTG1's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 1.91× lower at baseline in the lines without ACBD7 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent; its own permutation p |
| [[FAM72D]] | C | FAM72D activity raises PTTG1's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.15× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[CDCA3]] | C | CDCA3 activity raises PTTG1's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 2.47× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25C]] | C | PTTG1's natural level strengthens CDC25C's drug response | PTTG1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.08; direction not clear | 0.077 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.834). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.1, -57.5); signed map (-51.2, -41.4). **Vector** length 116, 45.7% of its response variance represented; |z| ≥ 3 in 907 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.77 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.62 to 48); *Resolution of Sister Chromatid Cohesion* (reactome, mean cos +0.66 to 33).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +2.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~91% of this change | +4.0 | +5.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | +3.9 | +3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.7 | +2.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | +2.3 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.6 | +1.4 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +2.3 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +1.9 | +2.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | -2.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.8 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -1.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~99% of this change | -5.3 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.9 | -0.9 |
|  | [[EX229 (drug)]] 5 µM |  | -3.9 | -2.8 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -3.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | PTTG1 regulator of sister chromatid separation, securin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.3 — chr5:160,421,855-160,428,739 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PTTG, HPTTG, EAP1, securin, ECRAR; previously TUTR1 |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 12 pathways, smallest: APC/C:Cdc20 mediated degradation of Securin; APC/C:Cdh1 mediated degradation of Cdc20 and other APC/C:Cdh1 targeted proteins in late mitosis/early G1; APC/C:Cdc20 mediated degradation of mitotic proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [O95997](https://www.uniprot.org/uniprotkb/O95997) (Securin):

> Regulatory protein, which plays a central role in chromosome stability, in the p53/TP53 pathway, and DNA repair. Probably acts by blocking the action of key proteins. During the mitosis, it blocks Separase/ESPL1 function, preventing the proteolysis of the cohesin complex and the subsequent segregation of the chromosomes. At the onset of anaphase, it is ubiquitinated, conducting to its destruction and to the liberation of ESPL1. Its function is however not limited to a blocking activity, since …

**Summary**, from NCBI Gene [9232](https://www.ncbi.nlm.nih.gov/gene/9232):

> The encoded protein is a homolog of yeast securin proteins, which prevent separins from promoting sister chromatid separation. It is an anaphase-promoting complex (APC) substrate that associates with a separin until activation of the APC. The gene product has transforming activity in vitro and tumorigenic activity in vivo, and the gene is highly expressed in various tumors. The gene product contains 2 PXXP motifs, which are required for its transforming and tumorigenic activities, as well as …

**Accessions** — [HGNC:9690](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9690) · Entrez [9232](https://www.ncbi.nlm.nih.gov/gene/9232) · UniProt [O95997](https://www.uniprot.org/uniprotkb/O95997) · Ensembl [ENSG00000164611](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164611)

## Data

Gene col 8971: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8971); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8971, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8971]; `tensor/DDL_lfc|DDL_z.npy` [8971]; `embed/gene_vectors.npy` [8971]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8971 or target_col == 8971). Every well: [[PTTG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTTG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
