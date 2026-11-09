---
symbol: "DLX6-AS1"
type: "gene"
col: 13811
ensembl_id: "ENSG00000231764"
name: "DLX6 antisense RNA 1"
location: "7q21.3"
module: 46
arm: "+"
pooled_cpm: 2.39
n_lines_expressing: 27
n_dd_up: 14
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 8
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# DLX6-AS1

*DLX6 antisense RNA 1* — 7q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.54× (z +10.6, q 1e-23, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.96× (z +8.3, q 1e-14, up in 3 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.532× (z -5.3, q 5e-05, down in 15 of 21 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRPM2-AS]] (+0.59, fdr 1e-05), [[HOTAIR]] (+0.57, fdr 2e-05), [[DHRS4L2]] (+0.55, fdr 1e-04); moves opposite to [[H3-3B]] (-0.47, fdr 3e-04), [[DYNLT1]] (-0.46, fdr 0.001, ⚠ one half only (not replicated)), [[PTPRH]] (-0.46, fdr 2e-04), [[HRH1]] (-0.46, fdr 1e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[EPDR1]] → it (grade B ⚠); 8 go from it, the strongest it → [[ATP6V0D1-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13811.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.54×** | +10.6 | 1e-23 | 2/2 (HEC-1-A, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.27×** | +10.3 | 1e-22 | 6/8 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.15×** | +9.3 | 4e-18 | 1/4 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +8.3 | 1e-14 | 3/17 (C32, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.28×** | +7.2 | 8e-11 | 10/21 (A-427, HEC-1-A, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +5.7 | 1e-06 | 8/23 (KATO III, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.69×** | +4.6 | 4e-04 | 2/16 (HepG2/C3A, HOP62) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.65×** | +4.4 | 9e-04 | 1/12 (PANC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.90×** | +4.0 | 0.004 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.87×** | +3.9 | 0.006 | 2/6 (SW480, NCI-H1573) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.013 | 2/21 (NCI-H1573, COLO 205) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.13×** | +3.5 | 0.026 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Arbutin (drug)]] 0.05 µM |  | **1.49×** | +3.2 | 0.058 | 0/17 | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.091 | 8/25 (HS-578T, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13811.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.532×** | -5.3 | 5e-05 | 15/21 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.556×** | -5.2 | 7e-05 | 13/22 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.563×** | -5.1 | 8e-05 | 17/24 (SNU-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.572×** | -4.9 | 1e-04 | 12/14 (NCI-H1573, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.629×** | -4.1 | 0.005 | 14/22 (HEC-1-A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.629×** | -3.9 | 0.008 | 3/21 (SW480, HOP62, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.651×** | -3.8 | 0.012 | 6/23 (NCI-H2030, HS-578T, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.680×** | -3.3 | 0.077 | 2/23 (J82, CHP-212) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.698×** | -3.2 | 0.087 | 12/23 (KATO III, HEC-1-A, …) | inconsistent across doses |  |
| [[Sinomenine (drug)]] 0.5 µM |  | **0.698×** | -3.2 | 0.087 | 4/21 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13811. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 12.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -13.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.121× (z -12.4) |
| [[PANC-1 (line)]] | alt | 2.16 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0413× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 13.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0497× (z -16.4) |
| [[J82 (line)]] | alt | 5.35 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0586× (z -16.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Monocrotaline (drug)]] 0.05 µM 0.0749× (z -9.8) |
| [[SNU-1 (line)]] | wt | 7.42 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0133× (z -13.1) |
| [[SW480 (line)]] | alt | 3.57 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0645× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 2.22 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0562× (z -9.2) |
| [[KATO III (line)]] | alt | 5.88 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.125× (z -8.5) |
| [[A-172 (line)]] | wt | 0.327 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.291 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.330 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.301 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.646 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.995 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.561 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.305 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.396 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.365 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.291 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.513 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.340 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.342 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.553 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.559 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.366 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13811), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRPM2-AS]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 | same gene group |
| [[HOTAIR]] | +0.57 | +0.49 / +0.51 | both halves | 2e-05 |  |
| [[DHRS4L2]] | +0.55 | +0.36 / +0.49 | both halves | 1e-04 |  |
| [[LRP5]] | +0.52 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[TESMIN]] | +0.52 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[TMEM218]] | +0.52 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[RAVER2]] | +0.51 | +0.40 / +0.52 | both halves | 4e-05 |  |
| [[VSIG10]] | +0.51 | +0.39 / +0.44 | both halves | 5e-05 |  |
| [[C10orf95-AS1]] | +0.51 | +0.46 / +0.35 | both halves | 1e-04 | same gene group |
| [[DMTN]] | +0.50 | +0.31 / +0.54 | both halves | 2e-04 |  |
| [[SLC35G1]] | +0.50 | +0.41 / +0.33 | both halves | 1e-04 |  |
| [[LINC02050]] | +0.49 | +0.50 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[H3-3B]] | -0.47 | -0.28 / -0.49 | both halves | 3e-04 |  |
| [[DYNLT1]] | -0.46 | -0.15 / -0.50 | ⚠ one half (not replicated) | 0.001 |  |
| [[PTPRH]] | -0.46 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[HRH1]] | -0.46 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[DLGAP4]] | -0.45 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[SERPINB1]] | -0.44 | -0.23 / -0.42 | both halves | 5e-04 |  |
| [[AREG]] | -0.44 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[HIVEP3]] | -0.44 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[POLD4]] | -0.43 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[MEA1]] | -0.43 | -0.37 / -0.33 | both halves | 1e-04 |  |
| [[PLIN3]] | -0.43 | -0.28 / -0.39 | both halves | 3e-04 |  |
| [[MYO1E]] | -0.42 | -0.29 / -0.34 | both halves | 2e-04 |  |
| [[SH3BGRL3]] | -0.42 | -0.32 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPDR1]] | B | EPDR1 activity raises DLX6-AS1's level | lines that do not express EPDR1 (14) vs lines expressing it (36) | 1.43× lower at baseline in the lines without EPDR1 | 0.053 | ⚠ within organs, on part of the lines; also absent: RBM24, BEX2, GATA3 |
| [[EMID1]] | B | EMID1 activity raises DLX6-AS1's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 1.52× lower at baseline in the lines without EMID1 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[TRPM2-AS]] | B | TRPM2-AS activity raises DLX6-AS1's level | lines that do not express TRPM2-AS (29) vs lines expressing it (21) | 2.00× lower at baseline in the lines without TRPM2-AS | 0.090 | ⚠ within organs, on part of the lines; also absent: LINC03046, KLRC2, PCK1 |
| [[LINC02050]] | C | LINC02050 activity raises DLX6-AS1's level | lines that do not express LINC02050 (37) vs lines expressing it (13) | 1.92× lower at baseline in the lines without LINC02050 | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000286329, ENSG00000242828, PASD1; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP6V0D1-DT]] | B | DLX6-AS1 activity raises ATP6V0D1-DT's level | lines that do not express DLX6-AS1 (23) vs lines expressing it (27) | 1.66× lower at baseline in the lines without DLX6-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000249776, FBXO27, KIF1A; maybe low, not absent |
| [[NUDT13]] | B | DLX6-AS1 activity raises NUDT13's level | lines that do not express DLX6-AS1 (23) vs lines expressing it (27) | 1.21× lower at baseline in the lines without DLX6-AS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000249776, FBXO27, KIF1A; maybe low, not absent |
| [[NEK5]] | B | DLX6-AS1 activity raises NEK5's level | lines that do not express DLX6-AS1 (23) vs lines expressing it (27) | 1.63× lower at baseline in the lines without DLX6-AS1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000249776, FBXO27, KIF1A; maybe low, not absent |
| [[ATP6V0D1-DT]] | B | DLX6-AS1 activity strengthens ATP6V0D1-DT's drug response | lines that do not express DLX6-AS1 (22) vs lines expressing it (25) | the lines without DLX6-AS1 respond 0.75× as strongly (z diff +1.48); strongest at Ouabain (Octahydrate) 0.5 µM: 0.40x vs 0.24x (z diff +2.1) | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000249776, FBXO27, KIF1A; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[RBBP4]] | B | DLX6-AS1 activity raises RBBP4's level | lines that do not express DLX6-AS1 (23) vs lines expressing it (27) | 1.31× lower at baseline in the lines without DLX6-AS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000249776, FBXO27, KIF1A; maybe low, not absent |
| [[SERPINB1]] | B | DLX6-AS1 activity lowers SERPINB1's level | lines that do not express DLX6-AS1 (23) vs lines expressing it (27) | 1.84× higher at baseline in the lines without DLX6-AS1 | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000249776, FBXO27, KIF1A; maybe low, not absent |
| [[PPP1CB-DT]] | B | DLX6-AS1 activity raises PPP1CB-DT's level | lines that do not express DLX6-AS1 (23) vs lines expressing it (27) | 1.53× lower at baseline in the lines without DLX6-AS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000249776, FBXO27, KIF1A; maybe low, not absent |
| [[RFXAP]] | B | DLX6-AS1 activity raises RFXAP's level | lines that do not express DLX6-AS1 (23) vs lines expressing it (27) | 1.38× lower at baseline in the lines without DLX6-AS1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000249776, FBXO27, KIF1A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.416). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (0.6, 28.1); signed map (37.0, -17.4). **Vector** length 37.9, 6.60% of its response variance represented; |z| ≥ 3 in 554 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.0 | +5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +10.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.0 | +3.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.8 | +2.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +0.8 | +0.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -1.5 | -5.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.4 | -5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.2 | -4.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.1 | -2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.8 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.7 | +0.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | DLX6 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q21.3 — chr7:96,955,141-97,014,088 (-) |
| Ensembl biotype | lncRNA |
| Also known as | uc.221, uc.220, FLJ34048, Evf-2; previously NCRNA00212 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [285987](https://www.ncbi.nlm.nih.gov/gene/285987):

> Predicted to be involved in forebrain development and positive regulation of DNA-templated transcription. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:37151](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37151) · Entrez [285987](https://www.ncbi.nlm.nih.gov/gene/285987) · Ensembl [ENSG00000231764](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231764)

## Data

Gene col 13811: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13811); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13811, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13811]; `tensor/DDL_lfc|DDL_z.npy` [13811]; `embed/gene_vectors.npy` [13811]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13811 or target_col == 13811). Every well: [[DLX6-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLX6-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
