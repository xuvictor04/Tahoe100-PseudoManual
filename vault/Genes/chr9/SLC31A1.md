---
symbol: "SLC31A1"
type: "gene"
col: 5924
ensembl_id: "ENSG00000136868"
name: "solute carrier family 31 member 1"
location: "9q32"
module: 56
arm: "+"
pooled_cpm: 87.46
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 26
n_dd_up_clean: 7
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# SLC31A1

*solute carrier family 31 member 1* — 9q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.12× (z +9.4, q 3e-18, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.64× (z +6.2, q 8e-08, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (3 with an alert ⚠); the strongest is [[Belumosudil (drug)]] 5 µM: 0.599× (z -6.2, q 4e-07, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMED9]] (+0.79, fdr 7e-06), [[P4HB]] (+0.79, fdr 7e-06), [[COG6]] (+0.79, fdr 7e-06).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FBXO16]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Anethole trithione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5924.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.12×** | +9.4 | 3e-18 | 44/48 (SNU-423, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.06×** | +9.0 | 5e-17 | 40/48 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.01×** | +8.7 | 4e-16 | 41/48 (SNU-423, A-427, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +6.2 | 8e-08 | 38/48 (NCI-H23, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +5.6 | 2e-06 | 34/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +5.1 | 4e-05 | 35/48 (HEC-1-A, NCI-H2030, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.95×** | +4.4 | 0.001 | 37/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.33×** | +3.6 | 0.021 | 26/48 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.021 | 26/48 (LOX-IMVI, RKO, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.32×** | +3.5 | 0.028 | 30/48 (A-427, LOX-IMVI, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.47×** | +3.4 | 0.034 | 30/48 (MIA PaCa-2, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.31×** | +3.4 | 0.037 | 25/48 (SNU-423, J82, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.30×** | +3.3 | 0.049 | 25/48 (SNU-1, HOP62, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.052 | 26/49 (NCI-H2347, J82, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.29×** | +3.2 | 0.058 | 23/48 (HOP62, SNU-1, …) | all doses, stronger at high dose |  |
| [[Fluvoxamine (maleate) (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.079 | 21/48 (CFPAC-1, J82, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5924.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **0.599×** | -6.2 | 4e-07 | 42/48 (NCI-H1573, RKO, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.661×** | -5.0 | 2e-04 | 33/48 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.679×** | -4.8 | 2e-04 | 30/48 (A498, HT-29, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.744×** | -4.6 | 5e-04 | 31/48 (A498, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.716×** | -4.2 | 0.003 | 34/49 (CFPAC-1, HT-29, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.752×** | -3.6 | 0.028 | 23/48 (A498, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.737×** | -3.5 | 0.028 | 25/44 (SHP-77, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.738×** | -3.5 | 0.028 | 23/47 (A498, SW1417, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.797×** | -3.5 | 0.028 | 25/48 (HS-578T, A498, …) | rises with dose | low cells (technical?) |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.760×** | -3.4 | 0.033 | 25/48 (H4, CFPAC-1, …) | rises with dose |  |
| [[Arbutin (drug)]] 0.05 µM |  | **0.745×** | -3.4 | 0.033 | 24/48 (HepG2/C3A, SNU-1, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.757×** | -3.3 | 0.048 | 24/48 (AsPC-1, RKO, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.773×** | -3.2 | 0.056 | 22/48 (HT-29, LOX-IMVI, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.776×** | -3.2 | 0.056 | 23/48 (HT-29, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.777×** | -3.2 | 0.056 | 20/49 (NCI-H1573, HT-29, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.778×** | -3.1 | 0.056 | 22/49 (H4, HT-29, …) | inconsistent across doses | position effect removed |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.779×** | -3.1 | 0.056 | 24/49 (HT-29, LS 180, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.780×** | -3.1 | 0.056 | 20/48 (LS 180, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5924. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 273 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -20.0) |
| [[LOX-IMVI (line)]] | wt | 68.9 | 3 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.37× (z +9.6) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 76.5 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.30× (z +9.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SNU-423 (line)]] | alt | 68.3 | 3 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.38× (z +9.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[A-427 (line)]] | wt | 30.7 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.54× (z +9.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HS-578T (line)]] | alt | 108 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -13.3) |
| [[KATO III (line)]] | alt | 168 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 44.0 | 2 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.69× (z +9.0) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[RKO (line)]] | wt | 145 | 1 (1 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.70× (z +8.6) ⚠ cell-cycle shift, explains ~26% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 62.0 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.72× (z +9.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[AsPC-1 (line)]] | alt | 84.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.337× (z -8.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 66.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 177 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -14.8) |
| [[HOP62 (line)]] | alt | 70.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 31.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -9.4) |
| [[NCI-H661 (line)]] | alt | 54.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -8.9) |
| [[SHP-77 (line)]] | alt | 77.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -12.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 80.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -8.7) |
| [[A-172 (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 56.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 89.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 78.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 71.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 82.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 134 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 98.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 98.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 87.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 84.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 99.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 76.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5924), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED9]] | +0.79 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[P4HB]] | +0.79 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[COG6]] | +0.79 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[GFPT1]] | +0.79 | +0.72 / +0.80 | both halves | 7e-06 |  |
| [[KDELR2]] | +0.77 | +0.78 / +0.74 | both halves | 7e-06 |  |
| [[TMEM263]] | +0.76 | +0.78 / +0.74 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.75 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[TXNDC11]] | +0.75 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[LMAN1]] | +0.74 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[IER3IP1]] | +0.74 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[COPA]] | +0.74 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[GPR107]] | +0.74 | +0.79 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO16]] | B | FBXO16 activity lowers SLC31A1's level | lines that do not express FBXO16 (9) vs lines expressing it (41) | 1.44× higher at baseline in the lines without FBXO16 | 0.034 | ⚠ within organs, on part of the lines; also absent: FZD3, PTPRU, OTUD7A; maybe low, not absent |
| [[SNHG18]] | B | SNHG18 activity raises SLC31A1's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.40× lower at baseline in the lines without SNHG18 | 0.0997 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | SLC31A1's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | SLC31A1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.58 | 0.491 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.834). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.4, -32.4); signed map (-51.0, 10.0). **Vector** length 148, 51.8% of its response variance represented; |z| ≥ 3 in 1,079 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.67 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.67 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.67 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +6.3 | +9.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +6.0 | +9.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +5.8 | +8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +6.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.8 | +4.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.9 | +3.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.6 | +3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.0 | -4.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.6 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.5 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.2 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.6 | -2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -6.3 | -6.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.4 | -2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.2 | -3.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -4.9 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 31 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q32 — chr9:113,221,544-113,264,492 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hCTR1, CTR1; previously COPT1 |
| Gene groups (HGNC) | Solute carrier family 31 |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Reactome | 3 pathways, smallest: Metal ion SLC transporters; SLC-mediated transmembrane transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [O15431](https://www.uniprot.org/uniprotkb/O15431) (High affinity copper uptake protein 1):

> [High affinity copper uptake protein 1]: Uniporter that mediates the transport of copper(1+) from the extracellular space to the cytoplasm, across the plasma membrane and delivers directly copper(1+) to specific chaperone such as ATOX1, via a copper(1+)- mediated transient interaction between the C-terminal domain and a copper(1+) chaperone, thus controlling intracellular copper(1+) levels. May function in copper(1+) import from the apical membrane thus may drive intestinal copper absorption …

**Summary**, from NCBI Gene [1317](https://www.ncbi.nlm.nih.gov/gene/1317):

> The protein encoded by this gene is a high-affinity copper transporter found in the cell membrane. The encoded protein functions as a homotrimer to effect the uptake of dietary copper. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:11016](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11016) · Entrez [1317](https://www.ncbi.nlm.nih.gov/gene/1317) · UniProt [O15431](https://www.uniprot.org/uniprotkb/O15431) · Ensembl [ENSG00000136868](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136868)

## Data

Gene col 5924: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5924); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5924, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5924]; `tensor/DDL_lfc|DDL_z.npy` [5924]; `embed/gene_vectors.npy` [5924]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5924 or target_col == 5924). Every well: [[SLC31A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC31A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
