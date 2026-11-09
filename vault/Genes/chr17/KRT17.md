---
symbol: "KRT17"
type: "gene"
col: 4882
ensembl_id: "ENSG00000128422"
name: "keratin 17"
location: "17q21.2"
module: 123
arm: "+"
pooled_cpm: 35.86
n_lines_expressing: 13
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# KRT17

*keratin 17* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.08× (z +9.6, q 6e-19, up in 11 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.71× (z +8.3, q 3e-14, up in 11 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (HT-29 0.297×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KRT16]] (+0.54, fdr 1e-05, ⚠ read-through risk), [[DUSP8]] (+0.51, fdr 6e-05), [[SHC2]] (+0.49, fdr 2e-04), [[RHOB]] (+0.48, fdr 1e-04); moves opposite to [[KIAA0753]] (-0.49, fdr 2e-04), [[RASA1]] (-0.45, fdr 6e-05), [[SPRED1]] (-0.43, fdr 5e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CDA]] → it (grade B ⚠); 6 go from it, the strongest it → [[CDA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4882.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.08×** | +9.6 | 6e-19 | 11/12 (HT-29, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.71×** | +8.3 | 3e-14 | 11/11 (LOX-IMVI, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.02×** | +7.6 | 7e-12 | 10/11 (KATO III, LS 180, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.54×** | +7.2 | 1e-10 | 7/11 (LS 180, H4, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **2.14×** | +6.3 | 3e-08 | 10/12 (HT-29, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.10×** | +6.2 | 7e-08 | 8/11 (KATO III, H4, …) | rises with dose | composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **3.14×** | +4.8 | 1e-04 | 9/11 (HT-29, LS 180, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **2.17×** | +4.6 | 3e-04 | 10/11 (HT-29, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.09×** | +4.3 | 1e-03 | 10/12 (Panc 03.27, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **2.03×** | +4.2 | 0.002 | 9/11 (HT-29, LS 180, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.97×** | +4.0 | 0.003 | 8/11 (LS 180, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.78×** | +3.9 | 0.004 | 9/11 (H4, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.91×** | +3.8 | 0.006 | 7/11 (LS 180, Hs 766T, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.94×** | +3.8 | 0.007 | 7/11 (HS-578T, KATO III, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +3.6 | 0.013 | 3/11 (KATO III, J82, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.78×** | +3.4 | 0.025 | 0/11 | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.75×** | +3.3 | 0.032 | 9/11 (KATO III, H4, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[vincristine (drug)]] 5 µM |  | **2.83×** | +3.2 | 0.039 | 5/10 (HT-29, LS 180, …) | two highest doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.65×** | +3.1 | 0.046 | 9/12 (CFPAC-1, H4, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.70×** | +3.0 | 0.062 | 6/11 (HT-29, LS 180, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4882.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (HT-29 0.297×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | 0.578× | -3.2 | 0.40 | 1/11 (H4) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.585× | -3.1 | 0.40 | 6/11 (H4, J82, …) | inconsistent across doses |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 0.593× | -3.1 | 0.40 | 1/11 (HS-578T) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4882. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 148 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +16.8) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[HT-29 (line)]] | alt | 119 | 1 | 1 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 3.81× (z +10.4) | [[Selinexor (drug)]] 5 µM 0.297× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 38.2 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.10× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 82.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.10× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 15.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 12.9× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 493 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.94× (z +9.3) | — |
| [[A-172 (line)]] | wt | 5.37 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.50 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.03 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.33 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 597 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.73 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.45 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.36 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 691 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.53 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.87 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.75 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.26 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.96 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.95 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4882), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 6 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRT16]] | +0.54 | +0.51 / +0.58 | both halves | 1e-05 | same gene group; pathway: Formation of the cornified envelope; STRING 880; ⚠ **readthrough risk**: KRT16 lies 3.5 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[DUSP8]] | +0.51 | +0.39 / +0.50 | both halves | 6e-05 |  |
| [[SHC2]] | +0.49 | +0.31 / +0.57 | both halves | 2e-04 |  |
| [[KRT14]] | +0.49 | +0.40 / +0.41 | both halves | 5e-05 | same gene group; pathway: Formation of the cornified envelope; STRING 814; ⚠ same locus (32.5 kb, same strand: neighbours can correlate without regulation) |
| [[RHOB]] | +0.48 | +0.33 / +0.53 | both halves | 1e-04 |  |
| [[MRTFA]] | +0.47 | +0.39 / +0.53 | both halves | 5e-05 |  |
| [[TRIM29]] | +0.47 | +0.29 / +0.58 | both halves | 2e-04 | STRING 588 |
| [[IL32]] | +0.46 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[ANXA1]] | +0.45 | +0.26 / +0.51 | both halves | 3e-04 |  |
| [[CDA]] | +0.45 | +0.32 / +0.52 | both halves | 2e-04 |  |
| [[SPINK1]] | +0.45 | +0.37 / +0.55 | both halves | 7e-05 |  |
| [[PTGES]] | +0.45 | +0.33 / +0.47 | both halves | 1e-04 |  |
| [[TRIM58]] | +0.45 | +0.24 / +0.56 | both halves | 5e-04 |  |
| [[MAFK]] | +0.44 | +0.39 / +0.43 | both halves | 6e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA0753]] | -0.49 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[RASA1]] | -0.45 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[SPRED1]] | -0.43 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[MYCBP]] | -0.42 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[IPPK]] | -0.41 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[MSANTD2]] | -0.40 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[IVD]] | -0.40 | -0.23 / -0.41 | both halves | 5e-04 |  |
| [[SUV39H2]] | -0.39 | -0.29 / -0.39 | both halves | 2e-04 |  |
| [[WT1]] | -0.39 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[FANCM]] | -0.39 | -0.26 / -0.40 | both halves | 4e-04 |  |
| [[DPY19L3]] | -0.39 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[BDH1]] | -0.38 | -0.27 / -0.48 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDA]] | B | CDA activity raises KRT17's level | lines that do not express CDA (16) vs lines expressing it (34) | 3.65× lower at baseline in the lines without CDA | 0.048 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG |
| [[KRT16]] | C | KRT16 activity raises KRT17's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 4.41× lower at baseline in the lines without KRT16 | 0.009 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6; co-absent with the target |
| [[TRIM29]] | C | TRIM29 activity raises KRT17's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 3.40× lower at baseline in the lines without TRIM29 | 0.036 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2; co-absent with the target |
| [[KRT14]] | C | KRT14 activity raises KRT17's level | lines that do not express KRT14 (43) vs lines expressing it (7) | 4.49× lower at baseline in the lines without KRT14 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230258, DSG4, SPINK13; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDA]] | B | KRT17 activity raises CDA's level | lines that do not express KRT17 (37) vs lines expressing it (13) | 2.09× lower at baseline in the lines without KRT17 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC5AC, FGFR2 |
| [[CFB]] | B | KRT17 activity raises CFB's level | lines that do not express KRT17 (37) vs lines expressing it (13) | 2.54× lower at baseline in the lines without KRT17 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC5AC, FGFR2 |
| [[TNFSF14]] | C | KRT17 activity raises TNFSF14's level | lines that do not express KRT17 (37) vs lines expressing it (13) | 1.41× lower at baseline in the lines without KRT17 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC5AC, FGFR2; co-absent with the target |
| [[C3]] | C | KRT17 activity raises C3's level | lines that do not express KRT17 (37) vs lines expressing it (13) | 1.85× lower at baseline in the lines without KRT17 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC5AC, FGFR2; co-absent with the target |
| [[KRT16]] | C | KRT17 activity raises KRT16's level | lines that do not express KRT17 (37) vs lines expressing it (13) | 2.27× lower at baseline in the lines without KRT17 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC5AC, FGFR2; co-absent with the target |
| [[TRIM29]] | C | KRT17 activity raises TRIM29's level | lines that do not express KRT17 (37) vs lines expressing it (13) | 2.20× lower at baseline in the lines without KRT17 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC5AC, FGFR2; co-absent with the target |

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.401). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.5, -0.6); signed map (53.5, -14.3). **Vector** length 44.1, 14.7% of its response variance represented; |z| ≥ 3 in 350 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +7.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.8 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.8 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +6.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +1.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.4 | -3.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -0.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.0 | -2.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.8 | +0.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -0.7 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | keratin 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:41,619,442-41,624,842 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PCHC1 |
| Gene groups (HGNC) | Keratins, type I |
| Hallmark sets | P53_PATHWAY |
| Reactome | 2 pathways, smallest: Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q04695](https://www.uniprot.org/uniprotkb/Q04695) (Keratin, type I cytoskeletal 17):

> Structural component of intermediate filaments in epithelial keratinocytes. Forms heteropolymers with type II keratins KRT6A and KRT6B, assembling into keratin filament networks that contribute to the structural integrity and specialized differentiation of various epithelial appendages, including nail and hair follicle. Required for the correct growth of hair follicles, in particular for the persistence of the anagen (growth) state (By similarity). Modulates the function of TNF in the specific …

**Summary**, from NCBI Gene [3872](https://www.ncbi.nlm.nih.gov/gene/3872):

> This gene encodes the type I intermediate filament chain keratin 17, expressed in nail bed, hair follicle, sebaceous glands, and other epidermal appendages. Mutations in this gene lead to Jackson-Lawler type pachyonychia congenita and steatocystoma multiplex. [provided by RefSeq, Aug 2008]

**Accessions** — [HGNC:6427](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6427) · Entrez [3872](https://www.ncbi.nlm.nih.gov/gene/3872) · UniProt [Q04695](https://www.uniprot.org/uniprotkb/Q04695) · Ensembl [ENSG00000128422](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128422)

## Data

Gene col 4882: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4882); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4882, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4882]; `tensor/DDL_lfc|DDL_z.npy` [4882]; `embed/gene_vectors.npy` [4882]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4882 or target_col == 4882). Every well: [[KRT17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRT17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
