---
symbol: "PIK3IP1-DT"
type: "gene"
col: 13678
ensembl_id: "ENSG00000228839"
name: "PIK3IP1 divergent transcript"
location: "22q12.2"
module: 181
arm: "+"
pooled_cpm: 6.44
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 9
n_dd_up_clean: 31
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/181"]
generated_by: "tahoemap"
---

# PIK3IP1-DT

*PIK3IP1 divergent transcript* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 11.6× (z +44.3, q 0e+00, up in 39 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.524× (z -8.3, q 6e-14, down in 24 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[NG25 (drug)]] 5 µM: 0.430× (z -5.7, q 4e-06, down in 11 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPHS1]] (+0.70, fdr 7e-06), [[HSD11B1-AS1]] (+0.69, fdr 1e-05), [[MMRN2]] (+0.69, fdr 7e-06); moves opposite to [[SKP2]] (-0.60, fdr 1e-05), [[IQCB1]] (-0.59, fdr 1e-05), [[FAR1]] (-0.58, fdr 2e-05).
> It is in [[Module 181]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13678.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **11.6×** | +44.3 | 0e+00 | 39/39 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **5.34×** | +20.6 | 0e+00 | 40/44 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.00×** | +19.9 | 0e+00 | 40/41 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.35×** | +13.1 | 3e-37 | 30/39 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.72×** | +11.7 | 2e-29 | 35/42 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.05×** | +9.2 | 4e-18 | 28/45 (MIA PaCa-2, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.05×** | +9.2 | 4e-18 | 25/45 (HS-578T, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.89×** | +8.2 | 2e-14 | 25/46 (SNU-423, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +7.5 | 3e-12 | 25/38 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.78×** | +7.4 | 9e-12 | 26/46 (A-172, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.76×** | +7.2 | 3e-11 | 26/45 (Hs 766T, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.73×** | +6.5 | 4e-09 | 5/17 (LoVo, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +6.4 | 6e-09 | 21/46 (A498, C32, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +6.2 | 2e-08 | 19/40 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +5.5 | 1e-06 | 15/45 (Hs 766T, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +5.4 | 3e-06 | 11/42 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13678.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.524×** | -8.3 | 6e-14 | 24/46 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.430×** | -5.7 | 4e-06 | 11/37 (LOX-IMVI, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.650×** | -5.3 | 2e-05 | 15/45 (NCI-H1573, PANC-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.658×** | -3.8 | 0.017 | 6/46 (NCI-H1792, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.737×** | -3.6 | 0.031 | 14/44 (SW 900, NCI-H1573, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.758×** | -3.6 | 0.031 | 17/45 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.589×** | -3.6 | 0.031 | 9/43 (LOX-IMVI, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.763×** | -3.4 | 0.057 | 9/45 (SW48, NCI-H1573, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.619×** | -3.2 | 0.080 | 8/42 (NCI-H1573, J82, …) | top dose only | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.787× | -3.1 | 0.11 | 8/46 (PANC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.790× | -3.0 | 0.12 | 6/46 (SK-MEL-2, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13678. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.19 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.3× (z +17.3) | — |
| [[Hs 766T (line)]] | wt | 9.99 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.1× (z +15.8) | — |
| [[LoVo (line)]] | wt | 8.76 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.3× (z +19.2) | — |
| [[NCI-H1573 (line)]] | alt | 14.6 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +19.4) | [[Belumosudil (drug)]] 5 µM 0.118× (z -10.8) |
| [[SNU-423 (line)]] | alt | 9.29 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 17.9× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.0931× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 5.74 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +12.0) | — |
| [[CFPAC-1 (line)]] | alt | 7.72 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +15.5) | — |
| [[HOP62 (line)]] | alt | 5.15 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.1× (z +17.1) | — |
| [[KATO III (line)]] | alt | 5.61 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.1× (z +17.1) | — |
| [[NCI-H460 (line)]] | wt | 3.69 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +15.7) | — |
| [[Panc 03.27 (line)]] | alt | 8.24 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.34× (z +11.1) | [[Omeprazole (drug)]] 0.5 µM 0.114× (z -9.2) |
| [[PANC-1 (line)]] | alt | 10.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +21.0) | — |
| [[A549 (line)]] | wt | 3.67 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.99× (z +9.3) | — |
| [[AsPC-1 (line)]] | alt | 3.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +11.6) | — |
| [[BT-474 (line)]] | alt | 9.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.13× (z +10.6) | — |
| [[C32 (line)]] | wt | 4.56 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.62× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 11.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +14.0) | — |
| [[HCT15 (line)]] | alt | 4.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.2× (z +10.4) | — |
| [[HEC-1-A (line)]] | alt | 10.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.90× (z +14.5) | — |
| [[HepG2_C3A (line)]] | wt | 12.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +12.0) | — |
| [[HS-578T (line)]] | alt | 2.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.1× (z +12.6) | — |
| [[HT-29 (line)]] | alt | 5.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.2× (z +14.7) | — |
| [[hTERT-HPNE (line)]] | wt | 4.16 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.7× (z +11.7) | — |
| [[J82 (line)]] | alt | 10.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.20× (z +13.5) | — |
| [[LOX-IMVI (line)]] | wt | 6.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 5.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 3.74 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 15.8× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 3.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +10.5) | — |
| [[NCI-H23 (line)]] | alt | 12.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.09× (z +13.5) | — |
| [[NCI-H2347 (line)]] | alt | 2.79 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.9× (z +16.5) | — |
| [[RPMI-7951 (line)]] | alt | 5.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +10.8) | — |
| [[SK-MEL-2 (line)]] | alt | 5.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.45× (z +10.3) | — |
| [[SW 900 (line)]] | alt | 3.00 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.7× (z +11.3) | — |
| [[SW1417 (line)]] | alt | 7.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +16.2) | — |
| [[SW48 (line)]] | wt | 5.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.3× (z +10.9) | — |
| [[SW480 (line)]] | alt | 3.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +10.7) | — |
| [[A-427 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13678), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPHS1]] | +0.70 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[HSD11B1-AS1]] | +0.69 | +0.78 / +0.51 | both halves | 1e-05 |  |
| [[MMRN2]] | +0.69 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[MSANTD3-TMEFF1]] | +0.68 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[BCL10-AS1]] | +0.68 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[COL11A2]] | +0.66 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[LINC02362]] | +0.66 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[IL34]] | +0.66 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[TGIF2-RAB5IF]] | +0.65 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[SAMD4A-AS1]] | +0.65 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[MAP3K20-AS1]] | +0.64 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[PLA2G4C]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKP2]] | -0.60 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[IQCB1]] | -0.59 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[FAR1]] | -0.58 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[WDR5]] | -0.57 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[ADPGK]] | -0.57 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[NAPG]] | -0.56 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[INTS10]] | -0.56 | -0.52 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PIK3IP1-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ARL14]] | B | ARL14 activity raises PIK3IP1-DT's level | lines that do not express ARL14 (23) vs lines expressing it (27) | 1.33× lower at baseline in the lines without ARL14 | 0.079 | ⚠ within organs, on part of the lines; also absent: TMEM92, LIPH, AFAP1L2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 181]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.736). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.2, -4.8); signed map (24.7, 7.3). **Vector** length 81.8, 15.8% of its response variance represented; |z| ≥ 3 in 1,055 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.1 | +44.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +19.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +6.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.7 | +20.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +13.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +9.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +6.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +5.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +0.6 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.9 | +4.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.1 | -8.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -3.6 |
|  | [[NG25 (drug)]] 5 µM |  | -3.0 | -5.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -3.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.0 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -1.6 |
|  | [[EX229 (drug)]] 5 µM |  | -2.7 | -2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.5 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | PIK3IP1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 22q12.2 — chr22:31,292,499-31,338,021 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously PIK3IP1-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:41072](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41072) · Entrez [101929760](https://www.ncbi.nlm.nih.gov/gene/101929760) · Ensembl [ENSG00000228839](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228839)

## Data

Gene col 13678: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13678); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13678, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13678]; `tensor/DDL_lfc|DDL_z.npy` [13678]; `embed/gene_vectors.npy` [13678]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13678 or target_col == 13678). Every well: [[PIK3IP1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIK3IP1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
