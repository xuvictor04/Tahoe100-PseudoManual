---
symbol: "B4GALT4"
type: "gene"
col: 4280
ensembl_id: "ENSG00000121578"
name: "beta-1,4-galactosyltransferase 4"
location: "3q13.32"
module: 49
arm: "+"
pooled_cpm: 31.31
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# B4GALT4

*beta-1,4-galactosyltransferase 4* — 3q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.52× (z +12.1, q 3e-31, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.638× (z -9.1, q 5e-17, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EAF2]] (+0.57, fdr 9e-06), [[INTS8]] (+0.56, fdr 2e-05), [[PRCP]] (+0.55, fdr 1e-05); moves opposite to [[PITPNB]] (-0.57, fdr 2e-05), [[SPATA5]] (-0.53, fdr 7e-05), [[URB2]] (-0.51, fdr 3e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HNF1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4280.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +12.1 | 3e-31 | 33/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +8.6 | 3e-15 | 31/47 (MIA PaCa-2, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.21×** | +5.7 | 3e-06 | 20/48 (J82, A549, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +4.7 | 4e-04 | 15/48 (J82, A-427, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.23×** | +4.2 | 0.003 | 15/44 (hTERT-HPNE, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.22×** | +4.0 | 0.005 | 12/48 (Panc 03.27, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.20×** | +3.8 | 0.013 | 18/47 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.029 | 11/48 (J82, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.048 | 6/44 (NCI-H1573, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.13× | +3.3 | 0.055 | 5/48 (AsPC-1, COLO 205, …) | two highest doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 1.15× | +3.1 | 0.087 | 10/48 (AsPC-1, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.16× | +3.1 | 0.091 | 12/48 (SK-MEL-2, A-427, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4280.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.638×** | -9.1 | 5e-17 | 30/48 (CFPAC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.686×** | -7.6 | 6e-12 | 29/48 (CFPAC-1, A498, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.722×** | -6.3 | 4e-08 | 27/47 (HS-578T, A498, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.757×** | -5.6 | 3e-06 | 20/48 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.592×** | -5.6 | 3e-06 | 21/48 (CFPAC-1, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.785×** | -4.9 | 9e-05 | 20/47 (NCI-H460, AsPC-1, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.791×** | -4.7 | 2e-04 | 23/46 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.664×** | -4.3 | 1e-03 | 15/45 (LOX-IMVI, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.808×** | -4.3 | 0.001 | 17/48 (CFPAC-1, HS-578T, …) | two highest doses | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.803×** | -4.1 | 0.002 | 14/37 (SHP-77, LS 180, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.818×** | -4.1 | 0.003 | 16/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.820×** | -4.0 | 0.003 | 16/48 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.872× | -3.9 | 0.004 | 16/48 (A498, SNU-1, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.827×** | -3.8 | 0.005 | 17/48 (CFPAC-1, KATO III, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.884× | -3.5 | 0.017 | 12/48 (SNU-423, C-33 A, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.840× | -3.4 | 0.025 | 16/48 (LoVo, NCI-H23, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.847× | -3.3 | 0.028 | 12/47 (A498, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4280. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 192 | 0 | 8 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.264× (z -15.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.282× (z -15.0) |
| [[HCT15 (line)]] | alt | 20.7 | 0 | 2 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0965× (z -11.6) |
| [[Hs 766T (line)]] | wt | 30.7 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.269× (z -8.5) |
| [[HS-578T (line)]] | alt | 52.6 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.284× (z -11.1) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.348× (z -9.7) |
| [[KATO III (line)]] | alt | 23.6 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.278× (z -9.5) |
| [[LS 180 (line)]] | wt | 21.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.275× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[MIA PaCa-2 (line)]] | alt | 22.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +11.6) | — |
| [[PANC-1 (line)]] | alt | 29.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +17.7) | — |
| [[A549 (line)]] | wt | 60.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -10.6) |
| [[AN3 CA (line)]] | alt | 29.7 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0790× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 17.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.177× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 24.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.8) | — |
| [[J82 (line)]] | alt | 27.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +11.3) | — |
| [[NCI-H2030 (line)]] | alt | 56.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.303× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.223× (z -11.8) ⚠ cell-cycle shift, explains ~14% of this change |
| [[Panc 03.27 (line)]] | alt | 23.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW1417 (line)]] | alt | 33.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +10.0) | — |
| [[SW48 (line)]] | wt | 18.5 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.117× (z -9.5) |
| [[SW480 (line)]] | alt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.0) | — |
| [[A-172 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4280), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EAF2]] | +0.57 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[INTS8]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[PRCP]] | +0.55 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[SLC15A2]] | +0.55 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[UFL1]] | +0.54 | +0.61 / +0.39 | both halves | 6e-05 |  |
| [[DNAJC25]] | +0.53 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[ATP23]] | +0.53 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[GAD1]] | +0.53 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[BTN3A1]] | +0.53 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[ZNF563]] | +0.53 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[CHCHD7]] | +0.52 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[TGDS]] | +0.51 | +0.50 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PITPNB]] | -0.57 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[SPATA5]] | -0.53 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[URB2]] | -0.51 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[POLR1A]] | -0.50 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[FAF1]] | -0.50 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[PIGM]] | -0.49 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[NOL10]] | -0.48 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[YWHAB]] | -0.48 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[PTK2]] | -0.48 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[DPH6]] | -0.48 | -0.56 / -0.40 | both halves | 4e-05 |  |
| [[EFTUD2]] | -0.48 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[ASAP1]] | -0.47 | -0.42 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HNF1B]] | B | HNF1B activity raises B4GALT4's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 1.34× lower at baseline in the lines without HNF1B | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.320). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.5, -40.9); signed map (-2.6, 4.0). **Vector** length 91.0, 17.9% of its response variance represented; |z| ≥ 3 in 953 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.9 | +12.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +8.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +4.3 | +5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +3.3 | +3.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +3.3 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +4.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.5 | +3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | +3.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.4 | +3.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +3.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.0 | -7.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.1 | -9.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.0 | -6.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -3.9 | -5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -3.4 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.7 | -4.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.4 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | beta-1,4-galactosyltransferase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.32 — chr3:119,211,732-119,240,946 (-) |
| Ensembl biotype | protein_coding |
| Also known as | beta4Gal-T4 |
| Gene groups (HGNC) | Beta 4-glycosyltransferases |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 8 pathways, smallest: N-Glycan antennae elongation; Keratan sulfate biosynthesis; N-glycan antennae elongation in the medial/trans-Golgi |
| Matched by | ensembl_id |

**Function**, from UniProt [O60513](https://www.uniprot.org/uniprotkb/O60513) (Beta-1,4-galactosyltransferase 4):

> Galactose (Gal) transferase involved in the synthesis of terminal N-acetyllactosamine (LacNac) unit present on glycan chains of glycoproteins and glycosphingolipids. Catalyzes the transfer of Gal residue via a beta1->4 linkage from UDP-Gal to the non-reducing terminal N-acetyl glucosamine 6-O-sulfate (6-O-sulfoGlcNAc) in the linearly growing chain of both N- and O-linked keratan sulfate proteoglycans. Cooperates with B3GNT7 N-acetyl glucosamine transferase and CHST6 and CHST1 sulfotransferases …

**Summary**, from NCBI Gene [8702](https://www.ncbi.nlm.nih.gov/gene/8702):

> This gene is one of seven beta-1,4-galactosyltransferase (beta4GalT) genes. They encode type II membrane-bound glycoproteins that appear to have exclusive specificity for the donor substrate UDP-galactose; all transfer galactose in a beta1,4 linkage to similar acceptor sugars: GlcNAc, Glc, and Xyl. Each beta4GalT has a distinct function in the biosynthesis of different glycoconjugates and saccharide structures. As type II membrane proteins, they have an N-terminal hydrophobic signal sequence …

**Accessions** — [HGNC:927](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:927) · Entrez [8702](https://www.ncbi.nlm.nih.gov/gene/8702) · UniProt [O60513](https://www.uniprot.org/uniprotkb/O60513) · Ensembl [ENSG00000121578](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121578)

## Data

Gene col 4280: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4280); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4280, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4280]; `tensor/DDL_lfc|DDL_z.npy` [4280]; `embed/gene_vectors.npy` [4280]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4280 or target_col == 4280). Every well: [[B4GALT4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B4GALT4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
