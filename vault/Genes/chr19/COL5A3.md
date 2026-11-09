---
symbol: "COL5A3"
type: "gene"
col: 1285
ensembl_id: "ENSG00000080573"
name: "collagen type V alpha 3 chain"
location: "19p13.2"
module: 13
arm: "+"
pooled_cpm: 13.13
n_lines_expressing: 26
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 21
direction_downstream: 27
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# COL5A3

*collagen type V alpha 3 chain* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 4.27× (z +17.5, q 0e+00, up in 17 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.622× (z -4.1, q 0.010, down in 12 of 22 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Budesonide (drug)]] 5 µM: 0.624× (z -4.1, q 0.010, down in 7 of 24 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0436×; ⚠ cell-cycle shift, explains ~34% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0663×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSF1R]] (+0.70, fdr 7e-06), [[IL11]] (+0.68, fdr 7e-06), [[COL7A1]] (+0.66, fdr 7e-06); moves opposite to [[CHPT1]] (-0.52, fdr 3e-05), [[ZFYVE9]] (-0.48, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[COL1A1]] → it (grade B ⚠); 27 go from it, the strongest it → [[RETREG1-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1285.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **4.27×** | +17.5 | 0e+00 | 17/22 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **7.33×** | +17.0 | 0e+00 | 19/23 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.83×** | +15.0 | 0e+00 | 16/21 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.46×** | +14.9 | 0e+00 | 16/19 (A-172, A549, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **5.09×** | +13.8 | 2e-41 | 16/22 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **4.11×** | +11.6 | 7e-29 | 17/22 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.23×** | +10.0 | 2e-21 | 17/23 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.11×** | +8.9 | 3e-17 | 3/11 (SW480, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.53×** | +7.9 | 2e-13 | 16/22 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.55×** | +7.6 | 1e-12 | 2/8 (A498, SW1417) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.28×** | +7.0 | 1e-10 | 13/19 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **2.03×** | +6.0 | 9e-08 | 4/15 (NCI-H460, SW480, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +5.6 | 1e-06 | 8/20 (SK-MEL-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.75×** | +4.7 | 9e-05 | 14/22 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.59×** | +3.8 | 0.005 | 9/17 (NCI-H460, SW480, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.026 | 4/21 (SW480, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1285.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0436×; ⚠ cell-cycle shift, explains ~34% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0663×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.622×** | -4.1 | 0.010 | 12/22 (A498, RPMI-7951, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.624×** | -4.1 | 0.010 | 7/24 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.601×** | -4.0 | 0.010 | 7/20 (RPMI-7951, HOP62, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.697× | -3.1 | 0.27 | 8/23 (HOP62, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1285. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.42 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 25.6× (z +16.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 11.9× (z +12.3) | — |
| [[SW480 (line)]] | alt | 5.18 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 6.14× (z +11.9) | — |
| [[A-172 (line)]] | wt | 15.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 24.5× (z +20.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 40.6× (z +16.1) | — |
| [[A549 (line)]] | wt | 5.26 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 37.8× (z +17.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 34.1× (z +11.4) | — |
| [[A498 (line)]] | wt | 5.98 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.07× (z +14.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.03× (z +9.6) | — |
| [[HS-578T (line)]] | alt | 96.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +11.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 7.37× (z +10.8) | — |
| [[hTERT-HPNE (line)]] | wt | 269 | 0 | 2 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0436× (z -10.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SK-MEL-2 (line)]] | alt | 5.47 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +11.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 50.8× (z +11.6) | — |
| [[SNU-423 (line)]] | alt | 5.72 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 26.8× (z +14.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 28.3× (z +10.1) | — |
| [[C32 (line)]] | wt | 5.39 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 14.6× (z +8.5) | — |
| [[H4 (line)]] | wt | 8.70 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.0× (z +11.2) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SW1417 (line)]] | alt | 6.82 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.04× (z +9.8) | — |
| [[A-427 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1285), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSF1R]] | +0.70 | +0.72 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[IL11]] | +0.68 | +0.63 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[COL7A1]] | +0.66 | +0.62 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 542 |
| [[KCNN3]] | +0.66 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[VAT1L]] | +0.65 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[GPR68]] | +0.63 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[APCDD1L-DT]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[ITGA11]] | +0.63 | +0.55 / +0.63 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[ADAMTSL1]] | +0.61 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[NTNG2]] | +0.60 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[CYTH4]] | +0.59 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[SAMD3]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHPT1]] | -0.52 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[ZFYVE9]] | -0.48 | -0.47 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 6, C 15. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL1A1]] | B | COL1A1 activity raises COL5A3's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 3.77× lower at baseline in the lines without COL1A1 | 0.005 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411 |
| [[CSF1R]] | B | CSF1R activity raises COL5A3's level | lines that do not express CSF1R (26) vs lines expressing it (24) | 2.61× lower at baseline in the lines without CSF1R | 0.043 | ⚠ within organs, on part of the lines; also absent: FKBP9P1-1, TIMP3, GDNF; maybe low, not absent |
| [[COL7A1]] | B | COL7A1 activity raises COL5A3's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 2.56× lower at baseline in the lines without COL7A1 | 0.046 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |
| [[MEG3]] | B | MEG3 activity raises COL5A3's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 2.50× lower at baseline in the lines without MEG3 | 0.049 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8 |
| [[NR3C1]] | B | NR3C1 activity lowers COL5A3's level | compounds that target NR3C1: 2 of 3 lower it (Betamethasone dipropionate, Budesonide) | 67% of the class's compounds vs 0.8% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds |
| [[BDKRB2]] | B | BDKRB2 activity raises COL5A3's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 1.97× lower at baseline in the lines without BDKRB2 | 0.095 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[GDNF]] | C | GDNF activity raises COL5A3's level | lines that do not express GDNF (38) vs lines expressing it (12) | 5.69× lower at baseline in the lines without GDNF | 1e-03 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9; co-absent with the target |
| [[GREM1]] | C | GREM1 activity raises COL5A3's level | lines that do not express GREM1 (38) vs lines expressing it (12) | 3.10× lower at baseline in the lines without GREM1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000203434, LINC01098, AFP; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises COL5A3's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 4.66× lower at baseline in the lines without APCDD1L | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises COL5A3's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 4.18× lower at baseline in the lines without ITGA11 | 0.005 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[INSYN2B]] | C | INSYN2B activity raises COL5A3's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 3.89× lower at baseline in the lines without INSYN2B | 0.020 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5; co-absent with the target |
| [[HHIP]] | C | HHIP activity raises COL5A3's level | lines that do not express HHIP (33) vs lines expressing it (17) | 2.84× lower at baseline in the lines without HHIP | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 16, C 11. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RETREG1-AS1]] | B | COL5A3 activity raises RETREG1-AS1's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 1.19× lower at baseline in the lines without COL5A3 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1 |
| [[CLIP2]] | B | COL5A3 activity raises CLIP2's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 1.46× lower at baseline in the lines without COL5A3 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1 |
| [[COL7A1]] | B | COL5A3 activity raises COL7A1's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 2.47× lower at baseline in the lines without COL5A3 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1 |
| [[MYO10]] | B | COL5A3 activity raises MYO10's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 1.96× lower at baseline in the lines without COL5A3 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1 |
| [[CAVIN1]] | B | COL5A3 activity raises CAVIN1's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 2.28× lower at baseline in the lines without COL5A3 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1 |
| [[GDNF-AS1]] | B | COL5A3 activity raises GDNF-AS1's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 1.88× lower at baseline in the lines without COL5A3 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1 |
| [[FMNL3]] | B | COL5A3 activity raises FMNL3's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 2.24× lower at baseline in the lines without COL5A3 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1 |
| [[FZD8]] | B | COL5A3 activity raises FZD8's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 1.76× lower at baseline in the lines without COL5A3 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1 |
| [[TGFB1]] | B | COL5A3 activity raises TGFB1's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 2.00× lower at baseline in the lines without COL5A3 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1 |
| [[APCDD1L-DT]] | B | COL5A3 activity raises APCDD1L-DT's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 2.69× lower at baseline in the lines without COL5A3 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1 |
| [[NMNAT2]] | B | COL5A3 activity weakens NMNAT2's drug response | lines that do not express COL5A3 (14) vs lines expressing it (15) | the lines without COL5A3 respond 2.36× as strongly (z diff -2.14); strongest at Tucidinostat 0.5 µM: 3.93x vs 2.26x (z diff -3.7) | 0.069 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1; target measured in part of the lines; artifact flags |
| [[MEG3]] | B | COL5A3 activity raises MEG3's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 1.90× lower at baseline in the lines without COL5A3 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.604). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.8, 14.0); signed map (21.1, 44.9). **Vector** length 74.8, 21.9% of its response variance represented; |z| ≥ 3 in 620 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +17.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.6 | +11.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.0 | +14.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.8 | +7.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.6 | +17.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.2 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +1.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -4.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -4.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -1.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.8 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | collagen type V alpha 3 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:9,959,561-10,010,504 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Fibrillar collagens |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 30 pathways, smallest: Fibronectin matrix formation; Attachment of bacteria to epithelial cells; Biofilm formation |
| Matched by | ensembl_id |

**Function**, from UniProt [P25940](https://www.uniprot.org/uniprotkb/P25940) (Collagen alpha-3(V) chain):

> Type V collagen is a member of group I collagen (fibrillar forming collagen). It is a minor connective tissue component of nearly ubiquitous distribution. Type V collagen binds to DNA, heparan sulfate, thrombospondin, heparin, and insulin.

**Summary**, from NCBI Gene [50509](https://www.ncbi.nlm.nih.gov/gene/50509):

> This gene encodes an alpha chain for one of the low abundance fibrillar collagens. Fibrillar collagen molecules are trimers that can be composed of one or more types of alpha chains. Type V collagen is found in tissues containing type I collagen and appears to regulate the assembly of heterotypic fibers composed of both type I and type V collagen. This gene product is closely related to type XI collagen and it is possible that the collagen chains of types V and XI constitute a single collagen …

**Accessions** — [HGNC:14864](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14864) · Entrez [50509](https://www.ncbi.nlm.nih.gov/gene/50509) · UniProt [P25940](https://www.uniprot.org/uniprotkb/P25940) · Ensembl [ENSG00000080573](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080573)

## Data

Gene col 1285: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1285); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1285, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1285]; `tensor/DDL_lfc|DDL_z.npy` [1285]; `embed/gene_vectors.npy` [1285]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1285 or target_col == 1285). Every well: [[COL5A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL5A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
