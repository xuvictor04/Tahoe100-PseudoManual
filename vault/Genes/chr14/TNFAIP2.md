---
symbol: "TNFAIP2"
type: "gene"
col: 11639
ensembl_id: "ENSG00000185215"
name: "TNF alpha induced protein 2"
location: "14q32.32"
module: 14
arm: "+"
pooled_cpm: 62.5
n_lines_expressing: 28
n_dd_up: 31
n_dd_down: 7
n_dd_up_clean: 25
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 30
direction_downstream: 35
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# TNFAIP2

*TNF alpha induced protein 2* — 14q32.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 18.0× (z +40.2, q 0e+00, up in 26 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.572× (z -5.5, q 2e-05, down in 15 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STAT5A]] (+0.83, fdr 7e-06), [[CSF1]] (+0.77, fdr 7e-06), [[BCL3]] (+0.77, fdr 7e-06); moves opposite to [[THBD]] (-0.57, fdr 2e-05), [[HERC2P3]] (-0.57, fdr 3e-05), [[WDR37]] (-0.57, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 30 arrows point to it, the strongest [[STAT5A]] → it (grade B ⚠); 35 go from it, the strongest it → [[BCL3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11639.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **18.0×** | +40.2 | 0e+00 | 26/26 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **13.3×** | +24.5 | 0e+00 | 26/26 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **8.71×** | +21.3 | 0e+00 | 26/26 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **6.28×** | +18.1 | 0e+00 | 25/26 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +10.7 | 9e-25 | 19/26 (J82, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.96×** | +9.3 | 9e-19 | 24/26 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.33×** | +8.3 | 8e-15 | 20/26 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.28×** | +8.1 | 5e-14 | 24/26 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.23×** | +7.3 | 2e-11 | 15/25 (J82, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.02×** | +6.9 | 3e-10 | 25/26 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.95×** | +6.5 | 3e-09 | 19/26 (SW 900, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +4.5 | 3e-04 | 17/25 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +4.5 | 3e-04 | 10/26 (J82, HOP62, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.61×** | +4.5 | 3e-04 | 17/26 (PANC-1, SNU-423, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.43×** | +4.1 | 0.001 | 16/26 (AsPC-1, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.46×** | +4.1 | 0.002 | 14/26 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.003 | 15/26 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.51×** | +3.7 | 0.005 | 15/25 (A549, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.016 | 15/25 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11639.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.572×** | -5.5 | 2e-05 | 15/26 (A549, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.586×** | -5.3 | 3e-05 | 13/26 (HT-29, A549, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.623×** | -4.6 | 6e-04 | 16/26 (MIA PaCa-2, HT-29, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.659×** | -4.1 | 0.006 | 13/26 (A549, NCI-H2347, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.671×** | -3.9 | 0.010 | 14/26 (A498, Panc 03.27, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.691×** | -3.7 | 0.022 | 18/26 (Panc 03.27, A498, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.698×** | -3.4 | 0.047 | 7/25 (MIA PaCa-2, Panc 03.27, …) | top dose only | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.729× | -3.1 | 0.11 | 11/26 (SW 1088, A498, …) | two highest doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | 0.552× | -3.1 | 0.11 | 15/26 (A498, PANC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.805× | -3.1 | 0.11 | 11/26 (SW 900, HT-29, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | 0.733× | -3.1 | 0.11 | 10/26 (BT-474, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11639. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 113 | 7 (1 ⚠) | 6 | [[Adagrasib (drug)]] 0.05 µM 2.55× (z +19.7) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 7.09× (z +16.6) | [[Panobinostat (drug)]] 5 µM 0.191× (z -9.9) |
| [[A498 (line)]] | wt | 255 | 6 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.72× (z +27.6) | [[Bortezomib (drug)]] 5 µM 0.0945× (z -11.8) ⚠ toxic; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.361× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 38.7 | 11 | 0 | [[Homoharringtonine (drug)]] 5 µM 75.1× (z +31.5) | — |
| [[NCI-H460 (line)]] | wt | 41.4 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +27.4) | — |
| [[A549 (line)]] | wt | 190 | 5 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +26.5) | [[Panobinostat (drug)]] 5 µM 0.218× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 176 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +31.2) | — |
| [[NCI-H1792 (line)]] | alt | 59.3 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 25.6× (z +21.2) | — |
| [[Panc 03.27 (line)]] | alt | 197 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +31.1) | [[Auranofin (drug)]] 5 µM 0.190× (z -12.6) |
| [[PANC-1 (line)]] | alt | 78.1 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 40.1× (z +40.0) | — |
| [[HOP62 (line)]] | alt | 30.2 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 109× (z +33.9) | — |
| [[hTERT-HPNE (line)]] | wt | 40.7 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 139× (z +29.4) | — |
| [[J82 (line)]] | alt | 74.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 57.3× (z +30.8) | — |
| [[NCI-H2347 (line)]] | alt | 71.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.8× (z +26.9) | — |
| [[SW 900 (line)]] | alt | 114 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.3× (z +23.1) | — |
| [[A-172 (line)]] | wt | 131 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.9× (z +22.7) | — |
| [[HS-578T (line)]] | alt | 30.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 33.7× (z +19.2) | — |
| [[CFPAC-1 (line)]] | alt | 237 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.2× (z +31.7) | — |
| [[RPMI-7951 (line)]] | alt | 29.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.2× (z +19.1) | — |
| [[SNU-423 (line)]] | alt | 37.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 77.6× (z +28.2) | — |
| [[Hs 766T (line)]] | wt | 57.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.51× (z +15.7) | — |
| [[HT-29 (line)]] | alt | 52.9 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +14.2) | [[Panobinostat (drug)]] 5 µM 0.110× (z -12.5) |
| [[BT-474 (line)]] | alt | 95.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.4× (z +22.6) | — |
| [[KATO III (line)]] | alt | 17.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +17.2) | — |
| [[NCI-H1573 (line)]] | alt | 22.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.14× (z +12.2) | — |
| [[SW 1088 (line)]] | alt | 80.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.3× (z +13.1) | — |
| [[A-427 (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.98 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.83 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 8.07 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.4 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.22 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.74 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.52 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.45 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.03 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.25 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.50 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.68 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.99 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 12.9 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.13 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.08 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.59 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.87 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.86 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 13.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11639), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STAT5A]] | +0.83 | +0.84 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CSF1]] | +0.77 | +0.69 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[BCL3]] | +0.77 | +0.72 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[IRF1]] | +0.76 | +0.75 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[LINC02605]] | +0.76 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[CX3CL1]] | +0.74 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[EFNA1]] | +0.74 | +0.68 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[REL]] | +0.73 | +0.65 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CCL5]] | +0.72 | +0.67 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[CXCL3]] | +0.72 | +0.75 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[DENND2B]] | +0.72 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[CXCL2]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THBD]] | -0.57 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[HERC2P3]] | -0.57 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[WDR37]] | -0.57 | -0.49 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 20, C 10. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STAT5A]] | B | STAT5A activity raises TNFAIP2's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 2.38× lower at baseline in the lines without STAT5A | 0.004 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[QPCT]] | B | QPCT activity raises TNFAIP2's level | lines that do not express QPCT (25) vs lines expressing it (25) | 2.01× lower at baseline in the lines without QPCT | 0.006 | ⚠ within organs, on part of the lines; also absent: WFDC10B, LRRN1, KRT81 |
| [[ETS2]] | B | ETS2 activity raises TNFAIP2's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 3.35× lower at baseline in the lines without ETS2 | 0.008 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[LGALS3]] | B | LGALS3 activity raises TNFAIP2's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 4.05× lower at baseline in the lines without LGALS3 | 0.013 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[ADGRG1]] | B | ADGRG1 activity raises TNFAIP2's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 3.19× lower at baseline in the lines without ADGRG1 | 0.026 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[TLR3]] | B | TLR3 activity raises TNFAIP2's level | lines that do not express TLR3 (12) vs lines expressing it (38) | 2.96× lower at baseline in the lines without TLR3 | 0.035 | ⚠ within organs, on part of the lines; also absent: LGALS3, GBP4, RAB27B; maybe low, not absent |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises TNFAIP2's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.46× lower at baseline in the lines without ELF3-AS1 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[TSPAN15]] | B | TSPAN15 activity raises TNFAIP2's level | lines that do not express TSPAN15 (15) vs lines expressing it (35) | 2.45× lower at baseline in the lines without TSPAN15 | 0.044 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |
| [[LRRN1]] | B | LRRN1 activity raises TNFAIP2's level | lines that do not express LRRN1 (31) vs lines expressing it (19) | 2.03× lower at baseline in the lines without LRRN1 | 0.046 | ⚠ within organs, on part of the lines; also absent: TACSTD2, PRKCH-AS1, SERPINB3; maybe low, not absent |
| [[CD74]] | B | CD74 activity raises TNFAIP2's level | lines that do not express CD74 (31) vs lines expressing it (19) | 1.82× lower at baseline in the lines without CD74 | 0.054 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5 |
| [[NEURL3]] | B | NEURL3 activity raises TNFAIP2's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 3.97× lower at baseline in the lines without NEURL3 | 0.055 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[ANO9]] | B | ANO9 activity raises TNFAIP2's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 1.89× lower at baseline in the lines without ANO9 | 0.057 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 27, C 8. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL3]] | B | TNFAIP2 activity raises BCL3's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 1.97× lower at baseline in the lines without TNFAIP2 | 0.005 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[STAT5A]] | B | TNFAIP2 activity raises STAT5A's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 1.81× lower at baseline in the lines without TNFAIP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[IRF1]] | B | TNFAIP2 activity raises IRF1's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 1.72× lower at baseline in the lines without TNFAIP2 | 0.013 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[NR1D1]] | B | TNFAIP2 activity raises NR1D1's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 1.60× lower at baseline in the lines without TNFAIP2 | 0.013 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[B2M]] | B | TNFAIP2 activity raises B2M's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 1.90× lower at baseline in the lines without TNFAIP2 | 0.014 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[SOD2]] | B | TNFAIP2 activity raises SOD2's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 2.48× lower at baseline in the lines without TNFAIP2 | 0.019 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[APOL3]] | B | TNFAIP2 activity raises APOL3's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 2.32× lower at baseline in the lines without TNFAIP2 | 0.020 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[TSPAN15]] | B | TNFAIP2 activity raises TSPAN15's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 2.05× lower at baseline in the lines without TNFAIP2 | 0.022 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[ETS2]] | B | TNFAIP2 activity raises ETS2's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 2.01× lower at baseline in the lines without TNFAIP2 | 0.030 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[TNIP1]] | B | TNFAIP2 activity raises TNIP1's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 1.75× lower at baseline in the lines without TNFAIP2 | 0.030 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[APOL6]] | B | TNFAIP2 activity raises APOL6's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 1.95× lower at baseline in the lines without TNFAIP2 | 0.031 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[ZC3H12A]] | B | TNFAIP2 activity raises ZC3H12A's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 1.97× lower at baseline in the lines without TNFAIP2 | 0.034 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.872). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.8, 4.3); signed map (44.4, 7.3). **Vector** length 130, 45.3% of its response variance represented; |z| ≥ 3 in 956 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *inflammatory response* (hallmark, mean cos +0.58 to 22); *Chemokine receptors bind chemokines* (reactome, mean cos +0.59 to 8); *allograft rejection* (hallmark, mean cos +0.56 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.1 | +24.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +9.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.8 | +6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +40.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.1 | +18.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.0 | +4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.9 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.8 | +4.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.4 | +2.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.7 | -3.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~81% of this change | -5.6 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.3 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -5.1 | -2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.5 | -4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.4 | -1.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.1 | -3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | TNF alpha induced protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.32 — chr14:103,121,476-103,137,439 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B94, EXOC3L3 |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03169](https://www.uniprot.org/uniprotkb/Q03169) (Tumor necrosis factor alpha-induced protein 2):

> May play a role as a mediator of inflammation and angiogenesis.

**Summary**, from NCBI Gene [7127](https://www.ncbi.nlm.nih.gov/gene/7127):

> This gene was identified as a gene whose expression can be induced by the tumor necrosis factor alpha (TNF) in umbilical vein endothelial cells. The expression of this gene was shown to be induced by retinoic acid in a cell line expressing a oncogenic version of the retinoic acid receptor alpha fusion protein, which suggested that this gene may be a retinoic acid target gene in acute promyelocytic leukemia. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11895](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11895) · Entrez [7127](https://www.ncbi.nlm.nih.gov/gene/7127) · UniProt [Q03169](https://www.uniprot.org/uniprotkb/Q03169) · Ensembl [ENSG00000185215](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185215)

## Data

Gene col 11639: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11639); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11639, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11639]; `tensor/DDL_lfc|DDL_z.npy` [11639]; `embed/gene_vectors.npy` [11639]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11639 or target_col == 11639). Every well: [[TNFAIP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFAIP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
