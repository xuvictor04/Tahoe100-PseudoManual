---
symbol: "PCDH7"
type: "gene"
col: 9859
ensembl_id: "ENSG00000169851"
name: "protocadherin 7"
location: "4p15.1"
module: 121
arm: "+"
pooled_cpm: 91.17
n_lines_expressing: 32
n_dd_up: 22
n_dd_down: 25
n_dd_up_clean: 22
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 6
direction_downstream: 7
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# PCDH7

*protocadherin 7* — 4p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.79× (z +9.2, q 3e-17, up in 19 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.499× (z -7.8, q 2e-12, down in 21 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MEIS2]] (+0.65, fdr 7e-06), [[ADAMTS3]] (+0.65, fdr 1e-05), [[ZNF827]] (+0.62, fdr 3e-05); moves opposite to [[DIP2A]] (-0.58, fdr 1e-05), [[HDAC11]] (-0.54, fdr 3e-05), [[TPD52L2]] (-0.54, fdr 7e-05).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MEF2C]] → it (grade B ⚠); 7 go from it, the strongest it → [[TFAP2A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, none with an alert; shown: the 15 strongest. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9859.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +9.2 | 3e-17 | 19/31 (HOP62, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.79×** | +6.3 | 1e-07 | 22/29 (NCI-H2347, hTERT-HPNE, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +5.6 | 5e-06 | 16/30 (hTERT-HPNE, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.59×** | +5.2 | 3e-05 | 15/30 (SW 900, hTERT-HPNE, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.58×** | +5.1 | 4e-05 | 23/30 (NCI-H1792, SW 900, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.9 | 1e-04 | 18/30 (HOP62, LS 180, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.008 | 19/30 (NCI-H1792, C32, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.41×** | +3.9 | 0.008 | 15/29 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.012 | 18/30 (CFPAC-1, NCI-H1792, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.013 | 14/30 (HOP62, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Omeprazole (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.013 | 15/30 (NCI-H1792, NCI-H2347, …) | inconsistent across doses |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.013 | 13/30 (NCI-H1792, CFPAC-1, …) | top dose only |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.44×** | +3.6 | 0.014 | 13/30 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.037 | 14/31 (NCI-H460, C32, …) | two highest doses | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.037 | 13/30 (hTERT-HPNE, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9859.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.499×** | -7.8 | 2e-12 | 21/30 (A-427, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.500×** | -7.8 | 2e-12 | 24/30 (C32, HCT15, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.503×** | -7.7 | 2e-12 | 22/30 (A-427, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.615×** | -7.7 | 2e-12 | 25/31 (NCI-H460, C32, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.548×** | -6.7 | 2e-09 | 20/30 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.557×** | -6.6 | 5e-09 | 20/30 (C32, HCT15, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.559×** | -6.5 | 6e-09 | 22/29 (NCI-H1792, A-172, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.584×** | -6.0 | 1e-07 | 21/30 (NCI-H1792, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.593×** | -5.8 | 3e-07 | 20/30 (A-427, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.596×** | -5.8 | 4e-07 | 21/30 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.578×** | -5.8 | 4e-07 | 19/30 (C32, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.588×** | -5.7 | 5e-07 | 23/29 (KATO III, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.604×** | -5.4 | 3e-06 | 16/29 (C32, NCI-H1792, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.619×** | -5.4 | 3e-06 | 18/29 (C32, NCI-H1792, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.587×** | -4.2 | 8e-04 | 17/30 (C32, NCI-H460, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.698×** | -3.9 | 0.004 | 16/30 (NCI-H460, Panc 03.27, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM |  | **0.788×** | -3.8 | 0.005 | 17/30 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 5 µM |  | **0.798×** | -3.6 | 0.010 | 15/31 (AN3 CA, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9859. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 609 | 0 | 24 (10 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0740× (z -17.8) |
| [[A-427 (line)]] | wt | 1,276 | 0 | 11 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.126× (z -23.0) |
| [[KATO III (line)]] | alt | 139 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -15.7) |
| [[NCI-H460 (line)]] | wt | 59.1 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.147× (z -12.0) |
| [[HCT15 (line)]] | alt | 129 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -13.0) |
| [[HOP62 (line)]] | alt | 63.3 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +13.2) | — |
| [[NCI-H1792 (line)]] | alt | 95.1 | 0 | 4 (2 ⚠) | — | [[Daptomycin (drug)]] 5 µM 0.206× (z -9.9) ⚠ unreliable plate only · without an alert: [[5-Azacytidine (drug)]] 5 µM 0.231× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 44.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +9.8) | [[Selinexor (drug)]] 5 µM 0.396× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 32.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +10.5) | — |
| [[NCI-H23 (line)]] | alt | 112 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.298× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 84.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -10.7) |
| [[SNU-423 (line)]] | alt | 103 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.240× (z -10.7) |
| [[CHP-212 (line)]] | wt | 181 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.328× (z -8.8) |
| [[HS-578T (line)]] | alt | 91.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +9.9) | — |
| [[hTERT-HPNE (line)]] | wt | 203 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +12.8) | — |
| [[PANC-1 (line)]] | alt | 56.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.303× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[SK-MEL-2 (line)]] | alt | 32.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +12.4) | — |
| [[SW 900 (line)]] | alt | 124 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +9.3) | — |
| [[A-172 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.6 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.54 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 248 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.10 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.93 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 22.7 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.00 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.35 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 382 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.57 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.35 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 21.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.98 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.98 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9859), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEIS2]] | +0.65 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[ADAMTS3]] | +0.65 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[ZNF827]] | +0.62 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[ZNF462]] | +0.59 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[DPY19L2]] | +0.58 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[CFH]] | +0.58 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[MEF2C]] | +0.58 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[GLI3]] | +0.57 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[FLRT2]] | +0.56 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[TFAP2A]] | +0.56 | +0.55 / +0.39 | both halves | 6e-05 |  |
| [[NREP]] | +0.55 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[UNC5C]] | +0.54 | +0.49 / +0.50 | both halves | 1e-05 | STRING 480 |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIP2A]] | -0.58 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[HDAC11]] | -0.54 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[TPD52L2]] | -0.54 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[TPCN2]] | -0.52 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[KCTD21]] | -0.51 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[CSGALNACT2]] | -0.50 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[WASF2]] | -0.50 | -0.59 / -0.35 | both halves | 1e-04 |  |
| [[ABTB1]] | -0.50 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[BCLAF3]] | -0.49 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[FCHSD1]] | -0.49 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[PSMD9]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[CRLF3]] | -0.48 | -0.46 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEF2C]] | B | MEF2C activity raises PCDH7's level | lines that do not express MEF2C (14) vs lines expressing it (36) | 3.17× lower at baseline in the lines without MEF2C | 0.045 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, RGS2, MYOSLID |
| [[PARP8]] | B | PARP8 activity raises PCDH7's level | lines that do not express PARP8 (6) vs lines expressing it (44) | 3.62× lower at baseline in the lines without PARP8 | 0.078 | ⚠ within organs, on part of the lines; also absent: ITPKB, ZNF785 |
| [[MEF2C-AS1]] | C | MEF2C-AS1 activity raises PCDH7's level | lines that do not express MEF2C-AS1 (16) vs lines expressing it (34) | 3.91× lower at baseline in the lines without MEF2C-AS1 | 0.036 | ⚠ within organs, on part of the lines; also absent: MEF2C, RGS2, ADGRL4; co-absent with the target |
| [[NLGN1]] | C | NLGN1 activity raises PCDH7's level | lines that do not express NLGN1 (30) vs lines expressing it (20) | 3.57× lower at baseline in the lines without NLGN1 | 0.047 | ⚠ within organs, on part of the lines; also absent: EPB41L3, PAX3, NEGR1; co-absent with the target |
| [[FAT4]] | C | FAT4 activity raises PCDH7's level | lines that do not express FAT4 (20) vs lines expressing it (30) | 4.55× lower at baseline in the lines without FAT4 | 0.054 | ⚠ within organs, on part of the lines; also absent: RFTN1, GPR176, GNG11; co-absent with the target |
| [[DPY19L2]] | C | DPY19L2 activity raises PCDH7's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 3.90× lower at baseline in the lines without DPY19L2 | 0.068 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TFAP2A]] | B | PCDH7 activity raises TFAP2A's level | lines that do not express PCDH7 (18) vs lines expressing it (32) | 1.75× lower at baseline in the lines without PCDH7 | 0.073 | ⚠ within organs, on part of the lines; also absent: ADGRL4, KCNQ5, ST8SIA4 |
| [[PARP8]] | B | PCDH7 activity raises PARP8's level | lines that do not express PCDH7 (18) vs lines expressing it (32) | 1.72× lower at baseline in the lines without PCDH7 | 0.073 | ⚠ within organs, on part of the lines; also absent: ADGRL4, KCNQ5, ST8SIA4 |
| [[NEGR1]] | B | PCDH7 activity raises NEGR1's level | lines that do not express PCDH7 (18) vs lines expressing it (32) | 2.62× lower at baseline in the lines without PCDH7 | 0.085 | ⚠ within organs, on part of the lines; also absent: ADGRL4, KCNQ5, ST8SIA4 |
| [[TENM3]] | B | PCDH7 activity raises TENM3's level | lines that do not express PCDH7 (18) vs lines expressing it (32) | 1.47× lower at baseline in the lines without PCDH7 | 0.095 | ⚠ within organs, on part of the lines; also absent: ADGRL4, KCNQ5, ST8SIA4 |
| [[ADAMTS3]] | B | PCDH7 activity raises ADAMTS3's level | lines that do not express PCDH7 (18) vs lines expressing it (32) | 1.95× lower at baseline in the lines without PCDH7 | 0.099 | ⚠ within organs, on part of the lines; also absent: ADGRL4, KCNQ5, ST8SIA4 |
| [[DPY19L2]] | C | PCDH7 activity raises DPY19L2's level | lines that do not express PCDH7 (18) vs lines expressing it (32) | 2.68× lower at baseline in the lines without PCDH7 | 0.080 | ⚠ within organs, on part of the lines; also absent: ADGRL4, KCNQ5, ST8SIA4; co-absent with the target |
| [[FAT4]] | C | PCDH7 activity raises FAT4's level | lines that do not express PCDH7 (18) vs lines expressing it (32) | 3.86× lower at baseline in the lines without PCDH7 | 0.081 | ⚠ within organs, on part of the lines; also absent: ADGRL4, KCNQ5, ST8SIA4; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.582). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.1, 26.5); signed map (44.8, 27.0). **Vector** length 104, 28.4% of its response variance represented; |z| ≥ 3 in 1,059 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +9.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +4.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +2.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.7 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | -0.8 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -4.9 | -7.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.9 | -7.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.4 | -5.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.4 | -7.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.1 | -6.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.0 | -5.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.7 | -5.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | protocadherin 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.1 — chr4:30,720,369-31,146,805 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BH-Pcdh, PPP1R120 |
| Gene groups (HGNC) | Non-clustered protocadherins; Protein phosphatase 1 regulatory subunits |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Reactome | 9 pathways, smallest: RHOB GTPase cycle; Platelet degranulation; Response to elevated platelet cytosolic Ca2+ |
| Matched by | ensembl_id |

UniProt [O60245](https://www.uniprot.org/uniprotkb/O60245) carries no function annotation.

**Summary**, from NCBI Gene [5099](https://www.ncbi.nlm.nih.gov/gene/5099):

> This gene belongs to the protocadherin gene family, a subfamily of the cadherin superfamily. The gene encodes a protein with an extracellular domain containing 7 cadherin repeats. The gene product is an integral membrane protein that is thought to function in cell-cell recognition and adhesion. Alternative splicing yields isoforms with unique cytoplasmic tails. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8659](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8659) · Entrez [5099](https://www.ncbi.nlm.nih.gov/gene/5099) · UniProt [O60245](https://www.uniprot.org/uniprotkb/O60245) · Ensembl [ENSG00000169851](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169851)

## Data

Gene col 9859: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9859); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9859, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9859]; `tensor/DDL_lfc|DDL_z.npy` [9859]; `embed/gene_vectors.npy` [9859]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9859 or target_col == 9859). Every well: [[PCDH7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCDH7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
