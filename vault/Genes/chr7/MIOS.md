---
symbol: "MIOS"
type: "gene"
col: 8981
ensembl_id: "ENSG00000164654"
name: "meiosis regulator for oocyte development"
location: "7p21.3"
module: 1
arm: "+"
pooled_cpm: 32.16
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# MIOS

*meiosis regulator for oocyte development* — 7p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.87× (z +15.3, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.626× (z -8.1, q 4e-13, down in 27 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.724× (z -7.9, q 9e-13, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GCFC2]] (+0.71, fdr 7e-06), [[YTHDC2]] (+0.71, fdr 7e-06), [[DCAF17]] (+0.67, fdr 7e-06); moves opposite to [[ALKBH5]] (-0.58, fdr 1e-05), [[BMT2]] (-0.55, fdr 2e-05), [[MBOAT7]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8981.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.87×** | +15.3 | 0e+00 | 43/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +9.7 | 8e-20 | 33/47 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.68×** | +8.6 | 2e-15 | 34/48 (BT-474, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.45×** | +6.4 | 2e-08 | 34/48 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +5.4 | 6e-06 | 24/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +4.9 | 1e-04 | 24/48 (BT-474, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +4.7 | 2e-04 | 20/47 (CFPAC-1, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | **1.28×** | +4.1 | 0.003 | 24/46 (Panc 03.27, NCI-H1573, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +4.0 | 0.004 | 18/48 (BT-474, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.18× | +4.0 | 0.004 | 12/48 (NCI-H460, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.9 | 0.005 | 17/48 (NCI-H2347, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.011 | 15/48 (BT-474, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 1.16× | +3.7 | 0.011 | 15/48 (NCI-H2347, J82, …) | top dose only | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.024 | 13/48 (HS-578T, A498, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.028 | 11/48 (PANC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.039 | 10/48 (NCI-H2347, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8981.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.626×** | -8.1 | 4e-13 | 27/46 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -7.9 | 9e-13 | 32/47 (PANC-1, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.649×** | -7.5 | 2e-11 | 36/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | **0.757×** | -4.6 | 5e-04 | 21/38 (Hs 766T, NCI-H2030, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.764×** | -4.5 | 9e-04 | 23/48 (NCI-H23, SW 1271, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.779×** | -4.2 | 0.003 | 20/47 (A-172, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.774×** | -4.1 | 0.003 | 22/42 (A-427, BT-474, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.869× | -3.4 | 0.041 | 19/48 (SNU-1, HOP62, …) | top dose only |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | **0.825×** | -3.3 | 0.056 | 12/48 (CFPAC-1, NCI-H661, …) | inconsistent across doses | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.774×** | -3.1 | 0.093 | 16/48 (SW 900, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.779× | -3.1 | 0.11 | 15/48 (SHP-77, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8981. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 28.4 | 11 | 0 | [[Clobetasol propionate (drug)]] 0.5 µM 5.30× (z +11.8) | — |
| [[BT-474 (line)]] | alt | 60.8 | 8 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +16.1) | [[Dinaciclib (drug)]] 0.05 µM 0.332× (z -8.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 60.7 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 31.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +11.8) | — |
| [[NCI-H2030 (line)]] | alt | 33.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[NCI-H2347 (line)]] | alt | 16.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +14.4) | — |
| [[NCI-H460 (line)]] | wt | 41.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.416× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.484× (z -8.5) |
| [[A-172 (line)]] | wt | 41.8 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -16.3) |
| [[A-427 (line)]] | wt | 32.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.95× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -11.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 29.6 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.367× (z -8.8) |
| [[LoVo (line)]] | wt | 30.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +14.3) | — |
| [[A498 (line)]] | wt | 36.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +8.6) | — |
| [[AsPC-1 (line)]] | alt | 22.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +12.4) | — |
| [[C-33 A (line)]] | alt | 38.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -8.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 14.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +10.1) | — |
| [[Hs 766T (line)]] | wt | 24.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[HT-29 (line)]] | alt | 18.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.11× (z +13.9) | — |
| [[KATO III (line)]] | alt | 38.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.1) | — |
| [[LS 180 (line)]] | wt | 19.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 43.8 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 41.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +12.6) | — |
| [[SNU-1 (line)]] | wt | 36.2 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.329× (z -9.5) |
| [[SW 1271 (line)]] | alt | 55.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0721× (z -9.1) |
| [[SW48 (line)]] | wt | 42.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -8.6) |
| [[SW480 (line)]] | alt | 33.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.436× (z -8.9) |
| [[A549 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8981), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCFC2]] | +0.71 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[YTHDC2]] | +0.71 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[DCAF17]] | +0.67 | +0.64 / +0.72 | both halves | 7e-06 | STRING 449 |
| [[WDR75]] | +0.67 | +0.64 / +0.71 | both halves | 7e-06 | same gene group |
| [[ANGEL1]] | +0.66 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[THUMPD2]] | +0.66 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[NHLRC2]] | +0.65 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[TIMM9]] | +0.64 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[ZNF485]] | +0.63 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[POGK]] | +0.63 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[N6AMT1]] | +0.62 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[ZC3H7B]] | +0.61 | +0.66 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALKBH5]] | -0.58 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[BMT2]] | -0.55 | -0.48 / -0.54 | both halves | 2e-05 | pathway: Amino acids regulate mTORC1; STRING 407 |
| [[MBOAT7]] | -0.55 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[TSEN34]] | -0.54 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[DEDD2]] | -0.54 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[MXD1]] | -0.54 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[KDELR1]] | -0.54 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[SAR1A]] | -0.54 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[LAPTM4A]] | -0.53 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[BNIP3L]] | -0.52 | -0.46 / -0.62 | both halves | 3e-05 |  |
| [[PBXIP1]] | -0.52 | -0.42 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MIOS's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.665). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-29.0, 4.0); signed map (-1.8, -39.2). **Vector** length 101, 23.9% of its response variance represented; |z| ≥ 3 in 1,023 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.4 | +9.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.7 | +8.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | +5.7 | +4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +15.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.7 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +3.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.2 | +2.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.0 | +3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.9 | +2.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +3.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.9 | -7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -7.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -1.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | meiosis regulator for oocyte development |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.3 — chr7:7,566,875-7,608,932 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20323, MIO, Sea4, Yulink |
| Gene groups (HGNC) | WD repeat domain containing; GATOR2 subcomplex |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 4 pathways, smallest: Amino acids regulate mTORC1; Cellular response to starvation; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXC5](https://www.uniprot.org/uniprotkb/Q9NXC5) (GATOR2 complex protein MIOS):

> As a component of the GATOR2 complex, functions as an activator of the amino acid-sensing branch of the mTORC1 signaling pathway. The GATOR2 complex indirectly activates mTORC1 through the inhibition of the GATOR1 subcomplex. GATOR2 probably acts as an E3 ubiquitin-protein ligase toward GATOR1. In the presence of abundant amino acids, the GATOR2 complex mediates ubiquitination of the NPRL2 core component of the GATOR1 complex, leading to GATOR1 inactivation. In the absence of amino acids, …

**Summary**, from NCBI Gene [54468](https://www.ncbi.nlm.nih.gov/gene/54468):

> Predicted to enable zinc ion binding activity. Involved in cellular response to amino acid starvation; positive regulation of TORC1 signaling; and protein-containing complex localization. Located in cytosol; lysosomal membrane; and nucleoplasm. Part of GATOR2 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21905](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21905) · Entrez [54468](https://www.ncbi.nlm.nih.gov/gene/54468) · UniProt [Q9NXC5](https://www.uniprot.org/uniprotkb/Q9NXC5) · Ensembl [ENSG00000164654](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164654)

## Data

Gene col 8981: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8981); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8981, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8981]; `tensor/DDL_lfc|DDL_z.npy` [8981]; `embed/gene_vectors.npy` [8981]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8981 or target_col == 8981). Every well: [[MIOS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIOS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
