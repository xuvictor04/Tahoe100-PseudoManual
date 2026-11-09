---
symbol: "NGFR"
type: "gene"
col: 742
ensembl_id: "ENSG00000064300"
name: "nerve growth factor receptor"
location: "17q21.33"
module: 94
arm: "+"
pooled_cpm: 9.61
n_lines_expressing: 31
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 22
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 14
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# NGFR

*nerve growth factor receptor* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 11.3× (z +25.9, q 0e+00, up in 29 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Berbamine (drug)]] 0.05 µM: 0.606× (z -4.2, q 0.015, down in 12 of 29 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.138×); [[Dinaciclib (drug)]] 5 µM in 1 line (AN3 CA 0.133×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Tofacitinib (citrate) (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0562×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP15]] (+0.72, fdr 7e-06), [[ARL4D]] (+0.67, fdr 7e-06), [[STK32A]] (+0.67, fdr 1e-05); moves opposite to [[TIMM23B-AGAP6]] (-0.55, fdr 3e-05), [[ANKMY1]] (-0.53, fdr 1e-04), [[HIRA]] (-0.51, fdr 1e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ITGA9-AS1]] → it (grade B ⚠); 14 go from it, the strongest it → [[ITGA9-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 2 with an alert ⚠; shown: the 15 strongest. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 742.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **11.3×** | +25.9 | 0e+00 | 29/29 (PANC-1, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **9.62×** | +24.1 | 0e+00 | 24/27 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **11.7×** | +20.5 | 0e+00 | 28/29 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **11.2×** | +20.1 | 0e+00 | 29/29 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **8.16×** | +16.8 | 0e+00 | 28/29 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **6.41×** | +15.5 | 0e+00 | 27/29 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.98×** | +15.3 | 0e+00 | 26/29 (SK-MEL-2, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.19×** | +15.2 | 0e+00 | 28/29 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **4.85×** | +13.2 | 1e-37 | 27/29 (PANC-1, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.48×** | +12.5 | 5e-34 | 22/27 (SW1417, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.35×** | +12.2 | 9e-33 | 25/29 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.57×** | +10.6 | 1e-24 | 27/29 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.39×** | +10.2 | 1e-22 | 26/29 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.35×** | +10.1 | 3e-22 | 23/29 (SK-MEL-2, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +7.1 | 4e-11 | 15/28 (A549, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 742.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.138×); [[Dinaciclib (drug)]] 5 µM in 1 line (AN3 CA 0.133×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Tofacitinib (citrate) (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0562×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Berbamine (drug)]] 0.05 µM |  | **0.606×** | -4.2 | 0.015 | 12/29 (A498, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.645×** | -3.7 | 0.067 | 11/29 (RPMI-7951, C32, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.742× | -3.4 | 0.15 | 12/29 (CFPAC-1, SW 1088, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.686× | -3.2 | 0.20 | 9/29 (C-33 A, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.689× | -3.1 | 0.20 | 12/27 (A-172, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 742. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 8.40 | 12 | 0 | [[Selinexor (drug)]] 5 µM 25.1× (z +18.7) | — |
| [[A549 (line)]] | wt | 4.75 | 9 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.7× (z +12.5) | — |
| [[A-427 (line)]] | wt | 10.00 | 7 | 0 | [[Selinexor (drug)]] 5 µM 12.0× (z +14.2) | — |
| [[HOP62 (line)]] | alt | 4.65 | 6 | 0 | [[Selinexor (drug)]] 5 µM 25.4× (z +13.7) | — |
| [[SK-MEL-2 (line)]] | alt | 21.4 | 6 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.28× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 5.04× (z +9.9) | — |
| [[A-172 (line)]] | wt | 11.9 | 5 | 0 | [[Selinexor (drug)]] 5 µM 16.7× (z +14.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 4.36 | 4 | 1 | [[Selinexor (drug)]] 5 µM 48.8× (z +12.1) | [[Tofacitinib (citrate) (drug)]] 0.05 µM 0.0562× (z -8.8) |
| [[SW 900 (line)]] | alt | 10.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.2× (z +13.9) | — |
| [[SW1417 (line)]] | alt | 74.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.39× (z +16.4) | — |
| [[Panc 03.27 (line)]] | alt | 33.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +16.4) | — |
| [[SW480 (line)]] | alt | 38.6 | 4 | 0 | [[Selinexor (drug)]] 0.05 µM 5.35× (z +12.2) | — |
| [[C-33 A (line)]] | alt | 8.84 | 3 | 0 | [[Selinexor (drug)]] 5 µM 20.5× (z +12.1) | — |
| [[RPMI-7951 (line)]] | alt | 14.8 | 3 | 0 | [[Selinexor (drug)]] 5 µM 11.8× (z +11.5) | — |
| [[SNU-423 (line)]] | alt | 14.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.15× (z +11.1) | — |
| [[AN3 CA (line)]] | alt | 79.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -9.4) |
| [[BT-474 (line)]] | alt | 15.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +10.8) | — |
| [[C32 (line)]] | wt | 9.72 | 2 | 0 | [[Selinexor (drug)]] 5 µM 11.6× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 5.26 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.96× (z +9.5) | — |
| [[HS-578T (line)]] | alt | 5.99 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 11.5× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 8.88 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +9.3) | — |
| [[CHP-212 (line)]] | wt | 25.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +9.3) | — |
| [[J82 (line)]] | alt | 6.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 13.2 | 1 | 0 | [[Selinexor (drug)]] 5 µM 7.35× (z +9.7) | — |
| [[A498 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.738 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.842 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.725 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.678 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.871 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.761 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 742), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP15]] | +0.72 | +0.59 / +0.80 | both halves | 7e-06 |  |
| [[ARL4D]] | +0.67 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[STK32A]] | +0.67 | +0.52 / +0.74 | both halves | 1e-05 |  |
| [[PCLO]] | +0.66 | +0.55 / +0.75 | both halves | 1e-05 |  |
| [[ZNF433]] | +0.64 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[TPPP]] | +0.64 | +0.50 / +0.76 | both halves | 1e-05 |  |
| [[TRPM4]] | +0.64 | +0.30 / +0.75 | both halves | 2e-04 |  |
| [[CAPN5]] | +0.62 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[SLC44A2]] | +0.61 | +0.31 / +0.71 | both halves | 2e-04 |  |
| [[SLC43A2]] | +0.59 | +0.48 / +0.78 | both halves | 2e-05 |  |
| [[TRAF4]] | +0.59 | +0.46 / +0.66 | both halves | 3e-05 | STRING 746 |
| [[RNF150]] | +0.58 | +0.39 / +0.68 | both halves | 6e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM23B-AGAP6]] | -0.55 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[ANKMY1]] | -0.53 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[HIRA]] | -0.51 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[GLYR1]] | -0.51 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[ZRANB3]] | -0.51 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[ARIH2]] | -0.50 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[MFSD14CP-1]] | -0.50 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[PGP]] | -0.50 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[AGAP6]] | -0.49 | -0.27 / -0.51 | both halves | 3e-04 |  |
| [[C2CD3]] | -0.49 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[PSMD1]] | -0.49 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[FARP2]] | -0.49 | -0.44 / -0.49 | both halves | 3e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA9-AS1]] | B | ITGA9-AS1 activity raises NGFR's level | lines that do not express ITGA9-AS1 (6) vs lines expressing it (44) | 2.54× lower at baseline in the lines without ITGA9-AS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: CTDSPL, SLC43A2; maybe low, not absent |
| [[DUSP15]] | C | DUSP15 activity raises NGFR's level | lines that do not express DUSP15 (15) vs lines expressing it (35) | 3.68× lower at baseline in the lines without DUSP15 | 0.052 | ⚠ within organs, on part of the lines; also absent: DLK2, ETNK2, C11orf96; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 11, C 3. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA9-AS1]] | B | NGFR activity raises ITGA9-AS1's level | lines that do not express NGFR (19) vs lines expressing it (31) | 1.06× lower at baseline in the lines without NGFR | 0.037 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, GNG11 |
| [[SLC44A2]] | B | NGFR activity raises SLC44A2's level | lines that do not express NGFR (19) vs lines expressing it (31) | 2.02× lower at baseline in the lines without NGFR | 0.041 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, GNG11 |
| [[NUDT16]] | B | NGFR activity raises NUDT16's level | lines that do not express NGFR (19) vs lines expressing it (31) | 1.24× lower at baseline in the lines without NGFR | 0.061 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, GNG11 |
| [[AMZ2P1-1]] | B | NGFR activity raises AMZ2P1-1's level | lines that do not express NGFR (19) vs lines expressing it (31) | 1.18× lower at baseline in the lines without NGFR | 0.065 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, GNG11 |
| [[ZNF442]] | B | NGFR activity raises ZNF442's level | lines that do not express NGFR (19) vs lines expressing it (31) | 1.66× lower at baseline in the lines without NGFR | 0.070 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, GNG11 |
| [[ZNF627]] | B | NGFR activity raises ZNF627's level | lines that do not express NGFR (19) vs lines expressing it (31) | 1.34× lower at baseline in the lines without NGFR | 0.071 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, GNG11 |
| [[SLC2A4RG]] | B | NGFR activity raises SLC2A4RG's level | lines that do not express NGFR (19) vs lines expressing it (31) | 1.52× lower at baseline in the lines without NGFR | 0.072 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, GNG11 |
| [[PCLO]] | B | NGFR activity raises PCLO's level | lines that do not express NGFR (19) vs lines expressing it (31) | 2.82× lower at baseline in the lines without NGFR | 0.073 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, GNG11 |
| [[ARL4D]] | B | NGFR activity raises ARL4D's level | lines that do not express NGFR (19) vs lines expressing it (31) | 1.92× lower at baseline in the lines without NGFR | 0.086 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, GNG11 |
| [[AMZ2P1]] | B | NGFR activity raises AMZ2P1's level | lines that do not express NGFR (19) vs lines expressing it (31) | 1.20× lower at baseline in the lines without NGFR | 0.088 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, GNG11 |
| [[ZNF433]] | B | NGFR activity raises ZNF433's level | lines that do not express NGFR (19) vs lines expressing it (31) | 2.02× lower at baseline in the lines without NGFR | 0.097 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, GNG11 |
| [[DUSP15]] | C | NGFR activity raises DUSP15's level | lines that do not express NGFR (19) vs lines expressing it (31) | 2.19× lower at baseline in the lines without NGFR | 0.004 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, GNG11; co-absent with the target |

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.680). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.7, 24.8); signed map (14.5, -16.2). **Vector** length 90.3, 24.1% of its response variance represented; |z| ≥ 3 in 859 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +11.0 | +25.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +8.3 | +20.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +15.3 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +6.6 | +20.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +10.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +4.2 | +13.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +6.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +2.5 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -3.3 | -3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -3.2 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | +0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.6 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.7 | -4.2 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | nerve growth factor receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:49,495,293-49,515,008 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TNFRSF16, CD271, p75NTR |
| Gene groups (HGNC) | CD molecules; Tumor necrosis factor receptor superfamily; MicroRNA protein coding host genes |
| Reactome | 16 pathways, smallest: Ceramide signalling; NFG and proNGF binds to p75NTR; Axonal growth stimulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P08138](https://www.uniprot.org/uniprotkb/P08138) (Tumor necrosis factor receptor superfamily member 16):

> Low affinity receptor which can bind to NGF, BDNF, NTF3, and NTF4. Forms a heterodimeric receptor with SORCS2 that binds the precursor forms of NGF, BDNF and NTF3 with high affinity, and has much lower affinity for mature NGF and BDNF. Plays an important role in differentiation and survival of specific neuronal populations during development (By similarity). Can mediate cell survival as well as cell death of neural cells. Plays a role in the inactivation of RHOA. Plays a role in the regulation …

**Summary**, from NCBI Gene [4804](https://www.ncbi.nlm.nih.gov/gene/4804):

> Nerve growth factor receptor contains an extracellular domain containing four 40-amino acid repeats with 6 cysteine residues at conserved positions followed by a serine/threonine-rich region, a single transmembrane domain, and a 155-amino acid cytoplasmic domain. The cysteine-rich region contains the nerve growth factor binding domain. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7809](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7809) · Entrez [4804](https://www.ncbi.nlm.nih.gov/gene/4804) · UniProt [P08138](https://www.uniprot.org/uniprotkb/P08138) · Ensembl [ENSG00000064300](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064300)

## Data

Gene col 742: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 742); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 742, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 742]; `tensor/DDL_lfc|DDL_z.npy` [742]; `embed/gene_vectors.npy` [742]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 742 or target_col == 742). Every well: [[NGFR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NGFR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
