---
symbol: "CENPM"
type: "gene"
col: 1883
ensembl_id: "ENSG00000100162"
name: "centromere protein M"
location: "22q13.2"
module: 6
arm: "+"
pooled_cpm: 4.04
n_lines_expressing: 47
n_dd_up: 20
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 13
direction_downstream: 36
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CENPM

*centromere protein M* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.60× (z +12.3, q 4e-32, up in 16 of 18 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.05 µM: 1.44× (z +3.2, q 0.047, up in 8 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.645× (z -6.0, q 9e-07, down in 15 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[E2F1]] (+0.89, fdr 7e-06), [[CDC45]] (+0.89, fdr 7e-06), [[DTL]] (+0.88, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[CDCA7]] → it (grade B ⚠); 36 go from it, the strongest it → [[CLSPN]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1883.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **3.60×** | +12.3 | 4e-32 | 16/18 (KATO III, LS 180, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **3.08×** | +10.4 | 8e-23 | 5/6 (PANC-1, CFPAC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.97×** | +9.7 | 7e-20 | 7/8 (SW480, PANC-1, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **2.05×** | +6.9 | 8e-10 | 13/31 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.95×** | +6.4 | 2e-08 | 21/43 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.71×** | +5.2 | 2e-05 | 12/43 (LoVo, A549, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~66% of this change | **1.67×** | +4.7 | 2e-04 | 10/24 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.60×** | +4.5 | 5e-04 | 12/42 (J82, KATO III, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.58×** | +4.4 | 8e-04 | 14/43 (LoVo, A549, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.32×** | +3.7 | 0.012 | 8/41 (SW480, HT-29, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +3.6 | 0.014 | 1/11 (HEC-1-A) | rises with dose | noisy plate (z scaled) |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.46×** | +3.6 | 0.014 | 4/41 (CFPAC-1, COLO 205, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.45×** | +3.6 | 0.016 | 4/42 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.44×** | +3.2 | 0.047 | 8/28 (A-427, SW1417, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~93% of this change | **1.42×** | +3.2 | 0.047 | 5/27 (C32, CFPAC-1, …) | top dose only | position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.39×** | +3.1 | 0.058 | 4/41 (LS 180, SW 900, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.87×** | +3.1 | 0.066 | 2/22 (PANC-1, NCI-H2347) | top dose only | noisy plate (z scaled) |
| [[Atazanavir (sulfate) (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.084 | 4/39 (A-172, CFPAC-1, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | **1.25×** | +2.9 | 0.092 | 2/42 (KATO III, PANC-1) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1883.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.645×** | -6.0 | 9e-07 | 15/36 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.547×** | -5.5 | 9e-06 | 16/39 (MIA PaCa-2, A-427, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.618×** | -4.7 | 5e-04 | 13/39 (J82, SK-MEL-2, …) | all doses, flat | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.720×** | -4.5 | 8e-04 | 15/42 (SNU-423, A-427, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.524×** | -4.5 | 9e-04 | 14/43 (SW480, KATO III, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.631×** | -4.2 | 0.002 | 4/43 (A-427, NCI-H23, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.763×** | -3.7 | 0.014 | 14/42 (Hs 766T, HCT15, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.708×** | -3.4 | 0.054 | 9/37 (J82, HEC-1-A, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.787×** | -3.3 | 0.057 | 14/43 (HT-29, Hs 766T, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.719×** | -3.2 | 0.071 | 7/43 (HEC-1-A, RKO, …) | inconsistent across doses | position effect removed |
| [[BAY1125976 (drug)]] 5 µM |  | **0.530×** | -3.2 | 0.078 | 7/44 (COLO 205, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Rapamycin (drug)]] 0.05 µM |  | **0.725×** | -3.1 | 0.080 | 5/42 (HCT15, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.12 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1883. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.75 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0993× (z -10.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.120× (z -9.6) |
| [[KATO III (line)]] | alt | 10.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -11.3) |
| [[A-427 (line)]] | wt | 9.19 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.167× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 8.83 | 0 | 1 | — | [[Thymopentin (drug)]] 0.05 µM 0.0612× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 4.53 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0801× (z -9.5) ⚠ cell-cycle shift, explains ~65% of this change |
| [[A-172 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.750 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.718 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.894 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1883), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[E2F1]] | +0.89 | +0.88 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[CDC45]] | +0.89 | +0.88 / +0.87 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 842 |
| [[DTL]] | +0.88 | +0.87 / +0.86 | both halves | 7e-06 | STRING 559 |
| [[PKMYT1]] | +0.88 | +0.90 / +0.86 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 568 |
| [[MCM10]] | +0.88 | +0.86 / +0.87 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 684 |
| [[WDR76]] | +0.87 | +0.89 / +0.84 | both halves | 7e-06 |  |
| [[EXO1]] | +0.87 | +0.88 / +0.83 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 460 |
| [[MCM4]] | +0.86 | +0.87 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 578 |
| [[E2F2]] | +0.86 | +0.84 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[MCM2]] | +0.86 | +0.84 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 477 |
| [[GINS2]] | +0.85 | +0.83 / +0.86 | both halves | 7e-06 | STRING 835 |
| [[CDC25A]] | +0.84 | +0.84 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 413 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 6, C 7. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDCA7]] | B | CDCA7 activity raises CENPM's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 2.06× lower at baseline in the lines without CDCA7 | 0.035 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises CENPM's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.13× lower at baseline in the lines without CDC25A | 0.036 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises CENPM's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.97× lower at baseline in the lines without E2F2 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[YBX2]] | B | YBX2 activity raises CENPM's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 1.48× lower at baseline in the lines without YBX2 | 0.044 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |
| [[FAM111B]] | B | FAM111B activity raises CENPM's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.51× lower at baseline in the lines without FAM111B | 0.074 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises CENPM's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.00× lower at baseline in the lines without E2F8 | 0.079 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[TCF19]] | C | TCF19 activity raises CENPM's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.35× lower at baseline in the lines without TCF19 | 0.013 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent; co-absent with the target |
| [[MCM10]] | C | MCM10 activity raises CENPM's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.11× lower at baseline in the lines without MCM10 | 0.050 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises CENPM's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.49× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises CENPM's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.48× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[SHMT1]] | C | SHMT1 activity raises CENPM's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 2.44× lower at baseline in the lines without SHMT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; co-absent with the target; its own permutation p |
| [[CLSPN]] | C | CLSPN activity raises CENPM's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 2.32× lower at baseline in the lines without CLSPN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 0, C 36. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLSPN]] | C | [[CDC45]], CENPM, [[SKA3]] activity raises CLSPN's level | lines that do not express CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 3.82× lower at baseline in the lines without CDC45, CENPM, SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[GINS1]] | C | [[C21orf58]], [[CDC45]], CENPM, [[SKA3]] activity raises GINS1's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 3.31× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[SPC25]] | C | [[C21orf58]], [[CDC45]], CENPM, [[SKA3]] activity raises SPC25's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 3.15× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[TK1]] | C | [[C21orf58]], [[CDC45]], CENPM, [[SKA3]] activity raises TK1's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.92× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[UBE2T]] | C | CENPM, [[SKA3]] activity raises UBE2T's level | lines that do not express CENPM, SKA3 (3) vs lines expressing them (47) | 2.81× lower at baseline in the lines without CENPM, SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[CENPH]] | C | [[C21orf58]], [[CDC45]], CENPM, [[SKA3]] activity raises CENPH's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.70× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[PCLAF]] | C | [[C21orf58]], [[CDC45]], CENPM activity raises PCLAF's level | lines that do not express C21orf58, CDC45, CENPM (3) vs lines expressing them (47) | 2.70× lower at baseline in the lines without C21orf58, CDC45, CENPM | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[MND1]] | C | [[C21orf58]], [[CDC45]], CENPM, [[SKA3]] activity raises MND1's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.69× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[VRK1]] | C | [[C21orf58]], [[CDC45]], CENPM, [[SKA3]] activity raises VRK1's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.64× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[BRCA1]] | C | [[C21orf58]], [[CDC45]], CENPM, [[SKA3]] activity raises BRCA1's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.60× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[NCAPD3]] | C | [[C21orf58]], [[CDC45]], CENPM, [[SKA3]] activity raises NCAPD3's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.38× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[CDCA4]] | C | [[CDC45]], CENPM, [[SKA3]] activity raises CDCA4's level | lines that do not express CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.37× lower at baseline in the lines without CDC45, CENPM, SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.895). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.2, -44.6); signed map (-37.9, -45.3). **Vector** length 73.3, 14.4% of its response variance represented; |z| ≥ 3 in 820 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.73 to 28); *DNA Replication* (reactome, mean cos +0.72 to 40); *E2F G1/S* (control, mean cos +0.73 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +3.3 | +9.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | +3.2 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | +3.1 | +12.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~93% of this change | +2.8 | +3.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.7 | +6.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.7 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.6 | +3.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.4 | +2.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.3 | +1.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.3 | +1.8 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -3.0 | -3.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.5 | -2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.4 | -5.5 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.7 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -2.3 | -4.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.1 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -4.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | centromere protein M |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:41,938,737-41,947,152 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Pane1, CENP-M, MGC861; previously C22orf18 |
| Gene groups (HGNC) | Minor histocompatibility antigens; Constitutive centromere associated network |
| Hallmark sets | E2F_TARGETS |
| Reactome | 20 pathways, smallest: Deposition of new CENPA-containing nucleosomes at the centromere; Nucleosome assembly; Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NSP4](https://www.uniprot.org/uniprotkb/Q9NSP4) (Centromere protein M):

> Component of the CENPA-NAC (nucleosome-associated) complex, a complex that plays a central role in assembly of kinetochore proteins, mitotic progression and chromosome segregation. The CENPA-NAC complex recruits the CENPA-CAD (nucleosome distal) complex and may be involved in incorporation of newly synthesized CENPA into centromeres.

**Summary**, from NCBI Gene [79019](https://www.ncbi.nlm.nih.gov/gene/79019):

> The protein encoded by this gene is an inner protein of the kinetochore, the multi-protein complex that binds spindle microtubules to regulate chromosome segregation during cell division. It belongs to the constitutive centromere-associated network protein group, whose members interact with outer kinetochore proteins and help to maintain centromere identity at each cell division cycle. The protein is structurally related to GTPases but cannot bind guanosine triphosphate. A point mutation that …

**Accessions** — [HGNC:18352](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18352) · Entrez [79019](https://www.ncbi.nlm.nih.gov/gene/79019) · UniProt [Q9NSP4](https://www.uniprot.org/uniprotkb/Q9NSP4) · Ensembl [ENSG00000100162](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100162)

## Data

Gene col 1883: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1883); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1883, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1883]; `tensor/DDL_lfc|DDL_z.npy` [1883]; `embed/gene_vectors.npy` [1883]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1883 or target_col == 1883). Every well: [[CENPM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CENPM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
