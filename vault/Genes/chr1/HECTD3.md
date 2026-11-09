---
symbol: "HECTD3"
type: "gene"
col: 4717
ensembl_id: "ENSG00000126107"
name: "HECT domain E3 ubiquitin protein ligase 3"
location: "1p34.1"
module: 2
arm: "+"
pooled_cpm: 11.83
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 19
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# HECTD3

*HECT domain E3 ubiquitin protein ligase 3* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.85× (z +9.2, q 1e-17, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.509× (z -14.4, q 4e-44, down in 36 of 46 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.558× (z -8.8, q 2e-16, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INTS11]] (+0.68, fdr 1e-05), [[NTAN1]] (+0.67, fdr 1e-05), [[ESYT1]] (+0.66, fdr 1e-05); moves opposite to [[ERCC6L2]] (-0.56, fdr 4e-05), [[ZNF638]] (-0.56, fdr 3e-05), [[GCFC2]] (-0.54, fdr 5e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4717.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.85×** | +9.2 | 1e-17 | 36/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.78×** | +8.7 | 9e-16 | 37/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.78×** | +8.7 | 9e-16 | 37/48 (HEC-1-A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.44×** | +7.8 | 1e-12 | 28/47 (J82, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +4.6 | 4e-04 | 17/45 (HEC-1-A, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.4 | 0.001 | 17/48 (NCI-H460, SW480, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.33×** | +4.3 | 0.001 | 12/43 (A549, NCI-H23, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +3.9 | 0.006 | 9/23 (LS 180, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | 1.46× | +3.0 | 0.16 | 2/46 (A498, PANC-1) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4717.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.509×** | -14.4 | 4e-44 | 36/46 (AsPC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.444×** | -11.7 | 2e-29 | 34/47 (A-172, NCI-H1573, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.483×** | -10.9 | 1e-25 | 40/48 (HOP62, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.498×** | -10.5 | 1e-23 | 33/44 (KATO III, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.558×** | -8.8 | 2e-16 | 36/46 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.588×** | -8.0 | 1e-13 | 32/46 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.681×** | -5.8 | 6e-07 | 22/43 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.704×** | -5.3 | 9e-06 | 23/47 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.783×** | -5.2 | 1e-05 | 18/48 (A498, HS-578T, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.718×** | -5.0 | 3e-05 | 19/45 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.749×** | -4.3 | 7e-04 | 15/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.743×** | -4.3 | 8e-04 | 15/45 (COLO 205, AsPC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.593×** | -4.1 | 0.002 | 14/46 (HS-578T, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.784×** | -3.7 | 0.010 | 13/46 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.790×** | -3.5 | 0.015 | 12/47 (LoVo, A-172, …) | all doses, stronger at high dose |  |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.800×** | -3.4 | 0.028 | 9/47 (AsPC-1, A498, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.738×** | -3.3 | 0.038 | 6/48 (HEC-1-A, NCI-H661, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.819×** | -3.0 | 0.080 | 15/47 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Afatinib (drug)]] 0.05 µM |  | 0.860× | -3.0 | 0.080 | 10/46 (NCI-H1573, BT-474, …) | inconsistent across doses | position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | 0.870× | -2.9 | 0.087 | 7/48 (PANC-1, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4717. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 13.8 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.170× (z -10.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[XRK3F2 (drug)]] 0.5 µM 0.125× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 12.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -13.5) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HOP62 (line)]] | alt | 12.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -12.9) ⚠ cell-cycle shift, explains ~38% of this change |
| [[LOX-IMVI (line)]] | wt | 13.3 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.134× (z -11.1) |
| [[A549 (line)]] | wt | 9.84 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -9.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Bosentan (hydrate) (drug)]] 5 µM 0.176× (z -8.5) |
| [[RKO (line)]] | wt | 8.73 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0520× (z -12.2) |
| [[SW480 (line)]] | alt | 11.2 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.279× (z -9.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 23.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -10.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[BT-474 (line)]] | alt | 6.03 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0881× (z -8.5) |
| [[C-33 A (line)]] | alt | 7.35 | 0 | 1 | — | [[Tofacitinib (drug)]] 0.05 µM 0.0666× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -9.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HS-578T (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -11.5) ⚠ cell-cycle shift, explains ~38% of this change |
| [[KATO III (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.123× (z -11.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 19.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -9.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H1573 (line)]] | alt | 6.32 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.129× (z -9.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 9.51 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -10.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H2347 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -9.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW48 (line)]] | wt | 8.48 | 0 | 1 | — | [[Cinacalcet (drug)]] 0.05 µM 0.0568× (z -9.3) |
| [[A-427 (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4717), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS11]] | +0.68 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[NTAN1]] | +0.67 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[ESYT1]] | +0.66 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[CRAT]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[LMF2]] | +0.66 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[VAMP3]] | +0.66 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ZDHHC8]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[LLGL1]] | +0.64 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[ZDHHC16]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[CAPN1]] | +0.64 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[PLD2]] | +0.64 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[TMUB1]] | +0.63 | +0.67 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6L2]] | -0.56 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[ZNF638]] | -0.56 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[GCFC2]] | -0.54 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[ENOSF1]] | -0.54 | -0.58 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers HECTD3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[VAT1]] | C | VAT1 activity raises HECTD3's level | lines that do not express VAT1 (3) vs lines expressing it (47) | 1.68× lower at baseline in the lines without VAT1 | 0.082 | ⚠ few lines (3 vs 47); across organs; also absent: SH2B3, C12orf75, SKAP2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.642). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-7.8, -21.2); signed map (-47.6, -11.1). **Vector** length 78.6, 14.2% of its response variance represented; |z| ≥ 3 in 1,010 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +4.2 | +7.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.5 | +9.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +8.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.3 | +8.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.9 | +4.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +1.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.8 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.7 | +2.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.3 | -0.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.8 | -5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -5.5 | -14.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.0 | -5.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.7 | -11.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.3 | -5.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -4.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.1 | -0.8 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.6 | -0.7 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | HECT domain E3 ubiquitin protein ligase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:45,002,540-45,011,324 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21156 |
| Gene groups (HGNC) | HECT domain E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T447](https://www.uniprot.org/uniprotkb/Q5T447) (E3 ubiquitin-protein ligase HECTD3):

> E3 ubiquitin-protein ligase that modifies a wide variety of substrates with different types of ubiquitin chains. Preferentially accepts ubiquitin from the UBE2D family of E2 ubiquitin-conjugating enzymes. Mediates ubiquitination of TRIOBP and its subsequent proteasomal degradation, thus facilitating cell cycle progression by regulating the turnover of TRIOBP. Mediates ubiquitination of STX8 (By similarity). Mediates ubiquitination of PARP1.

**Summary**, from NCBI Gene [79654](https://www.ncbi.nlm.nih.gov/gene/79654):

> The protein encoded by this gene transfers ubiquitin from an E2 ubiquitin-conjugating enzyme to targeted substrates, leading to the degradation of those substrates. The encoded protein has been shown to transfer ubiquitin to TRIOBP to facilitate cell cycle progression, and to STX8. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:26117](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26117) · Entrez [79654](https://www.ncbi.nlm.nih.gov/gene/79654) · UniProt [Q5T447](https://www.uniprot.org/uniprotkb/Q5T447) · Ensembl [ENSG00000126107](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126107)

## Data

Gene col 4717: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4717); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4717, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4717]; `tensor/DDL_lfc|DDL_z.npy` [4717]; `embed/gene_vectors.npy` [4717]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4717 or target_col == 4717). Every well: [[HECTD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HECTD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
