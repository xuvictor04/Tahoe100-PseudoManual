---
symbol: "DFFB"
type: "gene"
col: 9822
ensembl_id: "ENSG00000169598"
name: "DNA fragmentation factor subunit beta"
location: "1p36.32"
module: 36
arm: "+"
pooled_cpm: 4.48
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 17
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# DFFB

*DNA fragmentation factor subunit beta* — 1p36.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.65× (z +6.0, q 9e-07, up in 2 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.47× (z +4.8, q 3e-04, up in 9 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.456× (z -13.9, q 6e-41, down in 28 of 39 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.480× (z -9.0, q 3e-17, down in 24 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UTP18]] (+0.72, fdr 7e-06), [[SKP2]] (+0.68, fdr 7e-06), [[ACTR5]] (+0.67, fdr 7e-06); moves opposite to [[KCTD11]] (-0.67, fdr 7e-06), [[OFD1]] (-0.63, fdr 1e-05), [[PKNOX1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LRP3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9822.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +6.0 | 9e-07 | 2/6 (PANC-1, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +5.0 | 1e-04 | 4/11 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.47×** | +4.8 | 3e-04 | 9/47 (SNU-423, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.38×** | +4.1 | 0.007 | 6/46 (A549, SW 900, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +3.7 | 0.021 | 1/11 (PANC-1) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.034 | 5/46 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.22×** | +3.5 | 0.035 | 1/47 (SHP-77) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | 1.30× | +3.1 | 0.12 | 8/43 (PANC-1, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9822.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.456×** | -13.9 | 6e-41 | 28/39 (A498, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.413×** | -10.6 | 6e-24 | 29/44 (RKO, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.486×** | -9.0 | 3e-17 | 25/46 (LoVo, NCI-H2347, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.480×** | -9.0 | 3e-17 | 24/39 (SW48, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.644×** | -7.8 | 8e-13 | 21/40 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.551×** | -7.5 | 9e-12 | 22/46 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.557×** | -7.3 | 2e-11 | 17/39 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.614×** | -5.9 | 3e-07 | 20/39 (RKO, SW48, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.643×** | -5.5 | 2e-06 | 17/45 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.669×** | -5.0 | 3e-05 | 16/45 (NCI-H1792, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.698×** | -4.5 | 3e-04 | 11/44 (MIA PaCa-2, A498, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.806×** | -3.8 | 0.006 | 13/46 (A498, SW480, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | **0.831×** | -3.3 | 0.044 | 12/45 (NCI-H1573, HepG2/C3A, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.775×** | -3.1 | 0.088 | 8/44 (SK-MEL-2, SNU-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.779×** | -3.0 | 0.094 | 16/37 (NCI-H460, SW48, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.784×** | -3.0 | 0.094 | 9/45 (PANC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9822. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 7.41 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -12.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0805× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 4.05 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -12.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.117× (z -10.5) |
| [[A498 (line)]] | wt | 4.79 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0694× (z -18.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0902× (z -11.5) |
| [[C-33 A (line)]] | alt | 8.68 | 0 | 2 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0807× (z -9.9) |
| [[HOP62 (line)]] | alt | 3.71 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0966× (z -12.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H2030 (line)]] | alt | 5.18 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -9.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[RKO (line)]] | wt | 8.21 | 0 | 2 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0764× (z -10.7) |
| [[A-172 (line)]] | wt | 3.33 | 0 | 1 | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 0.5 µM 0.0675× (z -9.3) |
| [[C32 (line)]] | wt | 4.69 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.137× (z -9.8) |
| [[LoVo (line)]] | wt | 5.87 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -14.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[MIA PaCa-2 (line)]] | alt | 4.63 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0423× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H1792 (line)]] | alt | 3.56 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0752× (z -8.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW48 (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -9.4) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW480 (line)]] | alt | 5.98 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -9.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A-427 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9822), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP18]] | +0.72 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[SKP2]] | +0.68 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[ACTR5]] | +0.67 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[CHCHD6]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[ZNF692]] | +0.65 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[GPD1L]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[SORD]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[ERI3]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[NDRG3]] | +0.65 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[SAMM50]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[MRPS35]] | +0.65 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[XPO7]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD11]] | -0.67 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[OFD1]] | -0.63 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[PKNOX1]] | -0.61 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[PNRC2]] | -0.59 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[ZBED5]] | -0.58 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[SHOC2]] | -0.58 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[FOXD1]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.57 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[FBXO48]] | -0.57 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[RNF19A]] | -0.57 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[BOLA1]] | -0.57 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[CREB1]] | -0.57 | -0.55 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRP3]] | B | LRP3 activity raises DFFB's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 1.65× lower at baseline in the lines without LRP3 | 0.001 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises DFFB's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DUXAP9]] | B | DUXAP9 activity raises DFFB's level | lines that do not express DUXAP9 (8) vs lines expressing it (42) | 1.45× lower at baseline in the lines without DUXAP9 | 0.044 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, TTYH2; maybe low, not absent |
| [[GPX8]] | B | GPX8 activity raises DFFB's level | lines that do not express GPX8 (8) vs lines expressing it (42) | 1.26× lower at baseline in the lines without GPX8 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000232295, EMP3, LGALS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.538). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-7.8, -13.4); signed map (-39.5, -14.4). **Vector** length 61.9, 8.47% of its response variance represented; |z| ≥ 3 in 1,065 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +2.5 | +4.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | +2.4 | +3.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.3 | +2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +3.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.3 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | +1.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.3 | +2.6 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.2 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -4.4 | -13.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.6 | -10.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -3.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.0 | -9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -3.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -4.5 |
|  | [[Thymol (drug)]] 5 µM |  | -1.3 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | DNA fragmentation factor subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.32 — chr1:3,857,267-3,885,429 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAD, CPAN, DFF-40, DFF40 |
| Gene groups (HGNC) | DNA fragmentation factor subunits |
| Reactome | 4 pathways, smallest: Apoptosis induced DNA fragmentation; Apoptotic execution phase; Apoptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [O76075](https://www.uniprot.org/uniprotkb/O76075) (DNA fragmentation factor subunit beta):

> Nuclease that induces DNA fragmentation and chromatin condensation during apoptosis. Degrades naked DNA and induces apoptotic morphology.

**Summary**, from NCBI Gene [1677](https://www.ncbi.nlm.nih.gov/gene/1677):

> Apoptosis is a cell death process that removes toxic and/or useless cells during mammalian development. The apoptotic process is accompanied by shrinkage and fragmentation of the cells and nuclei and degradation of the chromosomal DNA into nucleosomal units. DNA fragmentation factor (DFF) is a heterodimeric protein of 40-kD (DFFB) and 45-kD (DFFA) subunits. DFFA is the substrate for caspase-3 and triggers DNA fragmentation during apoptosis. DFF becomes activated when DFFA is cleaved by …

**Accessions** — [HGNC:2773](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2773) · Entrez [1677](https://www.ncbi.nlm.nih.gov/gene/1677) · UniProt [O76075](https://www.uniprot.org/uniprotkb/O76075) · Ensembl [ENSG00000169598](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169598)

## Data

Gene col 9822: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9822); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9822, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9822]; `tensor/DDL_lfc|DDL_z.npy` [9822]; `embed/gene_vectors.npy` [9822]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9822 or target_col == 9822). Every well: [[DFFB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DFFB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
