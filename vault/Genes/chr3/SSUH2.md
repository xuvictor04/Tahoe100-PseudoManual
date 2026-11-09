---
symbol: "SSUH2"
type: "gene"
col: 4584
ensembl_id: "ENSG00000125046"
name: "ssu-2 homolog"
location: "3p25.3"
module: 39
arm: "+"
pooled_cpm: 6.25
n_lines_expressing: 47
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 7
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# SSUH2

*ssu-2 homolog* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.24× (z +19.5, q 0e+00, up in 36 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Radotinib (drug)]] 5 µM: 0.671× (z -5.4, q 3e-05, down in 21 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.0217×, HEC-1-A 0.144×); [[Belinostat (drug)]] 5 µM in 2 lines (SK-MEL-2 0.0933×, AsPC-1 0.0674×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.196×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SW480 0.0866×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYH15]] (+0.75, fdr 7e-06), [[PKD1L1]] (+0.74, fdr 7e-06), [[C3orf20]] (+0.72, fdr 7e-06); moves opposite to [[CDADC1]] (-0.64, fdr 1e-05), [[TERF1]] (-0.63, fdr 9e-06), [[PEX3]] (-0.63, fdr 9e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SCAT1]] → it (grade B ⚠); 7 go from it, the strongest it → [[CUBN]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4584.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.24×** | +19.5 | 0e+00 | 36/40 (J82, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **5.13×** | +15.6 | 0e+00 | 33/41 (A-172, SW480, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.37×** | +11.6 | 7e-29 | 35/39 (COLO 205, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.95×** | +9.9 | 4e-21 | 30/41 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.46×** | +7.9 | 3e-13 | 10/19 (LOX-IMVI, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +6.6 | 5e-09 | 19/38 (NCI-H1573, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.95×** | +6.4 | 2e-08 | 21/42 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.4 | 5e-06 | 17/42 (Hs 766T, HOP62, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.26×** | +4.1 | 0.003 | 3/40 (NCI-H2030, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.55×** | +4.0 | 0.004 | 12/40 (SW1417, NCI-H23, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.8 | 0.009 | 7/31 (NCI-H460, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +3.2 | 0.055 | 10/41 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.062 | 7/43 (NCI-H460, Hs 766T, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.86×** | +3.1 | 0.077 | 4/33 (COLO 205, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Acetohexamide (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.077 | 3/42 (SW1417, CFPAC-1, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.096 | 8/42 (SW1417, HepG2/C3A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4584.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.0217×, HEC-1-A 0.144×); [[Belinostat (drug)]] 5 µM in 2 lines (SK-MEL-2 0.0933×, AsPC-1 0.0674×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.196×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SW480 0.0866×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | **0.671×** | -5.4 | 3e-05 | 21/42 (COLO 205, AsPC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.687×** | -3.6 | 0.085 | 15/39 (SK-MEL-2, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | 0.706× | -3.4 | 0.15 | 15/41 (HCT15, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.05 µM |  | 0.712× | -3.3 | 0.15 | 16/40 (RPMI-7951, NCI-H1792, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 5 µM |  | 0.799× | -3.1 | 0.24 | 4/43 (CHP-212, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4584. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 26.3 | 0 | 5 (4 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0217× (z -16.8) |
| [[A-172 (line)]] | wt | 4.67 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +14.3) | — |
| [[LoVo (line)]] | wt | 6.77 | 2 | 1 | [[Harringtonine (drug)]] 5 µM 10.5× (z +9.0) | [[Menadione (drug)]] 0.05 µM 0.0873× (z -9.0) |
| [[COLO 205 (line)]] | alt | 16.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +12.0) | — |
| [[HepG2_C3A (line)]] | wt | 44.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -11.7) |
| [[HOP62 (line)]] | alt | 2.43 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.2× (z +13.3) | — |
| [[J82 (line)]] | alt | 5.81 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.7× (z +16.9) | — |
| [[NCI-H2347 (line)]] | alt | 1.95 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.4× (z +12.4) | — |
| [[NCI-H460 (line)]] | wt | 8.55 | 2 | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 7.06× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 1.89 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +12.0) | — |
| [[SW480 (line)]] | alt | 3.02 | 1 | 1 | [[Auranofin (drug)]] 5 µM 14.0× (z +11.0) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0866× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0674× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 5.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +10.4) | — |
| [[C32 (line)]] | wt | 4.22 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 2.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 43.0× (z +14.7) | — |
| [[HEC-1-A (line)]] | alt | 10.2 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.144× (z -8.6) |
| [[Hs 766T (line)]] | wt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.38× (z +11.4) | — |
| [[HS-578T (line)]] | alt | 4.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.89× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 4.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.1× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.90× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 8.06 | 0 | 1 | — | [[Dexamethasone (drug)]] 0.5 µM 0.0599× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 7.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 28.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 2.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +8.7) | — |
| [[A-427 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4584), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYH15]] | +0.75 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[PKD1L1]] | +0.74 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.72 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[PHEX]] | +0.72 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[MTNR1A]] | +0.72 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[TBILA]] | +0.71 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[SMCO2]] | +0.71 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[NANOS3]] | +0.70 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.70 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[MMP25]] | +0.70 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[LINC01191]] | +0.69 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[SLC22A1]] | +0.69 | +0.71 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDADC1]] | -0.64 | -0.52 / -0.67 | both halves | 1e-05 |  |
| [[TERF1]] | -0.63 | -0.57 / -0.60 | both halves | 9e-06 |  |
| [[PEX3]] | -0.63 | -0.57 / -0.60 | both halves | 9e-06 |  |
| [[ALG9]] | -0.63 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[SLC9A6]] | -0.63 | -0.67 / -0.47 | both halves | 2e-05 |  |
| [[SNX1]] | -0.63 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[SNX4]] | -0.63 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[GCSH]] | -0.63 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[CCZ1]] | -0.62 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[NCK1]] | -0.62 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[CCZ1B]] | -0.61 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[MMS19]] | -0.61 | -0.63 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCAT1]] | B | SCAT1 activity raises SSUH2's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 1.88× lower at baseline in the lines without SCAT1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[FER1L6]] | B | FER1L6 activity raises SSUH2's level | lines that do not express FER1L6 (7) vs lines expressing it (43) | 2.14× lower at baseline in the lines without FER1L6 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |
| [[ATXN1]] | C | ATXN1 activity raises SSUH2's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 2.12× lower at baseline in the lines without ATXN1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2; co-absent with the target |
| [[OXTR]] | C | OXTR activity raises SSUH2's level | lines that do not express OXTR (5) vs lines expressing it (45) | 2.20× lower at baseline in the lines without OXTR | 0.092 | ⚠ within organs, on part of the lines; also absent: IPCEF1, SSUH2, OPN3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CUBN]] | C | SSUH2 activity lowers CUBN's level | lines that do not express SSUH2 (3) vs lines expressing it (47) | 11.83× higher at baseline in the lines without SSUH2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GNA14, FRMD3, OXTR; maybe low, not absent; its own permutation p |
| [[ATXN1]] | C | SSUH2 activity raises ATXN1's level | lines that do not express SSUH2 (3) vs lines expressing it (47) | 7.76× lower at baseline in the lines without SSUH2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GNA14, FRMD3, OXTR; maybe low, not absent; co-absent with the target; its own permutation p |
| [[GATA4]] | C | SSUH2 activity lowers GATA4's level | lines that do not express SSUH2 (3) vs lines expressing it (47) | 6.77× higher at baseline in the lines without SSUH2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GNA14, FRMD3, OXTR; maybe low, not absent; its own permutation p |
| [[FLYWCH2]] | C | SSUH2 activity lowers FLYWCH2's level | lines that do not express SSUH2 (3) vs lines expressing it (47) | 1.75× higher at baseline in the lines without SSUH2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GNA14, FRMD3, OXTR; maybe low, not absent; its own permutation p |
| [[SLC2A9]] | C | SSUH2 activity raises SLC2A9's level | lines that do not express SSUH2 (3) vs lines expressing it (47) | 2.25× lower at baseline in the lines without SSUH2 | 0.069 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GNA14, FRMD3, OXTR; maybe low, not absent |
| [[FBXW10B]] | C | SSUH2 activity raises FBXW10B's level | lines that do not express SSUH2 (3) vs lines expressing it (47) | 2.74× lower at baseline in the lines without SSUH2 | 0.070 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GNA14, FRMD3, OXTR; maybe low, not absent |
| [[SPTBN5]] | C | SSUH2 activity raises SPTBN5's level | lines that do not express SSUH2 (3) vs lines expressing it (47) | 2.10× lower at baseline in the lines without SSUH2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GNA14, FRMD3, OXTR; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.698). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.3, -10.7); signed map (20.3, 8.3). **Vector** length 92.9, 18.8% of its response variance represented; |z| ≥ 3 in 1,177 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.2 | +15.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.0 | +19.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.9 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.8 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.4 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +3.2 |
| fall | [[Radotinib (drug)]] 5 µM |  | -3.8 | -5.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.4 | -3.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.6 | -1.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -0.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ssu-2 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:8,619,386-8,745,040 (-) |
| Ensembl biotype | protein_coding |
| Also known as | fls485, ssu-2; previously C3orf32 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2M2](https://www.uniprot.org/uniprotkb/Q9Y2M2) (Protein SSUH2 homolog):

> Plays a role in odontogenesis.

**Summary**, from NCBI Gene [51066](https://www.ncbi.nlm.nih.gov/gene/51066):

> Predicted to enable heat shock protein binding activity and unfolded protein binding activity. Involved in odontogenesis. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24809](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24809) · Entrez [51066](https://www.ncbi.nlm.nih.gov/gene/51066) · UniProt [Q9Y2M2](https://www.uniprot.org/uniprotkb/Q9Y2M2) · Ensembl [ENSG00000125046](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125046)

## Data

Gene col 4584: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4584); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4584, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4584]; `tensor/DDL_lfc|DDL_z.npy` [4584]; `embed/gene_vectors.npy` [4584]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4584 or target_col == 4584). Every well: [[SSUH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SSUH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
