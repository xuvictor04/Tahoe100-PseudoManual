---
symbol: "SLCO5A1"
type: "gene"
col: 6036
ensembl_id: "ENSG00000137571"
name: "solute carrier organic anion transporter family member 5A1"
location: "8q13.3"
module: 14
arm: "+"
pooled_cpm: 27.81
n_lines_expressing: 44
n_dd_up: 47
n_dd_down: 7
n_dd_up_clean: 37
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# SLCO5A1

*solute carrier organic anion transporter family member 5A1* — 8q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 47 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 15.6× (z +57.1, q 0e+00, up in 40 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[IQ 1 (drug)]] 0.5 µM: 0.508× (z -7.1, q 6e-10, down in 26 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLGAP1]] (+0.65, fdr 2e-05), [[GRIA4]] (+0.60, fdr 1e-05), [[IL32]] (+0.60, fdr 2e-05); moves opposite to [[ATG5]] (-0.50, fdr 1e-04), [[PXMP4]] (-0.50, fdr 1e-04), [[BAG4]] (-0.49, fdr 6e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[NANOS3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 47 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6036.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **15.6×** | +57.1 | 0e+00 | 40/41 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **6.45×** | +26.4 | 0e+00 | 35/40 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.31×** | +24.9 | 0e+00 | 36/41 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.54×** | +18.6 | 0e+00 | 33/39 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.95×** | +13.9 | 1e-41 | 31/42 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.91×** | +9.5 | 2e-19 | 29/42 (J82, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.67×** | +7.5 | 4e-12 | 22/42 (NCI-H2030, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +6.8 | 6e-10 | 18/40 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +6.7 | 1e-09 | 22/39 (A498, H4, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +6.7 | 2e-09 | 24/41 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pioglitazone (drug)]] 0.05 µM |  | **1.56×** | +6.5 | 3e-09 | 15/41 (hTERT-HPNE, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.4 | 8e-09 | 18/40 (BT-474, SNU-423, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.53×** | +6.3 | 2e-08 | 19/42 (LoVo, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Baicalin (drug)]] 5 µM |  | **1.34×** | +6.1 | 4e-08 | 16/42 (PANC-1, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.8 | 3e-07 | 17/38 (SNU-423, H4, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.08×** | +5.6 | 6e-07 | 19/42 (NCI-H2347, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6036.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[IQ 1 (drug)]] 0.5 µM |  | **0.508×** | -7.1 | 6e-10 | 26/40 (SHP-77, C32, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[IQ 1 (drug)]] 5 µM |  | **0.469×** | -5.8 | 1e-06 | 18/38 (SHP-77, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.532×** | -4.9 | 2e-04 | 14/37 (RKO, C32, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Ixazomib (drug)]] 5 µM |  | **0.537×** | -4.8 | 2e-04 | 13/39 (SHP-77, C32, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **0.729×** | -4.7 | 3e-04 | 13/42 (A-172, SNU-423, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.761×** | -4.1 | 0.005 | 10/39 (HCT15, A549, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.930× | -3.8 | 0.011 | 6/42 (AN3 CA, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -3.6 | 0.022 | 16/42 (SHP-77, J82, …) | top dose only | low cells (technical?) |
| [[Ixazomib (drug)]] 0.05 µM |  | **0.781×** | -3.4 | 0.035 | 10/39 (C32, RKO, …) | inconsistent across doses | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 0.5 µM |  | 0.813× | -3.1 | 0.12 | 8/40 (SW480, CHP-212, …) | inconsistent across doses | position effect removed |
| [[Tubulin inhibitor 6 (drug)]] 0.05 µM |  | 0.805× | -3.0 | 0.12 | 5/41 (SK-MEL-2, J82, …) | inconsistent across doses | position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | 0.817× | -3.0 | 0.13 | 7/41 (A498, NCI-H661, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6036. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 27.0 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.5× (z +27.6) | — |
| [[RKO (line)]] | wt | 127 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +15.0) | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Cepharanthine (drug)]] 5 µM 0.385× (z -9.2) |
| [[A-172 (line)]] | wt | 23.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.1× (z +23.6) | — |
| [[A498 (line)]] | wt | 55.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.1× (z +25.1) | — |
| [[A549 (line)]] | wt | 14.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 44.8× (z +25.7) | — |
| [[HS-578T (line)]] | alt | 14.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.8× (z +23.5) | — |
| [[NCI-H2347 (line)]] | alt | 12.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.0× (z +26.3) | — |
| [[NCI-H460 (line)]] | wt | 128 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[PANC-1 (line)]] | alt | 7.96 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 82.3× (z +28.5) | — |
| [[H4 (line)]] | wt | 19.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.0× (z +17.0) | — |
| [[HOP62 (line)]] | alt | 12.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 41.4× (z +25.4) | — |
| [[hTERT-HPNE (line)]] | wt | 13.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 42.4× (z +20.8) | — |
| [[J82 (line)]] | alt | 17.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.0× (z +20.9) | — |
| [[NCI-H1573 (line)]] | alt | 8.68 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 50.8× (z +21.2) | — |
| [[NCI-H1792 (line)]] | alt | 27.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.0× (z +22.9) | — |
| [[NCI-H2030 (line)]] | alt | 7.63 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 43.3× (z +20.7) | — |
| [[SNU-423 (line)]] | alt | 10.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.4× (z +19.3) | — |
| [[SW48 (line)]] | wt | 35.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +19.5) | — |
| [[BT-474 (line)]] | alt | 17.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +15.9) | — |
| [[C32 (line)]] | wt | 146 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +10.1) | [[Cepharanthine (drug)]] 5 µM 0.353× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 10.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.8× (z +20.8) | — |
| [[COLO 205 (line)]] | alt | 13.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.28× (z +12.1) | [[Harringtonine (drug)]] 0.05 µM 0.0865× (z -9.8) |
| [[HCT15 (line)]] | alt | 32.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.33× (z +13.1) | [[Temsirolimus (drug)]] 0.5 µM 0.147× (z -9.5) |
| [[HT-29 (line)]] | alt | 15.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.81× (z +16.9) | — |
| [[KATO III (line)]] | alt | 12.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.79× (z +15.8) | — |
| [[RPMI-7951 (line)]] | alt | 13.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.3× (z +16.2) | — |
| [[SW 900 (line)]] | alt | 45.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +21.3) | — |
| [[Hs 766T (line)]] | wt | 8.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.2× (z +12.8) | — |
| [[LOX-IMVI (line)]] | wt | 12.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +11.8) | — |
| [[LS 180 (line)]] | wt | 16.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.41× (z +15.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 7.94 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.8× (z +10.7) | — |
| [[NCI-H23 (line)]] | alt | 8.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.10× (z +11.9) | — |
| [[SHP-77 (line)]] | alt | 125 | 0 | 1 | — | [[Cepharanthine (drug)]] 5 µM 0.349× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 10.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +12.8) | — |
| [[SNU-1 (line)]] | wt | 51.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.66× (z +15.2) | — |
| [[SW 1271 (line)]] | alt | 14.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.8× (z +8.5) | — |
| [[A-427 (line)]] | wt | 5.14 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.13 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.16 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.43 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.83 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.54 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 22.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6036), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLGAP1]] | +0.65 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[GRIA4]] | +0.60 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[IL32]] | +0.60 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[LINC02605]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[RASGRP1]] | +0.58 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[PPP4R4]] | +0.57 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[WAKMAR2]] | +0.57 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[EYS]] | +0.56 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[S100A3]] | +0.56 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[STX11]] | +0.56 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[MMRN2]] | +0.55 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[SLC6A7]] | +0.54 | +0.49 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG5]] | -0.50 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[PXMP4]] | -0.50 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[BAG4]] | -0.49 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[GNPTG]] | -0.47 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[NUDT21]] | -0.47 | -0.49 / -0.32 | both halves | 1e-04 |  |
| [[MED23]] | -0.47 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[TTLL5]] | -0.46 | -0.45 / -0.26 | both halves | 4e-04 |  |
| [[MTMR12]] | -0.45 | -0.45 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLCO5A1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 9.8% of all compounds | 0.020 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TRAF1]] | B | TRAF1 activity raises SLCO5A1's level | lines that do not express TRAF1 (12) vs lines expressing it (38) | 1.35× lower at baseline in the lines without TRAF1 | 0.045 | ⚠ within organs, on part of the lines; also absent: MT2A, TUBA1A, ENSG00000230479; maybe low, not absent |
| [[ARNT2-DT]] | B | ARNT2-DT activity raises SLCO5A1's level | lines that do not express ARNT2-DT (27) vs lines expressing it (23) | 1.90× lower at baseline in the lines without ARNT2-DT | 0.076 | ⚠ within organs, on part of the lines; also absent: ARNT2, SOX11, ENSG00000233491 |
| [[IL23A]] | B | IL23A activity strengthens SLCO5A1's drug response | lines that do not express IL23A (6) vs lines expressing it (36) | the lines without IL23A respond 0.90× as strongly (z diff +1.21); strongest at Idarubicin (hydrochloride) 5 µM: 2.18x vs 3.18x (z diff +3.0) | 0.081 | ⚠ within organs, on part of the lines; also absent: MYRF; maybe low, not absent; target measured in part of the lines; the reference differs; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NANOS3]] | B | SLCO5A1 activity lowers NANOS3's level | lines that do not express SLCO5A1 (6) vs lines expressing it (44) | 1.75× higher at baseline in the lines without SLCO5A1 | 0.057 | ⚠ within organs, on part of the lines; also absent: EFCAB3P1; maybe low, not absent |
| [[TRPM3]] | C | SLCO5A1's natural level weakens TRPM3's drug response | SLCO5A1's natural level across 40 lines (lineage-adjusted; a glimpse) | r -0.69, reverse -0.62; direction not clear | 0.082 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.528). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.2, 3.9); signed map (41.2, 9.6). **Vector** length 91.5, 19.5% of its response variance represented; |z| ≥ 3 in 1,132 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.7 | +24.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.9 | +57.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +6.7 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +4.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +0.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +4.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -0.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.2 | +1.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +2.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.8 | -3.6 |
|  | [[NG25 (drug)]] 5 µM |  | -2.7 | -4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | +0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -2.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier organic anion transporter family member 5A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q13.3 — chr8:69,667,046-69,834,978 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OATPRP4, OATP-J, OATP5A1; previously SLC21A15 |
| Gene groups (HGNC) | Solute carrier organic anion transporter family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2Y9](https://www.uniprot.org/uniprotkb/Q9H2Y9) (Solute carrier organic anion transporter family member 5A1):

> Mediates the uptake of the hormone metabolite estrone-3-sulfate, the vitamin thiamine and the essential amino acid tyrosine. Mediates also efflux of L-glutamine and L-glycine.

**Summary**, from NCBI Gene [81796](https://www.ncbi.nlm.nih.gov/gene/81796):

> Predicted to enable transmembrane transporter activity. Predicted to be involved in sodium-independent organic anion transport. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19046](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19046) · Entrez [81796](https://www.ncbi.nlm.nih.gov/gene/81796) · UniProt [Q9H2Y9](https://www.uniprot.org/uniprotkb/Q9H2Y9) · Ensembl [ENSG00000137571](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137571)

## Data

Gene col 6036: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6036); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6036, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6036]; `tensor/DDL_lfc|DDL_z.npy` [6036]; `embed/gene_vectors.npy` [6036]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6036 or target_col == 6036). Every well: [[SLCO5A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLCO5A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
