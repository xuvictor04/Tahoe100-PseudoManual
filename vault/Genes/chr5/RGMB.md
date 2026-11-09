---
symbol: "RGMB"
type: "gene"
col: 10465
ensembl_id: "ENSG00000174136"
name: "repulsive guidance molecule BMP co-receptor b"
location: "5q15"
module: 151
arm: "+"
pooled_cpm: 26.1
n_lines_expressing: 49
n_dd_up: 27
n_dd_down: 4
n_dd_up_clean: 20
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 20
direction_downstream: 0
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# RGMB

*repulsive guidance molecule BMP co-receptor b* — 5q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.85× (z +16.0, q 0e+00, up in 31 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.707× (z -6.5, q 6e-08, down in 22 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.812× (z -3.9, q 0.027, down in 12 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 19 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.133×, J82 0.392×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 0.220×, J82 0.385×); [[Dinaciclib (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.0711×, NCI-H2347 0.187×; ⚠ toxic; transcription drop); [[Binimetinib (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.216×, RKO 0.387×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDE4DIPP2]] (+0.63, fdr 7e-06), [[RPSAP52]] (+0.61, fdr 9e-06), [[BNC1]] (+0.60, fdr 1e-05); moves opposite to [[UBE2H]] (-0.44, fdr 3e-05), [[MAP3K13]] (-0.41, fdr 7e-05), [[CEP126]] (-0.40, fdr 1e-04).
> It is in [[Module 151]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[RGS4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10465.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.85×** | +16.0 | 0e+00 | 31/46 (CFPAC-1, C32, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +14.2 | 3e-43 | 31/44 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.72×** | +10.0 | 3e-21 | 29/46 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +9.5 | 3e-19 | 28/43 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +8.2 | 2e-14 | 23/47 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.56×** | +8.2 | 2e-14 | 26/46 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.34×** | +7.7 | 1e-12 | 22/47 (H4, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.16×** | +7.4 | 8e-12 | 27/47 (MIA PaCa-2, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +7.2 | 3e-11 | 23/44 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.47×** | +7.1 | 7e-11 | 22/46 (MIA PaCa-2, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +7.0 | 2e-10 | 22/46 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +6.7 | 1e-09 | 23/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +6.6 | 1e-09 | 21/47 (Hs 766T, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +6.5 | 3e-09 | 22/45 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.42×** | +6.4 | 6e-09 | 22/46 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +5.8 | 3e-07 | 19/46 (CFPAC-1, C32, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +5.6 | 9e-07 | 18/44 (C32, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.33×** | +5.3 | 5e-06 | 21/46 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10465.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 19 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.133×, J82 0.392×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 0.220×, J82 0.385×); [[Dinaciclib (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.0711×, NCI-H2347 0.187×; ⚠ toxic; transcription drop); [[Binimetinib (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.216×, RKO 0.387×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.707×** | -6.5 | 6e-08 | 22/39 (PANC-1, A549, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.812×** | -3.9 | 0.027 | 12/46 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.816×** | -3.7 | 0.046 | 16/27 (MIA PaCa-2, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.833×** | -3.4 | 0.085 | 12/46 (HOP62, HS-578T, …) | top dose only |  |
| [[Retinoic acid (drug)]] 5 µM |  | 0.886× | -3.2 | 0.14 | 10/47 (J82, RKO, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10465. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 199 | 0 | 14 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -24.8) |
| [[HOP62 (line)]] | alt | 81.5 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.80× (z +11.3) | [[Tucidinostat (drug)]] 0.5 µM 0.361× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Clobetasol propionate (drug)]] 5 µM 0.367× (z -8.6) |
| [[J82 (line)]] | alt | 93.3 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.309× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.385× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 39.8 | 0 | 3 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.376× (z -22.4) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 5 µM 0.216× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 11.5 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.94× (z +13.0) | — |
| [[A549 (line)]] | wt | 8.97 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -10.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 10.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +12.2) | — |
| [[Hs 766T (line)]] | wt | 24.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.0) | — |
| [[LoVo (line)]] | wt | 15.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +11.1) | — |
| [[A498 (line)]] | wt | 21.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +10.2) | — |
| [[C-33 A (line)]] | alt | 8.92 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0917× (z -8.7) |
| [[C32 (line)]] | wt | 15.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +11.5) | — |
| [[HS-578T (line)]] | alt | 32.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +10.2) | — |
| [[HT-29 (line)]] | alt | 17.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 14.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -9.1) ⚠ cell-cycle shift, explains ~79% of this change |
| [[NCI-H2347 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -11.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 30.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -10.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 11.5 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.5 µM 0.0906× (z -8.5) |
| [[SNU-423 (line)]] | alt | 20.5 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.153× (z -11.6) |
| [[SW 1271 (line)]] | alt | 41.8 | 0 | 1 | — | [[Levobupivacaine (hydrochloride) (drug)]] 5 µM 0.0615× (z -8.6) |
| [[SW480 (line)]] | alt | 12.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +9.5) | — |
| [[A-172 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.38 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 70.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10465), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE4DIPP2]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[RPSAP52]] | +0.61 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[BNC1]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[NBPF9]] | +0.59 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[RDUR]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[FGF5]] | +0.57 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[RGS4]] | +0.57 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[VEPH1]] | +0.57 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[IQCJ-SCHIP1]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[NLRP3]] | +0.54 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[SCHIP1]] | +0.54 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[ADAMTS6]] | +0.53 | +0.48 / +0.56 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2H]] | -0.44 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[MAP3K13]] | -0.41 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[CEP126]] | -0.40 | -0.35 / -0.37 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 18, C 2. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGS4]] | B | RGS4 activity raises RGMB's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 2.36× lower at baseline in the lines without RGS4 | 8e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486 |
| [[LINC01812]] | B | LINC01812 activity raises RGMB's level | lines that do not express LINC01812 (35) vs lines expressing it (15) | 2.12× lower at baseline in the lines without LINC01812 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235495, ENSG00000224865, ENSG00000287622 |
| [[LINC01592]] | B | LINC01592 activity raises RGMB's level | lines that do not express LINC01592 (35) vs lines expressing it (15) | 2.44× lower at baseline in the lines without LINC01592 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHRDL1, ESM1, CCL3; maybe low, not absent |
| [[CCDC190]] | B | CCDC190 activity raises RGMB's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 2.39× lower at baseline in the lines without CCDC190 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337 |
| [[ROBO4]] | B | ROBO4 activity raises RGMB's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 1.99× lower at baseline in the lines without ROBO4 | 0.005 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[ADAMTS6]] | B | ADAMTS6 activity raises RGMB's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 1.89× lower at baseline in the lines without ADAMTS6 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2 |
| [[EVC]] | B | EVC activity raises RGMB's level | lines that do not express EVC (13) vs lines expressing it (37) | 1.50× lower at baseline in the lines without EVC | 0.008 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: RNF150, PYGO1, EHD3 |
| [[FGF5]] | B | FGF5 activity raises RGMB's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 2.09× lower at baseline in the lines without FGF5 | 0.009 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702 |
| [[RGS4]] | B | RGS4 activity weakens RGMB's drug response | lines that do not express RGS4 (34) vs lines expressing it (13) | the lines without RGS4 respond 4.23× as strongly (z diff -2.33); strongest at Idarubicin (hydrochloride) 5 µM: 1.90x vs 0.82x (z diff -6.5) | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486; target measured in part of the lines; artifact flags |
| [[LNCOG]] | B | LNCOG activity raises RGMB's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 2.04× lower at baseline in the lines without LNCOG | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1 |
| [[CCDC190]] | B | CCDC190 activity weakens RGMB's drug response | lines that do not express CCDC190 (37) vs lines expressing it (10) | the lines without CCDC190 respond 2.37× as strongly (z diff -1.72); strongest at Idarubicin (hydrochloride) 5 µM: 1.86x vs 0.68x (z diff -7.9) | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337; target measured in part of the lines; artifact flags |
| [[FGF5]] | B | FGF5 activity weakens RGMB's drug response | lines that do not express FGF5 (27) vs lines expressing it (20) | the lines without FGF5 respond 2.03× as strongly (z diff -1.57); strongest at Idarubicin (hydrochloride) 5 µM: 2.16x vs 0.95x (z diff -6.3) | 0.068 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.466). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.4, 13.2); signed map (17.0, 46.6). **Vector** length 99.2, 22.5% of its response variance represented; |z| ≥ 3 in 1,317 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.2 | +7.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.7 | +5.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.6 | +6.4 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +3.4 | +1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.3 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +5.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.6 | +2.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.3 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -2.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | -1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.6 | -6.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | -0.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.9 | -2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | repulsive guidance molecule BMP co-receptor b |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q15 — chr5:98,768,650-98,798,643 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ90406, DRAGON |
| Gene groups (HGNC) | Repulsive guidance molecule family |
| Reactome | 3 pathways, smallest: Netrin-1 signaling; Axon guidance; Nervous system development |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NW40](https://www.uniprot.org/uniprotkb/Q6NW40) (Repulsive guidance molecule B):

> Member of the repulsive guidance molecule (RGM) family that contributes to the patterning of the developing nervous system (By similarity). Acts as a bone morphogenetic protein (BMP) coreceptor that potentiates BMP signaling (By similarity). Promotes neuronal adhesion (By similarity). May inhibit neurite outgrowth.

**Summary**, from NCBI Gene [285704](https://www.ncbi.nlm.nih.gov/gene/285704):

> RGMB is a glycosylphosphatidylinositol (GPI)-anchored member of the repulsive guidance molecule family (see RGMA, MIM 607362) and contributes to the patterning of the developing nervous system (Samad et al., 2005 [PubMed 15671031]).[supplied by OMIM, Apr 2009]

**Accessions** — [HGNC:26896](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26896) · Entrez [285704](https://www.ncbi.nlm.nih.gov/gene/285704) · UniProt [Q6NW40](https://www.uniprot.org/uniprotkb/Q6NW40) · Ensembl [ENSG00000174136](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174136)

## Data

Gene col 10465: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10465); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10465, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10465]; `tensor/DDL_lfc|DDL_z.npy` [10465]; `embed/gene_vectors.npy` [10465]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10465 or target_col == 10465). Every well: [[RGMB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RGMB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
