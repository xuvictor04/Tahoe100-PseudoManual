---
symbol: "PTP4A3"
type: "gene"
col: 11544
ensembl_id: "ENSG00000184489"
name: "protein tyrosine phosphatase 4A3"
location: "8q24.3"
module: 14
arm: "+"
pooled_cpm: 3.93
n_lines_expressing: 43
n_dd_up: 2
n_dd_down: 12
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 6
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# PTP4A3

*protein tyrosine phosphatase 4A3* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.05× (z +6.5, q 4e-08, up in 1 of 6 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 7.58×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (BT-474 6.19×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.535× (z -5.9, q 2e-06, down in 19 of 39 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.601× (z -4.8, q 4e-04, down in 16 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC12A7]] (+0.63, fdr 1e-05), [[PRRC2A]] (+0.61, fdr 1e-05), [[IDUA]] (+0.59, fdr 1e-05); moves opposite to [[RAB2A]] (-0.58, fdr 2e-05), [[ACTR6]] (-0.56, fdr 3e-05), [[KLHL7]] (-0.55, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CBFA2T3]] → it (grade B ⚠); 6 go from it, the strongest it → [[UQCC2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11544.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 7.58×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (BT-474 6.19×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +6.5 | 4e-08 | 1/6 (NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +5.1 | 1e-04 | 2/8 (A498, HOP62) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Demeclocycline (drug)]] 5 µM |  | 1.25× | +3.0 | 0.48 | 4/38 (PANC-1, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11544.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.535×** | -5.9 | 2e-06 | 19/39 (HT-29, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.601×** | -4.8 | 4e-04 | 16/38 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.614×** | -4.6 | 7e-04 | 16/36 (PANC-1, SW480, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.617×** | -4.6 | 7e-04 | 16/35 (NCI-H23, LoVo, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.658×** | -4.0 | 0.008 | 14/36 (CHP-212, J82, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.662×** | -3.9 | 0.009 | 13/27 (SHP-77, HOP62, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.659×** | -3.7 | 0.016 | 17/33 (A498, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.699×** | -3.4 | 0.047 | 13/39 (A-427, NCI-H23, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.778×** | -3.4 | 0.047 | 10/39 (Hs 766T, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Vilanterol (drug)]] 5 µM |  | **0.779×** | -3.3 | 0.047 | 11/38 (SK-MEL-2, J82, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.708×** | -3.3 | 0.056 | 13/37 (SW480, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.703×** | -3.2 | 0.062 | 9/37 (SHP-77, SW48, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.726× | -3.0 | 0.10 | 11/39 (SHP-77, NCI-H23, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11544. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.16 | 1 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 7.58× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.130× (z -11.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 22.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.123× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[A-427 (line)]] | wt | 5.79 | 0 | 1 | — | [[Bentamapimod (drug)]] 0.05 µM 0.0806× (z -9.3) |
| [[BT-474 (line)]] | alt | 8.76 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 6.81 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -12.6) ⚠ cell-cycle shift, explains ~7% of this change |
| [[NCI-H23 (line)]] | alt | 7.70 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.126× (z -8.6) |
| [[SW 900 (line)]] | alt | 5.54 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0763× (z -8.5) |
| [[A-172 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.753 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.885 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.950 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.907 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.516 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.883 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.482 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11544), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC12A7]] | +0.63 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[PRRC2A]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[IDUA]] | +0.59 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[BAHCC1]] | +0.59 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[POGLUT1]] | +0.57 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[H6PD]] | +0.56 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[ANO9]] | +0.56 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[TMEM147-AS1]] | +0.55 | +0.56 / +0.39 | both halves | 6e-05 |  |
| [[NUP188]] | +0.55 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[ZNF641]] | +0.55 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[VARS1]] | +0.55 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[TKFC]] | +0.54 | +0.57 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB2A]] | -0.58 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[ACTR6]] | -0.56 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[KLHL7]] | -0.55 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[EMC3]] | -0.55 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[MED31]] | -0.53 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[ZNHIT1]] | -0.53 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[KLHDC10]] | -0.51 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[COPB1]] | -0.51 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[MACO1]] | -0.51 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[PPP1R12B]] | -0.49 | -0.50 / -0.36 | both halves | 9e-05 |  |
| [[MGST3]] | -0.49 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[SBNO1]] | -0.49 | -0.39 / -0.46 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CBFA2T3]] | B | CBFA2T3 activity raises PTP4A3's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 1.77× lower at baseline in the lines without CBFA2T3 | 0.041 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A |
| [[ADGRB1]] | B | ADGRB1 activity raises PTP4A3's level | lines that do not express ADGRB1 (18) vs lines expressing it (32) | 1.73× lower at baseline in the lines without ADGRB1 | 0.074 | ⚠ within organs, on part of the lines; also absent: KSR2, BEGAIN, B4GALNT4; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UQCC2]] | B | PTP4A3 activity raises UQCC2's level | lines that do not express PTP4A3 (7) vs lines expressing it (43) | 1.48× lower at baseline in the lines without PTP4A3 | 0.035 | ⚠ within organs, on part of the lines; also absent: RHOF, RHPN1, JAG2; maybe low, not absent |
| [[CHAMP1]] | B | PTP4A3 activity raises CHAMP1's level | lines that do not express PTP4A3 (7) vs lines expressing it (43) | 1.72× lower at baseline in the lines without PTP4A3 | 0.046 | ⚠ within organs, on part of the lines; also absent: RHOF, RHPN1, JAG2; maybe low, not absent |
| [[SAMD10]] | B | PTP4A3 activity raises SAMD10's level | lines that do not express PTP4A3 (7) vs lines expressing it (43) | 1.68× lower at baseline in the lines without PTP4A3 | 0.065 | ⚠ within organs, on part of the lines; also absent: RHOF, RHPN1, JAG2; maybe low, not absent |
| [[SLC5A6]] | B | PTP4A3 activity raises SLC5A6's level | lines that do not express PTP4A3 (7) vs lines expressing it (43) | 1.82× lower at baseline in the lines without PTP4A3 | 0.069 | ⚠ within organs, on part of the lines; also absent: RHOF, RHPN1, JAG2; maybe low, not absent |
| [[COPB1]] | B | PTP4A3 activity lowers COPB1's level | lines that do not express PTP4A3 (7) vs lines expressing it (43) | 1.43× higher at baseline in the lines without PTP4A3 | 0.084 | ⚠ within organs, on part of the lines; also absent: RHOF, RHPN1, JAG2; maybe low, not absent |
| [[UBR2]] | B | PTP4A3 activity lowers UBR2's level | lines that do not express PTP4A3 (7) vs lines expressing it (43) | 1.48× higher at baseline in the lines without PTP4A3 | 0.095 | ⚠ within organs, on part of the lines; also absent: RHOF, RHPN1, JAG2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.433). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-30.0, 23.9); signed map (18.3, -41.8). **Vector** length 52.8, 7.35% of its response variance represented; |z| ≥ 3 in 957 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.5 | -1.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.0 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +0.2 |
| fall | [[Selinexor (drug)]] 5 µM |  | -2.0 | -3.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -1.5 | -3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -1.5 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -4.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -0.9 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -4.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase 4A3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:141,391,995-141,432,454 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRL-3, PRL-R, PRL3 |
| Gene groups (HGNC) | Protein tyrosine phosphatase 4A family |
| Hallmark sets | MYOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [O75365](https://www.uniprot.org/uniprotkb/O75365) (Protein tyrosine phosphatase type IVA 3):

> Protein tyrosine phosphatase which stimulates progression from G1 into S phase during mitosis. Enhances cell proliferation, cell motility and invasive activity, and promotes cancer metastasis. May be involved in the progression of cardiac hypertrophy by inhibiting intracellular calcium mobilization in response to angiotensin II.

**Summary**, from NCBI Gene [11156](https://www.ncbi.nlm.nih.gov/gene/11156):

> This gene encodes a member of the protein-tyrosine phosphatase family. Protein tyrosine phosphatases are cell signaling molecules that play regulatory roles in a variety of cellular processes. Studies of this class of protein tyrosine phosphatase in mice demonstrates that they are prenylated in vivo, suggesting their association with cell plasma membrane. The encoded protein may enhance cell proliferation, and overexpression of this gene has been implicated in tumor metastasis. Alternative …

**Accessions** — [HGNC:9636](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9636) · Entrez [11156](https://www.ncbi.nlm.nih.gov/gene/11156) · UniProt [O75365](https://www.uniprot.org/uniprotkb/O75365) · Ensembl [ENSG00000184489](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184489)

## Data

Gene col 11544: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11544); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11544, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11544]; `tensor/DDL_lfc|DDL_z.npy` [11544]; `embed/gene_vectors.npy` [11544]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11544 or target_col == 11544). Every well: [[PTP4A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTP4A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
