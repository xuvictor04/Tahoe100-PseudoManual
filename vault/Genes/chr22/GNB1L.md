---
symbol: "GNB1L"
type: "gene"
col: 11739
ensembl_id: "ENSG00000185838"
name: "G protein subunit beta 1 like"
location: "22q11.21"
module: 68
arm: "-"
pooled_cpm: 11.37
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 19
n_dd_up_clean: 8
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# GNB1L

*G protein subunit beta 1 like* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.35× (z +14.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.466× (z -9.0, q 1e-16, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LPCAT1]] (+0.69, fdr 1e-05), [[ATAD3A]] (+0.68, fdr 1e-05), [[ATAD3B]] (+0.67, fdr 7e-06); moves opposite to [[ZNF563]] (-0.67, fdr 1e-05), [[ZNF442]] (-0.67, fdr 1e-05), [[WAC-AS1]] (-0.66, fdr 2e-05).
> It sits in the **-** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11739.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.35×** | +14.8 | 0e+00 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.53×** | +11.4 | 2e-27 | 43/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.45×** | +10.9 | 1e-25 | 40/47 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.97×** | +8.3 | 2e-14 | 36/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.72×** | +6.6 | 4e-09 | 24/43 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.56×** | +5.5 | 5e-06 | 24/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **2.23×** | +5.1 | 2e-05 | 17/46 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.7 | 2e-04 | 18/48 (NCI-H2030, A498, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.3 | 9e-04 | 4/48 (C-33 A, HS-578T, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.93×** | +4.2 | 0.002 | 15/42 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11739.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.466×** | -9.0 | 1e-16 | 30/46 (SW 900, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.697×** | -6.3 | 1e-07 | 26/43 (NCI-H2030, A498, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.607×** | -6.1 | 2e-07 | 27/47 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.609×** | -6.1 | 2e-07 | 25/45 (C-33 A, J82, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.718×** | -5.7 | 1e-06 | 22/47 (J82, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.652×** | -5.2 | 2e-05 | 22/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **0.702×** | -4.3 | 0.001 | 15/45 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.704×** | -4.3 | 0.001 | 18/42 (A498, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.783×** | -4.2 | 0.001 | 17/46 (HT-29, A498, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.622×** | -4.1 | 0.002 | 11/44 (HCT15, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.753×** | -4.1 | 0.002 | 11/46 (MIA PaCa-2, SW480, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **0.723×** | -3.8 | 0.006 | 17/46 (A-172, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.736×** | -3.7 | 0.008 | 15/46 (A498, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.746×** | -3.6 | 0.014 | 13/46 (HT-29, H4, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.756×** | -3.4 | 0.023 | 17/47 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.751×** | -3.4 | 0.024 | 13/45 (HT-29, HCT15, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.766×** | -3.0 | 0.081 | 17/43 (H4, HOP62, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.785×** | -3.0 | 0.090 | 15/46 (BT-474, C-33 A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11739. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.45 | 0 | 2 | — | [[Talc (drug)]] 0.05 µM 0.0694× (z -9.9) |
| [[A498 (line)]] | wt | 16.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0802× (z -15.6) ⚠ cell-cycle shift, explains ~24% of this change |
| [[C-33 A (line)]] | alt | 18.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0864× (z -11.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 5.63 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 4.62× (z +8.9) | [[Harringtonine (drug)]] 5 µM 0.198× (z -9.1) |
| [[SW 900 (line)]] | alt | 8.27 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0375× (z -12.3) |
| [[A-427 (line)]] | wt | 7.55 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.124× (z -9.2) |
| [[A549 (line)]] | wt | 6.75 | 0 | 1 | — | [[Dimethyl fumarate (drug)]] 0.05 µM 0.0444× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 5.99 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 9.53 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0880× (z -9.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 14.9 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.116× (z -9.1) |
| [[HT-29 (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0952× (z -12.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.152× (z -9.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 8.48 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.118× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -11.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SNU-423 (line)]] | alt | 5.43 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0745× (z -8.6) |
| [[SW48 (line)]] | wt | 22.1 | 0 | 1 | — | [[Tadalafil (drug)]] 0.05 µM 0.0845× (z -10.2) |
| [[SW480 (line)]] | alt | 18.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.13 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11739), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*37 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPCAT1]] | +0.69 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[ATAD3A]] | +0.68 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[ATAD3B]] | +0.67 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[TMEM104]] | +0.66 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SCART1]] | +0.63 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[SLC25A10]] | +0.63 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[PPM1F]] | +0.63 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[TRAP1]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[TBC1D24]] | +0.62 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[SLC27A5]] | +0.61 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[DPP9]] | +0.61 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[ERCC2]] | +0.59 | +0.41 / +0.49 | both halves | 4e-05 |  |

## Genes that move opposite

*63 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF563]] | -0.67 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[ZNF442]] | -0.67 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[WAC-AS1]] | -0.66 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[PIGP]] | -0.66 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[BAZ2B]] | -0.65 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[BTN2A1]] | -0.65 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[PAXIP1-AS2]] | -0.65 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[TCEAL4]] | -0.65 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[AHI1-DT]] | -0.65 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[WBP4]] | -0.64 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[CLN5]] | -0.64 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[HHLA3]] | -0.63 | -0.50 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers GNB1L's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers GNB1L's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **-** arm (projection on the module's main direction -0.658). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (11.2, 7.1); signed map (-46.1, -17.5). **Vector** length 90.6, 18.7% of its response variance represented; |z| ≥ 3 in 1,184 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.4 | +14.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.3 | +11.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | +10.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.5 | +6.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.6 | +1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +5.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.1 | -5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -6.0 | -6.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.8 | -9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -4.3 | -4.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.0 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit beta 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:19,783,223-19,854,939 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GY2, WDR14 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYB4](https://www.uniprot.org/uniprotkb/Q9BYB4) (Guanine nucleotide-binding protein subunit beta-like protein 1):

> Acts as a critical regulator of DNA damage response (DDR) signaling via specifically regulating phosphatidylinositol 3-kinase-related protein kinase (PIKK) family proteins.

**Summary**, from NCBI Gene [54584](https://www.ncbi.nlm.nih.gov/gene/54584):

> This gene encodes a G-protein beta-subunit-like polypeptide which is a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. This protein contains 6 WD …

**Accessions** — [HGNC:4397](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4397) · Entrez [54584](https://www.ncbi.nlm.nih.gov/gene/54584) · UniProt [Q9BYB4](https://www.uniprot.org/uniprotkb/Q9BYB4) · Ensembl [ENSG00000185838](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185838)

## Data

Gene col 11739: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11739); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11739, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11739]; `tensor/DDL_lfc|DDL_z.npy` [11739]; `embed/gene_vectors.npy` [11739]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11739 or target_col == 11739). Every well: [[GNB1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNB1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
