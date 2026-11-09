---
symbol: "FZD8"
type: "gene"
col: 10807
ensembl_id: "ENSG00000177283"
name: "frizzled class receptor 8"
location: "10p11.21"
module: 112
arm: "+"
pooled_cpm: 6.17
n_lines_expressing: 30
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 8
direction_downstream: 3
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# FZD8

*frizzled class receptor 8* — 10p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.08× (z +12.0, q 2e-30, up in 13 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.556× (z -4.3, q 0.010, down in 16 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HS-578T 0.224×, C-33 A 0.332×); [[Dexamethasone (drug)]] 5 µM in 2 lines (H4 0.0723×, HS-578T 0.219×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.0952×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change); [[Betamethasone dipropionate (drug)]] 0.5 µM in 1 line (H4 0.0409×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTHLH]] (+0.68, fdr 7e-06), [[FAM43A]] (+0.67, fdr 7e-06), [[INHBA]] (+0.66, fdr 7e-06); moves opposite to [[ACSL1]] (-0.56, fdr 1e-05), [[CLASP1]] (-0.53, fdr 1e-05), [[CHPT1]] (-0.51, fdr 1e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LINC02968]] → it (grade B ⚠); 3 go from it, the strongest it → [[BCL11B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10807.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.08×** | +12.0 | 2e-30 | 13/24 (J82, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.75×** | +10.8 | 8e-25 | 13/26 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.06×** | +8.5 | 5e-15 | 13/25 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.15×** | +8.3 | 1e-14 | 3/15 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.87×** | +6.7 | 3e-09 | 17/27 (BT-474, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.33×** | +6.4 | 1e-08 | 7/20 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.30×** | +6.0 | 1e-07 | 13/26 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +5.6 | 2e-06 | 8/22 (J82, HOP62, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +5.3 | 7e-06 | 9/19 (BT-474, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.90×** | +4.9 | 7e-05 | 12/26 (MIA PaCa-2, LOX-IMVI, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +4.7 | 2e-04 | 6/27 (SW 900, J82, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.92×** | +4.5 | 3e-04 | 3/16 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.72×** | +4.1 | 0.002 | 9/18 (CFPAC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.73×** | +4.0 | 0.003 | 14/26 (NCI-H1573, CFPAC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.68×** | +3.9 | 0.003 | 10/27 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +3.6 | 0.011 | 11/27 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +3.1 | 0.050 | 13/26 (BT-474, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.54×** | +3.0 | 0.078 | 7/24 (NCI-H460, C32, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10807.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HS-578T 0.224×, C-33 A 0.332×); [[Dexamethasone (drug)]] 5 µM in 2 lines (H4 0.0723×, HS-578T 0.219×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.0952×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change); [[Betamethasone dipropionate (drug)]] 0.5 µM in 1 line (H4 0.0409×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.556×** | -4.3 | 0.010 | 16/25 (A-172, NCI-H460, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | **0.601×** | -3.9 | 0.030 | 15/27 (H4, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.653× | -3.3 | 0.14 | 13/26 (H4, HS-578T, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | 0.655× | -3.2 | 0.14 | 9/27 (H4, HS-578T, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.655× | -3.2 | 0.14 | 12/26 (HS-578T, H4, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.661× | -3.2 | 0.15 | 9/26 (H4, HS-578T, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.648× | -3.1 | 0.18 | 9/26 (MIA PaCa-2, BT-474, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10807. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 36.4 | 0 | 11 (1 ⚠) | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.0409× (z -14.5) |
| [[HS-578T (line)]] | alt | 48.3 | 0 | 11 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -13.7) |
| [[NCI-H460 (line)]] | wt | 15.0 | 5 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 15.5× (z +15.0) | — |
| [[C-33 A (line)]] | alt | 60.7 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0952× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 8.57 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 19.2× (z +12.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 11.1× (z +10.8) | — |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.52× (z +9.3) | [[Clobetasol propionate (drug)]] 5 µM 0.0680× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 10.2 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.319× (z -14.6) ⚠ position not correctable · without an alert: [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.0443× (z -10.8) |
| [[A-172 (line)]] | wt | 14.2 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.256× (z -8.5) |
| [[A498 (line)]] | wt | 3.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.72× (z +9.5) | — |
| [[BT-474 (line)]] | alt | 8.71 | 0 | 1 | — | [[Neratinib (drug)]] 0.5 µM 0.0372× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.60× (z +14.3) | — |
| [[HOP62 (line)]] | alt | 4.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 7.93 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0567× (z -8.8) ⚠ cell-cycle shift, explains ~71% of this change |
| [[A-427 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.843 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.559 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.826 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.455 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.872 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.985 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.664 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.850 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10807), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTHLH]] | +0.68 | +0.60 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[FAM43A]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[INHBA]] | +0.66 | +0.63 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[SYNJ2]] | +0.64 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[MEG8]] | +0.62 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[CXCL8]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[LINC00973]] | +0.62 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[HBEGF]] | +0.62 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[IER3]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[AFF3]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[ISG20]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[GJA1]] | +0.60 | +0.50 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACSL1]] | -0.56 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[CLASP1]] | -0.53 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[CHPT1]] | -0.51 | -0.51 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02968]] | B | LINC02968 activity raises FZD8's level | lines that do not express LINC02968 (27) vs lines expressing it (23) | 2.03× lower at baseline in the lines without LINC02968 | 0.050 | ⚠ within organs, on part of the lines; also absent: LCP1, OR9Q1, IL11 |
| [[COL5A3]] | B | COL5A3 activity raises FZD8's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 1.76× lower at baseline in the lines without COL5A3 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1 |
| [[ANXA10]] | B | ANXA10 activity raises FZD8's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 1.68× lower at baseline in the lines without ANXA10 | 0.061 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP |
| [[TOP2A]] | B | TOP2A activity lowers FZD8's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MEG3]] | C | MEG3 activity raises FZD8's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 2.47× lower at baseline in the lines without MEG3 | 0.019 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8; co-absent with the target |
| [[MIR493HG]] | C | MIR493HG activity raises FZD8's level | lines that do not express MIR493HG (36) vs lines expressing it (14) | 2.36× lower at baseline in the lines without MIR493HG | 0.049 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252; co-absent with the target |
| [[ADAMTSL1]] | C | ADAMTSL1 activity raises FZD8's level | lines that do not express ADAMTSL1 (18) vs lines expressing it (32) | 2.70× lower at baseline in the lines without ADAMTSL1 | 0.065 | ⚠ within organs, on part of the lines; also absent: SHOX2, ACTN2, AK5; maybe low, not absent; co-absent with the target |
| [[SYNJ2]] | C | SYNJ2 activity lowers FZD8's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 2.17× higher at baseline in the lines without SYNJ2 | 0.090 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL11B]] | B | FZD8 activity raises BCL11B's level | lines that do not express FZD8 (20) vs lines expressing it (30) | 1.51× lower at baseline in the lines without FZD8 | 0.098 | ⚠ within organs, on part of the lines; also absent: RNF182, NRG1, FBXL7 |
| [[KCNMA1]] | C | FZD8 activity raises KCNMA1's level | lines that do not express FZD8 (20) vs lines expressing it (30) | 7.03× lower at baseline in the lines without FZD8 | 0.077 | ⚠ within organs, on part of the lines; also absent: RNF182, NRG1, FBXL7; co-absent with the target |
| [[AFF3]] | C | FZD8 activity raises AFF3's level | lines that do not express FZD8 (20) vs lines expressing it (30) | 5.17× lower at baseline in the lines without FZD8 | 0.0995 | ⚠ within organs, on part of the lines; also absent: RNF182, NRG1, FBXL7; co-absent with the target |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.690). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.9, 13.6); signed map (19.1, 50.3). **Vector** length 72.4, 17.2% of its response variance represented; |z| ≥ 3 in 741 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interleukin-10 signaling* (reactome, mean cos +0.52 to 5); *inflammatory response* (hallmark, mean cos +0.51 to 6); *Interleukin-4 and Interleukin-13 signaling* (reactome, mean cos +0.52 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +10.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +12.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +4.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +4.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +1.2 |
| fall | [[Clobetasol propionate (drug)]] 5 µM |  | -2.9 | -3.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.8 | -3.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.8 | -3.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.6 | -2.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.4 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | frizzled class receptor 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p11.21 — chr10:35,638,247-35,642,296 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FZ-8 |
| Gene groups (HGNC) | G protein-coupled receptors, Class F frizzled; MicroRNA protein coding host genes |
| Hallmark sets | WNT_BETA_CATENIN_SIGNALING, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 12 pathways, smallest: Signaling by RNF43 mutants; Regulation of FZD by ubiquitination; Signaling by WNT in cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H461](https://www.uniprot.org/uniprotkb/Q9H461) (Frizzled-8):

> Receptor for Wnt proteins. Component of the Wnt-Fzd-LRP5-LRP6 complex that triggers beta-catenin signaling through inducing aggregation of receptor-ligand complexes into ribosome-sized signalosomes. The beta-catenin canonical signaling pathway leads to the activation of disheveled proteins, inhibition of GSK-3 kinase, nuclear accumulation of beta-catenin and activation of Wnt target genes. A second signaling pathway involving PKC and calcium fluxes has been seen for some family members, but it …

**Summary**, from NCBI Gene [8325](https://www.ncbi.nlm.nih.gov/gene/8325):

> This intronless gene is a member of the frizzled gene family. Members of this family encode seven-transmembrane domain proteins that are receptors for the Wingless type MMTV integration site family of signaling proteins. Most frizzled receptors are coupled to the beta-catenin canonical signaling pathway. This gene is highly expressed in two human cancer cell lines, indicating that it may play a role in several types of cancer. The crystal structure of the extracellular cysteine-rich domain of a …

**Accessions** — [HGNC:4046](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4046) · Entrez [8325](https://www.ncbi.nlm.nih.gov/gene/8325) · UniProt [Q9H461](https://www.uniprot.org/uniprotkb/Q9H461) · Ensembl [ENSG00000177283](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177283)

## Data

Gene col 10807: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10807); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10807, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10807]; `tensor/DDL_lfc|DDL_z.npy` [10807]; `embed/gene_vectors.npy` [10807]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10807 or target_col == 10807). Every well: [[FZD8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FZD8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
