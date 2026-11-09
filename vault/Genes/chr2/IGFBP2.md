---
symbol: "IGFBP2"
type: "gene"
col: 3677
ensembl_id: "ENSG00000115457"
name: "insulin like growth factor binding protein 2"
location: "2q35"
module: 58
arm: "+"
pooled_cpm: 21.19
n_lines_expressing: 34
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 8
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# IGFBP2

*insulin like growth factor binding protein 2* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.79× (z +10.0, q 8e-21, up in 21 of 23 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.66× (z +5.4, q 1e-05, up in 15 of 28 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SW 900 5.66×, A-172 5.58×, PANC-1 3.90×, NCI-H1573 5.64×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.436× (z -6.2, q 3e-07, down in 23 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NMU]] (+0.62, fdr 1e-05), [[RNF24]] (+0.61, fdr 1e-05), [[GCHFR]] (+0.61, fdr 1e-05); moves opposite to [[PSMC5]] (-0.61, fdr 2e-05), [[RNF6]] (-0.60, fdr 1e-05), [[FLII]] (-0.59, fdr 1e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MTOR]] → it (grade B ⚠); 8 go from it, the strongest it → [[IDE]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 9 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3677.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SW 900 5.66×, A-172 5.58×, PANC-1 3.90×, NCI-H1573 5.64×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **3.79×** | +10.0 | 8e-21 | 21/23 (SW 900, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **3.21×** | +8.4 | 1e-14 | 12/16 (HEC-1-A, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.43×** | +6.2 | 1e-07 | 13/19 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +5.4 | 1e-05 | 15/28 (BT-474, A-172, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +5.0 | 5e-05 | 18/32 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.85×** | +4.6 | 3e-04 | 24/30 (NCI-H1573, COLO 205, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~64% of this change | **1.66×** | +3.8 | 0.011 | 12/28 (PANC-1, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.7 | 0.013 | 14/25 (HCT15, KATO III, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.63×** | +3.5 | 0.026 | 12/28 (BT-474, SW 900, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.2 | 0.088 | 13/29 (A-427, SW48, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.52×** | +3.1 | 0.088 | 9/31 (NCI-H2030, NCI-H1573, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3677.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.436×** | -6.2 | 3e-07 | 23/27 (A-427, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.595×** | -5.5 | 1e-05 | 21/29 (SHP-77, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.566×** | -4.0 | 0.010 | 19/29 (SHP-77, NCI-H460, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.384×** | -3.8 | 0.025 | 18/31 (AN3 CA, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.411×** | -3.5 | 0.048 | 19/32 (SHP-77, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.412×** | -3.5 | 0.048 | 15/32 (LS 180, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.620×** | -3.3 | 0.066 | 16/30 (NCI-H460, SW1417, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.430×** | -3.3 | 0.066 | 18/32 (LS 180, C32, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.664× | -3.1 | 0.12 | 16/31 (CHP-212, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~25% here); position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.648× | -3.1 | 0.12 | 14/32 (BT-474, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3677. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 16.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -10.0) |
| [[SHP-77 (line)]] | alt | 412 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -16.5) |
| [[A-172 (line)]] | wt | 18.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.58× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[CHP-212 (line)]] | wt | 30.1 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0561× (z -10.0) |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -9.2) |
| [[LS 180 (line)]] | wt | 35.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 19.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.64× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[PANC-1 (line)]] | alt | 20.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[RKO (line)]] | wt | 10.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0728× (z -10.2) |
| [[SW 900 (line)]] | alt | 39.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SW480 (line)]] | alt | 18.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -8.6) |
| [[A498 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 137 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.25 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.63 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.19 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.68 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.78 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3677), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NMU]] | +0.62 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[RNF24]] | +0.61 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[GCHFR]] | +0.61 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[PTMAP2]] ⚠ | +0.60 | +0.49 / +0.54 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CLEC11A]] | +0.59 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[PTMA]] | +0.58 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[A2MP1]] | +0.58 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[PTMAP5]] | +0.58 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[TNNI3]] | +0.57 | +0.44 / +0.59 | both halves | 3e-05 | pathway: HALLMARK_KRAS_SIGNALING_DN |
| [[RFX2]] | +0.57 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[PRKD3]] | +0.56 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[METRN]] | +0.56 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[NDUFA2]] | +0.56 | +0.40 / +0.58 | both halves | 4e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMC5]] | -0.61 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[RNF6]] | -0.60 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[FLII]] | -0.59 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[SBDSP1-1]] | -0.59 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[SBDSP1]] | -0.58 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[CCT6P3]] | -0.58 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[PSMD6]] | -0.57 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[EIF5]] | -0.57 | -0.53 / -0.51 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[ACTR8]] | -0.56 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ZXDB]] | -0.56 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[PARP3]] | -0.56 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[ZNF621]] | -0.56 | -0.60 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity raises IGFBP2's level | compounds that target MTOR: 3 of 8 lower it (Bimiralisib, GSK1059615, Sapanisertib) | 38% of the class's compounds vs 2.0% of all compounds | 0.088 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IDE]] | B | IGFBP2 activity raises IDE's level | lines that do not express IGFBP2 (16) vs lines expressing it (34) | 1.77× lower at baseline in the lines without IGFBP2 | 0.008 | ⚠ within organs, on part of the lines; also absent: CBFA2T3, CHRNA7, FSTL4 |
| [[RNF6]] | B | IGFBP2 activity raises RNF6's level | lines that do not express IGFBP2 (16) vs lines expressing it (34) | 1.32× lower at baseline in the lines without IGFBP2 | 0.026 | ⚠ within organs, on part of the lines; also absent: CBFA2T3, CHRNA7, FSTL4 |
| [[EGLN3]] | B | IGFBP2 activity strengthens EGLN3's drug response | lines that do not express IGFBP2 (16) vs lines expressing it (33) | the lines without IGFBP2 respond 0.90× as strongly (z diff +1.18); strongest at Harringtonine 5 µM: 0.85x vs 0.49x (z diff +5.7) | 0.045 | ⚠ within organs, on part of the lines; also absent: CBFA2T3, CHRNA7, FSTL4; target measured in part of the lines; artifact flags |
| [[RHBDD3]] | B | IGFBP2 activity raises RHBDD3's level | lines that do not express IGFBP2 (16) vs lines expressing it (34) | 1.57× lower at baseline in the lines without IGFBP2 | 0.046 | ⚠ within organs, on part of the lines; also absent: CBFA2T3, CHRNA7, FSTL4 |
| [[JARID2]] | B | IGFBP2 activity lowers JARID2's level | lines that do not express IGFBP2 (16) vs lines expressing it (34) | 1.67× higher at baseline in the lines without IGFBP2 | 0.076 | ⚠ within organs, on part of the lines; also absent: CBFA2T3, CHRNA7, FSTL4 |
| cells under [[Rutin (trihydrate) (drug)]] 0.05 µM | B | IGFBP2 activity raises the cells' numbers under Rutin (trihydrate) 0.05 µM (protects the cells) | lines that do not express IGFBP2 (16) vs lines expressing it (32) | the lines without IGFBP2: 0.84× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: CBFA2T3, CHRNA7, FSTL4 |
| [[CRIP1]] | B | IGFBP2 activity raises CRIP1's level | lines that do not express IGFBP2 (16) vs lines expressing it (34) | 2.38× lower at baseline in the lines without IGFBP2 | 0.096 | ⚠ within organs, on part of the lines; also absent: CBFA2T3, CHRNA7, FSTL4 |
| [[COL9A3]] | B | IGFBP2 activity raises COL9A3's level | lines that do not express IGFBP2 (16) vs lines expressing it (34) | 1.72× lower at baseline in the lines without IGFBP2 | 0.099 | ⚠ within organs, on part of the lines; also absent: CBFA2T3, CHRNA7, FSTL4 |

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.425). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.6, -9.6); signed map (-38.6, 16.6). **Vector** length 59.1, 14.2% of its response variance represented; |z| ≥ 3 in 481 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +5.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +2.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +5.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | +3.5 | +4.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.8 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | -0.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | -0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -6.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -2.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.6 | -2.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | -2.5 | -4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -0.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | insulin like growth factor binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:216,632,828-216,664,436 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously IBP2 |
| Gene groups (HGNC) | Insulin like growth factor binding proteins |
| Hallmark sets | KRAS_SIGNALING_DN, UV_RESPONSE_UP, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 1 pathways, smallest: Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [P18065](https://www.uniprot.org/uniprotkb/P18065) (Insulin-like growth factor-binding protein 2):

> Multifunctional protein that plays a critical role in regulating the availability of IGFs such as IGF1 and IGF2 to their receptors and thereby regulates IGF-mediated cellular processes including proliferation, differentiation, and apoptosis in a cell-type specific manner. Functions coordinately with receptor protein tyrosine phosphatase beta/PTPRB and the IGF1 receptor to regulate IGF1-mediated signaling by stimulating the phosphorylation of PTEN leading to its inactivation and AKT1 activation. …

**Summary**, from NCBI Gene [3485](https://www.ncbi.nlm.nih.gov/gene/3485):

> The protein encoded by this gene is one of six similar proteins that bind insulin-like growth factors I and II (IGF-I and IGF-II). The encoded protein can be secreted into the bloodstream, where it binds IGF-I and IGF-II with high affinity, or it can remain intracellular, interacting with many different ligands. High expression levels of this protein promote the growth of several types of tumors and may be predictive of the chances of recovery of the patient. Several transcript variants, one …

**Accessions** — [HGNC:5471](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5471) · Entrez [3485](https://www.ncbi.nlm.nih.gov/gene/3485) · UniProt [P18065](https://www.uniprot.org/uniprotkb/P18065) · Ensembl [ENSG00000115457](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115457)

## Data

Gene col 3677: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3677); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3677, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3677]; `tensor/DDL_lfc|DDL_z.npy` [3677]; `embed/gene_vectors.npy` [3677]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3677 or target_col == 3677). Every well: [[IGFBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGFBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
