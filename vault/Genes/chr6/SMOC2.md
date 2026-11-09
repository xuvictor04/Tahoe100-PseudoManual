---
symbol: "SMOC2"
type: "gene"
col: 3380
ensembl_id: "ENSG00000112562"
name: "SPARC related modular calcium binding 2"
location: "6q27"
module: 27
arm: "+"
pooled_cpm: 6.74
n_lines_expressing: 17
n_dd_up: 22
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 33
direction_downstream: 25
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# SMOC2

*SPARC related modular calcium binding 2* — 6q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.92× (z +20.1, q 0e+00, up in 5 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Artesunate (drug)]] 0.5 µM: 0.495× (z -5.2, q 1e-04, down in 3 of 14 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (SHP-77 0.0298×, SW480 0.0647×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SHP-77 0.127×, SW480 0.0738×; ⚠ cell-cycle shift, explains ~9% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (SHP-77 0.133×; ⚠ cell-cycle shift, explains ~20% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.247×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (SW480 0.0955×); [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (A-427 0.0564×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST18]] (+0.83, fdr 7e-06), [[RMST]] (+0.78, fdr 7e-06), [[PKHD1]] (+0.77, fdr 7e-06); moves opposite to [[PASD1]] (-0.47, fdr 6e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 33 arrows point to it, the strongest [[POU3F2]] → it (grade B ⚠); 25 go from it, the strongest it → [[PDK4-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3380.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.92×** | +20.1 | 0e+00 | 5/12 (NCI-H1573, SNU-423, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.70×** | +11.4 | 1e-27 | 4/11 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.80×** | +10.7 | 2e-24 | 4/11 (SNU-423, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.72×** | +9.7 | 5e-20 | 4/7 (HEC-1-A, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.61×** | +9.1 | 1e-17 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.40×** | +8.3 | 7e-15 | 0/3 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.47×** | +6.7 | 2e-09 | 6/13 (KATO III, SNU-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.82×** | +5.4 | 5e-06 | 4/13 (SW480, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +5.0 | 4e-05 | 3/13 (BT-474, HEC-1-A, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.96×** | +4.9 | 4e-05 | 0/12 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.59×** | +4.7 | 2e-04 | 1/13 (SW480) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.85×** | +4.4 | 6e-04 | 3/13 (NCI-H1573, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~7% here); composition shift |
| [[Alpelisib (drug)]] 5 µM |  | **2.96×** | +4.2 | 0.001 | 2/11 (SW480, COLO 205) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.68×** | +4.2 | 0.001 | 2/13 (SW480, BT-474) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.76×** | +4.2 | 0.001 | 3/13 (SW480, COLO 205, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.16×** | +4.1 | 0.002 | 1/10 (HEC-1-A) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.67×** | +3.7 | 0.007 | 1/14 (SW480) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **2.00×** | +3.6 | 0.009 | 1/13 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.69×** | +3.6 | 0.011 | 3/13 (SW480, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3380.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (SHP-77 0.0298×, SW480 0.0647×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SHP-77 0.127×, SW480 0.0738×; ⚠ cell-cycle shift, explains ~9% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (SHP-77 0.133×; ⚠ cell-cycle shift, explains ~20% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.247×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (SW480 0.0955×); [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (A-427 0.0564×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | **0.495×** | -5.2 | 1e-04 | 3/14 (COLO 205, BT-474, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.624× | -3.5 | 0.14 | 6/13 (SW480, SHP-77, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.655× | -3.1 | 0.33 | 4/13 (SW480, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.665× | -3.0 | 0.36 | 6/14 (LS 180, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3380. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 33.3 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0298× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.247× (z -10.7) |
| [[SW480 (line)]] | alt | 74.4 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0647× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0955× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 3.04 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 313× (z +19.5) | — |
| [[A-427 (line)]] | wt | 9.92 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0564× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 7.89 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0759× (z -8.7) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SNU-423 (line)]] | alt | 2.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.2× (z +10.7) | — |
| [[A-172 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.707 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.998 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.963 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.861 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.927 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.981 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.783 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.866 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.942 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.905 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.844 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.952 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.896 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.10 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3380), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST18]] | +0.83 | +0.81 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[RMST]] | +0.78 | +0.82 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[PKHD1]] | +0.77 | +0.77 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[JAKMIP2-AS1]] | +0.74 | +0.71 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1]] | +0.73 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[B3GAT1-DT]] | +0.73 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[LINC02058]] | +0.72 | +0.63 / +0.79 | both halves | 7e-06 |  |
| [[CHDH]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[HS3ST5]] | +0.69 | +0.67 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[PHYHIPL]] | +0.67 | +0.55 / +0.68 | both halves | 1e-05 | **novel candidate** |
| [[LINC00299]] | +0.67 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[LINC01814]] | +0.66 | +0.61 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PASD1]] | -0.47 | -0.41 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 3, C 30. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POU3F2]] | B | POU3F2 activity raises SMOC2's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 1.28× lower at baseline in the lines without POU3F2 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC |
| [[SLC7A8]] | B | SLC7A8 activity raises SMOC2's level | lines that do not express SLC7A8 (19) vs lines expressing it (31) | 1.87× lower at baseline in the lines without SLC7A8 | 0.089 | ⚠ within organs, on part of the lines; also absent: RAB17, LINC00698, RGS6 |
| [[MAP2K1]] | B | MAP2K1 activity lowers SMOC2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[TFF3]] | C | TFF3 activity raises SMOC2's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 3.35× lower at baseline in the lines without TFF3 | 0.004 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; co-absent with the target |
| [[LINC02050]] | C | LINC02050 activity raises SMOC2's level | lines that do not express LINC02050 (37) vs lines expressing it (13) | 2.50× lower at baseline in the lines without LINC02050 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000286329, ENSG00000242828, PASD1; co-absent with the target |
| [[PSG1]] | C | PSG1 activity raises SMOC2's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 3.21× lower at baseline in the lines without PSG1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB; co-absent with the target |
| [[MIR3667HG]] | C | MIR3667HG activity raises SMOC2's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 2.98× lower at baseline in the lines without MIR3667HG | 0.013 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA; co-absent with the target |
| [[MUC6]] | C | MUC6 activity raises SMOC2's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 4.94× lower at baseline in the lines without MUC6 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |
| [[PHYHIPL]] | C | PHYHIPL activity raises SMOC2's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 1.88× lower at baseline in the lines without PHYHIPL | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA; co-absent with the target |
| [[ST18]] | C | ST18 activity raises SMOC2's level | lines that do not express ST18 (39) vs lines expressing it (11) | 3.20× lower at baseline in the lines without ST18 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000213981, CALCA, KCNB2; maybe low, not absent; co-absent with the target |
| [[LINC02253]] | C | LINC02253 activity raises SMOC2's level | lines that do not express LINC02253 (35) vs lines expressing it (15) | 2.73× lower at baseline in the lines without LINC02253 | 0.021 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02058, ENSG00000289349; co-absent with the target |
| [[RUNX1T1]] | C | RUNX1T1 activity raises SMOC2's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 2.05× lower at baseline in the lines without RUNX1T1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 5, C 20. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDK4-AS1]] | B | SMOC2 activity raises PDK4-AS1's level | lines that do not express SMOC2 (33) vs lines expressing it (17) | 2.00× lower at baseline in the lines without SMOC2 | 0.024 | ⚠ within organs, on part of the lines; also absent: LINC01456, TFF3, MIR3667HG; maybe low, not absent |
| [[BCAR3-AS1]] | B | SMOC2 activity raises BCAR3-AS1's level | lines that do not express SMOC2 (33) vs lines expressing it (17) | 1.63× lower at baseline in the lines without SMOC2 | 0.030 | ⚠ within organs, on part of the lines; also absent: LINC01456, TFF3, MIR3667HG; maybe low, not absent |
| [[NCALD]] | B | SMOC2 activity raises NCALD's level | lines that do not express SMOC2 (33) vs lines expressing it (17) | 2.14× lower at baseline in the lines without SMOC2 | 0.039 | ⚠ within organs, on part of the lines; also absent: LINC01456, TFF3, MIR3667HG; maybe low, not absent |
| [[FGD3]] | B | SMOC2 activity raises FGD3's level | lines that do not express SMOC2 (33) vs lines expressing it (17) | 1.73× lower at baseline in the lines without SMOC2 | 0.048 | ⚠ within organs, on part of the lines; also absent: LINC01456, TFF3, MIR3667HG; maybe low, not absent |
| [[TSPOAP1]] | B | SMOC2 activity raises TSPOAP1's level | lines that do not express SMOC2 (33) vs lines expressing it (17) | 1.82× lower at baseline in the lines without SMOC2 | 0.056 | ⚠ within organs, on part of the lines; also absent: LINC01456, TFF3, MIR3667HG; maybe low, not absent |
| [[SYK]] | C | SMOC2 activity raises SYK's level | lines that do not express SMOC2 (33) vs lines expressing it (17) | 3.66× lower at baseline in the lines without SMOC2 | 0.002 | ⚠ within organs, on part of the lines; also absent: LINC01456, TFF3, MIR3667HG; maybe low, not absent; co-absent with the target |
| [[TFF3]] | C | SMOC2 activity raises TFF3's level | lines that do not express SMOC2 (33) vs lines expressing it (17) | 4.51× lower at baseline in the lines without SMOC2 | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC01456, TFF3, MIR3667HG; maybe low, not absent; co-absent with the target |
| [[PKHD1]] | C | SMOC2 activity raises PKHD1's level | lines that do not express SMOC2 (33) vs lines expressing it (17) | 2.20× lower at baseline in the lines without SMOC2 | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC01456, TFF3, MIR3667HG; maybe low, not absent; co-absent with the target |
| [[MYB]] | C | SMOC2 activity raises MYB's level | lines that do not express SMOC2 (33) vs lines expressing it (17) | 2.42× lower at baseline in the lines without SMOC2 | 0.010 | ⚠ within organs, on part of the lines; also absent: LINC01456, TFF3, MIR3667HG; maybe low, not absent; co-absent with the target |
| [[RAB17]] | C | SMOC2 activity raises RAB17's level | lines that do not express SMOC2 (33) vs lines expressing it (17) | 3.04× lower at baseline in the lines without SMOC2 | 0.013 | ⚠ within organs, on part of the lines; also absent: LINC01456, TFF3, MIR3667HG; maybe low, not absent; co-absent with the target |
| [[CLRN3]] | C | SMOC2 activity raises CLRN3's level | lines that do not express SMOC2 (33) vs lines expressing it (17) | 2.24× lower at baseline in the lines without SMOC2 | 0.018 | ⚠ within organs, on part of the lines; also absent: LINC01456, TFF3, MIR3667HG; maybe low, not absent; co-absent with the target |
| [[ST18]] | C | SMOC2 activity raises ST18's level | lines that do not express SMOC2 (33) vs lines expressing it (17) | 2.33× lower at baseline in the lines without SMOC2 | 0.020 | ⚠ within organs, on part of the lines; also absent: LINC01456, TFF3, MIR3667HG; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.829). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.1, 43.6); signed map (62.4, 15.9). **Vector** length 50.6, 17.1% of its response variance represented; |z| ≥ 3 in 353 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +8.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +20.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +4.1 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -5.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -1.6 | -1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -2.7 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | SPARC related modular calcium binding 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q27 — chr6:168,441,151-168,673,445 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SMAP2 |
| Gene groups (HGNC) | SPARC family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3U7](https://www.uniprot.org/uniprotkb/Q9H3U7) (SPARC-related modular calcium-binding protein 2):

> Promotes matrix assembly and cell adhesiveness (By similarity). Can stimulate endothelial cell proliferation, migration, as well as angiogenesis.

**Summary**, from NCBI Gene [64094](https://www.ncbi.nlm.nih.gov/gene/64094):

> This gene encodes a member of the SPARC family (secreted protein acidic and rich in cysteine/osteonectin/BM-40), which are highly expressed during embryogenesis and wound healing. The gene product is a matricellular protein which promotes matrix assembly and can stimulate endothelial cell proliferation and migration, as well as angiogenic activity. Associated with pulmonary function, this secretory gene product contains a Kazal domain, two thymoglobulin type-1 domains, and two EF-hand …

**Accessions** — [HGNC:20323](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20323) · Entrez [64094](https://www.ncbi.nlm.nih.gov/gene/64094) · UniProt [Q9H3U7](https://www.uniprot.org/uniprotkb/Q9H3U7) · Ensembl [ENSG00000112562](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112562)

## Data

Gene col 3380: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3380); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3380, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3380]; `tensor/DDL_lfc|DDL_z.npy` [3380]; `embed/gene_vectors.npy` [3380]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3380 or target_col == 3380). Every well: [[SMOC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMOC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
