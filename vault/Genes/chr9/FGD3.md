---
symbol: "FGD3"
type: "gene"
col: 4788
ensembl_id: "ENSG00000127084"
name: "FYVE, RhoGEF and PH domain containing 3"
location: "9q22.31"
module: 27
arm: "+"
pooled_cpm: 3.23
n_lines_expressing: 31
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 58
direction_downstream: 23
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# FGD3

*FYVE, RhoGEF and PH domain containing 3* — 9q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.28× (z +12.4, q 1e-32, up in 1 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.78× (z +7.2, q 6e-11, up in 7 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.603× (z -4.5, q 0.004, down in 13 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (COLO 205 0.0578×, HT-29 0.0852×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (COLO 205 0.0347×, SW480 0.147×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 0.0300×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 0.136×); [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 0.202×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B3GAT1-DT]] (+0.75, fdr 7e-06), [[KCNE3]] (+0.74, fdr 7e-06), [[LINC02058]] (+0.69, fdr 1e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 58 arrows point to it, the strongest [[SLC40A1]] → it (grade B ⚠); 23 go from it, the strongest it → [[TNFRSF14-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4788.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.28×** | +12.4 | 1e-32 | 1/4 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.93×** | +12.1 | 2e-31 | 2/7 (NCI-H2347, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.92×** | +11.2 | 7e-27 | 1/4 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.78×** | +7.2 | 6e-11 | 7/26 (KATO III, LS 180, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +6.4 | 2e-08 | 10/25 (SW1417, HS-578T, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +6.3 | 2e-08 | 5/19 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +6.0 | 1e-07 | 3/11 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.89×** | +5.6 | 1e-06 | 7/26 (SK-MEL-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +4.2 | 0.002 | 9/24 (NCI-H2347, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.59×** | +4.1 | 0.002 | 9/24 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.51×** | +3.6 | 0.015 | 8/25 (LS 180, LoVo, …) | top dose only |  |
| [[Decitabine (drug)]] 0.5 µM |  | **1.49×** | +3.5 | 0.019 | 2/20 (SW1417, SHP-77) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.47×** | +3.4 | 0.027 | 0/25 | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.027 | 4/27 (SW480, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +3.4 | 0.027 | 6/25 (SK-MEL-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.59×** | +2.9 | 0.092 | 1/18 (HCT15) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4788.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (COLO 205 0.0578×, HT-29 0.0852×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (COLO 205 0.0347×, SW480 0.147×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 0.0300×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 0.136×); [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 0.202×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.603×** | -4.5 | 0.004 | 13/27 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.625×** | -4.2 | 0.008 | 12/25 (SW480, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); position effect removed |
| [[Fusidic acid (drug)]] 5 µM |  | 0.768× | -3.3 | 0.15 | 1/26 (NCI-H2030) | top dose only |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 0.703× | -3.2 | 0.23 | 2/26 (HOP62, SW48) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.715× | -3.0 | 0.30 | 1/26 (C-33 A) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4788. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 21.7 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0300× (z -21.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.136× (z -12.4) |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0578× (z -17.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0347× (z -14.1) |
| [[HT-29 (line)]] | alt | 12.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0852× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0791× (z -9.7) |
| [[SW1417 (line)]] | alt | 10.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.11× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 0.545 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.675 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.795 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.962 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.928 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.812 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.519 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.601 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.541 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.804 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.906 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.549 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.583 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.601 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.797 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.664 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.462 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.674 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.969 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.784 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.98 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4788), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GAT1-DT]] | +0.75 | +0.81 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[KCNE3]] | +0.74 | +0.76 / +0.60 | both halves | 7e-06 |  |
| [[LINC02058]] | +0.69 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[LINC02253]] | +0.67 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[ABO]] | +0.67 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[CLRN3]] | +0.66 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[C11orf52]] | +0.66 | +0.74 / +0.49 | both halves | 1e-05 |  |
| [[VIL1]] | +0.66 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[ILDR1]] | +0.65 | +0.60 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[SULT1C2]] | +0.64 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[A1CF]] | +0.64 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[SYK]] | +0.64 | +0.62 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*58 arrows, 58 of them with an alert ⚠; grade A 0, B 30, C 28. Shown: the 12 strongest; 46 more arrows (46 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC40A1]] | B | SLC40A1 activity raises FGD3's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 2.09× lower at baseline in the lines without SLC40A1 | 0.004 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[TMEM139]] | B | TMEM139 activity raises FGD3's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 2.49× lower at baseline in the lines without TMEM139 | 0.004 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A |
| [[SERPINF1]] | B | SERPINF1 activity raises FGD3's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.57× lower at baseline in the lines without SERPINF1 | 0.007 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent |
| [[PHYHIPL]] | B | PHYHIPL activity raises FGD3's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 1.28× lower at baseline in the lines without PHYHIPL | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[RORC]] | B | RORC activity raises FGD3's level | lines that do not express RORC (30) vs lines expressing it (20) | 2.06× lower at baseline in the lines without RORC | 0.011 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[QPRT]] | B | QPRT activity raises FGD3's level | lines that do not express QPRT (21) vs lines expressing it (29) | 1.50× lower at baseline in the lines without QPRT | 0.013 | ⚠ within organs, on part of the lines; also absent: OPRD1, FREM2, SERPINF1 |
| [[TSPOAP1]] | B | TSPOAP1 activity raises FGD3's level | lines that do not express TSPOAP1 (25) vs lines expressing it (25) | 2.06× lower at baseline in the lines without TSPOAP1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RNF39, MAL2, VWA2 |
| [[LINC01819]] | B | LINC01819 activity raises FGD3's level | lines that do not express LINC01819 (29) vs lines expressing it (21) | 1.78× lower at baseline in the lines without LINC01819 | 0.033 | ⚠ within organs, on part of the lines; also absent: MOGAT3, LGR6, A1CF; maybe low, not absent |
| [[MIR4713HG]] | B | MIR4713HG activity raises FGD3's level | lines that do not express MIR4713HG (30) vs lines expressing it (20) | 2.35× lower at baseline in the lines without MIR4713HG | 0.035 | ⚠ within organs, on part of the lines; also absent: GLDN, C4BPB, IL20RA |
| [[PRR15]] | B | PRR15 activity raises FGD3's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 2.26× lower at baseline in the lines without PRR15 | 0.036 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |
| [[SLC44A3]] | B | SLC44A3 activity raises FGD3's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 1.90× lower at baseline in the lines without SLC44A3 | 0.037 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[C11orf52]] | B | C11orf52 activity raises FGD3's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 1.85× lower at baseline in the lines without C11orf52 | 0.039 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 8, C 15. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF14-AS1]] | B | FGD3 activity raises TNFRSF14-AS1's level | lines that do not express FGD3 (19) vs lines expressing it (31) | 1.85× lower at baseline in the lines without FGD3 | 0.031 | ⚠ within organs, on part of the lines; also absent: CGN, SPINT1-AS1, SPINT1; maybe low, not absent |
| [[ADCY4]] | B | FGD3 activity raises ADCY4's level | lines that do not express FGD3 (19) vs lines expressing it (31) | 2.08× lower at baseline in the lines without FGD3 | 0.055 | ⚠ within organs, on part of the lines; also absent: CGN, SPINT1-AS1, SPINT1; maybe low, not absent |
| [[SH3BGRL2]] | B | FGD3 activity raises SH3BGRL2's level | lines that do not express FGD3 (19) vs lines expressing it (31) | 2.99× lower at baseline in the lines without FGD3 | 0.070 | ⚠ within organs, on part of the lines; also absent: CGN, SPINT1-AS1, SPINT1; maybe low, not absent |
| [[SEMA4G]] | B | FGD3 activity raises SEMA4G's level | lines that do not express FGD3 (19) vs lines expressing it (31) | 2.04× lower at baseline in the lines without FGD3 | 0.071 | ⚠ within organs, on part of the lines; also absent: CGN, SPINT1-AS1, SPINT1; maybe low, not absent |
| [[RORC]] | B | FGD3 activity raises RORC's level | lines that do not express FGD3 (19) vs lines expressing it (31) | 2.04× lower at baseline in the lines without FGD3 | 0.071 | ⚠ within organs, on part of the lines; also absent: CGN, SPINT1-AS1, SPINT1; maybe low, not absent |
| cells under [[Ivermectin (drug)]] 0.5 µM | B | FGD3 activity raises the cells' numbers under Ivermectin 0.5 µM (protects the cells) | lines that do not express FGD3 (19) vs lines expressing it (29) | the lines without FGD3: 0.87× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: CGN, SPINT1-AS1, SPINT1; maybe low, not absent |
| [[SLC44A3]] | B | FGD3 activity raises SLC44A3's level | lines that do not express FGD3 (19) vs lines expressing it (31) | 2.41× lower at baseline in the lines without FGD3 | 0.082 | ⚠ within organs, on part of the lines; also absent: CGN, SPINT1-AS1, SPINT1; maybe low, not absent |
| [[LPAR5]] | B | FGD3 activity raises LPAR5's level | lines that do not express FGD3 (19) vs lines expressing it (31) | 1.87× lower at baseline in the lines without FGD3 | 0.094 | ⚠ within organs, on part of the lines; also absent: CGN, SPINT1-AS1, SPINT1; maybe low, not absent |
| [[RAB17]] | C | FGD3 activity raises RAB17's level | lines that do not express FGD3 (19) vs lines expressing it (31) | 3.30× lower at baseline in the lines without FGD3 | 0.010 | ⚠ within organs, on part of the lines; also absent: CGN, SPINT1-AS1, SPINT1; maybe low, not absent; co-absent with the target |
| [[PROM1]] | C | FGD3 activity raises PROM1's level | lines that do not express FGD3 (19) vs lines expressing it (31) | 3.11× lower at baseline in the lines without FGD3 | 0.034 | ⚠ within organs, on part of the lines; also absent: CGN, SPINT1-AS1, SPINT1; maybe low, not absent; co-absent with the target |
| [[HSD11B2]] | C | FGD3 activity raises HSD11B2's level | lines that do not express FGD3 (19) vs lines expressing it (31) | 2.14× lower at baseline in the lines without FGD3 | 0.035 | ⚠ within organs, on part of the lines; also absent: CGN, SPINT1-AS1, SPINT1; maybe low, not absent; co-absent with the target |
| [[TOX3]] | C | FGD3 activity raises TOX3's level | lines that do not express FGD3 (19) vs lines expressing it (31) | 3.94× lower at baseline in the lines without FGD3 | 0.041 | ⚠ within organs, on part of the lines; also absent: CGN, SPINT1-AS1, SPINT1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.5, 47.4); signed map (61.0, 12.7). **Vector** length 44.3, 7.87% of its response variance represented; |z| ≥ 3 in 605 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.7 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +11.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +12.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +3.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.5 | +2.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.1 | -4.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -1.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -1.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | FYVE, RhoGEF and PH domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.31 — chr9:92,947,523-93,036,236 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00004, ZFYVE5 |
| Gene groups (HGNC) | Zinc fingers FYVE-type; Pleckstrin homology domain containing; Dbl family Rho GEFs |
| Reactome | 11 pathways, smallest: NRAGE signals death through JNK; G alpha (12/13) signalling events; Cell death signalling via NRAGE, NRIF and NADE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JSP0](https://www.uniprot.org/uniprotkb/Q5JSP0) (FYVE, RhoGEF and PH domain-containing protein 3):

> Promotes the formation of filopodia. May activate CDC42, a member of the Ras-like family of Rho- and Rac proteins, by exchanging bound GDP for free GTP. Plays a role in regulating the actin cytoskeleton and cell shape (By similarity).

**Summary**, from NCBI Gene [89846](https://www.ncbi.nlm.nih.gov/gene/89846):

> Predicted to enable guanyl-nucleotide exchange factor activity and small GTPase binding activity. Predicted to be involved in actin cytoskeleton organization; filopodium assembly; and regulation of cell shape. Predicted to be located in Golgi apparatus; lamellipodium; and ruffle. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16027](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16027) · Entrez [89846](https://www.ncbi.nlm.nih.gov/gene/89846) · UniProt [Q5JSP0](https://www.uniprot.org/uniprotkb/Q5JSP0) · Ensembl [ENSG00000127084](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127084)

## Data

Gene col 4788: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4788); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4788, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4788]; `tensor/DDL_lfc|DDL_z.npy` [4788]; `embed/gene_vectors.npy` [4788]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4788 or target_col == 4788). Every well: [[FGD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
