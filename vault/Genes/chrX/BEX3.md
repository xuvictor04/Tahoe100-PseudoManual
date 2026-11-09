---
symbol: "BEX3"
type: "gene"
col: 9341
ensembl_id: "ENSG00000166681"
name: "brain expressed X-linked 3"
location: "Xq22.2"
module: 45
arm: "+"
pooled_cpm: 42.04
n_lines_expressing: 43
n_dd_up: 5
n_dd_down: 5
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# BEX3

*brain expressed X-linked 3* — Xq22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.45× (z +12.6, q 1e-33, up in 39 of 39 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (HEC-1-A 7.27×, A549 9.98×, NCI-H1792 11.1×, NCI-H1573 14.7×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (HEC-1-A 5.56×, NCI-H1792 9.31×, NCI-H460 5.82×, J82 5.92×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.485× (z -7.5, q 3e-11, down in 34 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTSF]] (+0.62, fdr 1e-05), [[SNRPN]] (+0.62, fdr 1e-05), [[ARL6IP5]] (+0.59, fdr 1e-05); moves opposite to [[REXO1]] (-0.58, fdr 1e-05), [[DPH2]] (-0.56, fdr 3e-05), [[PWP2]] (-0.53, fdr 9e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SLC22A17]] → it (grade B ⚠); 2 go from it, the strongest it → [[NENF]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9341.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (HEC-1-A 7.27×, A549 9.98×, NCI-H1792 11.1×, NCI-H1573 14.7×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (HEC-1-A 5.56×, NCI-H1792 9.31×, NCI-H460 5.82×, J82 5.92×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.45×** | +12.6 | 1e-33 | 39/39 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.05×** | +10.0 | 4e-21 | 33/34 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.01×** | +7.6 | 6e-12 | 34/37 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +4.4 | 0.001 | 37/39 (NCI-H2030, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.61×** | +3.5 | 0.044 | 29/40 (RPMI-7951, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | 1.32× | +3.0 | 0.25 | 22/41 (SK-MEL-2, Hs 766T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9341.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.485×** | -7.5 | 3e-11 | 34/41 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.408×** | -6.6 | 1e-08 | 32/40 (H4, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.344×** | -4.1 | 0.006 | 36/41 (CFPAC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.572×** | -4.1 | 0.006 | 28/41 (RPMI-7951, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.634×** | -3.3 | 0.094 | 25/41 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.645× | -3.2 | 0.10 | 25/41 (SNU-1, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.648× | -3.2 | 0.10 | 23/41 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.438× | -3.2 | 0.10 | 24/41 (NCI-H460, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | 0.452× | -3.1 | 0.14 | 26/41 (SW480, AN3 CA, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9341. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 64.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.23× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 67.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.27× (z +13.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 28.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -9.5) |
| [[A-172 (line)]] | wt | 43.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.89× (z +10.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 31.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.98× (z +12.4) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 71.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 58.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -9.9) |
| [[J82 (line)]] | alt | 73.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.71× (z +11.7) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 37.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.81× (z +10.3) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 47.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.61× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 22.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.1× (z +12.3) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 61.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.82× (z +10.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 48.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.98× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 67.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.44× (z +11.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 72.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.58× (z +10.1) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 49.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +10.2) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 30.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.89× (z +10.2) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 42.6 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.103× (z -8.6) ⚠ transcription drop |
| [[H4 (line)]] | wt | 56.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0917× (z -12.1) |
| [[HCT15 (line)]] | alt | 40.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.87× (z +9.2) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 22.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.53× (z +9.1) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 30.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.14× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 40.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 20.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.7× (z +12.3) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 58.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +9.3) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 45.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.70× (z +10.0) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 25.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.05× (z +10.9) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 54.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -15.1) |
| [[SW 900 (line)]] | alt | 45.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.53× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 48.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +9.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.19 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.01 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.19 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 70.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.92 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9341), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSF]] | +0.62 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[SNRPN]] | +0.62 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[ARL6IP5]] | +0.59 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[ATP5IF1]] | +0.56 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[PREPL]] | +0.56 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[RCOR3]] | +0.55 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[HMGN5]] | +0.55 | +0.40 / +0.39 | both halves | 5e-05 |  |
| [[TMEM59]] | +0.54 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[HMGN3]] | +0.54 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[USP33]] | +0.54 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[ASAH1]] | +0.53 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[ZNF821]] | +0.53 | +0.38 / +0.60 | both halves | 7e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REXO1]] | -0.58 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[DPH2]] | -0.56 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[PWP2]] | -0.53 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[IFRD2]] | -0.52 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[SACS]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[DDX21]] | -0.52 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[PUS1]] | -0.51 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[TRMT61A]] | -0.50 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[POGK]] | -0.49 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[NIP7]] | -0.49 | -0.54 / -0.37 | both halves | 7e-05 |  |
| [[GEMIN4]] | -0.48 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[ZNF696]] | -0.48 | -0.47 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC22A17]] | B | SLC22A17 activity raises BEX3's level | lines that do not express SLC22A17 (21) vs lines expressing it (29) | 2.21× lower at baseline in the lines without SLC22A17 | 0.023 | ⚠ within organs, on part of the lines; also absent: APBA2, TUB, COLEC12 |
| [[SACS]] | B | SACS activity raises BEX3's level | lines that do not express SACS (5) vs lines expressing it (45) | 4.07× lower at baseline in the lines without SACS | 0.047 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises BEX3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GNG11]] | B | GNG11 activity raises BEX3's level | lines that do not express GNG11 (21) vs lines expressing it (29) | 2.37× lower at baseline in the lines without GNG11 | 0.062 | ⚠ within organs, on part of the lines; also absent: LOXL2, SLC8A1, NALCN |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NENF]] | B | BEX3 activity raises NENF's level | lines that do not express BEX3 (7) vs lines expressing it (43) | 1.65× lower at baseline in the lines without BEX3 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000283491, LRP12, KIRREL1 |
| [[ZNF358]] | B | BEX3 activity raises ZNF358's level | lines that do not express BEX3 (7) vs lines expressing it (43) | 1.81× lower at baseline in the lines without BEX3 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000283491, LRP12, KIRREL1 |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.610). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-1.8, -19.2); signed map (-25.0, -4.4). **Vector** length 64.1, 20.5% of its response variance represented; |z| ≥ 3 in 536 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.0 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +1.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +0.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.8 | -6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.6 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -1.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -0.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -2.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | brain expressed X-linked 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.2 — chrX:103,376,395-103,378,164 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Bex, NADE, HGR74, Hero20, DXS6984E; previously NGFRAP1 |
| Gene groups (HGNC) | Brain expressed X-linked family |
| Reactome | 4 pathways, smallest: NADE modulates death signalling; Cell death signalling via NRAGE, NRIF and NADE; p75 NTR receptor-mediated signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00994](https://www.uniprot.org/uniprotkb/Q00994) (Protein BEX3):

> May be a signaling adapter molecule involved in NGFR/p75NTR-mediated apoptosis induced by NGF. Plays a role in zinc-triggered neuronal death. In absence of reductive stress, acts as a pseudosubstrate for the CRL2(FEM1B) complex: associates with FEM1B via zinc, thereby preventing association between FEM1B and its substrates.

**Summary**, from NCBI Gene [27018](https://www.ncbi.nlm.nih.gov/gene/27018):

> Enables identical protein binding activity. Predicted to be involved in negative regulation of protein ubiquitination and signal transduction. Predicted to act upstream of or within extrinsic apoptotic signaling pathway via death domain receptors. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13388](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13388) · Entrez [27018](https://www.ncbi.nlm.nih.gov/gene/27018) · UniProt [Q00994](https://www.uniprot.org/uniprotkb/Q00994) · Ensembl [ENSG00000166681](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166681)

## Data

Gene col 9341: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9341); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9341, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9341]; `tensor/DDL_lfc|DDL_z.npy` [9341]; `embed/gene_vectors.npy` [9341]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9341 or target_col == 9341). Every well: [[BEX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BEX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
