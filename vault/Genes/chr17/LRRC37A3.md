---
symbol: "LRRC37A3"
type: "gene"
col: 10752
ensembl_id: "ENSG00000176809"
name: "leucine rich repeat containing 37 member A3"
location: "17q24.1"
module: 23
arm: "+"
pooled_cpm: 5.58
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# LRRC37A3

*leucine rich repeat containing 37 member A3* — 17q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.72× (z +15.9, q 0e+00, up in 37 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.611× (z -5.6, q 1e-05, down in 20 of 46 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.734× (z -3.5, q 0.040, down in 18 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0803×; ⚠ cell-cycle shift, explains ~38% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0922×).
> Its strongest partners by |cos| (61 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 39 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEPTIN7-DT]] (+0.90, fdr 7e-06), [[TMEM202-AS1]] (+0.85, fdr 5e-05), [[INTS6-AS1]] (+0.82, fdr 3e-05); moves opposite to [[STUB1]] (-0.68, fdr 0.001, ⚠ not reproduced).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10752.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.72×** | +15.9 | 0e+00 | 37/42 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.49×** | +14.6 | 1e-45 | 29/40 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.32×** | +9.5 | 4e-19 | 29/40 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.18×** | +8.5 | 4e-15 | 25/32 (KATO III, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.67×** | +8.2 | 4e-14 | 25/47 (NCI-H460, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.52×** | +6.7 | 2e-09 | 20/46 (NCI-H2030, A-427, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +6.5 | 9e-09 | 2/7 (A498, NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +6.3 | 2e-08 | 18/40 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.57×** | +5.1 | 2e-05 | 16/45 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.50×** | +4.6 | 3e-04 | 17/47 (A-172, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +4.5 | 4e-04 | 6/14 (A498, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +4.2 | 0.001 | 13/47 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.003 | 11/47 (A498, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.35×** | +3.3 | 0.035 | 9/44 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.036 | 6/45 (NCI-H2030, SNU-423, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.037 | 10/40 (NCI-H460, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.075 | 3/47 (A498, A-172, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +2.9 | 0.098 | 3/47 (SW480, C-33 A, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.64×** | +2.9 | 0.098 | 5/45 (A-172, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +2.9 | 0.098 | 9/45 (NCI-H2030, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10752.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0803×; ⚠ cell-cycle shift, explains ~38% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0922×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.611×** | -5.6 | 1e-05 | 20/46 (NCI-H1792, AN3 CA, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.622×** | -5.4 | 2e-05 | 19/46 (SW480, C-33 A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **0.694×** | -4.0 | 0.012 | 11/32 (Hs 766T, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **0.723×** | -3.7 | 0.030 | 13/38 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.729×** | -3.6 | 0.036 | 16/45 (HS-578T, NCI-H1792, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.734×** | -3.5 | 0.040 | 18/45 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **0.816×** | -3.3 | 0.080 | 6/46 (PANC-1, SW480, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.760× | -3.1 | 0.12 | 7/47 (NCI-H661, A-427, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.602× | -3.0 | 0.16 | 5/34 (HT-29, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10752. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 4.74 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +15.2) | — |
| [[HS-578T (line)]] | alt | 3.11 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +10.1) | — |
| [[LoVo (line)]] | wt | 4.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 4.70 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0922× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 5.90 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0803× (z -8.9) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H2030 (line)]] | alt | 4.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 7.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +9.7) | — |
| [[A-172 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.70 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10752), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 38 of them with an alert (⚠; 38 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN7-DT]] | +0.90 | +0.88 / +0.66 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.85 | +0.87 / +0.39 | both halves | 5e-05 |  |
| [[INTS6-AS1]] | +0.82 | +0.87 / +0.45 | both halves | 3e-05 |  |
| [[PPP1R3F]] | +0.80 | +0.83 / +0.33 | both halves | 1e-04 |  |
| [[PCNX4-DT]] | +0.80 | +0.86 / +0.25 | both halves | 4e-04 |  |
| [[ATE1OSP]] | +0.80 | +0.84 / +0.26 | both halves | 4e-04 |  |
| [[PPP1R12A-AS2]] | +0.80 | +0.85 / +0.21 | both halves | 7e-04 |  |
| [[OXA1L-DT]] | +0.79 | +0.83 / +0.27 | both halves | 3e-04 |  |
| [[RFX3-DT]] | +0.79 | +0.85 / +0.20 | both halves | 7e-04 |  |
| [[F8]] | +0.78 | +0.81 / +0.43 | both halves | 3e-05 |  |
| [[PPP3CB-AS1]] | +0.77 | +0.81 / +0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[MAD2L1-DT]] | +0.77 | +0.80 / +0.27 | both halves | 3e-04 |  |
| [[H2AZ1-DT]] | +0.77 | +0.83 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STUB1]] | -0.68 | -0.42 / -0.15 | ⚠ not reproduced | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LRRC37A3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ANKRD20A21P]] | B | ANKRD20A21P activity raises LRRC37A3's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 1.38× lower at baseline in the lines without ANKRD20A21P | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[PPP1R1C]] | B | PPP1R1C activity raises LRRC37A3's level | lines that do not express PPP1R1C (13) vs lines expressing it (37) | 1.31× lower at baseline in the lines without PPP1R1C | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, LINC01239, ADGRL4; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises LRRC37A3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CDK6-AS1]] | B | CDK6-AS1 activity raises LRRC37A3's level | lines that do not express CDK6-AS1 (6) vs lines expressing it (44) | 1.32× lower at baseline in the lines without CDK6-AS1 | 0.090 | ⚠ within organs, on part of the lines; also absent: PLS3, CDK6, UACA; maybe low, not absent |
| [[FAM66C]] | B | FAM66C activity raises LRRC37A3's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 1.34× lower at baseline in the lines without FAM66C | 0.092 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |
| [[PLS3-AS1]] | B | PLS3-AS1 activity raises LRRC37A3's level | lines that do not express PLS3-AS1 (10) vs lines expressing it (40) | 1.27× lower at baseline in the lines without PLS3-AS1 | 0.095 | ⚠ within organs, on part of the lines; also absent: COPZ2, CAV2, DNAI1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.815). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (6.0, 15.6); signed map (26.5, -9.3). **Vector** length 71.3, 11.2% of its response variance represented; |z| ≥ 3 in 1,036 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +14.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +15.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +9.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.5 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +8.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +4.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -5.1 | -5.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -4.5 | -5.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -2.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -2.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -1.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.2 | -1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.1 | -3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.0 | -1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 37 member A3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q24.1 — chr17:64,854,130-64,919,480 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ34306, KIAA0563 |
| Matched by | ensembl_id |

UniProt [O60309](https://www.uniprot.org/uniprotkb/O60309) carries no function annotation.

**Summary**, from NCBI Gene [374819](https://www.ncbi.nlm.nih.gov/gene/374819):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:32427](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32427) · Entrez [374819](https://www.ncbi.nlm.nih.gov/gene/374819) · UniProt [O60309](https://www.uniprot.org/uniprotkb/O60309) · Ensembl [ENSG00000176809](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176809)

## Data

Gene col 10752: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10752); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10752, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10752]; `tensor/DDL_lfc|DDL_z.npy` [10752]; `embed/gene_vectors.npy` [10752]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10752 or target_col == 10752). Every well: [[LRRC37A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC37A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
