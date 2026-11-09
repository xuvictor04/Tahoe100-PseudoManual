---
symbol: "GPC3"
type: "gene"
col: 7169
ensembl_id: "ENSG00000147257"
name: "glypican 3"
location: "Xq26.2"
module: 82
arm: "+"
pooled_cpm: 18.4
n_lines_expressing: 15
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 6
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# GPC3

*glypican 3* — Xq26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.87× (z +15.7, q 0e+00, up in 6 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.07× (z +15.7, q 0e+00, up in 5 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.523× (z -6.5, q 5e-08, down in 10 of 11 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (HepG2/C3A 0.0731×, C-33 A 0.144×, A-427 0.314×, NCI-H23 0.154×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (HepG2/C3A 0.117×, A-427 0.121×, C-33 A 0.114×); [[Harringtonine (drug)]] 5 µM in 2 lines (A-427 0.111×, HepG2/C3A 0.232×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (A-427 0.230×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPYSL5]] (+0.70, fdr 7e-06), [[JAKMIP1]] (+0.65, fdr 7e-06), [[RET]] (+0.64, fdr 3e-05); moves opposite to [[GATAD1]] (-0.44, fdr 3e-04), [[SPRYD7]] (-0.44, fdr 2e-04), [[DNAL4]] (-0.43, fdr 7e-05).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GCG]] → it (grade C ⚠); 6 go from it, the strongest it → [[RFPL1S]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7169.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.87×** | +15.7 | 0e+00 | 6/9 (C32, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.07×** | +15.7 | 0e+00 | 5/10 (HepG2/C3A, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.72×** | +12.1 | 3e-31 | 3/6 (HepG2/C3A, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.50×** | +12.0 | 7e-31 | 2/4 (HepG2/C3A, NCI-H2030) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +8.5 | 2e-15 | 9/13 (NCI-H23, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.12×** | +7.4 | 1e-11 | 9/13 (C32, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +6.6 | 5e-09 | 1/10 (HepG2/C3A) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.90×** | +6.3 | 2e-08 | 7/13 (NCI-H2030, C32, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +5.8 | 4e-07 | 3/11 (HEC-1-A, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.2 | 1e-05 | 1/13 (RPMI-7951) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.66×** | +5.0 | 3e-05 | 0/12 | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.42×** | +4.6 | 2e-04 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.55×** | +4.3 | 7e-04 | 2/12 (HEC-1-A, BT-474) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.3 | 7e-04 | 0/12 | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +3.9 | 0.004 | 3/11 (BT-474, SNU-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.69×** | +3.7 | 0.008 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.037 | 7/12 (BT-474, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.083 | 2/12 (CHP-212, C32) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7169.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (HepG2/C3A 0.0731×, C-33 A 0.144×, A-427 0.314×, NCI-H23 0.154×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (HepG2/C3A 0.117×, A-427 0.121×, C-33 A 0.114×); [[Harringtonine (drug)]] 5 µM in 2 lines (A-427 0.111×, HepG2/C3A 0.232×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (A-427 0.230×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.523×** | -6.5 | 5e-08 | 10/11 (HepG2/C3A, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | 0.709× | -3.3 | 0.18 | 9/12 (A-427, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.710× | -3.3 | 0.18 | 5/12 (HEC-1-A, A-427, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.729× | -3.2 | 0.21 | 6/12 (A-427, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7169. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 30.4 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.111× (z -13.4) |
| [[HepG2_C3A (line)]] | wt | 1,081 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0731× (z -30.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.117× (z -17.9) |
| [[C-33 A (line)]] | alt | 44.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 7.44 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H661 (line)]] | alt | 885 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0989× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.80 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.48 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.12 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.43 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7169), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPYSL5]] | +0.70 | +0.61 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[JAKMIP1]] | +0.65 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[RET]] | +0.64 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[GCG]] | +0.63 | +0.55 / +0.50 | both halves | 1e-05 | **novel candidate** |
| [[CTNNA2]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[EPHA7]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ADCY1]] | +0.58 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[RFPL1S]] | +0.58 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[TMEM108]] | +0.57 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[VASH1]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ADD2]] | +0.56 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[ERBB4]] | +0.54 | +0.49 / +0.64 | both halves | 2e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATAD1]] | -0.44 | -0.42 / -0.27 | both halves | 3e-04 |  |
| [[SPRYD7]] | -0.44 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[DNAL4]] | -0.43 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[NME6]] | -0.42 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[CCAR1]] | -0.42 | -0.34 / -0.40 | both halves | 1e-04 | pathway: Dengue Virus-Host Interactions |
| [[ZNF181]] | -0.41 | -0.32 / -0.40 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GCG]] | C | GCG activity raises GPC3's level | lines that do not express GCG (46) vs lines expressing it (4) | 11.66× lower at baseline in the lines without GCG | 0.009 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, LINC01205, APOB; co-absent with the target |
| [[MMRN1]] | C | MMRN1 activity raises GPC3's level | lines that do not express MMRN1 (43) vs lines expressing it (7) | 4.93× lower at baseline in the lines without MMRN1 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, KRT5; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RFPL1S]] | B | GPC3 activity raises RFPL1S's level | lines that do not express GPC3 (35) vs lines expressing it (15) | 2.14× lower at baseline in the lines without GPC3 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TF, GCG, APOA2 |
| [[MED12L]] | B | GPC3 activity raises MED12L's level | lines that do not express GPC3 (35) vs lines expressing it (15) | 3.42× lower at baseline in the lines without GPC3 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TF, GCG, APOA2 |
| [[KCNQ2]] | C | GPC3 activity raises KCNQ2's level | lines that do not express GPC3 (35) vs lines expressing it (15) | 2.86× lower at baseline in the lines without GPC3 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TF, GCG, APOA2; co-absent with the target |
| [[PAX2]] | C | GPC3 activity raises PAX2's level | lines that do not express GPC3 (35) vs lines expressing it (15) | 1.93× lower at baseline in the lines without GPC3 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TF, GCG, APOA2; co-absent with the target |
| [[GRID1]] | C | GPC3 activity raises GRID1's level | lines that do not express GPC3 (35) vs lines expressing it (15) | 2.19× lower at baseline in the lines without GPC3 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TF, GCG, APOA2; co-absent with the target |
| [[LINC02643]] | C | GPC3 activity raises LINC02643's level | lines that do not express GPC3 (35) vs lines expressing it (15) | 2.98× lower at baseline in the lines without GPC3 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TF, GCG, APOA2; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.563). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.0, 38.9); signed map (27.1, 27.4). **Vector** length 30.7, 7.22% of its response variance represented; |z| ≥ 3 in 278 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +15.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.1 | +3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +12.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +15.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.9 | +1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +0.7 | -0.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.7 | +1.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -1.4 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -2.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -2.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -1.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -0.9 | -3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.8 | -2.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.8 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -2.7 |
|  | [[Belzutifan (drug)]] 5 µM |  | -0.6 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | glypican 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.2 — chrX:133,535,745-133,987,100 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OCI-5, SGBS, SGBS1, SGB, DGSX; previously SDYS |
| Gene groups (HGNC) | Glypicans |
| Hallmark sets | INFLAMMATORY_RESPONSE, GLYCOLYSIS, HYPOXIA |
| Reactome | 36 pathways, smallest: Defective EXT1 causes exostoses 1, TRPS2 and CHDS; Defective EXT2 causes exostoses 2; Defective B3GALT6 causes EDSP2 and SEMDJL1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P51654](https://www.uniprot.org/uniprotkb/P51654) (Glypican-3):

> Cell surface proteoglycan. Negatively regulates the hedgehog signaling pathway when attached via the GPI-anchor to the cell surface by competing with the hedgehog receptor PTC1 for binding to hedgehog proteins (By similarity). Binding to the hedgehog protein SHH triggers internalization of the complex by endocytosis and its subsequent lysosomal degradation (By similarity). Positively regulates the canonical Wnt signaling pathway by binding to the Wnt receptor Frizzled and stimulating the …

**Summary**, from NCBI Gene [2719](https://www.ncbi.nlm.nih.gov/gene/2719):

> Cell surface heparan sulfate proteoglycans are composed of a membrane-associated protein core substituted with a variable number of heparan sulfate chains. Members of the glypican-related integral membrane proteoglycan family (GRIPS) contain a core protein anchored to the cytoplasmic membrane via a glycosyl phosphatidylinositol linkage. These proteins may play a role in the control of cell division and growth regulation. The protein encoded by this gene can bind to and inhibit the dipeptidyl …

**Accessions** — [HGNC:4451](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4451) · Entrez [2719](https://www.ncbi.nlm.nih.gov/gene/2719) · UniProt [P51654](https://www.uniprot.org/uniprotkb/P51654) · Ensembl [ENSG00000147257](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147257)

## Data

Gene col 7169: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7169); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7169, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7169]; `tensor/DDL_lfc|DDL_z.npy` [7169]; `embed/gene_vectors.npy` [7169]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7169 or target_col == 7169). Every well: [[GPC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
