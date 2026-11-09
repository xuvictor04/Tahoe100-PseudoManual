---
symbol: "ZDHHC11B"
type: "gene"
col: 13033
ensembl_id: "ENSG00000206077"
name: "zDHHC palmitoyltransferase 11B (putative)"
location: "5p15.33"
module: 15
arm: "-"
pooled_cpm: 6.92
n_lines_expressing: 45
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 11
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ZDHHC11B

*zDHHC palmitoyltransferase 11B (putative)* — 5p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 6.99× (z +20.1, q 0e+00, up in 42 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.632× (z -4.8, q 0.001, down in 16 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 2 lines (HT-29 0.119×, KATO III 0.164×; ⚠ transcription drop; cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (LoVo 0.0550×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change); [[Esmolol (hydrochloride) (drug)]] 0.5 µM in 1 line (SW1417 0.0562×); [[Decitabine (drug)]] 0.5 µM in 1 line (SW 900 0.0657×); [[Bortezomib (drug)]] 0.05 µM in 1 line (HT-29 0.119×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPPP]] (+0.81, fdr 7e-06, ⚠ same locus), [[RAP1GAP]] (+0.66, fdr 9e-06), [[VIPR1]] (+0.62, fdr 9e-06), [[MYO7A]] (+0.59, fdr 1e-05); moves opposite to [[TRAPPC13]] (-0.60, fdr 5e-05), [[C2orf42]] (-0.54, fdr 3e-04), [[TMEM11-DT]] (-0.52, fdr 3e-05).
> It sits in the **-** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ABHD11]] → it (grade B ⚠); 11 go from it, the strongest it → [[CHKA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13033.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **6.99×** | +20.1 | 0e+00 | 42/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.65×** | +17.9 | 0e+00 | 40/42 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.78×** | +14.9 | 0e+00 | 23/37 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **4.20×** | +14.8 | 0e+00 | 39/42 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.21×** | +12.0 | 3e-31 | 37/42 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.97×** | +9.9 | 6e-21 | 25/41 (SW480, SW1417, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **2.06×** | +7.5 | 7e-12 | 25/41 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.06×** | +7.2 | 5e-11 | 22/40 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +7.1 | 6e-11 | 5/8 (LS 180, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.94×** | +6.8 | 4e-10 | 21/37 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **3.09×** | +6.1 | 6e-08 | 19/40 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +5.3 | 5e-06 | 17/40 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.43×** | +5.2 | 1e-05 | 18/41 (PANC-1, SW1417, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.60×** | +4.9 | 5e-05 | 17/40 (SW1417, NCI-H460, …) | all doses, flat | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.8 | 6e-05 | 16/35 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +4.1 | 0.001 | 13/35 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.028 | 16/40 (NCI-H460, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.061 | 8/42 (LS 180, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13033.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 2 lines (HT-29 0.119×, KATO III 0.164×; ⚠ transcription drop; cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (LoVo 0.0550×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change); [[Esmolol (hydrochloride) (drug)]] 0.5 µM in 1 line (SW1417 0.0562×); [[Decitabine (drug)]] 0.5 µM in 1 line (SW 900 0.0657×); [[Bortezomib (drug)]] 0.05 µM in 1 line (HT-29 0.119×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.632×** | -4.8 | 0.001 | 16/40 (MIA PaCa-2, SW480, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.731× | -3.3 | 0.27 | 14/40 (LoVo, A-427, …) | two highest doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.807× | -3.2 | 0.27 | 12/40 (HT-29, SW 900, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13033. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.45 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.6× (z +19.7) | — |
| [[PANC-1 (line)]] | alt | 4.75 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +11.3) | — |
| [[SW480 (line)]] | alt | 6.31 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 9.44× (z +10.9) | — |
| [[A549 (line)]] | wt | 6.81 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 10.1× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 30.7 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.119× (z -9.6) ⚠ transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.119× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 4.29 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 13.5× (z +8.8) | [[Ornidazole (drug)]] 0.5 µM 0.0700× (z -9.0) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 5.53 | 1 (1 ⚠) | 1 | [[Selinexor (drug)]] 5 µM 4.93× (z +8.7) ⚠ cell-cycle shift, explains ~38% of this change | [[Esmolol (hydrochloride) (drug)]] 0.5 µM 0.0562× (z -11.1) |
| [[A-172 (line)]] | wt | 4.44 | 0 | 1 | — | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM 0.0656× (z -8.8) |
| [[A498 (line)]] | wt | 5.16 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 13.4× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.134× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 14.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +8.7) | — |
| [[HCT15 (line)]] | alt | 14.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0692× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 1.79 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.2× (z +9.3) | — |
| [[Hs 766T (line)]] | wt | 4.44 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 16.0× (z +9.2) | — |
| [[KATO III (line)]] | alt | 25.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.164× (z -9.4) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0550× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[LS 180 (line)]] | wt | 20.3 | 1 | 0 | [[Selinexor (drug)]] 0.05 µM 4.59× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 2.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.99× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 9.93 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0657× (z -9.7) |
| [[A-427 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.946 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13033), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPPP]] | +0.81 | +0.76 / +0.83 | both halves | 7e-06 | ⚠ same locus (17.0 kb, same strand: neighbours can correlate without regulation) |
| [[RAP1GAP]] | +0.66 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[VIPR1]] | +0.62 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[MYO7A]] | +0.59 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[KCNQ1]] | +0.56 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[USP2]] | +0.55 | +0.40 / +0.63 | both halves | 4e-05 |  |
| [[SYT5]] | +0.55 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[MAPK8IP1]] | +0.55 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[PPFIBP2]] | +0.54 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[EPPK1]] | +0.54 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[NDRG4]] | +0.53 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[PPL]] | +0.53 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[C1orf226]] | +0.52 | +0.53 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC13]] | -0.60 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[C2orf42]] | -0.54 | -0.27 / -0.56 | both halves | 3e-04 |  |
| [[TMEM11-DT]] | -0.52 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[MFSD8]] | -0.52 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[DHX35]] | -0.52 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[TMEM267]] | -0.51 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[C8orf76]] | -0.50 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[ELMOD3]] | -0.49 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[ZNF595]] | -0.49 | -0.47 / -0.29 | both halves | 3e-04 |  |
| [[SNRNP40]] | -0.49 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[ANGEL2]] | -0.48 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[STARD7-AS1]] | -0.48 | -0.34 / -0.37 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABHD11]] | B | ABHD11 activity raises ZDHHC11B's level | lines that do not express ABHD11 (8) vs lines expressing it (42) | 2.55× lower at baseline in the lines without ABHD11 | 0.017 | ⚠ within organs, on part of the lines; also absent: E2F2, CXCL16, ABLIM2; maybe low, not absent |
| [[MYH14]] | B | MYH14 activity raises ZDHHC11B's level | lines that do not express MYH14 (21) vs lines expressing it (29) | 2.11× lower at baseline in the lines without MYH14 | 0.028 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[MCF2L]] | B | MCF2L activity raises ZDHHC11B's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 2.23× lower at baseline in the lines without MCF2L | 0.054 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[RSPH1]] | B | RSPH1 activity raises ZDHHC11B's level | lines that do not express RSPH1 (13) vs lines expressing it (37) | 2.54× lower at baseline in the lines without RSPH1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: SLC37A1, ABCG1, SHROOM3; maybe low, not absent |
| [[AMOT]] | B | AMOT activity raises ZDHHC11B's level | lines that do not express AMOT (12) vs lines expressing it (38) | 2.08× lower at baseline in the lines without AMOT | 0.096 | ⚠ within organs, on part of the lines; also absent: SYCP2, ENSG00000289956, ENSG00000132832 |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHKA]] | B | ZDHHC11B activity raises CHKA's level | lines that do not express ZDHHC11B (5) vs lines expressing it (45) | 2.60× lower at baseline in the lines without ZDHHC11B | 0.010 | ⚠ within organs, on part of the lines; also absent: CTSV, RTN4R, ATP11A; maybe low, not absent |
| [[TPPP]] | B | ZDHHC11B activity raises TPPP's level | lines that do not express ZDHHC11B (5) vs lines expressing it (45) | 2.11× lower at baseline in the lines without ZDHHC11B | 0.024 | ⚠ within organs, on part of the lines; also absent: CTSV, RTN4R, ATP11A; maybe low, not absent |
| [[CYSTM1]] | B | ZDHHC11B activity raises CYSTM1's level | lines that do not express ZDHHC11B (5) vs lines expressing it (45) | 2.41× lower at baseline in the lines without ZDHHC11B | 0.043 | ⚠ within organs, on part of the lines; also absent: CTSV, RTN4R, ATP11A; maybe low, not absent |
| [[MCF2L]] | B | ZDHHC11B activity raises MCF2L's level | lines that do not express ZDHHC11B (5) vs lines expressing it (45) | 4.99× lower at baseline in the lines without ZDHHC11B | 0.051 | ⚠ within organs, on part of the lines; also absent: CTSV, RTN4R, ATP11A; maybe low, not absent |
| [[TUFT1]] | B | ZDHHC11B activity raises TUFT1's level | lines that do not express ZDHHC11B (5) vs lines expressing it (45) | 3.12× lower at baseline in the lines without ZDHHC11B | 0.061 | ⚠ within organs, on part of the lines; also absent: CTSV, RTN4R, ATP11A; maybe low, not absent |
| [[TRAPPC13]] | B | ZDHHC11B activity raises TRAPPC13's level | lines that do not express ZDHHC11B (5) vs lines expressing it (45) | 1.47× lower at baseline in the lines without ZDHHC11B | 0.067 | ⚠ within organs, on part of the lines; also absent: CTSV, RTN4R, ATP11A; maybe low, not absent |
| [[AMDHD2]] | B | ZDHHC11B activity raises AMDHD2's level | lines that do not express ZDHHC11B (5) vs lines expressing it (45) | 1.52× lower at baseline in the lines without ZDHHC11B | 0.070 | ⚠ within organs, on part of the lines; also absent: CTSV, RTN4R, ATP11A; maybe low, not absent |
| [[AMOT]] | B | ZDHHC11B activity raises AMOT's level | lines that do not express ZDHHC11B (5) vs lines expressing it (45) | 3.44× lower at baseline in the lines without ZDHHC11B | 0.087 | ⚠ within organs, on part of the lines; also absent: CTSV, RTN4R, ATP11A; maybe low, not absent |
| [[SPIRE2]] | B | ZDHHC11B activity raises SPIRE2's level | lines that do not express ZDHHC11B (5) vs lines expressing it (45) | 2.22× lower at baseline in the lines without ZDHHC11B | 0.089 | ⚠ within organs, on part of the lines; also absent: CTSV, RTN4R, ATP11A; maybe low, not absent |
| [[MLXIPL]] | B | ZDHHC11B activity raises MLXIPL's level | lines that do not express ZDHHC11B (5) vs lines expressing it (45) | 2.83× lower at baseline in the lines without ZDHHC11B | 0.092 | ⚠ within organs, on part of the lines; also absent: CTSV, RTN4R, ATP11A; maybe low, not absent |
| [[MUC3A]] | B | ZDHHC11B activity raises MUC3A's level | lines that do not express ZDHHC11B (5) vs lines expressing it (45) | 2.60× lower at baseline in the lines without ZDHHC11B | 0.097 | ⚠ within organs, on part of the lines; also absent: CTSV, RTN4R, ATP11A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **-** arm (projection on the module's main direction -0.435). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (20.4, 18.3); signed map (-2.4, 23.8). **Vector** length 63.0, 9.64% of its response variance represented; |z| ≥ 3 in 1,136 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +3.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.1 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +9.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.3 | +0.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.3 | +0.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.2 | +2.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +1.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -1.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +0.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.7 | +4.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -1.8 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | -0.6 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.2 | -0.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | zDHHC palmitoyltransferase 11B (putative) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.33 — chr5:710,355-784,729 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Zinc fingers DHHC-type |
| Matched by | ensembl_id |

**Function**, from UniProt [P0C7U3](https://www.uniprot.org/uniprotkb/P0C7U3) (Probable palmitoyltransferase ZDHHC11B):

> Probable palmitoyltransferase that could catalyze the addition of palmitate onto various protein substrates and be involved in a variety of cellular processes (By similarity). May play a role in cell proliferation.

**Summary**, from NCBI Gene [653082](https://www.ncbi.nlm.nih.gov/gene/653082):

> Predicted to enable protein-cysteine S-palmitoyltransferase activity. Predicted to be involved in several processes, including antiviral innate immune response; peptidyl-L-cysteine S-palmitoylation; and positive regulation of defense response to virus by host. Predicted to be located in endosome membrane. Predicted to be active in Golgi apparatus and endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:32962](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32962) · Entrez [653082](https://www.ncbi.nlm.nih.gov/gene/653082) · UniProt [P0C7U3](https://www.uniprot.org/uniprotkb/P0C7U3) · Ensembl [ENSG00000206077](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206077)

## Data

Gene col 13033: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13033); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13033, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13033]; `tensor/DDL_lfc|DDL_z.npy` [13033]; `embed/gene_vectors.npy` [13033]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13033 or target_col == 13033). Every well: [[ZDHHC11B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZDHHC11B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
