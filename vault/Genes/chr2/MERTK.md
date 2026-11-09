---
symbol: "MERTK"
type: "gene"
col: 7702
ensembl_id: "ENSG00000153208"
name: "MER proto-oncogene, tyrosine kinase"
location: "2q13"
module: 115
arm: "+"
pooled_cpm: 17.13
n_lines_expressing: 41
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# MERTK

*MER proto-oncogene, tyrosine kinase* — 2q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.70× (z +12.5, q 6e-33, up in 28 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.923× (z -4.8, q 9e-04, down in 4 of 39 measured lines) ⚠ position not correctable. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 0.735× (z -3.7, q 0.068, down in 8 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.135×, C-33 A 0.206×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 0.219×, NCI-H460 0.266×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.215×, SHP-77 0.0977×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00937]] (+0.62, fdr 1e-05), [[MED12L]] (+0.58, fdr 1e-05), [[JAM3]] (+0.56, fdr 4e-05); moves opposite to [[LINS1]] (-0.48, fdr 2e-04), [[WAPL]] (-0.46, fdr 1e-04), [[CKMT2-AS1]] (-0.45, fdr 3e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MLXIPL]] → it (grade B ⚠); 1 goes from it, the strongest it → [[GNB5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7702.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.70×** | +12.5 | 6e-33 | 28/38 (HEC-1-A, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.09×** | +12.2 | 6e-32 | 25/38 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.08×** | +12.1 | 2e-31 | 29/38 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.07×** | +12.1 | 2e-31 | 29/38 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.04×** | +11.8 | 3e-30 | 24/38 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.65×** | +8.3 | 8e-15 | 21/38 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +8.2 | 2e-14 | 12/29 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +7.8 | 6e-13 | 23/38 (HT-29, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +7.5 | 4e-12 | 13/31 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.27×** | +7.1 | 8e-11 | 24/39 (PANC-1, NCI-H1792, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.45×** | +6.2 | 4e-08 | 17/38 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.01×** | +6.0 | 8e-08 | 16/30 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +5.9 | 2e-07 | 17/38 (Hs 766T, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +5.5 | 2e-06 | 13/35 (Hs 766T, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +5.0 | 2e-05 | 8/23 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.4 | 0.016 | 6/39 (SW 900, A549, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.022 | 11/38 (PANC-1, Hs 766T, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.46×** | +3.3 | 0.025 | 5/35 (NCI-H2347, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.28×** | +2.9 | 0.085 | 11/38 (NCI-H460, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7702.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.135×, C-33 A 0.206×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 0.219×, NCI-H460 0.266×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.215×, SHP-77 0.0977×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.923× | -4.8 | 9e-04 | 4/39 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.735×** | -3.7 | 0.068 | 8/38 (MIA PaCa-2, RKO, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.872× | -3.3 | 0.21 | 11/39 (SW1417, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7702. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 8.19 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.95× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 4.17× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 23.6 | 4 | 0 | [[Belinostat (drug)]] 5 µM 3.80× (z +11.5) | — |
| [[HOP62 (line)]] | alt | 11.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 19.8× (z +12.4) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 15.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.34× (z +14.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 8.07× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 20.9 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.76× (z +9.1) | — |
| [[A-427 (line)]] | wt | 74.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -18.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 42.2 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.36× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 32.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -15.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 15.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C-33 A (line)]] | alt | 43.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.206× (z -9.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 12.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1792 (line)]] | alt | 24.1 | 1 | 0 | [[Belinostat (drug)]] 5 µM 3.81× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 47.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -13.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H2347 (line)]] | alt | 52.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -9.6) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H460 (line)]] | wt | 10.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.272× (z -9.0) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 28.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0977× (z -14.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 48.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 9.36 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 2.95 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.08 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7702), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00937]] | +0.62 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[MED12L]] | +0.58 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[JAM3]] | +0.56 | +0.41 / +0.64 | both halves | 4e-05 | pathway: Cell surface interactions at the vascular wall |
| [[CERS6]] | +0.55 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[SDK2]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 | same gene group |
| [[ARHGAP44]] | +0.55 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[STRBP]] | +0.55 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[MPV17L]] | +0.53 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[SLC29A3]] | +0.53 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[ASIC1]] | +0.52 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[LMX1B]] | +0.52 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[FHL1]] | +0.51 | +0.31 / +0.55 | both halves | 2e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINS1]] | -0.48 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[WAPL]] | -0.46 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[CKMT2-AS1]] | -0.45 | -0.32 / -0.28 | both halves | 3e-04 |  |
| [[SYNRG]] | -0.45 | -0.29 / -0.49 | both halves | 3e-04 |  |
| [[UBE3B]] | -0.44 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[PDCD7]] | -0.44 | -0.24 / -0.47 | both halves | 4e-04 |  |
| [[EFCAB6]] | -0.44 | -0.20 / -0.52 | both halves | 7e-04 |  |
| [[TMEM187]] | -0.44 | -0.21 / -0.55 | both halves | 7e-04 |  |
| [[ARL17B]] | -0.44 | -0.52 / -0.30 | both halves | 2e-04 |  |
| [[MKRN3]] | -0.44 | -0.36 / -0.38 | both halves | 9e-05 |  |
| [[FANK1]] | -0.43 | -0.30 / -0.47 | both halves | 2e-04 | same gene group |
| [[ATRIP]] | -0.43 | -0.20 / -0.45 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MLXIPL]] | B | MLXIPL activity raises MERTK's level | lines that do not express MLXIPL (13) vs lines expressing it (37) | 2.58× lower at baseline in the lines without MLXIPL | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: GRTP1, PLS1, LAMP3; maybe low, not absent |
| [[GRTP1]] | B | GRTP1 activity raises MERTK's level | lines that do not express GRTP1 (11) vs lines expressing it (39) | 2.94× lower at baseline in the lines without GRTP1 | 0.049 | ⚠ within organs, on part of the lines; also absent: MLXIPL, PLS1, SLC37A1 |
| [[SHROOM2]] | B | SHROOM2 activity raises MERTK's level | lines that do not express SHROOM2 (15) vs lines expressing it (35) | 1.73× lower at baseline in the lines without SHROOM2 | 0.092 | ⚠ within organs, on part of the lines; also absent: GPR143, RASGEF1C |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNB5]] | B | MERTK activity raises GNB5's level | lines that do not express MERTK (9) vs lines expressing it (41) | 1.27× lower at baseline in the lines without MERTK | 0.099 | ⚠ within organs, on part of the lines; also absent: PARD6B, GRHL1, SDHAP3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.653). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (1.2, 39.0); signed map (-21.5, 38.0). **Vector** length 69.2, 12.2% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +12.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +8.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +1.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.5 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -1.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +0.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +0.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.4 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.3 | -1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | MER proto-oncogene, tyrosine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q13 — chr2:111,898,607-112,029,561 (+) |
| Ensembl biotype | protein_coding |
| Also known as | mer, RP38, c-Eyk, Tyro12 |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; AXL receptor tyrosine kinase family |
| Hallmark sets | ANDROGEN_RESPONSE, GLYCOLYSIS |
| Reactome | 5 pathways, smallest: Dengue Virus Attachment and Entry; Cell surface interactions at the vascular wall; Dengue Virus Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12866](https://www.uniprot.org/uniprotkb/Q12866) (Tyrosine-protein kinase Mer):

> Receptor tyrosine kinase that transduces signals from the extracellular matrix into the cytoplasm by binding to several ligands including LGALS3, TUB, TULP1 or GAS6. Regulates many physiological processes including cell survival, migration, differentiation, and phagocytosis of apoptotic cells (efferocytosis). Ligand binding at the cell surface induces autophosphorylation of MERTK on its intracellular domain that provides docking sites for downstream signaling molecules. Following activation by …

**Summary**, from NCBI Gene [10461](https://www.ncbi.nlm.nih.gov/gene/10461):

> This gene is a member of the MER/AXL/TYRO3 receptor kinase family and encodes a transmembrane protein with two fibronectin type-III domains, two Ig-like C2-type (immunoglobulin-like) domains, and one tyrosine kinase domain. Mutations in this gene have been associated with disruption of the retinal pigment epithelium (RPE) phagocytosis pathway and onset of autosomal recessive retinitis pigmentosa (RP). [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7027](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7027) · Entrez [10461](https://www.ncbi.nlm.nih.gov/gene/10461) · UniProt [Q12866](https://www.uniprot.org/uniprotkb/Q12866) · Ensembl [ENSG00000153208](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153208)

## Data

Gene col 7702: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7702); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7702, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7702]; `tensor/DDL_lfc|DDL_z.npy` [7702]; `embed/gene_vectors.npy` [7702]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7702 or target_col == 7702). Every well: [[MERTK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MERTK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
