---
symbol: "SPRED3"
type: "gene"
col: 12048
ensembl_id: "ENSG00000188766"
name: "sprouty related EVH1 domain containing 3"
location: "19q13"
module: 38
arm: "+"
pooled_cpm: 10.87
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 31
n_dd_up_clean: 10
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# SPRED3

*sprouty related EVH1 domain containing 3* — 19q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.79× (z +17.6, q 0e+00, up in 42 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (3 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.468× (z -8.9, q 4e-16, down in 31 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTLL3]] (+0.75, fdr 7e-06), [[GPATCH2L]] (+0.73, fdr 7e-06), [[SLC9A5]] (+0.73, fdr 7e-06); moves opposite to [[PYURF]] (-0.56, fdr 1e-05), [[DLD]] (-0.55, fdr 3e-05), [[EHMT2]] (-0.54, fdr 3e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12048.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.79×** | +17.6 | 0e+00 | 42/45 (A549, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.32×** | +10.2 | 4e-22 | 38/46 (HT-29, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.04×** | +8.2 | 5e-14 | 32/44 (COLO 205, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +7.5 | 1e-11 | 27/44 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.7 | 1e-06 | 18/48 (NCI-H2347, RKO, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.53×** | +5.1 | 3e-05 | 21/47 (HT-29, HEC-1-A, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.42×** | +4.1 | 0.003 | 15/39 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.56×** | +3.9 | 0.007 | 16/48 (COLO 205, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.82×** | +3.7 | 0.012 | 9/34 (A498, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.35×** | +3.5 | 0.026 | 18/46 (HEC-1-A, NCI-H460, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.067 | 7/43 (NCI-H460, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.067 | 10/43 (A549, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.081 | 11/44 (CFPAC-1, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.1 | 0.083 | 4/48 (SNU-1, SW48, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.05 µM |  | 1.28× | +3.0 | 0.10 | 5/46 (HepG2/C3A, NCI-H2030, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12048.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.468×** | -8.9 | 4e-16 | 31/45 (C32, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.539×** | -7.8 | 1e-12 | 30/48 (C32, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.524×** | -7.6 | 7e-12 | 28/45 (LOX-IMVI, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.549×** | -7.3 | 4e-11 | 24/47 (C32, SHP-77, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.615×** | -7.3 | 4e-11 | 28/48 (C32, SHP-77, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.569×** | -6.9 | 6e-10 | 26/47 (C32, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.555×** | -6.6 | 3e-09 | 27/47 (C32, SHP-77, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.608×** | -5.8 | 4e-07 | 25/45 (BT-474, NCI-H1573, …) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.642×** | -5.4 | 5e-06 | 22/47 (C32, PANC-1, …) | rises with dose | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.662×** | -5.0 | 3e-05 | 24/47 (NCI-H2030, KATO III, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.705×** | -4.6 | 2e-04 | 20/48 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.736×** | -4.3 | 7e-04 | 16/47 (SHP-77, C32, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.796×** | -3.9 | 0.004 | 19/47 (CFPAC-1, C32, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.534×** | -3.9 | 0.004 | 18/43 (AsPC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.734×** | -3.8 | 0.006 | 18/46 (LOX-IMVI, A-427, …) | two highest doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.805×** | -3.7 | 0.006 | 15/48 (C32, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12048. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 18.9 | 0 | 9 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0271× (z -19.8) |
| [[LOX-IMVI (line)]] | wt | 28.1 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.108× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.173× (z -10.5) |
| [[HOP62 (line)]] | alt | 19.1 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.199× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[A549 (line)]] | wt | 14.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.78× (z +12.6) | [[Erlotinib (drug)]] 0.05 µM 0.165× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 4.63 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.80× (z +8.5) | [[Betamethasone dipropionate (drug)]] 5 µM 0.0744× (z -8.6) |
| [[BT-474 (line)]] | alt | 12.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +9.1) | [[Belumosudil (drug)]] 5 µM 0.0594× (z -11.9) |
| [[H4 (line)]] | wt | 37.0 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0524× (z -15.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[KATO III (line)]] | alt | 11.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.109× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 9.33 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0998× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 5.55 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.20× (z +11.2) | — |
| [[PANC-1 (line)]] | alt | 8.00 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +10.8) | [[Cobimetinib (drug)]] 0.5 µM 0.199× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 9.80 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.216× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 15.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +11.6) | — |
| [[HT-29 (line)]] | alt | 8.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 6.63 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.107× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 4.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.42× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 5.38 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0963× (z -8.9) ⚠ cell-cycle shift, explains ~55% of this change |
| [[SHP-77 (line)]] | alt | 17.5 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.134× (z -9.8) |
| [[SW48 (line)]] | wt | 13.4 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0978× (z -8.5) |
| [[SW480 (line)]] | alt | 7.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +8.5) | — |
| [[A-172 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12048), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTLL3]] | +0.75 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[GPATCH2L]] | +0.73 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[SLC9A5]] | +0.73 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[IPPK]] | +0.68 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[LINC01588]] | +0.68 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[ASGR1]] | +0.68 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[ISY1-RAB43]] | +0.67 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[BLZF2P]] | +0.66 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[POU2F2]] | +0.64 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[ZNF432]] | +0.64 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[KCTD5]] | +0.63 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[ORAI2]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PYURF]] | -0.56 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[DLD]] | -0.55 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[EHMT2]] | -0.54 | -0.44 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SPRED3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01812]] | B | LINC01812 activity raises SPRED3's level | lines that do not express LINC01812 (35) vs lines expressing it (15) | 1.75× lower at baseline in the lines without LINC01812 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235495, ENSG00000224865, ENSG00000287622 |
| [[ECSCR]] | B | ECSCR activity raises SPRED3's level | lines that do not express ECSCR (35) vs lines expressing it (15) | 1.42× lower at baseline in the lines without ECSCR | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, ADGRF5, ENSG00000243486; maybe low, not absent |
| [[LAT]] | B | LAT activity raises SPRED3's level | lines that do not express LAT (7) vs lines expressing it (43) | 1.59× lower at baseline in the lines without LAT | 0.093 | ⚠ within organs, on part of the lines; also absent: FRG1BP; maybe low, not absent |
| [[PINLYP]] | B | PINLYP activity raises SPRED3's level | lines that do not express PINLYP (17) vs lines expressing it (33) | 1.41× lower at baseline in the lines without PINLYP | 0.0997 | ⚠ within organs, on part of the lines; also absent: C9, BMPER, CALD1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.713). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.3, -20.0); signed map (10.1, 14.0). **Vector** length 113, 27.4% of its response variance represented; |z| ≥ 3 in 1,232 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.9 | +17.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.3 | +10.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +7.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.3 | +8.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +5.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.8 | +2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +1.9 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.9 | -7.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.3 | -7.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.9 | -6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.9 | -7.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.7 | -7.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.6 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | sprouty related EVH1 domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13 — chr19:38,388,421-38,399,587 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sprouty related EVH1 domain containing |
| Reactome | 7 pathways, smallest: RAS signaling downstream of NF1 loss-of-function variants; Regulation of RAS by GAPs; Oncogenic MAPK signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2MJR0](https://www.uniprot.org/uniprotkb/Q2MJR0) (Sprouty-related, EVH1 domain-containing protein 3):

> Tyrosine kinase substrate that inhibits growth-factor-mediated activation of MAP kinase (By similarity). Inhibits fibroblast growth factor (FGF)-induced retinal lens fiber differentiation, probably by inhibiting FGF-mediated phosphorylation of ERK1/2 (By similarity). Inhibits TGFB-induced epithelial-to-mesenchymal transition in lens epithelial cells (By similarity).

**Summary**, from NCBI Gene [399473](https://www.ncbi.nlm.nih.gov/gene/399473):

> This gene encodes a protein with a C-terminal Sprouty-like cysteine-rich domain (SRY) and an N-terminal Ena/Vasodilator-stimulated phosphoprotein (VASP) homology-1 (EVH-1) domain. The encoded protein is a member of a family of proteins that negatively regulates mitogen-activated protein (MAP) kinase signaling, particularly during organogenesis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:31041](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31041) · Entrez [399473](https://www.ncbi.nlm.nih.gov/gene/399473) · UniProt [Q2MJR0](https://www.uniprot.org/uniprotkb/Q2MJR0) · Ensembl [ENSG00000188766](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188766)

## Data

Gene col 12048: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12048); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12048, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12048]; `tensor/DDL_lfc|DDL_z.npy` [12048]; `embed/gene_vectors.npy` [12048]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12048 or target_col == 12048). Every well: [[SPRED3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPRED3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
