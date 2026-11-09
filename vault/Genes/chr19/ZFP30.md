---
symbol: "ZFP30"
type: "gene"
col: 4220
ensembl_id: "ENSG00000120784"
name: "ZFP30 zinc finger protein"
location: "19q13.12"
module: 11
arm: "+"
pooled_cpm: 27.18
n_lines_expressing: 41
n_dd_up: 11
n_dd_down: 15
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 14
direction_downstream: 23
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# ZFP30

*ZFP30 zinc finger protein* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.69× (z +13.9, q 4e-41, up in 29 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.614× (z -9.1, q 6e-17, down in 20 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.682× (z -7.1, q 1e-10, down in 22 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DIS3L]] (+0.66, fdr 1e-05), [[ZNF253]] (+0.66, fdr 1e-05), [[ZNF507]] (+0.63, fdr 1e-05); moves opposite to [[QSOX1]] (-0.56, fdr 1e-05), [[P4HB]] (-0.53, fdr 1e-04), [[TPST2]] (-0.53, fdr 2e-04).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[ZNF570]] → it (grade B ⚠); 23 go from it, the strongest it → [[C3orf38]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4220.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +13.9 | 4e-41 | 29/39 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +12.0 | 1e-30 | 32/39 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.20×** | +6.9 | 8e-10 | 19/39 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.25×** | +6.0 | 4e-07 | 19/39 (SK-MEL-2, NCI-H23, …) | top dose only | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.4 | 9e-06 | 17/39 (HEC-1-A, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +4.9 | 1e-04 | 18/39 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +4.5 | 5e-04 | 16/39 (HOP62, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +4.2 | 0.002 | 13/39 (SW480, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +4.1 | 0.003 | 15/38 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +3.9 | 0.005 | 10/38 (SW480, BT-474, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.024 | 1/39 (HEC-1-A) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.074 | 7/38 (hTERT-HPNE, NCI-H2347, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.1 | 0.074 | 7/39 (A-427, NCI-H23, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.11 | 10/38 (A549, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4220.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.614×** | -9.1 | 6e-17 | 20/36 (SK-MEL-2, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.632×** | -8.5 | 4e-15 | 23/38 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.632×** | -8.5 | 5e-15 | 27/39 (PANC-1, MIA PaCa-2, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.659×** | -7.8 | 1e-12 | 24/39 (PANC-1, C-33 A, …) | two highest doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.667×** | -7.3 | 5e-11 | 18/29 (C-33 A, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.682×** | -7.1 | 1e-10 | 22/38 (RPMI-7951, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.699×** | -6.6 | 3e-09 | 23/39 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.705×** | -6.5 | 5e-09 | 23/38 (PANC-1, SHP-77, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.711×** | -6.4 | 1e-08 | 19/39 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.793×** | -4.1 | 0.002 | 16/39 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.791×** | -4.1 | 0.002 | 14/39 (CHP-212, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.808×** | -3.8 | 0.006 | 14/38 (C32, PANC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~9% of this change | **0.821×** | -3.7 | 0.010 | 15/37 (MIA PaCa-2, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.832×** | -3.4 | 0.028 | 15/38 (HOP62, BT-474, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.885× | -3.2 | 0.048 | 10/39 (HOP62, SW480, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.711×** | -3.0 | 0.098 | 9/37 (hTERT-HPNE, SW480, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4220. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 56.5 | 2 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.23× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.384× (z -12.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.465× (z -10.0) |
| [[A-427 (line)]] | wt | 35.9 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +28.9) | [[Dinaciclib (drug)]] 0.05 µM 0.224× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[NCI-H460 (line)]] | wt | 28.0 | 5 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 13.2× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SW480 (line)]] | alt | 50.2 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.02× (z +29.0) | — |
| [[C-33 A (line)]] | alt | 87.3 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.0960× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[SK-MEL-2 (line)]] | alt | 30.6 | 3 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 6.73× (z +13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.42× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[J82 (line)]] | alt | 61.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +17.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 67.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[C32 (line)]] | wt | 30.3 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.231× (z -10.3) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 42.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.244× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.362× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 38.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.76× (z +26.8) | — |
| [[SNU-1 (line)]] | wt | 19.9 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.05 µM 0.0766× (z -10.9) |
| [[SW1417 (line)]] | alt | 30.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +14.4) | — |
| [[CHP-212 (line)]] | wt | 37.0 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0858× (z -9.3) |
| [[RKO (line)]] | wt | 39.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -12.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[RPMI-7951 (line)]] | alt | 31.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.164× (z -12.0) |
| [[SHP-77 (line)]] | alt | 37.0 | 0 | 1 | — | [[vincristine (drug)]] 5 µM 0.0901× (z -8.7) |
| [[SW 900 (line)]] | alt | 22.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.163× (z -11.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.47 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.54 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.01 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4220), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIS3L]] | +0.66 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[ZNF253]] | +0.66 | +0.55 / +0.57 | both halves | 1e-05 | same gene group |
| [[ZNF507]] | +0.63 | +0.62 / +0.51 | both halves | 1e-05 | same gene group |
| [[ZNF606]] | +0.63 | +0.59 / +0.47 | both halves | 2e-05 | same gene group |
| [[NAIF1]] | +0.62 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[ZNF282]] | +0.62 | +0.64 / +0.46 | both halves | 2e-05 | same gene group |
| [[ZBTB6]] | +0.62 | +0.62 / +0.51 | both halves | 1e-05 | same gene group |
| [[POLR3C]] | +0.62 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[ZNF777]] | +0.61 | +0.62 / +0.52 | both halves | 1e-05 | same gene group |
| [[DNAAF2]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[AASDHPPT]] | +0.60 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[ZNF570]] | +0.60 | +0.70 / +0.51 | both halves | 1e-05 | same gene group; STRING 442 |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QSOX1]] | -0.56 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[P4HB]] | -0.53 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[TPST2]] | -0.53 | -0.57 / -0.29 | both halves | 2e-04 |  |
| [[HSPA5]] | -0.52 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[F11R]] | -0.52 | -0.44 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 8, C 6. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF570]] | B | ZNF570 activity raises ZFP30's level | lines that do not express ZNF570 (15) vs lines expressing it (35) | 2.61× lower at baseline in the lines without ZNF570 | 0.008 | ⚠ within organs, on part of the lines; also absent: ZNF569, PEG10, DNAAF9 |
| [[ZNF569]] | B | ZNF569 activity raises ZFP30's level | lines that do not express ZNF569 (14) vs lines expressing it (36) | 2.63× lower at baseline in the lines without ZNF569 | 0.013 | ⚠ within organs, on part of the lines; also absent: ZNF570, PEG10, DNAAF9 |
| [[ZNF429]] | B | ZNF429 activity raises ZFP30's level | lines that do not express ZNF429 (11) vs lines expressing it (39) | 2.81× lower at baseline in the lines without ZNF429 | 0.037 | ⚠ within organs, on part of the lines; also absent: ZNF724, ENSG00000283201, ZNF254 |
| [[ZNF790]] | B | ZNF790 activity raises ZFP30's level | lines that do not express ZNF790 (14) vs lines expressing it (36) | 2.63× lower at baseline in the lines without ZNF790 | 0.044 | ⚠ within organs, on part of the lines; also absent: ZNF345, ZNF606, ZNF569 |
| [[ZNF793]] | B | ZNF793 activity raises ZFP30's level | lines that do not express ZNF793 (22) vs lines expressing it (28) | 2.27× lower at baseline in the lines without ZNF793 | 0.058 | ⚠ within organs, on part of the lines; also absent: PEG10, MAP6, ZNF570 |
| [[ZNF155]] | B | ZNF155 activity raises ZFP30's level | lines that do not express ZNF155 (5) vs lines expressing it (45) | 4.50× lower at baseline in the lines without ZNF155 | 0.062 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF540, ZNF529-AS1, AGK |
| [[ZNF566]] | B | ZNF566 activity raises ZFP30's level | lines that do not express ZNF566 (5) vs lines expressing it (45) | 5.07× lower at baseline in the lines without ZNF566 | 0.067 | ⚠ within organs, on part of the lines; also absent: ZFP14, MPP1, ZNF540 |
| [[ZNF606]] | B | ZNF606 activity raises ZFP30's level | lines that do not express ZNF606 (13) vs lines expressing it (37) | 2.76× lower at baseline in the lines without ZNF606 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000176593, C19orf18, ZNF569 |
| [[ZNF675]] | C | ZNF675 activity raises ZFP30's level | lines that do not express ZNF675 (5) vs lines expressing it (45) | 6.28× lower at baseline in the lines without ZNF675 | 0.001 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF573, ZNF420; co-absent with the target |
| [[ZNF571]] | C | ZNF571 activity raises ZFP30's level | lines that do not express ZNF571 (6) vs lines expressing it (44) | 6.46× lower at baseline in the lines without ZNF571 | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF420, ZNF850, ZNF540; co-absent with the target |
| [[ZNF480]] | C | ZNF480 activity raises ZFP30's level | lines that do not express ZNF480 (3) vs lines expressing it (47) | 5.50× lower at baseline in the lines without ZNF480 | 0.020 | ⚠ few lines (3 vs 47); across organs; also absent: ZFP14, CIBAR1, ZNF540; maybe low, not absent |
| [[ZNF773]] | C | ZNF773 activity raises ZFP30's level | lines that do not express ZNF773 (9) vs lines expressing it (40) | 3.56× lower at baseline in the lines without ZNF773 | 0.032 | ⚠ within organs, on part of the lines; also absent: ZNF256, ZFP30, ZNF331; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 20, C 3. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C3orf38]] | B | ZFP30 activity raises C3orf38's level | lines that do not express ZFP30 (9) vs lines expressing it (41) | 1.49× lower at baseline in the lines without ZFP30 | 0.009 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF420, ZNF461 |
| [[ZNF260]] | B | ZFP30 activity raises ZNF260's level | lines that do not express ZFP30 (9) vs lines expressing it (41) | 3.23× lower at baseline in the lines without ZFP30 | 0.009 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF420, ZNF461 |
| [[ZNF573]] | B | ZFP30 activity raises ZNF573's level | lines that do not express ZFP30 (9) vs lines expressing it (41) | 2.65× lower at baseline in the lines without ZFP30 | 0.015 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF420, ZNF461 |
| [[ZNF84]] | B | ZFP30 activity raises ZNF84's level | lines that do not express ZFP30 (9) vs lines expressing it (41) | 2.22× lower at baseline in the lines without ZFP30 | 0.022 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF420, ZNF461 |
| [[ZNF711]] | B | ZFP30 activity raises ZNF711's level | lines that do not express ZFP30 (9) vs lines expressing it (41) | 2.62× lower at baseline in the lines without ZFP30 | 0.027 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF420, ZNF461 |
| [[ZBTB6]] | B | ZFP30 activity raises ZBTB6's level | lines that do not express ZFP30 (9) vs lines expressing it (41) | 1.37× lower at baseline in the lines without ZFP30 | 0.038 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF420, ZNF461 |
| [[ZNF429]] | B | ZFP30 activity raises ZNF429's level | lines that do not express ZFP30 (9) vs lines expressing it (41) | 2.85× lower at baseline in the lines without ZFP30 | 0.040 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF420, ZNF461 |
| [[ABRAXAS2]] | B | ZFP30 activity raises ABRAXAS2's level | lines that do not express ZFP30 (9) vs lines expressing it (41) | 1.12× lower at baseline in the lines without ZFP30 | 0.043 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF420, ZNF461 |
| [[ZNF566]] | B | ZFP30 activity raises ZNF566's level | lines that do not express ZFP30 (9) vs lines expressing it (41) | 2.87× lower at baseline in the lines without ZFP30 | 0.045 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF420, ZNF461 |
| [[ZNF510]] | B | ZFP30 activity raises ZNF510's level | lines that do not express ZFP30 (9) vs lines expressing it (41) | 1.29× lower at baseline in the lines without ZFP30 | 0.049 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF420, ZNF461 |
| [[ZNF480]] | B | ZFP30 activity raises ZNF480's level | lines that do not express ZFP30 (9) vs lines expressing it (41) | 2.03× lower at baseline in the lines without ZFP30 | 0.052 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF420, ZNF461 |
| [[ZNF790]] | B | ZFP30 activity raises ZNF790's level | lines that do not express ZFP30 (9) vs lines expressing it (41) | 2.88× lower at baseline in the lines without ZFP30 | 0.053 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF420, ZNF461 |

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.572). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-30.5, 13.8); signed map (3.2, -24.3). **Vector** length 84.5, 17.9% of its response variance represented; |z| ≥ 3 in 850 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +13.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +12.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +6.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +4.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.5 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +3.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.5 | +2.4 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -4.9 | -7.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.2 | -8.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -3.6 | -6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -2.9 | -9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -2.7 | -7.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -6.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | +0.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.4 | -2.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ZFP30 zinc finger protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:37,613,749-37,692,337 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF745, KIAA0961 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2G7](https://www.uniprot.org/uniprotkb/Q9Y2G7) (Zinc finger protein 30 homolog):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [22835](https://www.ncbi.nlm.nih.gov/gene/22835):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29555](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29555) · Entrez [22835](https://www.ncbi.nlm.nih.gov/gene/22835) · UniProt [Q9Y2G7](https://www.uniprot.org/uniprotkb/Q9Y2G7) · Ensembl [ENSG00000120784](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120784)

## Data

Gene col 4220: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4220); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4220, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4220]; `tensor/DDL_lfc|DDL_z.npy` [4220]; `embed/gene_vectors.npy` [4220]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4220 or target_col == 4220). Every well: [[ZFP30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFP30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
