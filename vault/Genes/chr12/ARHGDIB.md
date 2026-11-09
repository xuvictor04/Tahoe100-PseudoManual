---
symbol: "ARHGDIB"
type: "gene"
col: 3225
ensembl_id: "ENSG00000111348"
name: "Rho GDP dissociation inhibitor beta"
location: "12p12.3"
module: 29
arm: "+"
pooled_cpm: 4.86
n_lines_expressing: 27
n_dd_up: 14
n_dd_down: 10
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 16
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# ARHGDIB

*Rho GDP dissociation inhibitor beta* — 12p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.55× (z +16.7, q 0e+00, up in 16 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.54× (z +5.4, q 7e-06, up in 9 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 0.574× (z -5.0, q 4e-04, down in 10 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGK]] (+0.55, fdr 4e-05), [[COL4A1]] (+0.55, fdr 4e-05), [[PXDN]] (+0.55, fdr 4e-05); moves opposite to [[RBCK1]] (-0.58, fdr 3e-05), [[TRADD]] (-0.53, fdr 1e-04), [[EPB41L4A-AS1]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LY75]] → it (grade B ⚠); 16 go from it, the strongest it → [[PDK2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3225.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.55×** | +16.7 | 0e+00 | 16/17 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.74×** | +16.3 | 0e+00 | 11/12 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.46×** | +14.0 | 5e-42 | 10/12 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +5.6 | 3e-06 | 5/18 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +5.4 | 7e-06 | 9/23 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.83×** | +4.8 | 1e-04 | 1/4 (NCI-H2347) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.70×** | +4.7 | 2e-04 | 3/19 (NCI-H2347, SW480, …) | top dose only | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.87×** | +4.0 | 0.005 | 0/14 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +3.7 | 0.016 | 8/23 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.018 | 5/23 (NCI-H2347, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.018 | 2/23 (SW480, HepG2/C3A) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.50×** | +3.4 | 0.028 | 5/18 (Panc 03.27, Hs 766T, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **1.42×** | +3.1 | 0.088 | 3/15 (SW 900, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **1.62×** | +3.1 | 0.088 | 4/19 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3225.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.574×** | -5.0 | 4e-04 | 10/21 (SK-MEL-2, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Artesunate (drug)]] 5 µM |  | **0.724×** | -4.1 | 0.012 | 10/23 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.651×** | -3.8 | 0.016 | 10/23 (AN3 CA, LS 180, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.442×** | -3.8 | 0.016 | 9/22 (LS 180, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.447×** | -3.8 | 0.016 | 6/23 (LOX-IMVI, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.657×** | -3.8 | 0.016 | 11/23 (J82, LOX-IMVI, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.752×** | -3.6 | 0.024 | 14/23 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.657×** | -3.5 | 0.035 | 2/23 (LOX-IMVI, SW 900) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.683×** | -3.4 | 0.041 | 10/20 (LOX-IMVI, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.698×** | -3.2 | 0.071 | 6/23 (SNU-423, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3225. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 46.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -9.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Saquinavir (drug)]] 5 µM 0.199× (z -9.4) |
| [[BT-474 (line)]] | alt | 14.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 22.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.55× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 6.37 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 6.01 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -9.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[LOX-IMVI (line)]] | wt | 10.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0447× (z -12.5) |
| [[NCI-H2347 (line)]] | alt | 37.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -8.9) |
| [[A-172 (line)]] | wt | 0.487 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.387 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.364 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.537 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.631 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.637 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.566 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.445 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.349 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.833 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.506 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.746 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.965 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.487 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.486 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3225), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGK]] | +0.55 | +0.51 / +0.43 | both halves | 4e-05 |  |
| [[COL4A1]] | +0.55 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[PXDN]] | +0.55 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[POGLUT3]] | +0.54 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[CD302]] | +0.54 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[BANF1]] | +0.54 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[NME4]] | +0.54 | +0.57 / +0.31 | both halves | 2e-04 |  |
| [[C1GALT1C1]] | +0.54 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[CDKN2AIPNL]] | +0.54 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[GNG12]] | +0.54 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[ATP5F1A]] | +0.53 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[ACTB]] | +0.53 | +0.53 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBCK1]] | -0.58 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[TRADD]] | -0.53 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[EPB41L4A-AS1]] | -0.52 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[ZBTB43]] | -0.52 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[SNHG12]] | -0.51 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[ZNF766]] | -0.51 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[LRSAM1]] | -0.51 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[SNHG32]] | -0.51 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[MED10]] | -0.50 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[ZFAS1]] | -0.50 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[PEX16]] | -0.50 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[ZFAND2A]] | -0.49 | -0.40 / -0.41 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LY75]] | B | LY75 activity raises ARHGDIB's level | lines that do not express LY75 (30) vs lines expressing it (20) | 1.70× lower at baseline in the lines without LY75 | 0.014 | ⚠ within organs, on part of the lines; also absent: IL20RA, TINAGL1, CARD11 |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 15, C 1. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDK2]] | B | ARHGDIB activity raises PDK2's level | lines that do not express ARHGDIB (23) vs lines expressing it (27) | 1.62× lower at baseline in the lines without ARHGDIB | 0.004 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |
| [[ARHGAP18]] | B | ARHGDIB activity raises ARHGAP18's level | lines that do not express ARHGDIB (23) vs lines expressing it (27) | 2.58× lower at baseline in the lines without ARHGDIB | 0.011 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |
| [[SELENOK]] | B | ARHGDIB activity raises SELENOK's level | lines that do not express ARHGDIB (23) vs lines expressing it (27) | 1.31× lower at baseline in the lines without ARHGDIB | 0.013 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |
| [[SPAG7]] | B | ARHGDIB activity lowers SPAG7's level | lines that do not express ARHGDIB (23) vs lines expressing it (27) | 1.40× higher at baseline in the lines without ARHGDIB | 0.036 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |
| [[PCDHGC3]] | B | ARHGDIB activity raises PCDHGC3's level | lines that do not express ARHGDIB (23) vs lines expressing it (27) | 1.71× lower at baseline in the lines without ARHGDIB | 0.036 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |
| [[LY75]] | B | ARHGDIB activity raises LY75's level | lines that do not express ARHGDIB (23) vs lines expressing it (27) | 1.79× lower at baseline in the lines without ARHGDIB | 0.042 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |
| [[COL4A1]] | B | ARHGDIB activity raises COL4A1's level | lines that do not express ARHGDIB (23) vs lines expressing it (27) | 1.97× lower at baseline in the lines without ARHGDIB | 0.042 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |
| [[TAGLN2]] | B | ARHGDIB activity raises TAGLN2's level | lines that do not express ARHGDIB (23) vs lines expressing it (27) | 1.55× lower at baseline in the lines without ARHGDIB | 0.045 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |
| [[FAM98B]] | B | ARHGDIB activity lowers FAM98B's level | lines that do not express ARHGDIB (23) vs lines expressing it (27) | 1.27× higher at baseline in the lines without ARHGDIB | 0.051 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |
| [[COL4A2]] | B | ARHGDIB activity raises COL4A2's level | lines that do not express ARHGDIB (23) vs lines expressing it (27) | 1.95× lower at baseline in the lines without ARHGDIB | 0.057 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |
| cells under [[Belumosudil (drug)]] 5 µM | B | ARHGDIB activity raises the cells' numbers under Belumosudil 5 µM (protects the cells) | lines that do not express ARHGDIB (23) vs lines expressing it (25) | the lines without ARHGDIB: 0.65× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |
| [[CBR3-AS1]] | B | ARHGDIB activity raises CBR3-AS1's level | lines that do not express ARHGDIB (23) vs lines expressing it (27) | 1.56× lower at baseline in the lines without ARHGDIB | 0.077 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.487). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (36.0, -34.7); signed map (26.9, -42.7). **Vector** length 46.9, 9.76% of its response variance represented; |z| ≥ 3 in 517 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +16.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +14.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +16.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +3.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +3.6 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.1 | +0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.0 | -0.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -1.2 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.8 | -4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -3.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | Rho GDP dissociation inhibitor beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.3 — chr12:14,942,031-14,961,728 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Ly-GDI, RhoGDI2; previously RAP1GN1, GDIA2, GDID4 |
| Gene groups (HGNC) | Receptor ligands; Minor histocompatibility antigens; Rho GDP dissociation inhibitor family |
| Reactome | 9 pathways, smallest: RHOH GTPase cycle; RHOG GTPase cycle; RAC3 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P52566](https://www.uniprot.org/uniprotkb/P52566) (Rho GDP-dissociation inhibitor 2):

> Regulates the GDP/GTP exchange reaction of the Rho proteins by inhibiting the dissociation of GDP from them, and the subsequent binding of GTP to them. Regulates reorganization of the actin cytoskeleton mediated by Rho family members.

**Summary**, from NCBI Gene [397](https://www.ncbi.nlm.nih.gov/gene/397):

> Members of the Rho (or ARH) protein family (see MIM 165390) and other Ras-related small GTP-binding proteins (see MIM 179520) are involved in diverse cellular events, including cell signaling, proliferation, cytoskeletal organization, and secretion. The GTP-binding proteins are active only in the GTP-bound state. At least 3 classes of proteins tightly regulate cycling between the GTP-bound and GDP-bound states: GTPase-activating proteins (GAPs), guanine nucleotide-releasing factors (GRFs), and …

**Accessions** — [HGNC:679](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:679) · Entrez [397](https://www.ncbi.nlm.nih.gov/gene/397) · UniProt [P52566](https://www.uniprot.org/uniprotkb/P52566) · Ensembl [ENSG00000111348](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111348)

## Data

Gene col 3225: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3225); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3225, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3225]; `tensor/DDL_lfc|DDL_z.npy` [3225]; `embed/gene_vectors.npy` [3225]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3225 or target_col == 3225). Every well: [[ARHGDIB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGDIB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
