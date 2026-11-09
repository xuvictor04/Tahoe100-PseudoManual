---
symbol: "MLLT11"
type: "gene"
col: 13089
ensembl_id: "ENSG00000213190"
name: "MLLT11 transcription factor 7 cofactor"
location: "1q21.3"
module: 60
arm: "+"
pooled_cpm: 9.81
n_lines_expressing: 29
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# MLLT11

*MLLT11 transcription factor 7 cofactor* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 8.00× (z +20.5, q 0e+00, up in 26 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.600× (z -5.1, q 2e-04, down in 16 of 26 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H460 0.199×, SHP-77 0.151×, H4 0.170×, CHP-212 0.287×; ⚠ cell-cycle shift, explains ~52% of this change); [[Panobinostat (drug)]] 5 µM in 4 lines (NCI-H460 0.179×, H4 0.116×, A-172 0.267×, SHP-77 0.254×); [[Panobinostat (drug)]] 0.5 µM in 3 lines (H4 0.0908×, NCI-H460 0.235×, A-172 0.282×); [[Belinostat (drug)]] 5 µM in 3 lines (A-172 0.245×, SHP-77 0.259×, H4 0.209×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B4GALNT1]] (+0.68, fdr 7e-06), [[PSMA1]] (+0.62, fdr 1e-05), [[HSP90AA2P]] (+0.62, fdr 1e-05); moves opposite to [[MT1E]] (-0.48, fdr 5e-05), [[GPX4]] (-0.47, fdr 1e-04), [[MT2A]] (-0.45, fdr 9e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[FKBP4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13089.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **8.00×** | +20.5 | 0e+00 | 26/26 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **6.52×** | +18.5 | 0e+00 | 25/26 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **5.35×** | +15.6 | 0e+00 | 26/26 (NCI-H460, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **4.46×** | +14.7 | 0e+00 | 22/26 (HOP62, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.11×** | +13.9 | 5e-42 | 20/21 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.54×** | +13.0 | 2e-36 | 16/26 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.68×** | +12.4 | 4e-33 | 12/13 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.93×** | +9.8 | 9e-21 | 13/16 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.56×** | +6.2 | 5e-08 | 17/27 (NCI-H1792, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.71×** | +5.8 | 5e-07 | 19/27 (NCI-H1792, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.5 | 2e-06 | 5/27 (SW480, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.8 | 6e-05 | 10/19 (CFPAC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +4.4 | 5e-04 | 4/25 (SW480, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 0.05 µM |  | **1.54×** | +4.2 | 9e-04 | 14/26 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.84×** | +4.2 | 0.001 | 9/14 (SHP-77, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +3.5 | 0.012 | 7/23 (J82, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.030 | 3/26 (PANC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.76×** | +3.3 | 0.030 | 3/25 (NCI-H460, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.35×** | +2.9 | 0.091 | 5/25 (A-172, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13089.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H460 0.199×, SHP-77 0.151×, H4 0.170×, CHP-212 0.287×; ⚠ cell-cycle shift, explains ~52% of this change); [[Panobinostat (drug)]] 5 µM in 4 lines (NCI-H460 0.179×, H4 0.116×, A-172 0.267×, SHP-77 0.254×); [[Panobinostat (drug)]] 0.5 µM in 3 lines (H4 0.0908×, NCI-H460 0.235×, A-172 0.282×); [[Belinostat (drug)]] 5 µM in 3 lines (A-172 0.245×, SHP-77 0.259×, H4 0.209×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.600×** | -5.1 | 2e-04 | 16/26 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.688×** | -3.7 | 0.056 | 11/26 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM |  | 0.695× | -3.4 | 0.12 | 10/27 (CFPAC-1, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13089. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 40.0 | 5 (2 ⚠) | 4 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 9.58× (z +17.2) | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -17.4) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.179× (z -13.1) |
| [[H4 (line)]] | wt | 45.7 | 3 | 4 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 8.49× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -13.5) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0908× (z -13.0) |
| [[SHP-77 (line)]] | alt | 36.3 | 3 | 3 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 7.34× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -16.8) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.254× (z -8.6) |
| [[A-172 (line)]] | wt | 73.7 | 2 | 3 | [[Ixazomib citrate (drug)]] 0.5 µM 5.56× (z +11.7) | [[Belinostat (drug)]] 5 µM 0.245× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 15.4 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 14.2× (z +12.1) | — |
| [[A498 (line)]] | wt | 18.2 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 8.77× (z +11.7) | — |
| [[HOP62 (line)]] | alt | 10.5 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 18.8× (z +14.2) | — |
| [[SW480 (line)]] | alt | 6.44 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 11.5× (z +13.2) | — |
| [[C32 (line)]] | wt | 5.90 | 3 | 0 | [[Auranofin (drug)]] 5 µM 27.9× (z +10.8) | — |
| [[CFPAC-1 (line)]] | alt | 4.66 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 11.7× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 11.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 11.0× (z +10.6) | — |
| [[J82 (line)]] | alt | 5.57 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 9.07× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 19.1 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.11× (z +9.6) | — |
| [[PANC-1 (line)]] | alt | 3.47 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 11.3× (z +11.0) | — |
| [[A549 (line)]] | wt | 7.85 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 8.42× (z +9.3) | — |
| [[CHP-212 (line)]] | wt | 63.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -8.6) ⚠ cell-cycle shift, explains ~52% of this change |
| [[HepG2_C3A (line)]] | wt | 5.26 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 20.6× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 7.34 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 14.9× (z +9.2) | — |
| [[A-427 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.877 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.993 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.949 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.82 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13089), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B4GALNT1]] | +0.68 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[PSMA1]] | +0.62 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[HSP90AA2P]] | +0.62 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[SOD1]] | +0.62 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[PSMB2]] | +0.60 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[PSMD11]] | +0.60 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[PSMC5]] | +0.59 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[SERPINH1]] | +0.58 | +0.52 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[BHMT2]] | +0.57 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[PSMB4]] | +0.57 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[HSPB1]] | +0.57 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[NCF2]] | +0.57 | +0.46 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MT1E]] | -0.48 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[GPX4]] | -0.47 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[MT2A]] | -0.45 | -0.40 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MLLT11's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP1B]] | C | MAP1B activity raises MLLT11's level | lines that do not express MAP1B (16) vs lines expressing it (34) | 3.58× lower at baseline in the lines without MAP1B | 0.019 | ⚠ within organs, on part of the lines; also absent: MPDZ, GNB4, EVL; co-absent with the target |
| [[POPDC3]] | C | POPDC3 activity raises MLLT11's level | lines that do not express POPDC3 (18) vs lines expressing it (32) | 2.83× lower at baseline in the lines without POPDC3 | 0.019 | ⚠ within organs, on part of the lines; also absent: WIPF1, WDR17, BVES-AS1; co-absent with the target |
| [[B4GALNT1]] | C | B4GALNT1 activity raises MLLT11's level | lines that do not express B4GALNT1 (16) vs lines expressing it (34) | 3.46× lower at baseline in the lines without B4GALNT1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ARHGEF25, RFLNB, RASSF8-AS1; co-absent with the target |
| [[MAP1A]] | C | MAP1A activity raises MLLT11's level | lines that do not express MAP1A (17) vs lines expressing it (33) | 3.00× lower at baseline in the lines without MAP1A | 0.079 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FKBP4]] | B | MLLT11 activity lowers FKBP4's level | lines that do not express MLLT11 (21) vs lines expressing it (29) | 1.54× higher at baseline in the lines without MLLT11 | 0.081 | ⚠ within organs, on part of the lines; also absent: DZIP1, ADAMTS18, KCNJ6; maybe low, not absent |
| [[POPDC3]] | C | MLLT11 activity raises POPDC3's level | lines that do not express MLLT11 (21) vs lines expressing it (29) | 3.57× lower at baseline in the lines without MLLT11 | 0.024 | ⚠ within organs, on part of the lines; also absent: DZIP1, ADAMTS18, KCNJ6; maybe low, not absent; co-absent with the target |
| [[MAP1B]] | C | MLLT11 activity raises MAP1B's level | lines that do not express MLLT11 (21) vs lines expressing it (29) | 7.10× lower at baseline in the lines without MLLT11 | 0.029 | ⚠ within organs, on part of the lines; also absent: DZIP1, ADAMTS18, KCNJ6; maybe low, not absent; co-absent with the target |
| [[MAP1A]] | C | MLLT11 activity raises MAP1A's level | lines that do not express MLLT11 (21) vs lines expressing it (29) | 3.21× lower at baseline in the lines without MLLT11 | 0.081 | ⚠ within organs, on part of the lines; also absent: DZIP1, ADAMTS18, KCNJ6; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.660). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-18.9, -9.7); signed map (-25.3, -27.5). **Vector** length 74.8, 20.2% of its response variance represented; |z| ≥ 3 in 589 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +8.1 | +18.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.6 | +20.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.5 | +15.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +13.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.5 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +5.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | +1.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -3.0 | -2.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.9 | -5.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -3.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.5 | -2.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | MLLT11 transcription factor 7 cofactor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:151,060,397-151,069,544 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AF1Q |
| Hallmark sets | MTORC1_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13015](https://www.uniprot.org/uniprotkb/Q13015) (Protein AF1q):

> Cofactor for the transcription factor TCF7. Involved in regulation of lymphoid development by driving multipotent hematopoietic progenitor cells towards a T cell fate.

**Summary**, from NCBI Gene [10962](https://www.ncbi.nlm.nih.gov/gene/10962):

> The gene variously symbolized ALL1, HRX, or MLL located on 11q23 has been demonstrated to be fused with a number of translocation partners in cases of leukemia. t(1;11)(q21;q23) translocations that fused the MLL gene to a gene on chromosomal band 1q21 in 2 infants with acute myelomonocytic leukemia have been demonstrated. The N-terminal portion of the MLL gene is critical for leukemogenesis in translocations involving band 11q23. This gene encodes 90 amino acids. It was found to be highly …

**Accessions** — [HGNC:16997](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16997) · Entrez [10962](https://www.ncbi.nlm.nih.gov/gene/10962) · UniProt [Q13015](https://www.uniprot.org/uniprotkb/Q13015) · Ensembl [ENSG00000213190](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213190)

## Data

Gene col 13089: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13089); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13089, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13089]; `tensor/DDL_lfc|DDL_z.npy` [13089]; `embed/gene_vectors.npy` [13089]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13089 or target_col == 13089). Every well: [[MLLT11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MLLT11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
