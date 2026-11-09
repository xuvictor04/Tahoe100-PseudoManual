---
symbol: "SCART1"
type: "gene"
col: 13192
ensembl_id: "ENSG00000214279"
name: "scavenger receptor family member expressed on T cells 1"
location: "10q26.3"
module: 94
arm: "+"
pooled_cpm: 14.25
n_lines_expressing: 47
n_dd_up: 6
n_dd_down: 23
n_dd_up_clean: 6
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# SCART1

*scavenger receptor family member expressed on T cells 1* — 10q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 3.33× (z +12.3, q 6e-32, up in 42 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.509× (z -9.8, q 9e-20, down in 36 of 44 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYP2E1]] (+0.92, fdr 7e-06, ⚠ same locus), [[GNB1L]] (+0.63, fdr 1e-05), [[LINC02885]] (+0.57, fdr 3e-05), [[UCKL1-AS1]] (+0.55, fdr 1e-05); moves opposite to [[SLC16A14]] (-0.67, fdr 1e-05), [[ZNF442]] (-0.64, fdr 2e-05), [[ZNF433]] (-0.61, fdr 3e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 6 go from it, the strongest it → [[AHRR]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13192.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.33×** | +12.3 | 6e-32 | 42/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.35×** | +8.7 | 6e-16 | 36/44 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +7.2 | 1e-10 | 34/45 (A498, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.98×** | +7.0 | 4e-10 | 31/44 (SW480, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +3.6 | 0.043 | 21/44 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.100 | 15/43 (A-427, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[GSK1059615 (drug)]] 5 µM |  | 1.82× | +3.2 | 0.11 | 8/43 (A-427, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ivermectin (drug)]] 0.5 µM |  | 1.35× | +3.1 | 0.14 | 10/43 (HT-29, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13192.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.509×** | -9.8 | 9e-20 | 36/44 (HEC-1-A, COLO 205, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.390×** | -9.6 | 2e-19 | 40/44 (RPMI-7951, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.571×** | -8.1 | 1e-13 | 31/43 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.439×** | -7.8 | 6e-13 | 30/43 (hTERT-HPNE, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.479×** | -7.0 | 2e-10 | 30/38 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.520×** | -6.7 | 2e-09 | 32/43 (RPMI-7951, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.533×** | -6.4 | 1e-08 | 33/43 (RPMI-7951, HEC-1-A, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.589×** | -5.4 | 4e-06 | 24/42 (SW1417, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.591×** | -5.4 | 5e-06 | 25/44 (KATO III, hTERT-HPNE, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.582×** | -5.2 | 1e-05 | 24/38 (LS 180, HCT15, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.614×** | -5.0 | 3e-05 | 25/44 (H4, HEC-1-A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.609×** | -4.7 | 1e-04 | 20/40 (hTERT-HPNE, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.452×** | -4.2 | 1e-03 | 22/43 (SNU-1, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.653×** | -4.1 | 0.002 | 22/41 (CFPAC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.777×** | -3.6 | 0.010 | 17/45 (HEC-1-A, BT-474, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.709×** | -3.5 | 0.015 | 19/43 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.794×** | -3.3 | 0.026 | 14/44 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.803×** | -3.2 | 0.043 | 17/44 (RKO, AN3 CA, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **0.742×** | -3.0 | 0.060 | 6/43 (HS-578T, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13192. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 32.9 | 0 | 7 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0942× (z -10.8) |
| [[SW480 (line)]] | alt | 30.2 | 2 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.11× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -11.8) |
| [[LS 180 (line)]] | wt | 21.6 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.13× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.0673× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 11.6 | 0 | 4 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0583× (z -11.0) |
| [[KATO III (line)]] | alt | 14.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -11.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 16.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -12.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.126× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 23.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -13.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -8.6) |
| [[COLO 205 (line)]] | alt | 25.1 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0623× (z -13.4) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.246× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 20.4 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.266× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 23.8 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.90× (z +9.8) | [[Digitoxin (drug)]] 5 µM 0.213× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[RKO (line)]] | wt | 30.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.159× (z -9.7) |
| [[SW1417 (line)]] | alt | 10.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0607× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.102× (z -9.9) |
| [[HS-578T (line)]] | alt | 7.53 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0840× (z -9.6) |
| [[HT-29 (line)]] | alt | 10.9 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0623× (z -9.1) |
| [[LoVo (line)]] | wt | 8.61 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.268× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 5.98 | 0 | 1 | — | [[Orlistat (drug)]] 0.5 µM 0.0714× (z -9.8) |
| [[SHP-77 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[SNU-423 (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13192), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*29 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYP2E1]] | +0.92 | +0.89 / +0.90 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[GNB1L]] | +0.63 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[LINC02885]] | +0.57 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[UCKL1-AS1]] | +0.55 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[SND1]] | +0.55 | +0.33 / +0.49 | both halves | 1e-04 |  |
| [[SYS1-DBNDD2]] | +0.53 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[EP400P1]] | +0.53 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[RBM44]] | +0.53 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[CADM4]] | +0.53 | +0.34 / +0.38 | both halves | 1e-04 |  |
| [[CPLX1]] | +0.53 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[TGM2]] | +0.53 | +0.47 / +0.32 | both halves | 2e-04 |  |
| [[AHRR]] | +0.53 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[SMC5]] | +0.52 | +0.42 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*71 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC16A14]] | -0.67 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[ZNF442]] | -0.64 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[ZNF433]] | -0.61 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[ZNF563]] | -0.59 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[ZNF85]] | -0.59 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[C7orf31]] | -0.59 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[ZNF391]] | -0.58 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[TSTD3]] | -0.58 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[PHYH]] | -0.58 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[ATP6V0D1-DT]] | -0.56 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[RWDD3]] | -0.56 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[KLHL42]] | -0.55 | -0.42 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SCART1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers SCART1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[AHRR]] | C | AHRR activity raises SCART1's level | lines that do not express AHRR (3) vs lines expressing it (47) | 3.13× lower at baseline in the lines without AHRR | 0.035 | ⚠ few lines (3 vs 47); across organs; also absent: ZFP36, CYP2E1, BIVM; maybe low, not absent; co-absent with the target |
| [[RBM44]] | C | RBM44 activity raises SCART1's level | lines that do not express RBM44 (3) vs lines expressing it (47) | 2.78× lower at baseline in the lines without RBM44 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LINC02133, LYG1, SYCP2L; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AHRR]] | C | [[CYP2E1]], SCART1 activity raises AHRR's level | lines that do not express CYP2E1, SCART1 (3) vs lines expressing them (47) | 3.53× lower at baseline in the lines without CYP2E1, SCART1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AHRR, ARHGAP15, FAT1; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[RBM44]] | C | [[CYP2E1]], SCART1 activity raises RBM44's level | lines that do not express CYP2E1, SCART1 (3) vs lines expressing them (47) | 2.93× lower at baseline in the lines without CYP2E1, SCART1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AHRR, ARHGAP15, FAT1; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[UCKL1-AS1]] | C | [[CYP2E1]], SCART1 activity raises UCKL1-AS1's level | lines that do not express CYP2E1, SCART1 (3) vs lines expressing them (47) | 2.13× lower at baseline in the lines without CYP2E1, SCART1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AHRR, ARHGAP15, FAT1; maybe low, not absent; its own permutation p; co-absent genes |
| [[PIBF1]] | C | SCART1 activity raises PIBF1's level | lines that do not express SCART1 (3) vs lines expressing it (47) | 1.61× lower at baseline in the lines without SCART1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: AHRR, ARHGAP15, FAT1; maybe low, not absent; its own permutation p |
| [[TPCN2]] | C | [[CYP2E1]], SCART1 activity raises TPCN2's level | lines that do not express CYP2E1, SCART1 (3) vs lines expressing them (47) | 1.85× lower at baseline in the lines without CYP2E1, SCART1 | 0.084 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AHRR, ARHGAP15, FAT1; maybe low, not absent; co-absent genes |
| [[IDNK]] | C | SCART1 activity lowers IDNK's level | lines that do not express SCART1 (3) vs lines expressing it (47) | 1.34× higher at baseline in the lines without SCART1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: AHRR, ARHGAP15, FAT1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction -0.669). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.7, 22.9); signed map (7.7, 9.4). **Vector** length 88.7, 19.5% of its response variance represented; |z| ≥ 3 in 1,199 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +5.6 | +12.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.1 | +8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +7.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.8 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +0.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +0.2 |
|  | [[EX229 (drug)]] 5 µM |  | +1.5 | +1.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.4 | +0.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.6 | -9.8 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.3 | -3.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.2 | -7.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -8.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.8 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -5.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.6 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | scavenger receptor family member expressed on T cells 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.3 — chr10:133,453,928-133,523,558 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD163c-alpha |
| Gene groups (HGNC) | Scavenger receptor cysteine rich domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4G0T1](https://www.uniprot.org/uniprotkb/Q4G0T1) (Scavenger receptor cysteine-rich domain-containing protein SCART1):

> May play a role in the immune system, perhaps as a co-receptor on alphabeta and gammadelta T-cells.

**Summary**, from NCBI Gene [619207](https://www.ncbi.nlm.nih.gov/gene/619207):

> Predicted to enable scavenger receptor activity. Predicted to be involved in gamma-delta T cell lineage commitment. Located in brush border and cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:32411](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32411) · Entrez [619207](https://www.ncbi.nlm.nih.gov/gene/619207) · UniProt [Q4G0T1](https://www.uniprot.org/uniprotkb/Q4G0T1) · Ensembl [ENSG00000214279](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214279)

## Data

Gene col 13192: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13192); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13192, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13192]; `tensor/DDL_lfc|DDL_z.npy` [13192]; `embed/gene_vectors.npy` [13192]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13192 or target_col == 13192). Every well: [[SCART1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCART1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
