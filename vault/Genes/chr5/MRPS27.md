---
symbol: "MRPS27"
type: "gene"
col: 3427
ensembl_id: "ENSG00000113048"
name: "mitochondrial ribosomal protein S27"
location: "5q13.2"
module: 4
arm: "+"
pooled_cpm: 60.72
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# MRPS27

*mitochondrial ribosomal protein S27* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.42× (z +7.3, q 2e-10, up in 39 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.30× (z +5.4, q 1e-05, up in 24 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.621× (z -12.7, q 5e-34, down in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.833× (z -4.8, q 2e-04, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR1A]] (+0.81, fdr 7e-06), [[NAA25]] (+0.78, fdr 7e-06), [[COX10]] (+0.77, fdr 7e-06); moves opposite to [[RSRP1]] (-0.67, fdr 7e-06), [[ARID4A]] (-0.65, fdr 7e-06), [[ERO1B]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MVB12B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3427.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +7.3 | 2e-10 | 39/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.35×** | +6.1 | 2e-07 | 27/48 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +5.4 | 1e-05 | 24/48 (HOP62, NCI-H2347, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.27×** | +4.9 | 1e-04 | 26/48 (NCI-H1573, HOP62, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +4.5 | 7e-04 | 20/48 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.26×** | +4.4 | 9e-04 | 23/48 (SW 900, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.6 | 0.023 | 11/48 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 1.19× | +3.6 | 0.026 | 21/48 (AsPC-1, SW 900, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | 1.12× | +3.1 | 0.095 | 20/48 (NCI-H1573, AsPC-1, …) | top dose only | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.16× | +3.1 | 0.095 | 11/48 (NCI-H1573, LS 180, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.095 | 16/48 (NCI-H1573, KATO III, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.095 | 12/48 (AsPC-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[Finasteride (drug)]] 5 µM |  | 1.16× | +3.0 | 0.10 | 5/48 (HepG2/C3A, C-33 A, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 1.16× | +3.0 | 0.10 | 19/48 (AsPC-1, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3427.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.621×** | -12.7 | 5e-34 | 40/48 (RKO, SW1417, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.689×** | -7.4 | 5e-11 | 32/48 (A-427, PANC-1, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.833×** | -4.8 | 2e-04 | 23/48 (SNU-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.791×** | -4.8 | 2e-04 | 25/48 (RKO, SNU-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change | **0.796×** | -4.7 | 3e-04 | 24/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.692×** | -4.0 | 0.007 | 17/48 (HT-29, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.826×** | -3.8 | 0.012 | 24/48 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.891× | -3.2 | 0.089 | 8/48 (SHP-77, A-427, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -3.1 | 0.10 | 18/50 (NCI-H460, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3427. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 85.8 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -10.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -8.5) |
| [[A-172 (line)]] | wt | 45.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -10.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -9.8) |
| [[PANC-1 (line)]] | alt | 86.9 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.454× (z -11.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 112 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.339× (z -13.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HEC-1-A (line)]] | alt | 55.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.538× (z -9.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[RKO (line)]] | wt | 97.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -14.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 52.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[A498 (line)]] | wt | 51.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -8.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A549 (line)]] | wt | 61.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -9.2) ⚠ cell-cycle shift, explains ~33% of this change |
| [[C-33 A (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0969× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[C32 (line)]] | wt | 52.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[HOP62 (line)]] | alt | 59.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -9.4) |
| [[J82 (line)]] | alt | 61.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -10.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[LOX-IMVI (line)]] | wt | 63.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 53.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[NCI-H23 (line)]] | alt | 75.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[SHP-77 (line)]] | alt | 78.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SNU-1 (line)]] | wt | 81.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -13.6) |
| [[SNU-423 (line)]] | alt | 49.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -9.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW1417 (line)]] | alt | 40.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -11.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW48 (line)]] | wt | 72.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.292× (z -8.5) ⚠ cell-cycle shift, explains ~59% of this change |
| [[SW480 (line)]] | alt | 85.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.420× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[AN3 CA (line)]] | alt | 97.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 82.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 75.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 80.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3427), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR1A]] | +0.81 | +0.80 / +0.82 | both halves | 7e-06 |  |
| [[NAA25]] | +0.78 | +0.77 / +0.79 | both halves | 7e-06 |  |
| [[COX10]] | +0.77 | +0.81 / +0.81 | both halves | 7e-06 |  |
| [[EFTUD2]] | +0.77 | +0.79 / +0.72 | both halves | 7e-06 |  |
| [[TSEN2]] | +0.76 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[HEATR1]] | +0.76 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[MDN1]] | +0.75 | +0.68 / +0.77 | both halves | 7e-06 |  |
| [[COA1]] | +0.75 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[DIS3L2]] | +0.74 | +0.68 / +0.78 | both halves | 7e-06 |  |
| [[NOL10]] | +0.74 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[NUP155]] | +0.73 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[ELAC2]] | +0.72 | +0.67 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSRP1]] | -0.67 | -0.63 / -0.66 | both halves | 7e-06 |  |
| [[ARID4A]] | -0.65 | -0.70 / -0.65 | both halves | 7e-06 |  |
| [[ERO1B]] | -0.64 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[SMIM14]] | -0.64 | -0.56 / -0.66 | both halves | 1e-05 |  |
| [[OPTN]] | -0.64 | -0.66 / -0.64 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MVB12B]] | B | MVB12B activity raises MRPS27's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 1.67× lower at baseline in the lines without MVB12B | 0.025 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[OVOL1]] | B | OVOL1 activity lowers MRPS27's level | lines that do not express OVOL1 (33) vs lines expressing it (17) | 1.26× higher at baseline in the lines without OVOL1 | 0.047 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[PSMB5]] | B | PSMB5 activity lowers MRPS27's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.868). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-11.2, -34.4); signed map (-10.7, -48.6). **Vector** length 116, 30.4% of its response variance represented; |z| ≥ 3 in 838 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v1* (hallmark, mean cos +0.52 to 21); *tRNA Aminoacylation* (reactome, mean cos +0.58 to 7); *tRNA processing in the nucleus* (reactome, mean cos +0.63 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.5 | +7.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | +5.8 | +4.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +5.8 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.0 | +5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.6 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.6 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -6.4 | -12.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -4.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.7 | -7.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -3.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.7 | -4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.0 | -1.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S27 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:72,214,953-72,321,717 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0264, mS27 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Pentatricopeptide repeat containing; Small subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92552](https://www.uniprot.org/uniprotkb/Q92552) (Small ribosomal subunit protein mS27):

> RNA-binding component of the mitochondrial small ribosomal subunit (mt-SSU) that plays a role in mitochondrial protein synthesis. Stimulates mitochondrial mRNA translation of subunit components of the mitochondrial electron transport chain. Binds to the mitochondrial 12S rRNA (12S mt-rRNA) and tRNA(Glu). Involved also in positive regulation of cell proliferation and tumor cell growth.

**Summary**, from NCBI Gene [23107](https://www.ncbi.nlm.nih.gov/gene/23107):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14512](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14512) · Entrez [23107](https://www.ncbi.nlm.nih.gov/gene/23107) · UniProt [Q92552](https://www.uniprot.org/uniprotkb/Q92552) · Ensembl [ENSG00000113048](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113048)

## Data

Gene col 3427: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3427); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3427, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3427]; `tensor/DDL_lfc|DDL_z.npy` [3427]; `embed/gene_vectors.npy` [3427]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3427 or target_col == 3427). Every well: [[MRPS27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
