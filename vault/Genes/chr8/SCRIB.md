---
symbol: "SCRIB"
type: "gene"
col: 11144
ensembl_id: "ENSG00000180900"
name: "scribble planar cell polarity protein"
location: "8q24.3"
module: 127
arm: "+"
pooled_cpm: 18.86
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# SCRIB

*scribble planar cell polarity protein* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.55× (z +16.1, q 0e+00, up in 29 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.73× (z +10.3, q 1e-22, up in 32 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.648× (z -8.2, q 1e-13, down in 29 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (BT-474 0.180×, NCI-H1573 0.155×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Simotinib (drug)]] 5 µM in 1 line (AsPC-1 0.168×; ⚠ toxic); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0853×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (SNU-1 0.0721×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Panc 03.27 0.432×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DBN1]] (+0.67, fdr 7e-06), [[ATP13A1]] (+0.67, fdr 7e-06), [[MTA1]] (+0.67, fdr 7e-06); moves opposite to [[SMIM27]] (-0.59, fdr 4e-05), [[TRIM7-AS2]] (-0.58, fdr 3e-05), [[RNF181]] (-0.57, fdr 4e-05).
> It is in [[Module 127]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC4A3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11144.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.55×** | +16.1 | 0e+00 | 29/30 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.06×** | +14.8 | 0e+00 | 39/41 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.98×** | +13.4 | 2e-38 | 35/37 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +10.3 | 1e-22 | 32/46 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.98×** | +9.0 | 2e-17 | 36/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.76×** | +7.4 | 9e-12 | 31/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +6.3 | 2e-08 | 27/48 (SW1417, LS 180, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.52×** | +5.5 | 3e-06 | 25/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +5.2 | 1e-05 | 24/45 (C32, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.47×** | +5.1 | 2e-05 | 24/47 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +4.5 | 4e-04 | 21/43 (NCI-H460, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.38×** | +4.3 | 1e-03 | 20/48 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.011 | 15/46 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.5 | 0.017 | 15/47 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Crizotinib (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.026 | 9/46 (LS 180, KATO III, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.62×** | +3.3 | 0.029 | 12/47 (A498, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Folic acid (drug)]] 5 µM |  | 1.18× | +3.0 | 0.075 | 12/48 (NCI-H2347, PANC-1, …) | inconsistent across doses | position effect removed |
| [[crizotinib (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.076 | 7/47 (NCI-H23, LoVo, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11144.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (BT-474 0.180×, NCI-H1573 0.155×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Simotinib (drug)]] 5 µM in 1 line (AsPC-1 0.168×; ⚠ toxic); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0853×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (SNU-1 0.0721×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Panc 03.27 0.432×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.648×** | -8.2 | 1e-13 | 29/46 (Panc 03.27, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.831× | -3.5 | 0.12 | 10/48 (A-427, RKO, …) | rises with dose | position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | 0.798× | -3.0 | 0.45 | 15/47 (C32, NCI-H23, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11144. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 13.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.30× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.49× (z +9.7) | — |
| [[A498 (line)]] | wt | 19.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +11.3) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 15.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.21× (z +11.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 20.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.87× (z +9.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 14.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.43× (z +9.9) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 25.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.80× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 9.54 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +10.9) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 34.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.18× (z +10.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -8.9) |
| [[PANC-1 (line)]] | alt | 17.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +10.2) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.168× (z -10.8) ⚠ toxic |
| [[BT-474 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.180× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0719× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 20.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 23.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.20× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 45.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +10.2) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 16.1 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0853× (z -10.4) |
| [[SNU-1 (line)]] | wt | 13.0 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0721× (z -9.7) |
| [[SNU-423 (line)]] | alt | 7.49 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.47× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 33.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +12.3) | — |
| [[A-172 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11144), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DBN1]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[ATP13A1]] | +0.67 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[MTA1]] | +0.67 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[CUL9]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[RMRP]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[WDR1]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 | same gene group |
| [[PRPF31]] | +0.63 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[OCRL]] | +0.63 | +0.42 / +0.68 | both halves | 4e-05 | pathway: RHOJ GTPase cycle |
| [[PIGO]] | +0.62 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[LAS1L]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[U2AF2]] | +0.62 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[USP19]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM27]] | -0.59 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[TRIM7-AS2]] | -0.58 | -0.43 / -0.63 | both halves | 3e-05 |  |
| [[RNF181]] | -0.57 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[NDUFA7]] | -0.56 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[HIGD2A]] | -0.55 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[RABAC1]] | -0.54 | -0.43 / -0.56 | both halves | 4e-05 |  |
| [[ING2]] | -0.54 | -0.23 / -0.64 | both halves | 5e-04 |  |
| [[ADGRL3-AS1]] | -0.53 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[OST4]] | -0.53 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[DDT]] | -0.53 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[FAU]] | -0.53 | -0.37 / -0.59 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC4A3]] | B | SLC4A3 activity raises SCRIB's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 1.40× lower at baseline in the lines without SLC4A3 | 0.092 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.679). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.8, -25.9); signed map (-12.6, -33.6). **Vector** length 105, 24.5% of its response variance represented; |z| ≥ 3 in 967 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +11.3 | +16.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.7 | +14.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.8 | +13.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.0 | +6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +10.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | +2.5 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +1.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -8.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -1.3 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.5 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.5 | -2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.9 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.1 | -3.0 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.1 | -0.7 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.8 | -0.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | scribble planar cell polarity protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:143,790,920-143,815,773 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0147, SCRB1, Vartul |
| Gene groups (HGNC) | PDZ domain containing; Scribble complex; MicroRNA protein coding host genes |
| Reactome | 12 pathways, smallest: RND2 GTPase cycle; RND3 GTPase cycle; Asymmetric localization of PCP proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [C0HLS1](https://www.uniprot.org/uniprotkb/C0HLS1) (SCRIB overlapping open reading frame protein):

> Regulates the binding of WDR5 to multiple interaction partners, including KMT2A and KIF2A. Promotes WDR5 interaction with KIF2A which ensures correct WDR5 spindle pole localization, leading to correct spindle assembly. Inhibits interaction of WDR5 with KMT2A, preventing binding to and methylation of off-target genes. Directly competes with multiple WDR5 interaction partners for binding to WDR5. Competes with KMT2A/MLL1 for binding to WDR5 which results in inhibition of the methyltransferase …

**Summary**, from NCBI Gene [23513](https://www.ncbi.nlm.nih.gov/gene/23513):

> This gene encodes a protein that was identified as being similar to the Drosophila scribble protein. The mammalian protein is involved in tumor suppression pathways. As a scaffold protein involved in cell polarization processes, this protein binds to many other proteins. The encoded protein binds to papillomavirus E6 protein via its PDZ domain and the C-terminus of E6. Two alternatively spliced transcript variants that encode different protein isoforms have been found for this gene. [provided …

**Accessions** — [HGNC:30377](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30377) · Entrez [23513](https://www.ncbi.nlm.nih.gov/gene/23513) · UniProt [C0HLS1](https://www.uniprot.org/uniprotkb/C0HLS1) · Ensembl [ENSG00000180900](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180900)

## Data

Gene col 11144: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11144); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11144, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11144]; `tensor/DDL_lfc|DDL_z.npy` [11144]; `embed/gene_vectors.npy` [11144]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11144 or target_col == 11144). Every well: [[SCRIB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCRIB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
