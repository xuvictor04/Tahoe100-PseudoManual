---
symbol: "ALPK2"
type: "gene"
col: 12682
ensembl_id: "ENSG00000198796"
name: "alpha kinase 2"
location: "18q21.31-q21.32"
module: 66
arm: "+"
pooled_cpm: 25.0
n_lines_expressing: 19
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 9
direction_downstream: 24
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# ALPK2

*alpha kinase 2* — 18q21.31-q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.62× (z +14.8, q 0e+00, up in 10 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.60× (z +7.7, q 2e-12, up in 3 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.705× (z -4.0, q 0.034, down in 7 of 16 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 0.130×, HepG2/C3A 0.133×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (HepG2/C3A 0.134×, NCI-H460 0.180×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (NCI-H460 0.153×, HepG2/C3A 0.185×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.182×); [[Tofacitinib (drug)]] 5 µM in 1 line (C32 0.231×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL12A1]] (+0.71, fdr 7e-06), [[TGFB2]] (+0.68, fdr 7e-06), [[TMPRSS15]] (+0.65, fdr 3e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 24 go from it, the strongest it → [[CALD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12682.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.62×** | +14.8 | 0e+00 | 10/14 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.61×** | +14.2 | 3e-43 | 10/14 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.52×** | +9.7 | 4e-20 | 9/14 (HS-578T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +7.7 | 2e-12 | 3/16 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.47×** | +6.2 | 5e-08 | 12/16 (A-172, A498, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +5.8 | 8e-07 | 10/17 (J82, A-172, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.0 | 4e-05 | 3/17 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.54×** | +4.8 | 1e-04 | 13/15 (A549, HS-578T, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.51×** | +4.6 | 3e-04 | 10/17 (A549, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.37×** | +4.3 | 0.001 | 12/17 (A549, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.42×** | +4.0 | 0.003 | 6/17 (A549, J82, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +4.0 | 0.003 | 4/14 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.39×** | +3.8 | 0.007 | 5/15 (SNU-423, A-172, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.7 | 0.009 | 2/11 (A-172, SNU-423) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.009 | 11/16 (A549, H4, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +3.5 | 0.015 | 10/16 (SNU-423, J82, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.025 | 8/17 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[AZD-7648 (drug)]] 5 µM |  | **1.74×** | +3.3 | 0.026 | 2/15 (A549, A498) | rises with dose | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.038 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Procainamide (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.038 | 0/16 | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.055 | 9/15 (RPMI-7951, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12682.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 0.130×, HepG2/C3A 0.133×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (HepG2/C3A 0.134×, NCI-H460 0.180×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (NCI-H460 0.153×, HepG2/C3A 0.185×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.182×); [[Tofacitinib (drug)]] 5 µM in 1 line (C32 0.231×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.705×** | -4.0 | 0.034 | 7/16 (HepG2/C3A, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 0.754× | -3.2 | 0.26 | 0/16 | inconsistent across doses | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.758× | -3.2 | 0.26 | 6/16 (NCI-H460, A498, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.765× | -3.1 | 0.26 | 0/15 | two highest doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.749× | -3.0 | 0.26 | 0/16 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12682. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 172 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -16.4) |
| [[NCI-H460 (line)]] | wt | 226 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.130× (z -16.6) |
| [[A-172 (line)]] | wt | 37.7 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.85× (z +17.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[A498 (line)]] | wt | 41.1 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.43× (z +13.4) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[A549 (line)]] | wt | 31.9 | 3 (1 ⚠) | 0 | [[Trametinib (drug)]] 0.05 µM 4.56× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 19.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.78× (z +12.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[C32 (line)]] | wt | 20.6 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.231× (z -8.7) |
| [[H4 (line)]] | wt | 58.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +8.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HOP62 (line)]] | alt | 6.99 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.05× (z +10.4) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 29.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +11.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[J82 (line)]] | alt | 56.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +8.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SNU-423 (line)]] | alt | 22.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +9.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[A-427 (line)]] | wt | 3.56 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.15 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 105 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.57 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.70 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.25 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.23 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12682), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL12A1]] | +0.71 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[TGFB2]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[TMPRSS15]] | +0.65 | +0.46 / +0.75 | both halves | 3e-05 |  |
| [[ROS1]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[GLIPR1]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ABCC9]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[CPED1]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[PALLD]] | +0.61 | +0.61 / +0.58 | both halves | 7e-06 | same gene group |
| [[CALD1]] | +0.59 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[THBS1]] | +0.59 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[BDNF]] | +0.59 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[NREP]] | +0.58 | +0.54 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers ALPK2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[NLGN4Y]] | C | NLGN4Y activity raises ALPK2's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 5.80× lower at baseline in the lines without NLGN4Y | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[AKR1B10]] | C | AKR1B10 activity raises ALPK2's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 1.94× lower at baseline in the lines without AKR1B10 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[MARCOL]], [[SPINK13]] | C | MARCOL, SPINK13 activity raises ALPK2's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 3.71× lower at baseline in the lines without MARCOL, SPINK13 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[FBN2]] | C | FBN2 activity raises ALPK2's level | lines that do not express FBN2 (31) vs lines expressing it (19) | 3.09× lower at baseline in the lines without FBN2 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZEB2, ENSG00000289884, ABI3BP; maybe low, not absent; co-absent with the target |
| [[C5orf46]] | C | C5orf46 activity raises ALPK2's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 3.92× lower at baseline in the lines without C5orf46 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[TENM3-AS1]] | C | TENM3-AS1 activity raises ALPK2's level | lines that do not express TENM3-AS1 (19) vs lines expressing it (31) | 2.93× lower at baseline in the lines without TENM3-AS1 | 0.081 | ⚠ within organs, on part of the lines; also absent: TENM3, LRCH2, FBXL7; maybe low, not absent; co-absent with the target |
| [[TENM3]] | C | TENM3 activity raises ALPK2's level | lines that do not express TENM3 (20) vs lines expressing it (30) | 2.87× lower at baseline in the lines without TENM3 | 0.090 | ⚠ within organs, on part of the lines; also absent: TENM3-AS1, ZEB2, SRPX; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises ALPK2's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 3.14× lower at baseline in the lines without LINC03000 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 6, C 18. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALD1]] | B | ALPK2 activity raises CALD1's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 5.24× lower at baseline in the lines without ALPK2 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4 |
| [[SYNE1]] | B | ALPK2 activity raises SYNE1's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 3.62× lower at baseline in the lines without ALPK2 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4 |
| [[STARD13]] | B | ALPK2 activity raises STARD13's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 2.75× lower at baseline in the lines without ALPK2 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4 |
| cells under [[Omeprazole (drug)]] 0.05 µM | B | ALPK2 activity raises the cells' numbers under Omeprazole 0.05 µM (protects the cells) | lines that do not express ALPK2 (31) vs lines expressing it (17) | the lines without ALPK2: 0.80× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4 |
| [[NREP]] | B | ALPK2 activity raises NREP's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 4.44× lower at baseline in the lines without ALPK2 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4 |
| [[PDE1C]] | B | ALPK2 activity raises PDE1C's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 3.00× lower at baseline in the lines without ALPK2 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4 |
| [[FBN2]] | C | ALPK2 activity raises FBN2's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 4.04× lower at baseline in the lines without ALPK2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4; co-absent with the target |
| [[NLGN4Y]] | C | ALPK2 activity raises NLGN4Y's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 5.68× lower at baseline in the lines without ALPK2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4; co-absent with the target |
| [[PSG4]] | C | ALPK2 activity raises PSG4's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 2.23× lower at baseline in the lines without ALPK2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4; co-absent with the target |
| [[DGKI]] | C | ALPK2 activity raises DGKI's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 3.17× lower at baseline in the lines without ALPK2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4; co-absent with the target |
| [[PTN]] | C | ALPK2 activity raises PTN's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 5.77× lower at baseline in the lines without ALPK2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4; co-absent with the target |
| [[CCDC80]] | C | ALPK2 activity raises CCDC80's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 5.28× lower at baseline in the lines without ALPK2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.703). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.6, 21.4); signed map (45.4, 20.3). **Vector** length 80.6, 32.5% of its response variance represented; |z| ≥ 3 in 485 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +14.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +9.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +14.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.5 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +4.3 |
| fall | [[BAY1125976 (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.8 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | alpha kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.31-q21.32 — chr18:58,481,247-58,629,091 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HAK |
| Gene groups (HGNC) | I-set domain containing; Alpha kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86TB3](https://www.uniprot.org/uniprotkb/Q86TB3) (Alpha-protein kinase 2):

> Protein kinase that recognizes phosphorylation sites in which the surrounding peptides have an alpha-helical conformation.

**Summary**, from NCBI Gene [115701](https://www.ncbi.nlm.nih.gov/gene/115701):

> Predicted to enable ATP binding activity; protein serine kinase activity; and protein serine/threonine kinase activity. Involved in several processes, including epicardium morphogenesis; heart development; and negative regulation of Wnt signaling pathway involved in heart development. Acts upstream of or within regulation of gene expression. Located in basolateral plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20565](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20565) · Entrez [115701](https://www.ncbi.nlm.nih.gov/gene/115701) · UniProt [Q86TB3](https://www.uniprot.org/uniprotkb/Q86TB3) · Ensembl [ENSG00000198796](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198796)

## Data

Gene col 12682: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12682); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12682, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12682]; `tensor/DDL_lfc|DDL_z.npy` [12682]; `embed/gene_vectors.npy` [12682]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12682 or target_col == 12682). Every well: [[ALPK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALPK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
