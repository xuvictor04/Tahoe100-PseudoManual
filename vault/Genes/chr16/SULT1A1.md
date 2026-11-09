---
symbol: "SULT1A1"
type: "gene"
col: 12221
ensembl_id: "ENSG00000196502"
name: "sulfotransferase family 1A member 1"
location: "16p11.2"
module: 146
arm: "+"
pooled_cpm: 5.97
n_lines_expressing: 34
n_dd_up: 8
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# SULT1A1

*sulfotransferase family 1A member 1* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.23× (z +7.9, q 1e-12, up in 5 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 0.5 µM: 1.69× (z +5.1, q 5e-05, up in 16 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.251× (z -14.1, q 4e-42, down in 28 of 31 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGD3]] (+0.59, fdr 2e-05), [[GSTO2]] (+0.56, fdr 2e-05), [[C10orf95-AS1]] (+0.52, fdr 1e-05); moves opposite to [[CLIC1]] (-0.56, fdr 2e-05), [[RP2]] (-0.46, fdr 5e-05), [[CD59]] (-0.46, fdr 4e-05).
> It sits in the **+** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MANSC1]] → it (grade B ⚠); 3 go from it, the strongest it → [[LRRC61]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12221.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +7.9 | 1e-12 | 5/7 (A498, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.14×** | +7.8 | 1e-12 | 12/20 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.69×** | +5.1 | 5e-05 | 16/30 (LS 180, KATO III, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.57×** | +4.6 | 5e-04 | 15/30 (BT-474, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +3.6 | 0.042 | 6/15 (A498, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.065 | 5/31 (HepG2/C3A, BT-474, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +3.3 | 0.068 | 1/13 (SW480) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.24×** | +3.2 | 0.097 | 8/31 (AsPC-1, HepG2/C3A, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12221.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.251×** | -14.1 | 4e-42 | 28/31 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.388×** | -13.6 | 1e-39 | 24/27 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.336×** | -10.6 | 9e-24 | 25/30 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.432×** | -8.1 | 6e-14 | 21/29 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.455×** | -8.0 | 1e-13 | 20/27 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.445×** | -7.9 | 3e-13 | 19/28 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.492×** | -7.2 | 5e-11 | 20/27 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.604×** | -5.1 | 2e-05 | 13/29 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.402×** | -4.8 | 8e-05 | 13/26 (SW1417, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.427×** | -4.5 | 3e-04 | 15/28 (SW48, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.640×** | -4.5 | 3e-04 | 14/30 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.671×** | -4.0 | 0.003 | 13/30 (NCI-H460, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.711×** | -3.3 | 0.050 | 9/30 (SW48, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.740×** | -3.0 | 0.098 | 8/31 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.741×** | -3.0 | 0.098 | 11/31 (LoVo, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12221. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.98 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0749× (z -22.1) |
| [[SW480 (line)]] | alt | 9.77 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.159× (z -11.4) |
| [[A498 (line)]] | wt | 26.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 5.51 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 13.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0343× (z -15.4) |
| [[SW48 (line)]] | wt | 15.4 | 0 | 2 | — | [[TAK-901 (drug)]] 0.05 µM 0.0933× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 3.70 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 2.88 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0467× (z -13.7) |
| [[COLO 205 (line)]] | alt | 4.63 | 0 | 1 | — | [[Tazarotene (drug)]] 0.05 µM 0.0498× (z -8.6) |
| [[HT-29 (line)]] | alt | 4.88 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0448× (z -13.9) |
| [[J82 (line)]] | alt | 6.66 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -13.4) |
| [[KATO III (line)]] | alt | 5.44 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -8.9) |
| [[LoVo (line)]] | wt | 5.59 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0507× (z -12.5) ⚠ toxic; cell-cycle shift, explains ~24% of this change |
| [[NCI-H1573 (line)]] | alt | 5.81 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -11.3) |
| [[PANC-1 (line)]] | alt | 1.94 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0698× (z -9.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0280× (z -12.5) |
| [[A-172 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.632 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.746 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.580 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.874 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.774 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.749 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.516 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.893 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12221), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGD3]] | +0.59 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[GSTO2]] | +0.56 | +0.52 / +0.47 | both halves | 2e-05 | pathway: Biological oxidations |
| [[C10orf95-AS1]] | +0.52 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[MAP2K6]] | +0.49 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[PCBD1]] | +0.48 | +0.37 / +0.50 | both halves | 9e-05 |  |
| [[SLC5A4-AS1]] | +0.48 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[SEC14L4]] | +0.47 | +0.38 / +0.47 | both halves | 7e-05 |  |
| [[EPHX2]] | +0.47 | +0.50 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[ALDH5A1]] | +0.47 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[DNPH1]] | +0.47 | +0.40 / +0.46 | both halves | 4e-05 |  |
| [[PSMA1]] | +0.47 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[TTPA]] | +0.47 | +0.47 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLIC1]] | -0.56 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[RP2]] | -0.46 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[CD59]] | -0.46 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[VGF]] | -0.46 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[WNT9A]] | -0.45 | -0.42 / -0.37 | both halves | 9e-05 |  |
| [[UACA]] | -0.45 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[GPS2]] | -0.43 | -0.30 / -0.33 | both halves | 2e-04 |  |
| [[JOSD1]] | -0.43 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[PLEC]] | -0.41 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[EFCAB13]] | -0.41 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[PLXNA3]] | -0.41 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[PDLIM7]] | -0.41 | -0.45 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MANSC1]] | B | MANSC1 activity raises SULT1A1's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 1.86× lower at baseline in the lines without MANSC1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[LRRC61]] | B | LRRC61 activity raises SULT1A1's level | lines that do not express LRRC61 (16) vs lines expressing it (34) | 2.23× lower at baseline in the lines without LRRC61 | 0.039 | ⚠ within organs, on part of the lines; also absent: ACTR3C, ARHGEF5, ENPP4 |
| [[SLC27A2]] | B | SLC27A2 activity raises SULT1A1's level | lines that do not express SLC27A2 (19) vs lines expressing it (31) | 1.97× lower at baseline in the lines without SLC27A2 | 0.044 | ⚠ within organs, on part of the lines; also absent: ICA1, BTC, ENSG00000288656 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC61]] | B | SULT1A1 activity raises LRRC61's level | lines that do not express SULT1A1 (16) vs lines expressing it (34) | 2.37× lower at baseline in the lines without SULT1A1 | 0.081 | ⚠ within organs, on part of the lines; also absent: ARHGEF5, KRT18, MARVELD2 |
| [[SLC5A4-AS1]] | B | SULT1A1 activity raises SLC5A4-AS1's level | lines that do not express SULT1A1 (16) vs lines expressing it (34) | 1.68× lower at baseline in the lines without SULT1A1 | 0.081 | ⚠ within organs, on part of the lines; also absent: ARHGEF5, KRT18, MARVELD2 |
| [[TPD52L1]] | B | SULT1A1 activity raises TPD52L1's level | lines that do not express SULT1A1 (16) vs lines expressing it (34) | 2.35× lower at baseline in the lines without SULT1A1 | 0.095 | ⚠ within organs, on part of the lines; also absent: ARHGEF5, KRT18, MARVELD2 |

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **+** arm (projection on the module's main direction 0.471). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (25.7, -40.2); signed map (17.6, -48.3). **Vector** length 47.6, 8.47% of its response variance represented; |z| ≥ 3 in 606 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.0 | +3.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.9 | +0.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | -1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +3.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.4 | +5.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.3 | -0.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -14.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -10.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -0.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.6 | -4.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.0 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | sulfotransferase family 1A member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:28,605,196-28,610,044 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P-PST; previously STP, STP1 |
| Gene groups (HGNC) | Sulfotransferases, cytosolic |
| Hallmark sets | UV_RESPONSE_UP, ADIPOGENESIS |
| Reactome | 5 pathways, smallest: Cytosolic sulfonation of small molecules; Paracetamol ADME; Phase II - Conjugation of compounds |
| Matched by | ensembl_id |

**Function**, from UniProt [P50225](https://www.uniprot.org/uniprotkb/P50225) (Sulfotransferase 1A1):

> Sulfotransferase that utilizes 3'-phospho-5'-adenylyl sulfate (PAPS) as sulfonate donor to catalyze the sulfate conjugation of a wide variety of acceptor molecules bearing a hydroxyl or an amine group. Sulfonation increases the water solubility of most compounds, and therefore their renal excretion, but it can also result in bioactivation to form active metabolites. Displays broad substrate specificity for small phenolic compounds. Plays an important role in the sulfonation of endogenous …

**Summary**, from NCBI Gene [6817](https://www.ncbi.nlm.nih.gov/gene/6817):

> Sulfotransferase enzymes catalyze the sulfate conjugation of many hormones, neurotransmitters, drugs, and xenobiotic compounds. These cytosolic enzymes are different in their tissue distributions and substrate specificities. The gene structure (number and length of exons) is similar among family members. This gene encodes one of two phenol sulfotransferases with thermostable enzyme activity. Multiple alternatively spliced variants that encode two isoforms have been identified for this gene. …

**Accessions** — [HGNC:11453](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11453) · Entrez [6817](https://www.ncbi.nlm.nih.gov/gene/6817) · UniProt [P50225](https://www.uniprot.org/uniprotkb/P50225) · Ensembl [ENSG00000196502](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196502)

## Data

Gene col 12221: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12221); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12221, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12221]; `tensor/DDL_lfc|DDL_z.npy` [12221]; `embed/gene_vectors.npy` [12221]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12221 or target_col == 12221). Every well: [[SULT1A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SULT1A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
