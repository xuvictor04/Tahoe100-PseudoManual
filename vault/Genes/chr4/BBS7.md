---
symbol: "BBS7"
type: "gene"
col: 6215
ensembl_id: "ENSG00000138686"
name: "Bardet-Biedl syndrome 7"
location: "4q27"
module: 65
arm: "+"
pooled_cpm: 22.19
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# BBS7

*Bardet-Biedl syndrome 7* — 4q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.01× (z +15.4, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.581× (z -6.3, q 2e-07, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RETSAT]] (+0.64, fdr 3e-05), [[P2RX4]] (+0.62, fdr 7e-06), [[HSDL2]] (+0.58, fdr 1e-05); moves opposite to [[DOK3]] (-0.55, fdr 2e-05), [[NOP2]] (-0.55, fdr 4e-05), [[MYLK2]] (-0.53, fdr 2e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6215.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.01×** | +15.4 | 0e+00 | 46/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +14.7 | 0e+00 | 26/33 (HEC-1-A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.91×** | +14.2 | 9e-44 | 45/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +13.4 | 4e-39 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +11.8 | 4e-30 | 32/43 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +11.8 | 6e-30 | 33/48 (A498, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +10.9 | 1e-25 | 24/46 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +9.6 | 6e-20 | 31/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +8.0 | 7e-14 | 26/44 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +7.7 | 9e-13 | 30/48 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.88×** | +7.3 | 2e-11 | 24/48 (RKO, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +7.3 | 2e-11 | 21/47 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +7.0 | 8e-11 | 23/48 (SK-MEL-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +6.6 | 2e-09 | 23/48 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.32×** | +6.1 | 3e-08 | 22/48 (Panc 03.27, A498, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +5.7 | 4e-07 | 18/48 (LoVo, LS 180, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.31×** | +5.7 | 4e-07 | 20/48 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +5.4 | 2e-06 | 20/47 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6215.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.581×** | -6.3 | 2e-07 | 22/47 (MIA PaCa-2, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.638×** | -5.2 | 6e-05 | 20/48 (A-427, H4, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.942× | -4.7 | 5e-04 | 3/48 (COLO 205, RPMI-7951, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -4.0 | 0.008 | 11/48 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.853× | -3.5 | 0.051 | 11/48 (NCI-H23, SW480, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.744×** | -3.4 | 0.057 | 11/47 (MIA PaCa-2, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.897× | -3.4 | 0.057 | 8/48 (A-427, NCI-H2347, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.856× | -3.3 | 0.081 | 13/47 (NCI-H2347, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6215. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 46.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +12.6) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -9.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 37.5 | 3 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.56× (z +12.4) | — |
| [[C32 (line)]] | wt | 13.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +12.0) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.44× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 27.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.71× (z +11.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 17.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +12.3) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 19.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.85× (z +17.7) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +10.4) | — |
| [[A-427 (line)]] | wt | 32.7 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.204× (z -10.0) ⚠ toxic |
| [[A549 (line)]] | wt | 21.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +10.2) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[CHP-212 (line)]] | wt | 30.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.05 µM 0.0901× (z -8.9) |
| [[H4 (line)]] | wt | 26.4 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0928× (z -8.7) |
| [[HCT15 (line)]] | alt | 34.8 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.263× (z -8.8) |
| [[LoVo (line)]] | wt | 24.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.85× (z +18.0) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[LOX-IMVI (line)]] | wt | 16.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +11.1) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 22.5 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.210× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 15.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.86× (z +8.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 20.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.38× (z +13.4) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[SNU-1 (line)]] | wt | 22.4 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.119× (z -10.4) |
| [[SW48 (line)]] | wt | 23.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +9.2) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[SW480 (line)]] | alt | 15.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +11.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6215), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RETSAT]] | +0.64 | +0.45 / +0.74 | both halves | 3e-05 |  |
| [[P2RX4]] | +0.62 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[HSDL2]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[FIG4]] | +0.57 | +0.44 / +0.69 | both halves | 3e-05 |  |
| [[ACTR10]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[LRRC40]] | +0.55 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[TAB3]] | +0.55 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[WDR41]] | +0.55 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[DCP1B]] | +0.54 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[TCP11L1]] | +0.54 | +0.32 / +0.58 | both halves | 2e-04 |  |
| [[NDFIP1]] | +0.53 | +0.26 / +0.56 | both halves | 4e-04 |  |
| [[TP53TG1]] | +0.53 | +0.54 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOK3]] | -0.55 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[NOP2]] | -0.55 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[MYLK2]] | -0.53 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[IL9RP3]] | -0.52 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[DNAH1]] | -0.51 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[TRA2B]] | -0.51 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[TUBA8]] | -0.49 | -0.60 / -0.35 | both halves | 1e-04 | pathway: Assembly of the 9+0 primary cilium |
| [[PPRC1]] | -0.49 | -0.47 / -0.45 | both halves | 3e-05 | pathway: Organelle biogenesis and maintenance |
| [[LINC01250]] | -0.49 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[GAL3ST2]] | -0.49 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[PHF5A]] | -0.49 | -0.29 / -0.56 | both halves | 2e-04 |  |
| [[RRP7BP-1]] | -0.49 | -0.53 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BBS7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.364). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-19.0, 21.2); signed map (-3.2, -0.0). **Vector** length 76.0, 14.1% of its response variance represented; |z| ≥ 3 in 1,025 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.1 | +11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +11.8 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.0 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +9.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +1.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +5.7 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.2 | +3.5 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.9 | -3.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.8 | -5.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | Bardet-Biedl syndrome 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q27 — chr4:121,824,329-121,870,487 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10715, BBS2L1 |
| Gene groups (HGNC) | BBSome |
| Reactome | 5 pathways, smallest: BBSome-mediated cargo-targeting to cilium; Cargo trafficking to the periciliary membrane; Assembly of the 9+0 primary cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWZ6](https://www.uniprot.org/uniprotkb/Q8IWZ6) (BBSome complex member BBS7):

> The BBSome complex is thought to function as a coat complex required for sorting of specific membrane proteins to the primary cilia. The BBSome complex is required for ciliogenesis but is dispensable for centriolar satellite function. This ciliogenic function is mediated in part by the Rab8 GDP/GTP exchange factor, which localizes to the basal body and contacts the BBSome. Rab8(GTP) enters the primary cilium and promotes extension of the ciliary membrane. Firstly the BBSome associates with the …

**Summary**, from NCBI Gene [55212](https://www.ncbi.nlm.nih.gov/gene/55212):

> This gene encodes one of eight proteins that form the BBSome complex containing BBS1, BBS2, BBS4, BBS5, BBS7, BBS8, BBS9 and BBIP10. The BBSome complex is believed to recruit Rab8(GTP) to the primary cilium and promote ciliogenesis. The BBSome complex assembly is mediated by a complex composed of three chaperonin-like BBS proteins (BBS6, BBS10, and BBS12) and CCT/TRiC family chaperonins. Mutations in this gene are implicated in Bardet-Biedl syndrome, a genetic disorder whose symptoms include …

**Accessions** — [HGNC:18758](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18758) · Entrez [55212](https://www.ncbi.nlm.nih.gov/gene/55212) · UniProt [Q8IWZ6](https://www.uniprot.org/uniprotkb/Q8IWZ6) · Ensembl [ENSG00000138686](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138686)

## Data

Gene col 6215: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6215); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6215, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6215]; `tensor/DDL_lfc|DDL_z.npy` [6215]; `embed/gene_vectors.npy` [6215]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6215 or target_col == 6215). Every well: [[BBS7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BBS7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
