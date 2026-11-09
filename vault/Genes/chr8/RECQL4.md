---
symbol: "RECQL4"
type: "gene"
col: 8399
ensembl_id: "ENSG00000160957"
name: "RecQ like helicase 4"
location: "8q24.3"
module: 6
arm: "+"
pooled_cpm: 6.64
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 7
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# RECQL4

*RecQ like helicase 4* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.02× (z +12.0, q 3e-30, up in 45 of 47 measured lines) ⚠ cell-cycle shift, explains ~59% of this change. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.53× (z +3.3, q 0.038, up in 4 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 1 line (RKO 6.24×; ⚠ cell-cycle shift, explains ~59% of this change).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.856× (z -6.1, q 4e-07, down in 21 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.673× (z -4.2, q 0.004, down in 15 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (A498 0.262×, LoVo 0.170×; ⚠ cell-cycle shift, explains ~40% of this change); [[Tucidinostat (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0652×; ⚠ cell-cycle shift, explains ~82% of this change); [[Selinexor (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0549×; ⚠ cell-cycle shift, explains ~45% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A498 0.355×); [[Saquinavir (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.103×); [[Amsacrine (drug)]] 5 µM in 1 line (A498 0.398×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TONSL]] (+0.89, fdr 7e-06), [[PKMYT1]] (+0.84, fdr 7e-06), [[CHTF18]] (+0.84, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 16 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8399.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 1 line (RKO 6.24×; ⚠ cell-cycle shift, explains ~59% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **3.02×** | +12.0 | 3e-30 | 45/47 (RKO, SW480, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **2.48×** | +9.9 | 2e-20 | 21/26 (LS 180, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **2.28×** | +8.9 | 9e-17 | 34/45 (RKO, SW480, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **2.24×** | +8.4 | 5e-15 | 5/9 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **2.14×** | +8.2 | 2e-14 | 31/46 (RKO, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.61×** | +7.3 | 3e-11 | 23/39 (A549, NCI-H2030, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **2.05×** | +7.2 | 6e-11 | 10/15 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.55×** | +4.7 | 1e-04 | 12/32 (HS-578T, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.50×** | +4.4 | 8e-04 | 14/46 (NCI-H2030, MIA PaCa-2, …) | two highest doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.51×** | +4.3 | 0.001 | 12/38 (HS-578T, RKO, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.46×** | +3.9 | 0.005 | 13/41 (LS 180, HS-578T, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~81% of this change | **1.42×** | +3.6 | 0.013 | 10/33 (Panc 03.27, LoVo, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +3.5 | 0.022 | 10/45 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.25×** | +3.4 | 0.026 | 8/48 (SW480, HOP62, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.53×** | +3.3 | 0.038 | 4/35 (SW1417, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.052 | 10/45 (HOP62, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8399.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (A498 0.262×, LoVo 0.170×; ⚠ cell-cycle shift, explains ~40% of this change); [[Tucidinostat (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0652×; ⚠ cell-cycle shift, explains ~82% of this change); [[Selinexor (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0549×; ⚠ cell-cycle shift, explains ~45% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A498 0.355×); [[Saquinavir (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.103×); [[Amsacrine (drug)]] 5 µM in 1 line (A498 0.398×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.856× | -6.1 | 4e-07 | 21/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.574×** | -6.1 | 4e-07 | 23/44 (SK-MEL-2, HT-29, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.681×** | -6.0 | 5e-07 | 17/46 (A498, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.673×** | -4.2 | 0.004 | 15/42 (A-172, SNU-1, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.677×** | -4.0 | 0.006 | 16/44 (LS 180, SHP-77, …) | inconsistent across doses | position effect removed |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.620×** | -3.7 | 0.017 | 6/47 (A-427, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.713×** | -3.7 | 0.017 | 7/46 (KATO III, NCI-H661, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.727×** | -3.5 | 0.034 | 16/44 (MIA PaCa-2, A-427, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.752× | -3.1 | 0.11 | 13/38 (Panc 03.27, NCI-H23, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.821× | -3.1 | 0.12 | 12/47 (SNU-1, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.99 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8399. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 12.1 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.262× (z -12.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.355× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 6.10 | 0 | 2 (2 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0652× (z -10.2) ⚠ cell-cycle shift, explains ~82% of this change |
| [[LoVo (line)]] | wt | 4.31 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.170× (z -10.0) ⚠ cell-cycle shift, explains ~40% of this change |
| [[MIA PaCa-2 (line)]] | alt | 6.31 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.103× (z -8.8) |
| [[RKO (line)]] | wt | 16.7 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.24× (z +9.0) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 5.97 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0549× (z -10.1) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A-172 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8399), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TONSL]] | +0.89 | +0.85 / +0.90 | both halves | 7e-06 | STRING 402 |
| [[PKMYT1]] | +0.84 | +0.80 / +0.84 | both halves | 7e-06 | STRING 621 |
| [[CHTF18]] | +0.84 | +0.83 / +0.84 | both halves | 7e-06 | STRING 951 |
| [[POLE]] | +0.83 | +0.82 / +0.83 | both halves | 7e-06 | STRING 711 |
| [[FANCA]] | +0.83 | +0.79 / +0.82 | both halves | 7e-06 | STRING 662 |
| [[RAD51]] | +0.82 | +0.79 / +0.81 | both halves | 7e-06 | STRING 982 |
| [[CDC45]] | +0.81 | +0.77 / +0.80 | both halves | 7e-06 | STRING 982 |
| [[NCAPH2]] | +0.81 | +0.80 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[RAD54L]] | +0.80 | +0.78 / +0.77 | both halves | 7e-06 | STRING 820 |
| [[XRCC3]] | +0.80 | +0.73 / +0.82 | both halves | 7e-06 | STRING 905 |
| [[RRM2]] | +0.79 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[GINS2]] | +0.79 | +0.74 / +0.77 | both halves | 7e-06 | STRING 556 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises RECQL4's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.98× lower at baseline in the lines without CDC25A | 0.020 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises RECQL4's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.04× lower at baseline in the lines without TCF19 | 0.074 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[ZNF367]] | C | ZNF367 activity raises RECQL4's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 2.12× lower at baseline in the lines without ZNF367 | 0.038 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |
| [[MCM3]] | C | MCM3's natural level weakens RECQL4's drug response | MCM3's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.39; direction not clear | 0.076 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.808). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.8, -43.0); signed map (-36.1, -45.6). **Vector** length 82.2, 16.2% of its response variance represented; |z| ≥ 3 in 899 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.61 to 65); *DNA strand elongation* (reactome, mean cos +0.65 to 28); *DNA Replication* (reactome, mean cos +0.65 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +4.1 | +12.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +3.3 | +8.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +3.2 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | +2.7 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | +2.4 | +9.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +3.3 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.4 | +2.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.3 | +2.6 |
|  | [[Methotrexate (drug)]] 5 µM |  | +1.3 | +1.0 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -4.8 | -6.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -4.7 | -6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | -3.9 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -3.7 | -3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -3.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | RecQ like helicase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,511,288-144,517,845 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RecQ4 |
| Gene groups (HGNC) | RecQ like helicases |
| Matched by | ensembl_id |

**Function**, from UniProt [O94761](https://www.uniprot.org/uniprotkb/O94761) (ATP-dependent DNA helicase Q4):

> An ATP-dependent DNA helicase which unwinds dsDNA with a 3'-overhang in a 3'-5' direction. Does not unwind more than 18 bp of dsDNA. May modulate chromosome segregation. The N-terminal domain (residues 1-54) binds DNA Y-shaped DNA better than ss- or dsDNA. The core helicase domain binds ssDNA.

**Summary**, from NCBI Gene [9401](https://www.ncbi.nlm.nih.gov/gene/9401):

> The protein encoded by this gene is a DNA helicase that belongs to the RecQ helicase family. DNA helicases unwind double-stranded DNA into single-stranded DNAs and may modulate chromosome segregation. This gene is predominantly expressed in thymus and testis. Mutations in this gene are associated with Rothmund-Thomson, RAPADILINO and Baller-Gerold syndromes. [provided by RefSeq, Jan 2010]

**Accessions** — [HGNC:9949](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9949) · Entrez [9401](https://www.ncbi.nlm.nih.gov/gene/9401) · UniProt [O94761](https://www.uniprot.org/uniprotkb/O94761) · Ensembl [ENSG00000160957](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160957)

## Data

Gene col 8399: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8399); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8399, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8399]; `tensor/DDL_lfc|DDL_z.npy` [8399]; `embed/gene_vectors.npy` [8399]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8399 or target_col == 8399). Every well: [[RECQL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RECQL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
