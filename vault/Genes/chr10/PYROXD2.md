---
symbol: "PYROXD2"
type: "gene"
col: 4140
ensembl_id: "ENSG00000119943"
name: "pyridine nucleotide-disulphide oxidoreductase domain 2"
location: "10q24.2"
module: 53
arm: "+"
pooled_cpm: 11.22
n_lines_expressing: 43
n_dd_up: 2
n_dd_down: 17
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 15
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# PYROXD2

*pyridine nucleotide-disulphide oxidoreductase domain 2* — 10q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.44× (z +4.2, q 0.011, up in 14 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 3.21×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.404× (z -10.3, q 3e-22, down in 29 of 41 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.254× (z -8.2, q 5e-14, down in 30 of 37 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPR2]] (+0.57, fdr 1e-05), [[ITGA9]] (+0.56, fdr 1e-05), [[CD96]] (+0.53, fdr 1e-04); moves opposite to [[KIF2A]] (-0.44, fdr 1e-04), [[GTF2E2]] (-0.44, fdr 6e-04), [[NHP2]] (-0.43, fdr 2e-04).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NYAP2]] → it (grade B ⚠); 15 go from it, the strongest it → [[PKD1L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4140.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 3.21×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +4.2 | 0.011 | 14/40 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.29×** | +4.1 | 0.011 | 15/40 (AsPC-1, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.34× | +3.4 | 0.13 | 9/37 (SK-MEL-2, H4, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.22× | +3.2 | 0.17 | 6/41 (SW1417, HepG2/C3A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4140.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.404×** | -10.3 | 3e-22 | 29/41 (HOP62, C32, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.412×** | -10.1 | 1e-21 | 26/33 (LS 180, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.254×** | -8.2 | 5e-14 | 30/37 (LoVo, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.500×** | -7.9 | 4e-13 | 27/40 (C32, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.537×** | -7.1 | 2e-10 | 24/39 (HOP62, BT-474, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.520×** | -6.9 | 4e-10 | 22/38 (NCI-H1792, AsPC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.546×** | -6.9 | 5e-10 | 22/39 (NCI-H1573, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.572×** | -6.4 | 1e-08 | 23/41 (C32, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.554×** | -6.3 | 3e-08 | 25/34 (NCI-H1792, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.596×** | -5.9 | 2e-07 | 21/41 (C32, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.391×** | -5.6 | 1e-06 | 19/35 (Panc 03.27, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.615×** | -5.5 | 1e-06 | 20/38 (Hs 766T, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.634×** | -5.2 | 9e-06 | 19/39 (C32, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.652×** | -4.6 | 2e-04 | 16/38 (C32, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.693×** | -4.2 | 0.001 | 17/40 (Hs 766T, C32, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.704×** | -4.0 | 0.002 | 17/35 (HT-29, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.816×** | -3.3 | 0.037 | 11/39 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4140. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 77.1 | 0 | 25 (10 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0696× (z -16.0) |
| [[HOP62 (line)]] | alt | 19.7 | 0 | 6 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.147× (z -12.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LOX-IMVI (line)]] | wt | 12.7 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H1792 (line)]] | alt | 12.5 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0400× (z -14.6) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[Hs 766T (line)]] | wt | 30.9 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.165× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.245× (z -8.6) |
| [[LoVo (line)]] | wt | 16.3 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.239× (z -9.4) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A498 (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 8.47 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 9.12 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0788× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[COLO 205 (line)]] | alt | 5.40 | 0 | 1 (1 ⚠) | — | [[Glasdegib (drug)]] 0.05 µM 0.0544× (z -9.2) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 13.2 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.163× (z -9.3) |
| [[LS 180 (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0528× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H1573 (line)]] | alt | 9.37 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.108× (z -10.2) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H460 (line)]] | wt | 7.56 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 9.24 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -8.5) ⚠ cell-cycle shift, explains ~84% of this change |
| [[SNU-423 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.113× (z -10.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW480 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -9.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4140), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPR2]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ITGA9]] | +0.56 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[CD96]] | +0.53 | +0.41 / +0.35 | both halves | 1e-04 |  |
| [[LINC01762]] | +0.52 | +0.46 / +0.38 | both halves | 7e-05 |  |
| [[LRP2BP]] | +0.51 | +0.45 / +0.39 | both halves | 5e-05 |  |
| [[C2CD6]] | +0.50 | +0.39 / +0.40 | both halves | 5e-05 |  |
| [[TAS2R4]] | +0.49 | +0.45 / +0.40 | both halves | 5e-05 |  |
| [[LOXL4]] | +0.49 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[CFAP53]] | +0.49 | +0.39 / +0.40 | both halves | 6e-05 |  |
| [[LINC02955]] | +0.49 | +0.43 / +0.26 | both halves | 3e-04 |  |
| [[LINC01135]] | +0.49 | +0.53 / +0.30 | both halves | 2e-04 |  |
| [[LINC02343]] | +0.48 | +0.47 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF2A]] | -0.44 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[GTF2E2]] | -0.44 | -0.36 / -0.22 | both halves | 6e-04 |  |
| [[NHP2]] | -0.43 | -0.29 / -0.33 | both halves | 2e-04 |  |
| [[PIP4K2A]] | -0.42 | -0.47 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[UBE2G1]] | -0.42 | -0.35 / -0.31 | both halves | 2e-04 |  |
| [[TMEM256]] | -0.42 | -0.25 / -0.25 | both halves | 4e-04 |  |
| [[GNA12]] | -0.42 | -0.39 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[DHTKD1]] | -0.42 | -0.24 / -0.29 | both halves | 4e-04 |  |
| [[USP42]] | -0.41 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[SCAMP1]] | -0.41 | -0.31 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NYAP2]] | B | NYAP2 activity raises PYROXD2's level | lines that do not express NYAP2 (16) vs lines expressing it (34) | 1.78× lower at baseline in the lines without NYAP2 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, CHSY3, AIM2; maybe low, not absent |
| [[LOXL4]] | B | LOXL4 activity raises PYROXD2's level | lines that do not express LOXL4 (30) vs lines expressing it (20) | 1.63× lower at baseline in the lines without LOXL4 | 0.073 | ⚠ within organs, on part of the lines; also absent: HSD17B2, BATF, TFF3 |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PKD1L1]] | B | PYROXD2 activity lowers PKD1L1's level | lines that do not express PYROXD2 (7) vs lines expressing it (43) | 1.86× higher at baseline in the lines without PYROXD2 | 0.009 | ⚠ within organs, on part of the lines; also absent: ATP1B1, SMARCA2, ZMIZ1; maybe low, not absent |
| [[SEPTIN7-DT]] | B | PYROXD2 activity lowers SEPTIN7-DT's level | lines that do not express PYROXD2 (7) vs lines expressing it (43) | 1.57× higher at baseline in the lines without PYROXD2 | 0.021 | ⚠ within organs, on part of the lines; also absent: ATP1B1, SMARCA2, ZMIZ1; maybe low, not absent |
| [[ST8SIA5]] | B | PYROXD2 activity lowers ST8SIA5's level | lines that do not express PYROXD2 (7) vs lines expressing it (43) | 1.79× higher at baseline in the lines without PYROXD2 | 0.042 | ⚠ within organs, on part of the lines; also absent: ATP1B1, SMARCA2, ZMIZ1; maybe low, not absent |
| cells under [[Pralsetinib (drug)]] 0.05 µM | B | PYROXD2 activity lowers the cells' numbers under Pralsetinib 0.05 µM (makes them more sensitive) | lines that do not express PYROXD2 (7) vs lines expressing it (41) | the lines without PYROXD2: 1.31× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: ATP1B1, SMARCA2, ZMIZ1; maybe low, not absent |
| [[YJEFN3]] | B | PYROXD2 activity lowers YJEFN3's level | lines that do not express PYROXD2 (7) vs lines expressing it (43) | 1.54× higher at baseline in the lines without PYROXD2 | 0.053 | ⚠ within organs, on part of the lines; also absent: ATP1B1, SMARCA2, ZMIZ1; maybe low, not absent |
| [[UBE2G1]] | B | PYROXD2 activity lowers UBE2G1's level | lines that do not express PYROXD2 (7) vs lines expressing it (43) | 1.56× higher at baseline in the lines without PYROXD2 | 0.054 | ⚠ within organs, on part of the lines; also absent: ATP1B1, SMARCA2, ZMIZ1; maybe low, not absent |
| [[GTF2IRD2]] | B | PYROXD2 activity raises GTF2IRD2's level | lines that do not express PYROXD2 (7) vs lines expressing it (43) | 1.79× lower at baseline in the lines without PYROXD2 | 0.057 | ⚠ within organs, on part of the lines; also absent: ATP1B1, SMARCA2, ZMIZ1; maybe low, not absent |
| cells under [[Harringtonine (drug)]] 0.5 µM | B | PYROXD2 activity raises the cells' numbers under Harringtonine 0.5 µM (protects the cells) | lines that do not express PYROXD2 (7) vs lines expressing it (41) | the lines without PYROXD2: 0.57× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: ATP1B1, SMARCA2, ZMIZ1; maybe low, not absent |
| cells under [[Lonafarnib (drug)]] 0.05 µM | B | PYROXD2 activity lowers the cells' numbers under Lonafarnib 0.05 µM (makes them more sensitive) | lines that do not express PYROXD2 (7) vs lines expressing it (41) | the lines without PYROXD2: 1.28× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: ATP1B1, SMARCA2, ZMIZ1; maybe low, not absent |
| cells under [[Cysteamine (hydrochloride) (drug)]] 5 µM | B | PYROXD2 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express PYROXD2 (7) vs lines expressing it (41) | the lines without PYROXD2: 0.87× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: ATP1B1, SMARCA2, ZMIZ1; maybe low, not absent |
| cells under [[vincristine (drug)]] 0.05 µM | B | PYROXD2 activity raises the cells' numbers under vincristine 0.05 µM (protects the cells) | lines that do not express PYROXD2 (7) vs lines expressing it (41) | the lines without PYROXD2: 0.77× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: ATP1B1, SMARCA2, ZMIZ1; maybe low, not absent |
| cells under [[Homoharringtonine (drug)]] 0.5 µM | B | PYROXD2 activity raises the cells' numbers under Homoharringtonine 0.5 µM (protects the cells) | lines that do not express PYROXD2 (7) vs lines expressing it (41) | the lines without PYROXD2: 0.34× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: ATP1B1, SMARCA2, ZMIZ1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.388). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.4, -9.1); signed map (21.7, 7.0). **Vector** length 64.8, 11.3% of its response variance represented; |z| ≥ 3 in 947 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.6 | -0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +1.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | +3.2 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.8 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.6 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +4.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.5 | -7.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.8 | -4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.6 | -5.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -2.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.2 | -6.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -5.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | +0.3 |
|  | [[Riluzole hydrochloride (drug)]] 0.05 µM |  | -1.0 | -0.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | pyridine nucleotide-disulphide oxidoreductase domain 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.2 — chr10:98,383,565-98,415,182 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23849; previously C10orf33 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Oxidoreductases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N2H3](https://www.uniprot.org/uniprotkb/Q8N2H3) (Pyridine nucleotide-disulfide oxidoreductase domain-containing protein 2):

> Probable oxidoreductase that may play a role as regulator of mitochondrial function.

**Summary**, from NCBI Gene [84795](https://www.ncbi.nlm.nih.gov/gene/84795):

> Predicted to enable oxidoreductase activity. Involved in mitochondrion organization. Located in mitochondrial matrix. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23517](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23517) · Entrez [84795](https://www.ncbi.nlm.nih.gov/gene/84795) · UniProt [Q8N2H3](https://www.uniprot.org/uniprotkb/Q8N2H3) · Ensembl [ENSG00000119943](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119943)

## Data

Gene col 4140: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4140); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4140, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4140]; `tensor/DDL_lfc|DDL_z.npy` [4140]; `embed/gene_vectors.npy` [4140]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4140 or target_col == 4140). Every well: [[PYROXD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PYROXD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
