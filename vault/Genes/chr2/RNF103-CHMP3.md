---
symbol: "RNF103-CHMP3"
type: "gene"
col: 14647
ensembl_id: "ENSG00000249884"
name: "RNF103-CHMP3 readthrough"
location: "2p11.2"
module: 68
arm: "+"
pooled_cpm: 26.01
n_lines_expressing: 45
n_dd_up: 47
n_dd_down: 0
n_dd_up_clean: 39
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 8
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# RNF103-CHMP3

*RNF103-CHMP3 readthrough* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 47 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 23.6× (z +48.2, q 0e+00, up in 40 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 2 lines (COLO 205 0.138×, HT-29 0.231×; ⚠ cell-cycle shift, explains ~72% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HepG2/C3A 0.0736×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (COLO 205 0.102×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00571]] (+0.75, fdr 1e-05), [[DNAH12]] (+0.71, fdr 1e-05), [[LINC01090]] (+0.70, fdr 1e-05); moves opposite to [[NUP93]] (-0.70, fdr 8e-06), [[NUDT21]] (-0.67, fdr 1e-05), [[SKP2]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[VNN1]] → it (grade B ⚠); 8 go from it, the strongest it → [[EIF5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 47 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14647.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **23.6×** | +48.2 | 0e+00 | 40/40 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **10.4×** | +25.2 | 0e+00 | 37/37 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **7.14×** | +20.4 | 0e+00 | 38/40 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.37×** | +18.5 | 0e+00 | 33/40 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **5.11×** | +17.6 | 0e+00 | 41/41 (HCT15, HT-29, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.65×** | +7.6 | 2e-12 | 27/43 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.93×** | +7.0 | 2e-10 | 25/41 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.79×** | +6.2 | 3e-08 | 23/42 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +6.0 | 9e-08 | 23/36 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.5 | 2e-06 | 21/43 (HOP62, A498, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **2.37×** | +4.8 | 7e-05 | 23/39 (A498, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.57×** | +4.8 | 7e-05 | 18/41 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Adagrasib (drug)]] 5 µM |  | **1.51×** | +4.3 | 9e-04 | 24/41 (A549, H4, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.1 | 0.001 | 15/39 (A-172, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.001 | 17/44 (NCI-H1573, SW480, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +4.0 | 0.002 | 15/41 (BT-474, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14647.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 2 lines (COLO 205 0.138×, HT-29 0.231×; ⚠ cell-cycle shift, explains ~72% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HepG2/C3A 0.0736×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (COLO 205 0.102×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 0.754× | -3.1 | 0.93 | 10/44 (NCI-H1573, SNU-423, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14647. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 12.3 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 64.9× (z +26.0) | — |
| [[NCI-H460 (line)]] | wt | 11.0 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 57.9× (z +28.0) | — |
| [[A498 (line)]] | wt | 17.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.9× (z +27.7) | — |
| [[C32 (line)]] | wt | 6.57 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.1× (z +14.4) | — |
| [[COLO 205 (line)]] | alt | 111 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 36.6× (z +27.5) | [[Panobinostat (drug)]] 5 µM 0.102× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 26.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.7× (z +24.8) | — |
| [[NCI-H2347 (line)]] | alt | 26.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.6× (z +23.4) | — |
| [[PANC-1 (line)]] | alt | 7.03 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.49× (z +17.8) | — |
| [[AsPC-1 (line)]] | alt | 38.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.3× (z +27.6) | — |
| [[BT-474 (line)]] | alt | 29.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +11.6) | — |
| [[HepG2_C3A (line)]] | wt | 64.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 25.8× (z +23.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0736× (z -12.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 7.29 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 87.4× (z +24.3) | — |
| [[HT-29 (line)]] | alt | 50.7 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +15.8) | [[Docetaxel (drug)]] 0.05 µM 0.227× (z -9.5) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 36.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 45.4× (z +34.2) | — |
| [[LOX-IMVI (line)]] | wt | 7.65 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 121× (z +26.7) | — |
| [[NCI-H23 (line)]] | alt | 6.59 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 39.5× (z +20.4) | — |
| [[Panc 03.27 (line)]] | alt | 31.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +21.1) | — |
| [[RKO (line)]] | wt | 7.97 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 38.2× (z +12.6) | — |
| [[SNU-423 (line)]] | alt | 71.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.28× (z +19.8) | [[Dinaciclib (drug)]] 0.05 µM 0.212× (z -9.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 65.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.54× (z +22.5) | — |
| [[HCT15 (line)]] | alt | 13.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.8× (z +16.3) | — |
| [[HEC-1-A (line)]] | alt | 64.9 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.22× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 74.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +23.6) | — |
| [[NCI-H1573 (line)]] | alt | 30.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.6× (z +25.3) | — |
| [[NCI-H1792 (line)]] | alt | 17.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.5× (z +25.0) | — |
| [[NCI-H2030 (line)]] | alt | 20.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 83.2× (z +34.4) | — |
| [[SK-MEL-2 (line)]] | alt | 19.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.1× (z +19.2) | — |
| [[SW 900 (line)]] | alt | 20.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.6× (z +23.3) | — |
| [[A549 (line)]] | wt | 29.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +18.2) | — |
| [[C-33 A (line)]] | alt | 9.20 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.55× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 16.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.6× (z +19.3) | — |
| [[H4 (line)]] | wt | 15.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.6× (z +15.6) | — |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 35.4× (z +17.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.56 | 2 | 0 | [[Auranofin (drug)]] 5 µM 16.1× (z +12.0) | — |
| [[RPMI-7951 (line)]] | alt | 17.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.9× (z +15.0) | — |
| [[SW1417 (line)]] | alt | 64.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +10.9) | — |
| [[SW48 (line)]] | wt | 11.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.6× (z +15.2) | — |
| [[A-427 (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.89 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.29 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.12 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.14 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.69 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14647), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00571]] | +0.75 | +0.76 / +0.55 | both halves | 1e-05 |  |
| [[DNAH12]] | +0.71 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[LINC01090]] | +0.70 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[CELF6]] | +0.69 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.68 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[SLC22A1]] | +0.67 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[LURAP1L-AS1]] | +0.66 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[NEB]] | +0.66 | +0.68 / +0.41 | both halves | 4e-05 |  |
| [[HDAC9]] | +0.66 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[RRAGC-DT]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[NUTM2E]] | +0.65 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[UBE2D3-AS1]] | +0.65 | +0.65 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP93]] | -0.70 | -0.66 / -0.58 | both halves | 8e-06 |  |
| [[NUDT21]] | -0.67 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[SKP2]] | -0.66 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[WDR5]] | -0.66 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[NCAPD3]] | -0.65 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[ELP1]] | -0.65 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[RPA1]] | -0.64 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[FAR1]] | -0.64 | -0.66 / -0.45 | both halves | 3e-05 |  |
| [[METAP1]] | -0.63 | -0.69 / -0.40 | both halves | 5e-05 |  |
| [[ANAPC5]] | -0.62 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[SDHAF3]] | -0.61 | -0.62 / -0.38 | both halves | 7e-05 |  |
| [[BRAT1]] | -0.60 | -0.56 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VNN1]] | B | VNN1 activity raises RNF103-CHMP3's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 2.75× lower at baseline in the lines without VNN1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[RASEF]] | B | RASEF activity raises RNF103-CHMP3's level | lines that do not express RASEF (20) vs lines expressing it (30) | 2.19× lower at baseline in the lines without RASEF | 0.007 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[HLA-V-1]] | B | HLA-V-1 activity raises RNF103-CHMP3's level | lines that do not express HLA-V-1 (21) vs lines expressing it (29) | 2.31× lower at baseline in the lines without HLA-V-1 | 0.014 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MST1R, KIAA0040 |
| [[ADGRF4]] | B | ADGRF4 activity raises RNF103-CHMP3's level | lines that do not express ADGRF4 (23) vs lines expressing it (27) | 2.13× lower at baseline in the lines without ADGRF4 | 0.022 | ⚠ within organs, on part of the lines; also absent: VNN1, PTPRB, PTPRR |
| [[PSORS1C1]] | B | PSORS1C1 activity raises RNF103-CHMP3's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 2.02× lower at baseline in the lines without PSORS1C1 | 0.031 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |
| [[KPNA7]] | B | KPNA7 activity raises RNF103-CHMP3's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 2.54× lower at baseline in the lines without KPNA7 | 0.042 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[ALDH1A2]] | B | ALDH1A2 activity raises RNF103-CHMP3's level | lines that do not express ALDH1A2 (13) vs lines expressing it (37) | 1.82× lower at baseline in the lines without ALDH1A2 | 0.053 | ⚠ within organs, on part of the lines; also absent: SH3TC1, GBP2, CCDC194; maybe low, not absent |
| [[LINC01226]] | B | LINC01226 activity raises RNF103-CHMP3's level | lines that do not express LINC01226 (16) vs lines expressing it (34) | 2.14× lower at baseline in the lines without LINC01226 | 0.063 | ⚠ within organs, on part of the lines; also absent: LASTR, TRIM29, ENSG00000287003; maybe low, not absent |
| [[BMP2]] | B | BMP2 activity raises RNF103-CHMP3's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 1.72× lower at baseline in the lines without BMP2 | 0.080 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[MTOR]] | B | MTOR activity lowers RNF103-CHMP3's level | compounds that target MTOR: 5 of 8 raise it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 9.2% of all compounds | 0.084 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TNK1]] | B | TNK1 activity raises RNF103-CHMP3's level | lines that do not express TNK1 (13) vs lines expressing it (37) | 2.29× lower at baseline in the lines without TNK1 | 0.089 | ⚠ within organs, on part of the lines; also absent: TUBA4A, CDCP1, CHMP4C; maybe low, not absent |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EIF5]] | B | RNF103-CHMP3 activity raises EIF5's level | lines that do not express RNF103-CHMP3 (5) vs lines expressing it (45) | 1.44× lower at baseline in the lines without RNF103-CHMP3 | 0.031 | ⚠ within organs, on part of the lines; also absent: TMEM144, YBX3, DTX4; maybe low, not absent |
| [[HERC4]] | B | RNF103-CHMP3 activity raises HERC4's level | lines that do not express RNF103-CHMP3 (5) vs lines expressing it (45) | 1.70× lower at baseline in the lines without RNF103-CHMP3 | 0.047 | ⚠ within organs, on part of the lines; also absent: TMEM144, YBX3, DTX4; maybe low, not absent |
| [[SNRNP40]] | B | RNF103-CHMP3 activity lowers SNRNP40's level | lines that do not express RNF103-CHMP3 (5) vs lines expressing it (45) | 1.62× higher at baseline in the lines without RNF103-CHMP3 | 0.052 | ⚠ within organs, on part of the lines; also absent: TMEM144, YBX3, DTX4; maybe low, not absent |
| [[KDM1A]] | B | RNF103-CHMP3 activity lowers KDM1A's level | lines that do not express RNF103-CHMP3 (5) vs lines expressing it (45) | 1.31× higher at baseline in the lines without RNF103-CHMP3 | 0.076 | ⚠ within organs, on part of the lines; also absent: TMEM144, YBX3, DTX4; maybe low, not absent |
| [[C6orf62]] | B | RNF103-CHMP3 activity raises C6orf62's level | lines that do not express RNF103-CHMP3 (5) vs lines expressing it (45) | 1.10× lower at baseline in the lines without RNF103-CHMP3 | 0.080 | ⚠ within organs, on part of the lines; also absent: TMEM144, YBX3, DTX4; maybe low, not absent |
| cells under [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM | B | RNF103-CHMP3 activity raises the cells' numbers under S-Adenosyl-L-methionine (disulfate tosylate) 0.5 µM (protects the cells) | lines that do not express RNF103-CHMP3 (5) vs lines expressing it (43) | the lines without RNF103-CHMP3: 0.77× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: TMEM144, YBX3, DTX4; maybe low, not absent |
| [[DUSP16]] | B | RNF103-CHMP3 activity raises DUSP16's level | lines that do not express RNF103-CHMP3 (5) vs lines expressing it (45) | 2.62× lower at baseline in the lines without RNF103-CHMP3 | 0.089 | ⚠ within organs, on part of the lines; also absent: TMEM144, YBX3, DTX4; maybe low, not absent |
| [[SKP2]] | B | RNF103-CHMP3 activity lowers SKP2's level | lines that do not express RNF103-CHMP3 (5) vs lines expressing it (45) | 1.83× higher at baseline in the lines without RNF103-CHMP3 | 0.089 | ⚠ within organs, on part of the lines; also absent: TMEM144, YBX3, DTX4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.658). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (17.6, 13.2); signed map (24.9, 2.9). **Vector** length 120, 32.8% of its response variance represented; |z| ≥ 3 in 1,184 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.2 | +17.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.3 | +25.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.6 | +48.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.2 | +20.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.5 | +7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.6 | +2.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.3 | +3.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | -5.8 | -2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.5 | +1.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | +0.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -1.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.0 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -1.5 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -2.6 | -2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | RNF103-CHMP3 readthrough |
| Locus type | readthrough (other) |
| Location | 2p11.2 — chr2:86,505,668-86,721,122 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously RNF103-VPS24 |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100526767](https://www.ncbi.nlm.nih.gov/gene/100526767):

> This locus represents naturally occurring read-through transcription between the neighboring RNF103 (ring finger protein 103) and CHMP3 (charged multivesicular body protein 3) genes. The read-through transcript encodes a fusion protein that shares sequence identity with each individual gene product. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:38847](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:38847) · Entrez [100526767](https://www.ncbi.nlm.nih.gov/gene/100526767) · Ensembl [ENSG00000249884](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249884)

## Data

Gene col 14647: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14647); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14647, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14647]; `tensor/DDL_lfc|DDL_z.npy` [14647]; `embed/gene_vectors.npy` [14647]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14647 or target_col == 14647). Every well: [[RNF103-CHMP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF103-CHMP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
