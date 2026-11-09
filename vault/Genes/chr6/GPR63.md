---
symbol: "GPR63"
type: "gene"
col: 3337
ensembl_id: "ENSG00000112218"
name: "G protein-coupled receptor 63"
location: "6q16.1"
module: 18
arm: "+"
pooled_cpm: 5.11
n_lines_expressing: 40
n_dd_up: 32
n_dd_down: 2
n_dd_up_clean: 23
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 7
direction_downstream: 4
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# GPR63

*G protein-coupled receptor 63* — 6q16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (9 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.52× (z +16.5, q 0e+00, up in 35 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.388× (z -6.3, q 2e-07, down in 14 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C-33 A 0.176×, A-427 0.241×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.329×); [[TAK-901 (drug)]] 5 µM in 1 line (A-427 0.0767×); [[Talc (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0581×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPV]] (+0.61, fdr 4e-05), [[ZYG11A]] (+0.60, fdr 1e-05), [[UCK2]] (+0.60, fdr 9e-05); moves opposite to [[PRPF18]] (-0.60, fdr 2e-04), [[TOX4]] (-0.54, fdr 5e-05), [[UMAD1]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SLC16A10]] → it (grade B ⚠); 4 go from it, the strongest it → [[GAL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3337.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.52×** | +16.5 | 0e+00 | 35/36 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.02×** | +14.0 | 5e-42 | 32/36 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.91×** | +13.5 | 2e-39 | 31/36 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +13.5 | 2e-39 | 21/30 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.10×** | +13.2 | 6e-38 | 19/32 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.66×** | +12.4 | 3e-33 | 28/36 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.58×** | +11.5 | 7e-29 | 17/20 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.40×** | +11.1 | 1e-26 | 25/36 (HEC-1-A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.40×** | +11.1 | 1e-26 | 28/33 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.12×** | +9.5 | 1e-19 | 14/31 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.73×** | +8.7 | 1e-16 | 20/35 (PANC-1, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.96×** | +8.2 | 1e-14 | 1/6 (PANC-1) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +7.3 | 1e-11 | 13/26 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.77×** | +7.2 | 2e-11 | 21/36 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.75×** | +7.1 | 4e-11 | 17/32 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +4.6 | 2e-04 | 7/32 (NCI-H460, HOP62, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.65×** | +3.3 | 0.026 | 1/26 (SW480) | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.027 | 2/26 (NCI-H460, A549) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3337.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C-33 A 0.176×, A-427 0.241×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.329×); [[TAK-901 (drug)]] 5 µM in 1 line (A-427 0.0767×); [[Talc (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0581×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.388×** | -6.3 | 2e-07 | 14/35 (A-427, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.671×** | -4.9 | 3e-04 | 10/32 (NCI-H2030, LS 180, …) | top dose only | cell-cycle shift (explains ~14% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3337. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 21.8 | 0 | 3 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.329× (z -10.7) |
| [[SW480 (line)]] | alt | 8.77 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.41× (z +9.4) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 27.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change |
| [[LoVo (line)]] | wt | 9.94 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 2.30 | 0 | 1 | — | [[Talc (drug)]] 0.5 µM 0.0581× (z -9.0) |
| [[PANC-1 (line)]] | alt | 4.92 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.97× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 2.47 | 0 | 1 | — | [[Voriconazole (drug)]] 0.05 µM 0.0592× (z -8.8) |
| [[A-172 (line)]] | wt | 0.643 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.448 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.486 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.923 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.506 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3337), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPV]] | +0.61 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[ZYG11A]] | +0.60 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[UCK2]] | +0.60 | +0.36 / +0.60 | both halves | 9e-05 |  |
| [[NETO2]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[TMEM131L]] | +0.56 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[CACHD1]] | +0.55 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[POLR3G]] | +0.54 | +0.39 / +0.65 | both halves | 5e-05 |  |
| [[SOBP]] | +0.53 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[TSPAN12]] | +0.53 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[LONRF2]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[PPARGC1B]] | +0.53 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[TBC1D30]] | +0.53 | +0.51 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF18]] | -0.60 | -0.31 / -0.57 | both halves | 2e-04 |  |
| [[TOX4]] | -0.54 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[UMAD1]] | -0.52 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[ATP6V1D]] | -0.52 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[TMUB2]] | -0.51 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[ZZEF1]] | -0.51 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[IFT43]] | -0.50 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[PPP1R7]] | -0.50 | -0.11 / -0.47 | ⚠ not reproduced | 0.002 |  |
| [[USP49]] | -0.49 | -0.16 / -0.30 | ⚠ not reproduced | 0.001 |  |
| [[TMCO1]] | -0.49 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[CSNK2B]] | -0.49 | -0.29 / -0.64 | both halves | 2e-04 |  |
| [[ATP6V1E1]] | -0.49 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[VPS4B]] | -0.49 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[SERINC3]] | -0.48 | -0.36 / -0.55 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A10]] | B | SLC16A10 activity raises GPR63's level | lines that do not express SLC16A10 (15) vs lines expressing it (35) | 2.38× lower at baseline in the lines without SLC16A10 | 0.015 | ⚠ within organs, on part of the lines; also absent: SH3GL2, FZD3, TTYH2 |
| [[PLAAT1]] | B | PLAAT1 activity raises GPR63's level | lines that do not express PLAAT1 (20) vs lines expressing it (30) | 2.20× lower at baseline in the lines without PLAAT1 | 0.036 | ⚠ within organs, on part of the lines; also absent: SDK1, PDGFD, SNCA |
| [[TSPAN12]] | B | TSPAN12 activity raises GPR63's level | lines that do not express TSPAN12 (13) vs lines expressing it (37) | 2.33× lower at baseline in the lines without TSPAN12 | 0.051 | ⚠ within organs, on part of the lines; also absent: ATP8A1, PPP1R9A, SH3BGRL2; maybe low, not absent |
| [[SOBP]] | B | SOBP activity raises GPR63's level | lines that do not express SOBP (19) vs lines expressing it (31) | 2.02× lower at baseline in the lines without SOBP | 0.065 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[SLC6A15]] | B | SLC6A15 activity raises GPR63's level | lines that do not express SLC6A15 (32) vs lines expressing it (18) | 1.75× lower at baseline in the lines without SLC6A15 | 0.067 | ⚠ within organs, on part of the lines; also absent: PAX3, CNKSR2, ENSG00000286251 |
| [[CELF4]] | B | CELF4 activity raises GPR63's level | lines that do not express CELF4 (24) vs lines expressing it (26) | 2.04× lower at baseline in the lines without CELF4 | 0.076 | ⚠ within organs, on part of the lines; also absent: CHST8, ASXL3, SULT4A1; maybe low, not absent |
| [[NETO2]] | C | NETO2 activity raises GPR63's level | lines that do not express NETO2 (11) vs lines expressing it (39) | 2.34× lower at baseline in the lines without NETO2 | 0.079 | ⚠ within organs, on part of the lines; also absent: BEND6, ZDBF2, CPQ; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GAL]] | B | GPR63 activity raises GAL's level | lines that do not express GPR63 (10) vs lines expressing it (40) | 2.31× lower at baseline in the lines without GPR63 | 0.057 | ⚠ within organs, on part of the lines; also absent: ZNF618, BEX3, OLFM2 |
| [[SLC16A10]] | B | GPR63 activity raises SLC16A10's level | lines that do not express GPR63 (10) vs lines expressing it (40) | 2.54× lower at baseline in the lines without GPR63 | 0.067 | ⚠ within organs, on part of the lines; also absent: ZNF618, BEX3, OLFM2 |
| [[ZNF485]] | B | GPR63 activity raises ZNF485's level | lines that do not express GPR63 (10) vs lines expressing it (40) | 1.47× lower at baseline in the lines without GPR63 | 0.093 | ⚠ within organs, on part of the lines; also absent: ZNF618, BEX3, OLFM2 |
| [[NETO2]] | C | GPR63 activity raises NETO2's level | lines that do not express GPR63 (10) vs lines expressing it (40) | 4.00× lower at baseline in the lines without GPR63 | 0.037 | ⚠ within organs, on part of the lines; also absent: ZNF618, BEX3, OLFM2; co-absent with the target |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.467). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-19.8, 31.9); signed map (10.4, -0.5). **Vector** length 47.3, 6.73% of its response variance represented; |z| ≥ 3 in 873 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +16.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +11.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.6 | +7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +11.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.5 | +14.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +2.7 |
|  | [[EX229 (drug)]] 5 µM |  | +1.4 | +1.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.4 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +3.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -2.0 | -6.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | +0.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | +1.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | -2.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.05 µM |  | -0.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | G protein-coupled receptor 63 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q16.1 — chr6:96,794,125-96,837,477 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PSP24(beta), PSP24B |
| Gene groups (HGNC) | G protein-coupled receptors, Class A orphans |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZJ6](https://www.uniprot.org/uniprotkb/Q9BZJ6) (Probable G protein-coupled receptor 63):

> Orphan receptor. May play a role in brain function.

**Summary**, from NCBI Gene [81491](https://www.ncbi.nlm.nih.gov/gene/81491):

> Predicted to enable G protein-coupled receptor activity. Predicted to be involved in G protein-coupled receptor signaling pathway. Part of signaling receptor complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13302](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13302) · Entrez [81491](https://www.ncbi.nlm.nih.gov/gene/81491) · UniProt [Q9BZJ6](https://www.uniprot.org/uniprotkb/Q9BZJ6) · Ensembl [ENSG00000112218](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112218)

## Data

Gene col 3337: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3337); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3337, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3337]; `tensor/DDL_lfc|DDL_z.npy` [3337]; `embed/gene_vectors.npy` [3337]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3337 or target_col == 3337). Every well: [[GPR63 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPR63.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
