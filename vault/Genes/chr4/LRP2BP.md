---
symbol: "LRP2BP"
type: "gene"
col: 3079
ensembl_id: "ENSG00000109771"
name: "LRP2 binding protein"
location: "4q35.1"
module: 26
arm: "+"
pooled_cpm: 7.92
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 10
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# LRP2BP

*LRP2 binding protein* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.26× (z +28.2, q 0e+00, up in 41 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.719× (z -5.6, q 2e-05, down in 10 of 47 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.748× (z -4.9, q 1e-04, down in 15 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (LOX-IMVI 0.0600×; ⚠ toxic; cell-cycle shift, explains ~50% of this change); [[Imiquimod (maleate) (drug)]] 0.5 µM in 1 line (HS-578T 0.0650×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H23 0.132×; ⚠ cell-cycle shift, would explain all of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (HEC-1-A 0.152×); [[Canagliflozin (drug)]] 5 µM in 1 line (SW48 0.0735×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2D3-AS1]] (+0.82, fdr 7e-06), [[CPEB2-DT]] (+0.81, fdr 7e-06), [[LINC02955]] (+0.81, fdr 7e-06); moves opposite to [[WRAP73]] (-0.71, fdr 3e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3079.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.26×** | +28.2 | 0e+00 | 41/44 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.66×** | +16.5 | 0e+00 | 37/46 (SHP-77, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.30×** | +13.0 | 4e-36 | 13/22 (PANC-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +12.3 | 2e-32 | 23/43 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +11.1 | 8e-27 | 28/43 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +9.1 | 8e-18 | 25/43 (HOP62, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.60×** | +7.9 | 3e-13 | 16/35 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +7.5 | 3e-12 | 20/48 (A-172, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +7.5 | 5e-12 | 16/37 (A-172, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.32×** | +6.7 | 2e-09 | 18/48 (NCI-H2347, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +5.3 | 8e-06 | 17/43 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.1 | 0.002 | 9/48 (NCI-H2347, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +4.1 | 0.002 | 3/16 (NCI-H2030, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Cepharanthine (drug)]] 5 µM |  | 1.16× | +3.5 | 0.022 | 5/48 (LoVo, NCI-H460, …) | rises with dose | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.085 | 10/44 (SNU-423, RKO, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3079.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (LOX-IMVI 0.0600×; ⚠ toxic; cell-cycle shift, explains ~50% of this change); [[Imiquimod (maleate) (drug)]] 0.5 µM in 1 line (HS-578T 0.0650×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H23 0.132×; ⚠ cell-cycle shift, would explain all of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (HEC-1-A 0.152×); [[Canagliflozin (drug)]] 5 µM in 1 line (SW48 0.0735×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.719×** | -5.6 | 2e-05 | 10/47 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.738×** | -5.1 | 6e-05 | 12/46 (H4, hTERT-HPNE, …) | all doses, flat | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.739×** | -5.1 | 6e-05 | 14/46 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.748×** | -4.9 | 1e-04 | 15/43 (HepG2/C3A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.763×** | -4.6 | 6e-04 | 13/47 (SK-MEL-2, NCI-H1573, …) | all doses, flat | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.768×** | -4.4 | 8e-04 | 16/44 (BT-474, SK-MEL-2, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.794×** | -3.9 | 0.009 | 14/48 (NCI-H23, NCI-H1573, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.797×** | -3.8 | 0.010 | 10/48 (H4, NCI-H23, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.805×** | -3.6 | 0.017 | 9/43 (BT-474, C-33 A, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.821×** | -3.3 | 0.050 | 12/48 (NCI-H23, HS-578T, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.880× | -3.0 | 0.12 | 6/48 (HOP62, BT-474, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3079. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 8.24 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.98× (z +15.2) | — |
| [[HS-578T (line)]] | alt | 6.28 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.71× (z +11.4) | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.0650× (z -11.5) |
| [[SW48 (line)]] | wt | 13.0 | 0 | 3 | — | [[Canagliflozin (drug)]] 5 µM 0.0735× (z -9.5) |
| [[HOP62 (line)]] | alt | 9.76 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.31× (z +14.2) | — |
| [[LoVo (line)]] | wt | 12.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +11.6) | — |
| [[LOX-IMVI (line)]] | wt | 7.02 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.91× (z +10.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0600× (z -12.9) ⚠ toxic; cell-cycle shift, explains ~50% of this change |
| [[NCI-H1573 (line)]] | alt | 27.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +13.3) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.245× (z -8.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H2347 (line)]] | alt | 7.94 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.29× (z +15.9) | — |
| [[NCI-H460 (line)]] | wt | 6.09 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +13.2) | — |
| [[SW480 (line)]] | alt | 8.55 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +11.3) | — |
| [[AsPC-1 (line)]] | alt | 4.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.16× (z +9.7) | — |
| [[BT-474 (line)]] | alt | 7.11 | 0 | 1 | — | [[Mebendazole (drug)]] 0.05 µM 0.0918× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 6.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +10.2) | — |
| [[HEC-1-A (line)]] | alt | 9.54 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.152× (z -9.9) |
| [[KATO III (line)]] | alt | 8.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 4.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 6.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.47× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 4.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.44× (z +11.0) | — |
| [[RKO (line)]] | wt | 10.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.07× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 10.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.32× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 7.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.53× (z +10.4) | — |
| [[A-427 (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3079), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2D3-AS1]] | +0.82 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[CPEB2-DT]] | +0.81 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[LINC02955]] | +0.81 | +0.76 / +0.59 | both halves | 7e-06 |  |
| [[PSMD7-DT]] | +0.80 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[LINC00880]] | +0.80 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[NUP210L]] | +0.80 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[FAM184B]] | +0.78 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[ZFHX2-AS1]] | +0.77 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[CCT6B]] | +0.77 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[LINC02936]] | +0.77 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[CCDC62]] | +0.77 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[PARD6G-AS1]] | +0.77 | +0.71 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WRAP73]] | -0.71 | -0.60 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LRP2BP's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ADGRG7]] | B | ADGRG7 activity raises LRP2BP's level | lines that do not express ADGRG7 (40) vs lines expressing it (10) | 1.64× lower at baseline in the lines without ADGRG7 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000287474, ENSG00000253642, ENSG00000287172 |
| [[HDAC6]] | B | HDAC6 activity raises LRP2BP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.784). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (11.8, 18.6); signed map (24.8, -1.6). **Vector** length 77.8, 13.2% of its response variance represented; |z| ≥ 3 in 1,065 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.1 | +28.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.4 | +16.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +13.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +9.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +11.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +7.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +4.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -5.0 | -5.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -4.3 | -3.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -3.9 | -3.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.8 | -4.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -2.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.2 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | LRP2 binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1 — chr4:185,363,872-185,395,924 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761O0113 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2M1](https://www.uniprot.org/uniprotkb/Q9P2M1) (LRP2-binding protein):

> May act as an adapter that regulates LRP2 function.

**Summary**, from NCBI Gene [55805](https://www.ncbi.nlm.nih.gov/gene/55805):

> Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25434](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25434) · Entrez [55805](https://www.ncbi.nlm.nih.gov/gene/55805) · UniProt [Q9P2M1](https://www.uniprot.org/uniprotkb/Q9P2M1) · Ensembl [ENSG00000109771](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109771)

## Data

Gene col 3079: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3079); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3079, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3079]; `tensor/DDL_lfc|DDL_z.npy` [3079]; `embed/gene_vectors.npy` [3079]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3079 or target_col == 3079). Every well: [[LRP2BP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRP2BP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
