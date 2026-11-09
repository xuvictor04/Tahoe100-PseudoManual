---
symbol: "SEMA6B"
type: "gene"
col: 9517
ensembl_id: "ENSG00000167680"
name: "semaphorin 6B"
location: "19p13.3"
module: 100
arm: "+"
pooled_cpm: 9.51
n_lines_expressing: 36
n_dd_up: 15
n_dd_down: 22
n_dd_up_clean: 11
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 12
direction_downstream: 41
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# SEMA6B

*semaphorin 6B* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.67× (z +18.1, q 0e+00, up in 30 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.592× (z -6.8, q 5e-09, down in 16 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADGRB2]] (+0.65, fdr 1e-05), [[TMCC2]] (+0.63, fdr 1e-05), [[ADGRL1]] (+0.63, fdr 8e-06); moves opposite to [[GPATCH2]] (-0.55, fdr 7e-05), [[ENOX2]] (-0.50, fdr 1e-04), [[UBE3B]] (-0.50, fdr 2e-04).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[KREMEN2]] → it (grade B ⚠); 41 go from it, the strongest it → [[ARRB2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9517.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.67×** | +18.1 | 0e+00 | 30/33 (A-172, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.43×** | +16.1 | 0e+00 | 31/33 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +8.4 | 1e-14 | 6/14 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.81×** | +7.7 | 2e-12 | 20/33 (A-172, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +7.4 | 1e-11 | 21/33 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +5.7 | 1e-06 | 11/33 (PANC-1, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.52×** | +5.5 | 4e-06 | 12/23 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.73×** | +4.7 | 2e-04 | 7/28 (SW480, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +4.6 | 2e-04 | 12/33 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +4.6 | 3e-04 | 14/32 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.89×** | +4.3 | 7e-04 | 10/34 (NCI-H23, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.86×** | +4.2 | 0.001 | 5/22 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 0.5 µM |  | **1.65×** | +4.2 | 0.001 | 8/33 (A-172, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.083 | 7/28 (SK-MEL-2, NCI-H661, …) | inconsistent across doses |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.26×** | +3.1 | 0.084 | 5/33 (SW 900, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9517.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.592×** | -6.8 | 5e-09 | 16/33 (AN3 CA, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.612×** | -6.4 | 4e-08 | 18/33 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.618×** | -6.3 | 6e-08 | 18/31 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.642×** | -5.8 | 9e-07 | 17/33 (LOX-IMVI, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.642×** | -5.8 | 9e-07 | 20/33 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.666×** | -5.3 | 1e-05 | 14/33 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.690×** | -4.8 | 1e-04 | 15/30 (AN3 CA, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.710×** | -4.5 | 5e-04 | 12/32 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.719×** | -4.3 | 0.001 | 14/33 (A-427, HepG2/C3A, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.712×** | -4.3 | 0.001 | 8/33 (LoVo, NCI-H23, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.728×** | -4.1 | 0.002 | 11/33 (A-427, MIA PaCa-2, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.554×** | -4.0 | 0.003 | 11/28 (A-427, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.813×** | -3.8 | 0.006 | 13/34 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.817×** | -3.7 | 0.008 | 9/34 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.603×** | -3.5 | 0.021 | 5/34 (MIA PaCa-2, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.771×** | -3.4 | 0.025 | 9/33 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.837× | -3.3 | 0.033 | 11/34 (A-427, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9517. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 51.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.207× (z -12.8) |
| [[A-172 (line)]] | wt | 17.0 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.35× (z +10.9) | — |
| [[A-427 (line)]] | wt | 18.9 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.220× (z -10.2) |
| [[C-33 A (line)]] | alt | 19.9 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.113× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 9.06 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.63× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 31.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 28.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -11.2) |
| [[A498 (line)]] | wt | 14.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.42× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 30.9 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0791× (z -8.9) |
| [[H4 (line)]] | wt | 7.19 | 0 | 1 | — | [[Norepinephrine (hydrochloride) (drug)]] 0.5 µM 0.0578× (z -8.9) |
| [[HCT15 (line)]] | alt | 8.06 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0788× (z -8.6) |
| [[LoVo (line)]] | wt | 10.8 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.167× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 11.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.87× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 19.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.313× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 15.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0880× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 4.49 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.18× (z +9.6) | — |
| [[PANC-1 (line)]] | alt | 3.62 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.89× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 2.45 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 12.1× (z +9.3) | — |
| [[SW48 (line)]] | wt | 8.19 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 9.88 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -9.9) |
| [[A549 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.972 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9517), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRB2]] | +0.65 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[TMCC2]] | +0.63 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[ADGRL1]] | +0.63 | +0.57 / +0.62 | both halves | 8e-06 |  |
| [[REEP2]] | +0.62 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[KCNQ2]] | +0.61 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[NRTN]] | +0.61 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[SHF]] | +0.61 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[CFD]] | +0.60 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[LINC00937]] | +0.60 | +0.46 / +0.67 | both halves | 3e-05 |  |
| [[RPS6KA1]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[NOVA2]] | +0.59 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[MAST1]] | +0.58 | +0.45 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH2]] | -0.55 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[ENOX2]] | -0.50 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[UBE3B]] | -0.50 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[RABL2B]] | -0.49 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[AVEN]] | -0.48 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[RABL2A]] | -0.48 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[NEK11]] | -0.48 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[NIPAL2]] | -0.47 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KREMEN2]] | B | KREMEN2 activity raises SEMA6B's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 2.35× lower at baseline in the lines without KREMEN2 | 0.016 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |
| [[TSPAN33]] | B | TSPAN33 activity raises SEMA6B's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 2.46× lower at baseline in the lines without TSPAN33 | 0.022 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[SLC29A4]] | B | SLC29A4 activity raises SEMA6B's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 3.81× lower at baseline in the lines without SLC29A4 | 0.023 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[NOVA2]] | B | NOVA2 activity raises SEMA6B's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 2.21× lower at baseline in the lines without NOVA2 | 0.037 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1 |
| [[LHX2]] | B | LHX2 activity raises SEMA6B's level | lines that do not express LHX2 (26) vs lines expressing it (24) | 1.93× lower at baseline in the lines without LHX2 | 0.038 | ⚠ within organs, on part of the lines; also absent: CECR2, COL4A4, GHR |
| [[PARD6G]] | B | PARD6G activity raises SEMA6B's level | lines that do not express PARD6G (10) vs lines expressing it (40) | 2.96× lower at baseline in the lines without PARD6G | 0.041 | ⚠ within organs, on part of the lines; also absent: CTXN1, NT5M, RRAGD; maybe low, not absent |
| [[TLE2]] | B | TLE2 activity raises SEMA6B's level | lines that do not express TLE2 (10) vs lines expressing it (40) | 2.29× lower at baseline in the lines without TLE2 | 0.044 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC02643]] | B | LINC02643 activity raises SEMA6B's level | lines that do not express LINC02643 (38) vs lines expressing it (12) | 2.85× lower at baseline in the lines without LINC02643 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, GCG, ENSG00000289530 |
| [[SEPTIN3]] | B | SEPTIN3 activity raises SEMA6B's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 2.17× lower at baseline in the lines without SEPTIN3 | 0.048 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[PDZD4]] | B | PDZD4 activity raises SEMA6B's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 1.99× lower at baseline in the lines without PDZD4 | 0.050 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[MAN1C1]] | B | MAN1C1 activity raises SEMA6B's level | lines that do not express MAN1C1 (11) vs lines expressing it (39) | 2.41× lower at baseline in the lines without MAN1C1 | 0.063 | ⚠ within organs, on part of the lines; also absent: DHRS2; maybe low, not absent |
| [[MYT1]] | B | MYT1 activity raises SEMA6B's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 2.19× lower at baseline in the lines without MYT1 | 0.095 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2 |

### Downstream of this gene

*41 arrows, 41 of them with an alert ⚠; grade A 0, B 40, C 1. Shown: the 12 strongest; 29 more arrows (29 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARRB2]] | B | SEMA6B activity raises ARRB2's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.76× lower at baseline in the lines without SEMA6B | 0.002 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[TMCC2]] | B | SEMA6B activity raises TMCC2's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.89× lower at baseline in the lines without SEMA6B | 0.003 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[TSPAN33]] | B | SEMA6B activity raises TSPAN33's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 2.09× lower at baseline in the lines without SEMA6B | 0.004 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[SEPTIN6]] | B | SEMA6B activity raises SEPTIN6's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.67× lower at baseline in the lines without SEMA6B | 0.006 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[ADGRB2]] | B | SEMA6B activity raises ADGRB2's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.73× lower at baseline in the lines without SEMA6B | 0.006 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[ADGRL1]] | B | SEMA6B activity raises ADGRL1's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 2.18× lower at baseline in the lines without SEMA6B | 0.006 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[ATP1A3]] | B | SEMA6B activity raises ATP1A3's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 2.00× lower at baseline in the lines without SEMA6B | 0.007 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[MAST1]] | B | SEMA6B activity raises MAST1's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 2.00× lower at baseline in the lines without SEMA6B | 0.008 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[NOVA2]] | B | SEMA6B activity raises NOVA2's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 2.49× lower at baseline in the lines without SEMA6B | 0.009 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[REEP2]] | B | SEMA6B activity raises REEP2's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 2.06× lower at baseline in the lines without SEMA6B | 0.009 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[NPTXR]] | B | SEMA6B activity raises NPTXR's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 2.19× lower at baseline in the lines without SEMA6B | 0.009 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[ASIC1]] | B | SEMA6B activity raises ASIC1's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.84× lower at baseline in the lines without SEMA6B | 0.012 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.774). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (2.5, 35.9); signed map (20.5, 22.2). **Vector** length 75.7, 16.4% of its response variance represented; |z| ≥ 3 in 801 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.1 | +18.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.4 | +16.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.9 | +7.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.6 | +4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +4.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.9 | +7.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +4.7 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +2.0 | +4.2 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.0 | -6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -5.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.9 | -0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -3.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | semaphorin 6B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:4,542,593-4,581,776 (-) |
| Ensembl biotype | protein_coding |
| Also known as | semaZ, SEMA-VIB, SEM-SEMA-Z; previously SEMAN |
| Gene groups (HGNC) | Semaphorins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3T3](https://www.uniprot.org/uniprotkb/Q9H3T3) (Semaphorin-6B):

> Functions as a cell surface repellent for mossy fibers of developing neurons in the hippocampus where it plays a role in axon guidance. May function through the PLXNA4 receptor expressed by mossy cell axons.; (Microbial infection) Acts as a receptor for P.sordellii toxin TcsL in the in the vascular endothelium.

**Summary**, from NCBI Gene [10501](https://www.ncbi.nlm.nih.gov/gene/10501):

> This gene encodes a member of the semaphorin family, a group of proteins characterized by the presence of a conserved semaphorin (sema) domain. Whereas some semaphorins are transmembrane proteins, others are secreted. Semaphorins play a major role in axon guidance. The protein encoded by this gene may be involved in both peripheral and central nervous system development. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10739](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10739) · Entrez [10501](https://www.ncbi.nlm.nih.gov/gene/10501) · UniProt [Q9H3T3](https://www.uniprot.org/uniprotkb/Q9H3T3) · Ensembl [ENSG00000167680](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167680)

## Data

Gene col 9517: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9517); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9517, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9517]; `tensor/DDL_lfc|DDL_z.npy` [9517]; `embed/gene_vectors.npy` [9517]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9517 or target_col == 9517). Every well: [[SEMA6B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEMA6B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
