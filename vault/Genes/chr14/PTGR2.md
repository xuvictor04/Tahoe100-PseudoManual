---
symbol: "PTGR2"
type: "gene"
col: 6370
ensembl_id: "ENSG00000140043"
name: "prostaglandin reductase 2"
location: "14q24.3"
module: 25
arm: "+"
pooled_cpm: 17.05
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 17
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# PTGR2

*prostaglandin reductase 2* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.17× (z +11.6, q 1e-28, up in 23 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 1.25× (z +3.5, q 0.044, up in 9 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HEC-1-A 3.72×, NCI-H1792 4.46×, LoVo 3.16×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 2.99×, LS 180 4.52×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 3.33×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.542× (z -13.5, q 6e-39, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERLIN2]] (+0.65, fdr 4e-05), [[DARS2]] (+0.65, fdr 1e-05), [[MBTPS2]] (+0.65, fdr 1e-05); moves opposite to [[PMM1]] (-0.66, fdr 8e-06), [[RPL36AL]] (-0.62, fdr 5e-05, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[BAHD1]] (-0.62, fdr 2e-05), [[METRNL]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NUP210]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6370.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HEC-1-A 3.72×, NCI-H1792 4.46×, LoVo 3.16×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 2.99×, LS 180 4.52×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 3.33×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +11.6 | 1e-28 | 23/28 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.09×** | +11.6 | 2e-28 | 33/41 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +9.6 | 1e-19 | 22/33 (HEC-1-A, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.27×** | +3.7 | 0.029 | 11/47 (A-427, HOP62, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.5 | 0.044 | 0/48 | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.044 | 9/47 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.15× | +3.1 | 0.17 | 15/47 (NCI-H2347, CFPAC-1, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6370.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.542×** | -13.5 | 6e-39 | 39/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.573×** | -8.7 | 9e-16 | 30/47 (NCI-H23, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.578×** | -8.6 | 2e-15 | 30/46 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.581×** | -8.5 | 3e-15 | 30/47 (NCI-H23, PANC-1, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.610×** | -7.7 | 1e-12 | 28/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.615×** | -7.6 | 3e-12 | 28/46 (PANC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.669×** | -6.3 | 3e-08 | 23/47 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.677×** | -5.9 | 3e-07 | 20/46 (PANC-1, SNU-1, …) | top dose only | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.694×** | -5.4 | 5e-06 | 22/48 (KATO III, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.816×** | -4.5 | 4e-04 | 20/48 (NCI-H2030, Panc 03.27, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.627×** | -3.8 | 0.007 | 21/44 (NCI-H2030, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.633×** | -3.7 | 0.009 | 14/48 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.796×** | -3.6 | 0.016 | 15/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.803×** | -3.4 | 0.024 | 13/47 (HEC-1-A, SW 1271, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.809×** | -3.3 | 0.035 | 18/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.812×** | -3.2 | 0.041 | 7/47 (AN3 CA, NCI-H2030, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.815×** | -3.2 | 0.046 | 16/47 (NCI-H1573, HepG2/C3A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6370. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 21.1 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.244× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.424× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 17.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -12.7) |
| [[SW480 (line)]] | alt | 26.0 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.99× (z +11.3) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.317× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.492× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 30.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.269× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.322× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 24.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +10.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 21.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.52× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -10.6) |
| [[COLO 205 (line)]] | alt | 14.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -9.3) |
| [[HCT15 (line)]] | alt | 19.5 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.124× (z -9.7) |
| [[HOP62 (line)]] | alt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 10.0 | 0 | 1 | — | [[Orlistat (drug)]] 0.5 µM 0.134× (z -8.7) |
| [[LoVo (line)]] | wt | 14.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +8.5) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0641× (z -8.7) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.256× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 14.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 22.5 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0716× (z -11.7) |
| [[SW48 (line)]] | wt | 14.3 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0787× (z -9.5) |
| [[A-172 (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.90 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6370), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERLIN2]] | +0.65 | +0.42 / +0.68 | both halves | 4e-05 |  |
| [[DARS2]] | +0.65 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[MBTPS2]] | +0.65 | +0.49 / +0.71 | both halves | 1e-05 |  |
| [[TMEM123]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[LIN7C]] | +0.63 | +0.40 / +0.67 | both halves | 5e-05 |  |
| [[SCCPDH]] | +0.62 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[ALG10B]] | +0.61 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[ALG10]] | +0.61 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[PNPO]] | +0.61 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[DDX3X]] | +0.60 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[STRADB]] | +0.60 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[TMX1]] | +0.59 | +0.47 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMM1]] | -0.66 | -0.62 / -0.58 | both halves | 8e-06 |  |
| [[RPL36AL]] ⚠ | -0.62 | -0.39 / -0.63 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[BAHD1]] | -0.62 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[METRNL]] | -0.61 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.61 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[TRAPPC4]] | -0.61 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[CDC34]] | -0.60 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[ZFAND2B]] | -0.60 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[SIRT7]] | -0.60 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[MAP1S]] | -0.59 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[RCE1]] | -0.59 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[CDKN2D]] | -0.59 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[NAGK]] | -0.58 | -0.61 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUP210]] | B | NUP210 activity raises PTGR2's level | lines that do not express NUP210 (13) vs lines expressing it (37) | 1.60× lower at baseline in the lines without NUP210 | 0.069 | ⚠ within organs, on part of the lines; also absent: PRR36, NEBL, FAM169A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.672). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-29.7, -19.1); signed map (-16.5, -39.8). **Vector** length 69.0, 11.8% of its response variance represented; |z| ≥ 3 in 969 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +9.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +2.6 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +1.3 | +1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.2 | +1.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +1.2 | +0.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +1.1 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | -13.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -8.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.9 | -6.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.7 | -0.7 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | prostaglandin reductase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:73,851,831-73,885,726 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ39091; previously ZADH1 |
| Reactome | 4 pathways, smallest: Synthesis of Prostaglandins (PG) and Thromboxanes (TX); Arachidonate metabolism; Fatty acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N8N7](https://www.uniprot.org/uniprotkb/Q8N8N7) (Prostaglandin reductase 2):

> Functions as 15-oxo-prostaglandin 13-reductase and acts on 15-keto-PGE1, 15-keto-PGE2, 15-keto-PGE1-alpha and 15-keto-PGE2-alpha with highest activity towards 15-keto-PGE2. Overexpression represses transcriptional activity of PPARG and inhibits adipocyte differentiation (By similarity).

**Summary**, from NCBI Gene [145482](https://www.ncbi.nlm.nih.gov/gene/145482):

> This gene encodes an enzyme involved in the metabolism of prostaglandins. The encoded protein catalyzes the NADPH-dependent conversion of 15-keto-prostaglandin E2 to 15-keto-13,14-dihydro-prostaglandin E2. This protein may also be involved in regulating activation of the peroxisome proliferator-activated receptor. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:20149](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20149) · Entrez [145482](https://www.ncbi.nlm.nih.gov/gene/145482) · UniProt [Q8N8N7](https://www.uniprot.org/uniprotkb/Q8N8N7) · Ensembl [ENSG00000140043](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140043)

## Data

Gene col 6370: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6370); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6370, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6370]; `tensor/DDL_lfc|DDL_z.npy` [6370]; `embed/gene_vectors.npy` [6370]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6370 or target_col == 6370). Every well: [[PTGR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTGR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
