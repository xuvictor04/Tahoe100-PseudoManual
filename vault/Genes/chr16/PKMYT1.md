---
symbol: "PKMYT1"
type: "gene"
col: 4822
ensembl_id: "ENSG00000127564"
name: "protein kinase, membrane associated tyrosine/threonine 1"
location: "16p13.3"
module: 6
arm: "+"
pooled_cpm: 5.85
n_lines_expressing: 47
n_dd_up: 25
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 25
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# PKMYT1

*protein kinase, membrane associated tyrosine/threonine 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (24 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.43× (z +10.7, q 6e-24, up in 10 of 10 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.42× (z +3.0, q 0.062, up in 10 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A498 4.67×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.596× (z -6.6, q 2e-08, down in 23 of 42 measured lines) ⚠ cell-cycle shift, explains ~57% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (A498 0.138×, A-427 0.183×; ⚠ cell-cycle shift, explains ~57% of this change); [[Amsacrine (drug)]] 5 µM in 1 line (LS 180 0.120×); [[Demeclocycline (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0618×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[E2F1]] (+0.90, fdr 7e-06), [[CENPM]] (+0.88, fdr 7e-06), [[MCM10]] (+0.87, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); 25 go from it, the strongest it → [[AURKB]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 24 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 24 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4822.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A498 4.67×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **3.43×** | +10.7 | 6e-24 | 10/10 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **2.91×** | +9.6 | 2e-19 | 22/24 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **2.51×** | +7.7 | 3e-12 | 14/15 (SW480, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.64×** | +6.3 | 4e-08 | 24/38 (A549, SNU-423, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~62% of this change | **1.88×** | +5.4 | 6e-06 | 12/28 (A549, MIA PaCa-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.76×** | +4.9 | 9e-05 | 14/35 (PANC-1, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.70×** | +4.8 | 2e-04 | 14/27 (PANC-1, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.42×** | +4.5 | 6e-04 | 19/42 (SNU-1, AsPC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.64×** | +4.4 | 6e-04 | 15/37 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~58% of this change | **1.67×** | +4.4 | 6e-04 | 12/28 (SW480, PANC-1, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.65×** | +4.3 | 7e-04 | 17/40 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.60×** | +4.2 | 0.001 | 12/42 (SW480, KATO III, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.37×** | +4.0 | 0.003 | 15/45 (SW480, NCI-H460, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.33×** | +3.8 | 0.006 | 4/16 (J82, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.49×** | +3.6 | 0.011 | 9/43 (A549, SW480, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.42×** | +3.0 | 0.062 | 10/41 (C32, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4822.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (A498 0.138×, A-427 0.183×; ⚠ cell-cycle shift, explains ~57% of this change); [[Amsacrine (drug)]] 5 µM in 1 line (LS 180 0.120×); [[Demeclocycline (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0618×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.596×** | -6.6 | 2e-08 | 23/42 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.455×** | -5.1 | 1e-04 | 20/44 (COLO 205, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.587×** | -4.8 | 2e-04 | 20/40 (SNU-1, A498, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.613×** | -4.2 | 0.004 | 21/40 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.694× | -3.3 | 0.10 | 12/36 (A498, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.511× | -3.0 | 0.20 | 13/35 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | 0.513× | -3.0 | 0.20 | 13/41 (A498, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.10 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4822. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 13.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.67× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | [[Selinexor (drug)]] 5 µM 0.138× (z -16.4) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A-427 (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.183× (z -11.4) ⚠ cell-cycle shift, explains ~57% of this change |
| [[HEC-1-A (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -9.0) ⚠ cell-cycle shift, explains ~78% of this change |
| [[LS 180 (line)]] | wt | 5.83 | 0 | 1 | — | [[Amsacrine (drug)]] 5 µM 0.120× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 4.97 | 0 | 1 | — | [[Demeclocycline (drug)]] 0.05 µM 0.0618× (z -9.4) |
| [[A-172 (line)]] | wt | 8.83 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.05 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4822), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[E2F1]] | +0.90 | +0.89 / +0.89 | both halves | 7e-06 | pathway: Mitotic G2-G2/M phases; STRING 699 |
| [[CENPM]] | +0.88 | +0.90 / +0.86 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 568 |
| [[MCM10]] | +0.87 | +0.86 / +0.85 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 466 |
| [[XRCC3]] | +0.87 | +0.84 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[MYBL2]] | +0.87 | +0.89 / +0.83 | both halves | 7e-06 | pathway: G2/M Transition; STRING 621 |
| [[CDC45]] | +0.86 | +0.86 / +0.83 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 736 |
| [[WDR76]] | +0.85 | +0.87 / +0.82 | both halves | 7e-06 |  |
| [[E2F2]] | +0.85 | +0.83 / +0.84 | both halves | 7e-06 | STRING 463 |
| [[DTL]] | +0.85 | +0.85 / +0.82 | both halves | 7e-06 | STRING 412 |
| [[CLSPN]] | +0.85 | +0.87 / +0.82 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[CHAF1A]] | +0.85 | +0.84 / +0.84 | both halves | 7e-06 |  |
| [[MCM4]] | +0.84 | +0.86 / +0.81 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 586 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises PKMYT1's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.24× lower at baseline in the lines without CDC25A | 0.017 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises PKMYT1's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.12× lower at baseline in the lines without E2F2 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises PKMYT1's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.22× lower at baseline in the lines without E2F8 | 0.053 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[TCF19]] | C | TCF19 activity raises PKMYT1's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.59× lower at baseline in the lines without TCF19 | 0.028 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent; co-absent with the target |
| [[ZNF367]] | C | ZNF367 activity raises PKMYT1's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 2.30× lower at baseline in the lines without ZNF367 | 0.044 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises PKMYT1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.59× lower at baseline in the lines without AURKB | 0.050 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[MYBL2]] | C | MYBL2 activity raises PKMYT1's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.42× lower at baseline in the lines without MYBL2 | 0.061 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises PKMYT1's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.21× lower at baseline in the lines without MCM10 | 0.086 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises PKMYT1's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.40× lower at baseline in the lines without E2F1, MCM3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 0, C 25. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AURKB]] | C | PKMYT1 activity raises AURKB's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 4.05× lower at baseline in the lines without PKMYT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent; co-absent with the target; its own permutation p |
| [[DIAPH3]] | C | PKMYT1 activity raises DIAPH3's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 3.89× lower at baseline in the lines without PKMYT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent; co-absent with the target; its own permutation p |
| [[SKA3]] | C | PKMYT1 activity raises SKA3's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 3.54× lower at baseline in the lines without PKMYT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent; co-absent with the target; its own permutation p |
| [[MCM4]] | C | PKMYT1 activity raises MCM4's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 3.22× lower at baseline in the lines without PKMYT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent; co-absent with the target; its own permutation p |
| [[CENPK]] | C | PKMYT1 activity raises CENPK's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 3.07× lower at baseline in the lines without PKMYT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent; co-absent with the target; its own permutation p |
| [[PCLAF]] | C | PKMYT1 activity raises PCLAF's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 2.76× lower at baseline in the lines without PKMYT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent; its own permutation p |
| [[CENPU]] | C | PKMYT1 activity raises CENPU's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 2.53× lower at baseline in the lines without PKMYT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent; its own permutation p |
| [[CHTF18]] | C | PKMYT1 activity raises CHTF18's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 2.33× lower at baseline in the lines without PKMYT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent; its own permutation p |
| [[BRIP1]] | C | PKMYT1 activity raises BRIP1's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 2.24× lower at baseline in the lines without PKMYT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent; its own permutation p |
| [[C9orf40]] | C | PKMYT1 activity raises C9orf40's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 1.89× lower at baseline in the lines without PKMYT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent; its own permutation p |
| [[MCM6]] | C | PKMYT1 activity raises MCM6's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 3.27× lower at baseline in the lines without PKMYT1 | 0.061 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent; co-absent with the target |
| [[DTL]] | C | PKMYT1 activity raises DTL's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 2.66× lower at baseline in the lines without PKMYT1 | 0.069 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.874). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.4, -44.5); signed map (-38.0, -45.6). **Vector** length 82.0, 18.6% of its response variance represented; |z| ≥ 3 in 802 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.66 to 65); *DNA strand elongation* (reactome, mean cos +0.71 to 28); *DNA Replication* (reactome, mean cos +0.70 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | +3.8 | +9.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | +3.6 | +10.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~62% of this change | +3.5 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | +3.3 | +7.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +3.1 | +4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +1.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.6 | +2.2 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +1.4 | +1.8 |
|  | [[Gemcitabine (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.1 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -4.2 | -4.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -3.9 | -6.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -3.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | -3.1 | -4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.6 | -1.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[palbociclib (drug)]] 5 µM |  | -1.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase, membrane associated tyrosine/threonine 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,968,024-2,980,479 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MYT1, PPP1R126 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; WEE family dual specificity kinases |
| Reactome | 9 pathways, smallest: G2/M DNA replication checkpoint; Polo-like kinase mediated events; Cyclin A/B1/B2 associated events during G2/M transition |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99640](https://www.uniprot.org/uniprotkb/Q99640) (Membrane-associated tyrosine- and threonine-specific cdc2-inhibitory kinase):

> Acts as a negative regulator of entry into mitosis (G2 to M transition) by phosphorylation of the CDK1 kinase specifically when CDK1 is complexed to cyclins. Mediates phosphorylation of CDK1 predominantly on 'Thr-14'. Also involved in Golgi fragmentation. May be involved in phosphorylation of CDK1 on 'Tyr-15' to a lesser degree, however tyrosine kinase activity is unclear and may be indirect.

**Summary**, from NCBI Gene [9088](https://www.ncbi.nlm.nih.gov/gene/9088):

> This gene encodes a member of the serine/threonine protein kinase family. The encoded protein is a membrane-associated kinase that negatively regulates the G2/M transition of the cell cycle by phosphorylating and inactivating cyclin-dependent kinase 1. The activity of the encoded protein is regulated by polo-like kinase 1. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, May 2012]

**Accessions** — [HGNC:29650](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29650) · Entrez [9088](https://www.ncbi.nlm.nih.gov/gene/9088) · UniProt [Q99640](https://www.uniprot.org/uniprotkb/Q99640) · Ensembl [ENSG00000127564](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127564)

## Data

Gene col 4822: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4822); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4822, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4822]; `tensor/DDL_lfc|DDL_z.npy` [4822]; `embed/gene_vectors.npy` [4822]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4822 or target_col == 4822). Every well: [[PKMYT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKMYT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
