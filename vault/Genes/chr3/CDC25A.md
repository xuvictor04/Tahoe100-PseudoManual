---
symbol: "CDC25A"
type: "gene"
col: 8843
ensembl_id: "ENSG00000164045"
name: "cell division cycle 25A"
location: "3p21.31"
module: 6
arm: "+"
pooled_cpm: 6.64
n_lines_expressing: 45
n_dd_up: 34
n_dd_down: 22
n_dd_up_clean: 6
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 5
direction_downstream: 108
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CDC25A

*cell division cycle 25A* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (28 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 4.07× (z +13.5, q 7e-39, up in 38 of 41 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 4.25× (z +7.3, q 2e-11, up in 26 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.636× (z -6.0, q 1e-06, down in 22 of 40 measured lines) ⚠ cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Temsirolimus (drug)]] 0.5 µM: 0.664× (z -4.0, q 0.006, down in 10 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCM10]] (+0.91, fdr 7e-06), [[CDC45]] (+0.89, fdr 7e-06), [[MCM3]] (+0.86, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); 108 go from it, the strongest it → [[SKA3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 29 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 28 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8843.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **4.07×** | +13.5 | 7e-39 | 38/41 (SW480, J82, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **3.48×** | +12.0 | 1e-30 | 35/39 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **3.26×** | +11.4 | 1e-27 | 38/40 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **3.15×** | +11.1 | 3e-26 | 29/34 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **2.27×** | +7.9 | 3e-13 | 28/41 (NCI-H2347, LOX-IMVI, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.21×** | +7.6 | 3e-12 | 27/41 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.15×** | +7.3 | 2e-11 | 24/41 (LOX-IMVI, NCI-H2347, …) | two highest doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.14×** | +7.3 | 2e-11 | 23/38 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **4.25×** | +7.3 | 2e-11 | 26/39 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **2.12×** | +6.9 | 2e-10 | 16/27 (NCI-H460, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.97×** | +6.5 | 4e-09 | 22/42 (LOX-IMVI, NCI-H2347, …) | two highest doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.65×** | +6.4 | 8e-09 | 16/36 (SW1417, SHP-77, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.11×** | +5.7 | 5e-07 | 19/31 (SW1417, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.89×** | +5.6 | 7e-07 | 5/12 (PANC-1, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~69% of this change | **1.83×** | +5.6 | 9e-07 | 10/26 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +3.8 | 0.004 | 11/40 (SW480, C32, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.005 | 12/42 (J82, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.017 | 12/33 (SHP-77, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.030 | 8/36 (LS 180, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8843.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.636×** | -6.0 | 1e-06 | 22/40 (KATO III, COLO 205, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.635×** | -4.4 | 0.003 | 18/38 (A498, Hs 766T, …) | all doses, flat |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.541×** | -4.3 | 0.003 | 13/43 (HT-29, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.647×** | -4.2 | 0.003 | 17/38 (SW1417, SHP-77, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.638×** | -4.2 | 0.003 | 16/37 (Panc 03.27, A-172, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.664×** | -4.0 | 0.006 | 10/31 (MIA PaCa-2, A549, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.463×** | -3.9 | 0.008 | 9/39 (HEC-1-A, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **0.678×** | -3.8 | 0.010 | 11/40 (KATO III, RKO, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.693×** | -3.8 | 0.010 | 11/41 (A-427, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.746×** | -3.7 | 0.013 | 14/40 (LS 180, SW480, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.691×** | -3.6 | 0.016 | 10/40 (MIA PaCa-2, A498, …) | all doses, flat |  |
| [[Larotrectinib sulfate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.694×** | -3.6 | 0.017 | 10/41 (H4, RKO, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.731×** | -3.5 | 0.024 | 11/40 (A-427, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.707×** | -3.4 | 0.028 | 10/40 (RPMI-7951, KATO III, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.709×** | -3.4 | 0.028 | 13/41 (A-427, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.740×** | -3.3 | 0.034 | 14/40 (COLO 205, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.705×** | -3.3 | 0.034 | 10/37 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.793×** | -3.1 | 0.068 | 8/41 (A-427, PANC-1, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.736×** | -3.0 | 0.080 | 7/40 (SK-MEL-2, HEC-1-A, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.738×** | -3.0 | 0.081 | 10/40 (LoVo, RKO, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.738×** | -3.0 | 0.081 | 6/42 (A-427, A498, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.656×** | -2.9 | 0.087 | 10/34 (A498, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.37 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8843. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 15.3 | 5 (5 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 5.83× (z +10.7) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[A-427 (line)]] | wt | 15.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -10.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 4.87 | 0 | 1 | — | [[Osimertinib (mesylate) (drug)]] 5 µM 0.0561× (z -10.0) |
| [[A498 (line)]] | wt | 4.78 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.205× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 13.8 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.94× (z +8.7) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[A549 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8843), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM10]] | +0.91 | +0.91 / +0.91 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 850 |
| [[CDC45]] | +0.89 | +0.88 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 949 |
| [[MCM3]] | +0.86 | +0.88 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 553 |
| [[UHRF1]] | +0.86 | +0.82 / +0.89 | both halves | 7e-06 | STRING 473 |
| [[E2F2]] | +0.86 | +0.81 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 606 |
| [[FEN1]] | +0.86 | +0.86 / +0.85 | both halves | 7e-06 | pathway: S Phase; STRING 633 |
| [[CLSPN]] | +0.85 | +0.85 / +0.84 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 818 |
| [[E2F1]] | +0.85 | +0.85 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 907 |
| [[WDR76]] | +0.85 | +0.85 / +0.85 | both halves | 7e-06 |  |
| [[MCM4]] | +0.85 | +0.82 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 715 |
| [[MCM5]] | +0.85 | +0.85 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 556 |
| [[FANCA]] | +0.85 | +0.83 / +0.86 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises CDC25A's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.34× lower at baseline in the lines without E2F2 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises CDC25A's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[TCF19]] | B | TCF19 activity raises CDC25A's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.32× lower at baseline in the lines without TCF19 | 0.098 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises CDC25A's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.63× lower at baseline in the lines without MCM10 | 0.083 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target |
| [[ZNF367]] | C | ZNF367 activity raises CDC25A's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 2.75× lower at baseline in the lines without ZNF367 | 0.096 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*108 arrows, 108 of them with an alert ⚠; grade A 0, B 100, C 8. Shown: the 12 strongest; 96 more arrows (96 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SKA3]] | B | CDC25A activity raises SKA3's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.74× lower at baseline in the lines without CDC25A | 0.007 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[MCM4]] | B | CDC25A activity raises MCM4's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 3.07× lower at baseline in the lines without CDC25A | 0.009 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[ORC6]] | B | CDC25A activity raises ORC6's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.38× lower at baseline in the lines without CDC25A | 0.010 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[GINS1]] | B | CDC25A activity raises GINS1's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.89× lower at baseline in the lines without CDC25A | 0.012 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[MELK]] | B | CDC25A activity raises MELK's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.86× lower at baseline in the lines without CDC25A | 0.012 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[DYNC2I2]] | B | CDC25A activity raises DYNC2I2's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.19× lower at baseline in the lines without CDC25A | 0.012 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[ERCC6L]] | B | CDC25A activity raises ERCC6L's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.24× lower at baseline in the lines without CDC25A | 0.014 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[XRCC2]] | B | CDC25A activity raises XRCC2's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.79× lower at baseline in the lines without CDC25A | 0.015 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[SPC24]] | B | CDC25A activity raises SPC24's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.36× lower at baseline in the lines without CDC25A | 0.016 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[CENPK]] | B | CDC25A activity raises CENPK's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.93× lower at baseline in the lines without CDC25A | 0.016 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[PKMYT1]] | B | CDC25A activity raises PKMYT1's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.24× lower at baseline in the lines without CDC25A | 0.017 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[CLSPN]] | B | CDC25A activity raises CLSPN's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.92× lower at baseline in the lines without CDC25A | 0.017 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.851). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.7, -44.4); signed map (-37.8, -45.9). **Vector** length 98.1, 24.1% of its response variance represented; |z| ≥ 3 in 1,112 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.72 to 28); *DNA Replication* (reactome, mean cos +0.71 to 40); *E2F G1/S* (control, mean cos +0.72 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +4.1 | +5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.9 | +12.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~69% of this change | +3.8 | +5.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.6 | +11.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +3.4 | +11.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +3.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.7 | +1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +2.2 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +1.1 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +1.5 | +3.2 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -4.0 | -6.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.2 | -3.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | -3.1 | -4.4 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -3.0 | -4.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.7 | -2.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.6 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -3.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.4 | -3.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.4 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle 25A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:48,157,146-48,188,417 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Class III Cys-based CDC25 phosphatases |
| Hallmark sets | MTORC1_SIGNALING, G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 26 pathways, smallest: Polo-like kinase mediated events; Transcription of E2F targets under negative control by DREAM complex; Deregulated CDK5 triggers multiple neurodegenerative pathways in Alzheimer's disease models |
| Matched by | ensembl_id |

**Function**, from UniProt [P30304](https://www.uniprot.org/uniprotkb/P30304) (M-phase inducer phosphatase 1):

> Tyrosine protein phosphatase which functions as a dosage-dependent inducer of mitotic progression. Directly dephosphorylates CDK1 and stimulates its kinase activity. Also dephosphorylates CDK2 in complex with cyclin-E, in vitro.

**Summary**, from NCBI Gene [993](https://www.ncbi.nlm.nih.gov/gene/993):

> CDC25A is a member of the CDC25 family of phosphatases. CDC25A is required for progression from G1 to the S phase of the cell cycle. It activates the cyclin-dependent kinase CDC2 by removing two phosphate groups. CDC25A is specifically degraded in response to DNA damage, which prevents cells with chromosomal abnormalities from progressing through cell division. CDC25A is an oncogene, although its exact role in oncogenesis has not been demonstrated. Two transcript variants encoding different …

**Accessions** — [HGNC:1725](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1725) · Entrez [993](https://www.ncbi.nlm.nih.gov/gene/993) · UniProt [P30304](https://www.uniprot.org/uniprotkb/P30304) · Ensembl [ENSG00000164045](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164045)

## Data

Gene col 8843: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8843); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8843, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8843]; `tensor/DDL_lfc|DDL_z.npy` [8843]; `embed/gene_vectors.npy` [8843]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8843 or target_col == 8843). Every well: [[CDC25A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC25A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
