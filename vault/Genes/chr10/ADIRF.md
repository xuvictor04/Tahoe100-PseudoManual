---
symbol: "ADIRF"
type: "gene"
col: 7302
ensembl_id: "ENSG00000148671"
name: "adipogenesis regulatory factor"
location: "10q23.2"
module: 73
arm: "+"
pooled_cpm: 10.38
n_lines_expressing: 19
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 8
direction_downstream: 5
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# ADIRF

*adipogenesis regulatory factor* — 10q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.10× (z +11.6, q 2e-28, up in 13 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.81× (z +9.4, q 1e-18, up in 7 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.543× (z -4.0, q 0.041, down in 11 of 15 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.561× (z -3.7, q 0.050, down in 11 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LoVo 0.138×; ⚠ cell-cycle shift, explains ~49% of this change).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C19orf33]] (+0.60, fdr 3e-05), [[CRIP1]] (+0.59, fdr 2e-04), [[CTNNA3]] (+0.55, fdr 1e-05); moves opposite to [[POFUT1]] (-0.41, fdr 4e-04), [[NARS1]] (-0.41, fdr 1e-04), [[NUDC]] (-0.41, fdr 1e-04).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ATRNL1]] → it (grade B ⚠); 5 go from it, the strongest it → cells under [[Temuterkib (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7302.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.10×** | +11.6 | 2e-28 | 13/13 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **3.34×** | +10.9 | 2e-25 | 8/14 (A-172, AsPC-1, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.32×** | +10.3 | 1e-22 | 11/11 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.81×** | +9.4 | 1e-18 | 7/15 (A-172, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.02×** | +8.2 | 2e-14 | 12/13 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **2.56×** | +5.8 | 7e-07 | 6/15 (SW480, A-172, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.23×** | +5.1 | 3e-05 | 13/15 (SW1417, NCI-H1573, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.74×** | +5.0 | 5e-05 | 9/15 (SW480, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.72×** | +4.6 | 3e-04 | 14/15 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +4.2 | 0.001 | 7/14 (MIA PaCa-2, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.94×** | +4.2 | 0.001 | 4/15 (SW1417, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.74×** | +4.0 | 0.002 | 3/7 (NCI-H2347, SW480, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.17×** | +3.5 | 0.017 | 11/15 (BT-474, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +3.4 | 0.030 | 4/14 (MIA PaCa-2, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.69×** | +3.4 | 0.030 | 4/14 (A-172, SW1417, …) | rises with dose |  |
| [[Arbutin (drug)]] 5 µM |  | **1.68×** | +3.2 | 0.047 | 11/15 (LS 180, A-172, …) | top dose only |  |
| [[Filgotinib (drug)]] 0.5 µM |  | **1.64×** | +3.2 | 0.050 | 8/15 (SW48, LoVo, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.95×** | +3.0 | 0.071 | 8/15 (Hs 766T, LS 180, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.94×** | +3.0 | 0.071 | 5/15 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7302.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LoVo 0.138×; ⚠ cell-cycle shift, explains ~49% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.543×** | -4.0 | 0.041 | 11/15 (Hs 766T, LoVo, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.561×** | -3.7 | 0.050 | 11/15 (LoVo, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.601× | -3.1 | 0.41 | 2/15 (A-172, SW480) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.75 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7302. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.43 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.84× (z +9.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.66× (z +8.7) | — |
| [[AsPC-1 (line)]] | alt | 7.75 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.45× (z +8.8) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[LoVo (line)]] | wt | 19.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -8.7) ⚠ cell-cycle shift, explains ~49% of this change |
| [[SW480 (line)]] | alt | 11.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.29× (z +10.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 0.814 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.898 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 97.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.868 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.794 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7302), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 10 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C19orf33]] | +0.60 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[CRIP1]] | +0.59 | +0.32 / +0.64 | both halves | 2e-04 |  |
| [[CTNNA3]] | +0.55 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[PHGR1]] | +0.54 | +0.54 / +0.40 | both halves | 4e-05 |  |
| [[S100A2]] | +0.54 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[PCDH11X]] | +0.52 | +0.43 / +0.48 | both halves | 4e-05 |  |
| [[REG4]] | +0.52 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[EPCAM]] | +0.51 | +0.26 / +0.53 | both halves | 4e-04 |  |
| [[TFF2]] | +0.51 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[RHOD]] | +0.49 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[TSTD1]] | +0.49 | +0.21 / +0.65 | both halves | 7e-04 |  |
| [[S100A4]] | +0.49 | +0.36 / +0.52 | both halves | 1e-04 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POFUT1]] | -0.41 | -0.26 / -0.50 | both halves | 4e-04 |  |
| [[NARS1]] | -0.41 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[NUDC]] | -0.41 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[CDK5RAP2]] | -0.39 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[TOP3B]] | -0.38 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[EP400]] | -0.37 | -0.24 / -0.38 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATRNL1]] | B | ATRNL1 activity lowers ADIRF's level | lines that do not express ATRNL1 (21) vs lines expressing it (29) | 2.66× higher at baseline in the lines without ATRNL1 | 0.078 | ⚠ within organs, on part of the lines; also absent: CAMK4, BVES, NEGR1; maybe low, not absent |
| [[PCDH11X]] | B | PCDH11X activity raises ADIRF's level | lines that do not express PCDH11X (15) vs lines expressing it (35) | 2.11× lower at baseline in the lines without PCDH11X | 0.078 | ⚠ within organs, on part of the lines; also absent: XDH, CRYBG2, SPATA6L; maybe low, not absent |
| [[CEACAM6]] | C | CEACAM6 activity raises ADIRF's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 5.17× lower at baseline in the lines without CEACAM6 | 0.006 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17; co-absent with the target |
| [[FGFBP1]] | C | FGFBP1 activity raises ADIRF's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 4.23× lower at baseline in the lines without FGFBP1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5; co-absent with the target |
| [[COL17A1]] | C | COL17A1 activity raises ADIRF's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 4.32× lower at baseline in the lines without COL17A1 | 0.021 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1; co-absent with the target |
| [[S100A2]] | C | S100A2 activity raises ADIRF's level | lines that do not express S100A2 (25) vs lines expressing it (25) | 2.03× lower at baseline in the lines without S100A2 | 0.073 | ⚠ within organs, on part of the lines; also absent: KRT81, LINC00408, FGFBP1; maybe low, not absent; co-absent with the target |
| [[FXYD3]] | C | FXYD3 activity raises ADIRF's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 3.40× lower at baseline in the lines without FXYD3 | 0.076 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2; co-absent with the target |
| [[TSPAN1]] | C | TSPAN1 activity raises ADIRF's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 3.24× lower at baseline in the lines without TSPAN1 | 0.080 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Temuterkib (drug)]] 5 µM | B | ADIRF activity lowers the cells' numbers under Temuterkib 5 µM (makes them more sensitive) | lines that do not express ADIRF (31) vs lines expressing it (17) | the lines without ADIRF: 1.14× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: CEACAM6, FGFBP1, KRT6A |
| [[CEACAM6]] | C | ADIRF activity raises CEACAM6's level | lines that do not express ADIRF (31) vs lines expressing it (19) | 5.03× lower at baseline in the lines without ADIRF | 0.026 | ⚠ within organs, on part of the lines; also absent: CEACAM6, FGFBP1, KRT6A; co-absent with the target |
| [[LINC02484]] | C | ADIRF activity raises LINC02484's level | lines that do not express ADIRF (31) vs lines expressing it (19) | 1.41× lower at baseline in the lines without ADIRF | 0.063 | ⚠ within organs, on part of the lines; also absent: CEACAM6, FGFBP1, KRT6A; co-absent with the target |
| [[FXYD3]] | C | ADIRF activity raises FXYD3's level | lines that do not express ADIRF (31) vs lines expressing it (19) | 2.95× lower at baseline in the lines without ADIRF | 0.083 | ⚠ within organs, on part of the lines; also absent: CEACAM6, FGFBP1, KRT6A; co-absent with the target |
| [[COL17A1]] | C | ADIRF activity raises COL17A1's level | lines that do not express ADIRF (31) vs lines expressing it (19) | 4.58× lower at baseline in the lines without ADIRF | 0.089 | ⚠ within organs, on part of the lines; also absent: CEACAM6, FGFBP1, KRT6A; co-absent with the target |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.383). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (0.4, 55.9); signed map (47.2, -4.5). **Vector** length 43.3, 15.0% of its response variance represented; |z| ≥ 3 in 240 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +10.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +3.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.1 | +4.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -0.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.2 | -0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.0 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | adipogenesis regulatory factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.2 — chr10:86,968,432-86,983,934 (+) |
| Ensembl biotype | protein_coding |
| Also known as | APM2, AFRO; previously C10orf116 |
| Reactome | 2 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; Adipogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15847](https://www.uniprot.org/uniprotkb/Q15847) (Adipogenesis regulatory factor):

> Plays a role in fat cell development; promotes adipogenic differentiation and stimulates transcription initiation of master adipogenesis factors like PPARG and CEBPA at early stages of preadipocyte differentiation. Its overexpression confers resistance to the anticancer chemotherapeutic drug cisplatin.

**Summary**, from NCBI Gene [10974](https://www.ncbi.nlm.nih.gov/gene/10974):

> APM2 gene is exclusively expressed in adipose tissue. Its function is currently unknown. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:24043](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24043) · Entrez [10974](https://www.ncbi.nlm.nih.gov/gene/10974) · UniProt [Q15847](https://www.uniprot.org/uniprotkb/Q15847) · Ensembl [ENSG00000148671](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148671)

## Data

Gene col 7302: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7302); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7302, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7302]; `tensor/DDL_lfc|DDL_z.npy` [7302]; `embed/gene_vectors.npy` [7302]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7302 or target_col == 7302). Every well: [[ADIRF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADIRF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
