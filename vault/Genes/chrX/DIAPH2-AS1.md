---
symbol: "DIAPH2-AS1"
type: "gene"
col: 14072
ensembl_id: "ENSG00000236256"
name: "DIAPH2 antisense RNA 1"
location: "Xq21.33"
module: 158
arm: "+"
pooled_cpm: 10.71
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/158"]
generated_by: "tahoemap"
---

# DIAPH2-AS1

*DIAPH2 antisense RNA 1* — Xq21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.70× (z +20.4, q 0e+00, up in 31 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.900× (z -5.4, q 5e-05, down in 10 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Diphenhydramine (drug)]] 0.05 µM: 0.766× (z -3.6, q 0.091, down in 8 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Fluvoxamine (drug)]] 5 µM in 1 line (SNU-423 0.0622×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.103×; ⚠ toxic); [[Lonafarnib (drug)]] 5 µM in 1 line (SW1417 0.0764×; ⚠ toxic); [[Decitabine (drug)]] 5 µM in 1 line (NCI-H23 0.0662×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL14]] (+0.62, fdr 1e-05), [[OTUD6B-AS1]] (+0.62, fdr 1e-05), [[CD163L1]] (+0.60, fdr 1e-05); moves opposite to [[SETD3]] (-0.56, fdr 3e-05), [[ADAM15]] (-0.54, fdr 3e-05), [[AP2A1]] (-0.54, fdr 2e-05).
> It is in [[Module 158]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[ICAM2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14072.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.70×** | +20.4 | 0e+00 | 31/41 (AsPC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.41×** | +12.8 | 4e-35 | 26/41 (SW1417, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.86×** | +12.8 | 4e-35 | 26/47 (SW1417, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +11.3 | 2e-27 | 8/16 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.14×** | +10.7 | 2e-24 | 28/44 (AsPC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +9.5 | 2e-19 | 28/46 (KATO III, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +8.7 | 2e-16 | 14/31 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 0.05 µM |  | **1.79×** | +8.5 | 2e-15 | 23/47 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +7.3 | 2e-11 | 4/21 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.65×** | +7.3 | 2e-11 | 23/44 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.65×** | +7.3 | 2e-11 | 23/45 (SW480, AsPC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.58×** | +6.7 | 1e-09 | 23/45 (SW1417, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.9 | 1e-07 | 17/41 (NCI-H2030, A549, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +5.4 | 3e-06 | 14/35 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +4.1 | 0.002 | 13/41 (KATO III, SNU-1, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +3.8 | 0.005 | 13/44 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.30×** | +3.8 | 0.006 | 3/45 (LoVo, BT-474, …) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.020 | 4/43 (SNU-423, BT-474, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.020 | 10/45 (NCI-H1792, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.023 | 6/38 (NCI-H23, SW 900, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14072.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Fluvoxamine (drug)]] 5 µM in 1 line (SNU-423 0.0622×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.103×; ⚠ toxic); [[Lonafarnib (drug)]] 5 µM in 1 line (SW1417 0.0764×; ⚠ toxic); [[Decitabine (drug)]] 5 µM in 1 line (NCI-H23 0.0662×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.900× | -5.4 | 5e-05 | 10/48 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.766×** | -3.6 | 0.091 | 8/46 (HepG2/C3A, HS-578T, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.795× | -3.2 | 0.23 | 5/44 (Hs 766T, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14072. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 18.4 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +22.3) | — |
| [[SW1417 (line)]] | alt | 27.4 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +16.0) | [[Lonafarnib (drug)]] 5 µM 0.0764× (z -9.2) ⚠ toxic |
| [[SW480 (line)]] | alt | 18.0 | 6 | 0 | [[Selinexor (drug)]] 5 µM 3.04× (z +12.0) | — |
| [[RKO (line)]] | wt | 5.12 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.0× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 26.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +12.9) | — |
| [[HOP62 (line)]] | alt | 10.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +11.5) | — |
| [[Hs 766T (line)]] | wt | 67.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +13.8) | — |
| [[HT-29 (line)]] | alt | 8.19 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.67× (z +12.3) | — |
| [[LS 180 (line)]] | wt | 6.69 | 2 | 0 | [[Selinexor (drug)]] 5 µM 6.81× (z +11.7) | — |
| [[NCI-H2347 (line)]] | alt | 15.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +11.4) | — |
| [[Panc 03.27 (line)]] | alt | 15.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.17× (z +16.3) | — |
| [[C32 (line)]] | wt | 13.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.103× (z -9.7) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 34.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +10.6) | — |
| [[J82 (line)]] | alt | 8.86 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.44× (z +8.8) | — |
| [[KATO III (line)]] | alt | 8.34 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.61× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 5.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.53× (z +11.0) | — |
| [[NCI-H1792 (line)]] | alt | 10.6 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.69× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 4.77 | 0 | 1 | — | [[Decitabine (drug)]] 5 µM 0.0662× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 7.03 | 1 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 5.98× (z +10.6) | — |
| [[SK-MEL-2 (line)]] | alt | 18.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.177× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~50% of this change |
| [[SNU-423 (line)]] | alt | 7.64 | 0 | 1 | — | [[Fluvoxamine (drug)]] 5 µM 0.0622× (z -11.5) |
| [[SW 900 (line)]] | alt | 6.92 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +9.0) | — |
| [[A-172 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14072), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL14]] | +0.62 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[OTUD6B-AS1]] | +0.62 | +0.53 / +0.64 | both halves | 1e-05 | same gene group |
| [[CD163L1]] | +0.60 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[DUSP15]] | +0.58 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[RNF103-CHMP3]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[HDAC9]] | +0.57 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[PRKG2-AS1]] | +0.57 | +0.60 / +0.52 | both halves | 1e-05 | same gene group |
| [[PLA2G4C]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ALOXE3]] | +0.56 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[MED18]] | +0.55 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[CFLAR-AS1]] | +0.55 | +0.62 / +0.44 | both halves | 3e-05 | same gene group |
| [[PTER]] | +0.55 | +0.60 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD3]] | -0.56 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[ADAM15]] | -0.54 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[AP2A1]] | -0.54 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[TRAF7]] | -0.53 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[RABL6]] | -0.53 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[METTL9]] | -0.52 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[FOXK2]] | -0.52 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[ATRN]] | -0.51 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[C2CD2L]] | -0.51 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[SAP130]] | -0.51 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[SDHA]] | -0.51 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[CTDP1]] | -0.51 | -0.56 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ICAM2]] | B | ICAM2 activity raises DIAPH2-AS1's level | lines that do not express ICAM2 (23) vs lines expressing it (27) | 1.77× lower at baseline in the lines without ICAM2 | 0.023 | ⚠ within organs, on part of the lines; also absent: TINAGL1, GALNT5, PCSK9; maybe low, not absent |
| [[HCP5]] | B | HCP5 activity raises DIAPH2-AS1's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 1.64× lower at baseline in the lines without HCP5 | 0.032 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451 |
| [[ARL14]] | B | ARL14 activity raises DIAPH2-AS1's level | lines that do not express ARL14 (23) vs lines expressing it (27) | 1.52× lower at baseline in the lines without ARL14 | 0.041 | ⚠ within organs, on part of the lines; also absent: TMEM92, LIPH, AFAP1L2; maybe low, not absent |
| [[LINC00944]] | B | LINC00944 activity raises DIAPH2-AS1's level | lines that do not express LINC00944 (20) vs lines expressing it (30) | 1.55× lower at baseline in the lines without LINC00944 | 0.042 | ⚠ within organs, on part of the lines; also absent: RDUR, ENSG00000289600, LINC02405 |
| [[STK32A]] | B | STK32A activity raises DIAPH2-AS1's level | lines that do not express STK32A (23) vs lines expressing it (27) | 1.44× lower at baseline in the lines without STK32A | 0.044 | ⚠ within organs, on part of the lines; also absent: CHSY3, FRMPD4, SAA1 |
| [[NEURL3]] | B | NEURL3 activity raises DIAPH2-AS1's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 1.51× lower at baseline in the lines without NEURL3 | 0.050 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[GNG2]] | B | GNG2 activity raises DIAPH2-AS1's level | lines that do not express GNG2 (22) vs lines expressing it (28) | 1.53× lower at baseline in the lines without GNG2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SNAI2, LBH, PLAT |
| [[S100A2]] | B | S100A2 activity strengthens DIAPH2-AS1's drug response | lines that do not express S100A2 (25) vs lines expressing it (23) | the lines without S100A2 respond 0.70× as strongly (z diff +0.93); strongest at Homoharringtonine 5 µM: 2.00x vs 4.17x (z diff +3.6) | 0.075 | ⚠ within organs, on part of the lines; also absent: KRT81, LINC00408, FGFBP1; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[PSORS1C1]] | B | PSORS1C1 activity raises DIAPH2-AS1's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 1.70× lower at baseline in the lines without PSORS1C1 | 0.086 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |
| [[HLA-V-1]] | B | HLA-V-1 activity raises DIAPH2-AS1's level | lines that do not express HLA-V-1 (21) vs lines expressing it (29) | 1.68× lower at baseline in the lines without HLA-V-1 | 0.088 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MST1R, KIAA0040 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 158]]; 27 genes; every member is in the + arm (projection on the module's main direction 0.637). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.9, 4.1); signed map (12.6, -16.0). **Vector** length 77.7, 13.2% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +9.0 | +12.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +12.8 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.7 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +20.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +1.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.2 | +7.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +3.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +1.1 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -2.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | -2.9 | +0.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -1.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -0.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -0.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | DIAPH2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | Xq21.33 — chrX:97,431,286-97,642,589 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14236](https://www.uniprot.org/uniprotkb/Q14236) (Early lymphoid activation gene protein):

> May function as an early signal that helps mediate the activation of T-cells.

**Summary**, from NCBI Gene [10824](https://www.ncbi.nlm.nih.gov/gene/10824):

> Predicted to be involved in signal transduction. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16972](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16972) · Entrez [10824](https://www.ncbi.nlm.nih.gov/gene/10824) · UniProt [Q14236](https://www.uniprot.org/uniprotkb/Q14236) · Ensembl [ENSG00000236256](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236256)

## Data

Gene col 14072: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14072); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14072, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14072]; `tensor/DDL_lfc|DDL_z.npy` [14072]; `embed/gene_vectors.npy` [14072]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14072 or target_col == 14072). Every well: [[DIAPH2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DIAPH2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
