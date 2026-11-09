---
symbol: "HDAC7"
type: "gene"
col: 698
ensembl_id: "ENSG00000061273"
name: "histone deacetylase 7"
location: "12q13.11"
module: 127
arm: "+"
pooled_cpm: 41.6
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 24
n_dd_up_clean: 5
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# HDAC7

*histone deacetylase 7* — 12q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 1.59× (z +4.2, q 0.012, up in 23 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.186× (z -26.0, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNMT3A]] (+0.60, fdr 1e-05), [[PKN3]] (+0.57, fdr 1e-05), [[PHF2]] (+0.56, fdr 1e-05); moves opposite to [[ENPP4]] (-0.54, fdr 4e-05), [[ECHS1]] (-0.53, fdr 1e-04), [[GCOM1]] (-0.50, fdr 1e-04).
> It is in [[Module 127]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ARHGEF17]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 698.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.59×** | +4.2 | 0.012 | 23/47 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.32×** | +4.1 | 0.012 | 21/47 (C32, NCI-H2347, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.51×** | +3.8 | 0.028 | 19/48 (MIA PaCa-2, HOP62, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.52×** | +3.4 | 0.097 | 11/44 (LS 180, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.098 | 14/47 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.43× | +3.2 | 0.11 | 13/48 (BT-474, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 698.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.186×** | -26.0 | 0e+00 | 48/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.186×** | -25.9 | 0e+00 | 47/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.250×** | -21.4 | 0e+00 | 47/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.491×** | -11.0 | 8e-26 | 43/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.638×** | -9.8 | 1e-20 | 29/48 (Hs 766T, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.643×** | -9.6 | 7e-20 | 39/48 (SNU-1, C32, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.550×** | -9.2 | 3e-18 | 36/48 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.538×** | -9.2 | 3e-18 | 38/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.427×** | -6.9 | 4e-10 | 36/49 (LOX-IMVI, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.440×** | -6.6 | 2e-09 | 34/48 (SW1417, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.667×** | -6.2 | 2e-08 | 36/48 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.764×** | -5.8 | 3e-07 | 32/48 (C32, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.722×** | -5.0 | 2e-05 | 23/48 (C-33 A, SW1417, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.727×** | -4.9 | 4e-05 | 26/48 (SNU-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.758×** | -4.3 | 8e-04 | 23/48 (PANC-1, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.606×** | -4.0 | 0.002 | 25/47 (SNU-1, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 698. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 129 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0690× (z -27.5) |
| [[NCI-H460 (line)]] | wt | 41.7 | 0 | 8 | — | [[Panobinostat (drug)]] 0.5 µM 0.126× (z -20.6) |
| [[C32 (line)]] | wt | 78.3 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0974× (z -17.7) |
| [[AsPC-1 (line)]] | alt | 34.9 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.101× (z -17.3) |
| [[HEC-1-A (line)]] | alt | 64.7 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.123× (z -21.5) |
| [[NCI-H2347 (line)]] | alt | 50.5 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -15.8) |
| [[SNU-1 (line)]] | wt | 55.9 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.101× (z -14.5) |
| [[A-172 (line)]] | wt | 52.5 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.188× (z -14.6) |
| [[J82 (line)]] | alt | 50.1 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -16.0) |
| [[LoVo (line)]] | wt | 27.9 | 2 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.201× (z -13.4) |
| [[Panc 03.27 (line)]] | alt | 85.2 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -16.2) |
| [[RKO (line)]] | wt | 55.2 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -15.7) |
| [[SW1417 (line)]] | alt | 35.4 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -16.3) |
| [[SW480 (line)]] | alt | 40.8 | 1 (1 ⚠) | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.130× (z -22.0) |
| [[C-33 A (line)]] | alt | 21.7 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0776× (z -13.6) |
| [[Hs 766T (line)]] | wt | 59.4 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -15.8) |
| [[HT-29 (line)]] | alt | 43.3 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.131× (z -16.2) |
| [[NCI-H1792 (line)]] | alt | 33.1 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.135× (z -13.5) |
| [[A498 (line)]] | wt | 37.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.177× (z -16.0) |
| [[A549 (line)]] | wt | 29.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.192× (z -12.5) |
| [[AN3 CA (line)]] | alt | 66.2 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.193× (z -8.6) |
| [[HOP62 (line)]] | alt | 34.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.166× (z -15.4) |
| [[HS-578T (line)]] | alt | 36.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0984× (z -17.9) |
| [[hTERT-HPNE (line)]] | wt | 40.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.118× (z -13.5) |
| [[KATO III (line)]] | alt | 37.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.137× (z -15.4) |
| [[LS 180 (line)]] | wt | 31.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -12.4) |
| [[MIA PaCa-2 (line)]] | alt | 22.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0789× (z -17.4) |
| [[NCI-H1573 (line)]] | alt | 25.9 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.168× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 35.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.338× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 29.6 | 1 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -11.8) |
| [[PANC-1 (line)]] | alt | 50.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -17.3) |
| [[SW 900 (line)]] | alt | 40.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -15.1) |
| [[H4 (line)]] | wt | 45.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.146× (z -12.4) |
| [[SHP-77 (line)]] | alt | 20.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.196× (z -8.7) |
| [[BT-474 (line)]] | alt | 31.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0947× (z -16.1) |
| [[CFPAC-1 (line)]] | alt | 36.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.267× (z -9.6) |
| [[HCT15 (line)]] | alt | 38.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.205× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 31.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.195× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 20.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.155× (z -10.4) |
| [[SNU-423 (line)]] | alt | 21.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -9.1) |
| [[SW 1271 (line)]] | alt | 38.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0250× (z -11.2) |
| [[SW48 (line)]] | wt | 23.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -9.4) |
| [[A-427 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 698), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNMT3A]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 | pathway: SUMO E3 ligases SUMOylate target proteins; STRING 431 |
| [[PKN3]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[PHF2]] | +0.56 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[RAB4B]] | +0.55 | +0.37 / +0.56 | both halves | 7e-05 |  |
| [[RAB11FIP3]] | +0.55 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[AKAP8L]] | +0.55 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[ALYREF]] | +0.54 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[PPP1R26-AS1]] | +0.54 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[FBXL18]] | +0.54 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[BCL7A]] | +0.53 | +0.35 / +0.61 | both halves | 1e-04 |  |
| [[NACC2]] | +0.53 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[SEMA4C]] | +0.53 | +0.50 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENPP4]] | -0.54 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[ECHS1]] | -0.53 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[GCOM1]] | -0.50 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[CLCN3]] | -0.49 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[LZTFL1]] | -0.48 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[PRELID3B]] | -0.47 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[COMMD8]] | -0.47 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[PHF6]] | -0.46 | -0.20 / -0.54 | both halves | 7e-04 |  |
| [[ABLIM1]] | -0.46 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[STYX]] | -0.45 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[ZBTB41]] | -0.45 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[LIN7C]] | -0.45 | -0.29 / -0.56 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGEF17]] | C | ARHGEF17 activity raises HDAC7's level | lines that do not express ARHGEF17 (4) vs lines expressing it (46) | 1.51× lower at baseline in the lines without ARHGEF17 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RGS10; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction -0.222). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.4, 11.8); signed map (6.1, -2.7). **Vector** length 96.9, 26.2% of its response variance represented; |z| ≥ 3 in 961 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +10.0 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +1.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | -9.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.9 | +4.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.6 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +0.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.9 | +3.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.9 | +2.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.0 | -3.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.5 | -4.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.4 | -9.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -6.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.9 | -1.8 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.5 | -4.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.2 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | histone deacetylase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.11 — chr12:47,782,722-47,833,132 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP586J0917; previously HDAC7A |
| Gene groups (HGNC) | Histone deacetylases, class IIA; NCoR/SMRT transcriptional repression complex subunits |
| Reactome | 21 pathways, smallest: Notch-HLH transcription pathway; NOTCH signaling regulates gene expression in endothelial stalk cells; NOTCH1 Intracellular Domain Regulates Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUI4](https://www.uniprot.org/uniprotkb/Q8WUI4) (Histone deacetylase 7):

> Responsible for the deacetylation of lysine residues on the N-terminal part of the core histones (H2A, H2B, H3 and H4) (By similarity). Histone deacetylation gives a tag for epigenetic repression and plays an important role in transcriptional regulation, cell cycle progression and developmental events (By similarity). Histone deacetylases act via the formation of large multiprotein complexes (By similarity). Involved in muscle maturation by repressing transcription of myocyte enhancer factors …

**Summary**, from NCBI Gene [51564](https://www.ncbi.nlm.nih.gov/gene/51564):

> Histones play a critical role in transcriptional regulation, cell cycle progression, and developmental events. Histone acetylation/deacetylation alters chromosome structure and affects transcription factor access to DNA. The protein encoded by this gene has sequence homology to members of the histone deacetylase family. This gene is orthologous to mouse HDAC7 gene whose protein promotes repression mediated via the transcriptional corepressor SMRT. Alternatively spliced transcript variants …

**Accessions** — [HGNC:14067](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14067) · Entrez [51564](https://www.ncbi.nlm.nih.gov/gene/51564) · UniProt [Q8WUI4](https://www.uniprot.org/uniprotkb/Q8WUI4) · Ensembl [ENSG00000061273](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000061273)

## Data

Gene col 698: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 698); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 698, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 698]; `tensor/DDL_lfc|DDL_z.npy` [698]; `embed/gene_vectors.npy` [698]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 698 or target_col == 698). Every well: [[HDAC7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HDAC7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
