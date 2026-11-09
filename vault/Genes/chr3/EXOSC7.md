---
symbol: "EXOSC7"
type: "gene"
col: 1137
ensembl_id: "ENSG00000075914"
name: "exosome component 7"
location: "3p21.31"
module: 5
arm: "+"
pooled_cpm: 30.92
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 3
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# EXOSC7

*exosome component 7* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.54× (z +14.6, q 1e-45, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.704× (z -8.3, q 4e-14, down in 26 of 46 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (C32 0.0998×, LoVo 0.174×, NCI-H23 0.244×, SW48 0.192×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (HEC-1-A 0.368×, SW48 0.166×, Panc 03.27 0.217×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 0.218×, A-427 0.417×; ⚠ cell-cycle shift, explains ~52% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.0883×); [[Auranofin (drug)]] 5 µM in 1 line (C32 0.295×); [[PH-797804 (drug)]] 5 µM in 1 line (C32 0.111×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX31]] (+0.67, fdr 7e-06), [[C1orf109]] (+0.66, fdr 1e-05), [[CHCHD4]] (+0.63, fdr 1e-05); moves opposite to [[GPR137C]] (-0.50, fdr 4e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NT5M]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1137.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +14.6 | 1e-45 | 36/48 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.24×** | +5.2 | 6e-05 | 18/48 (COLO 205, NCI-H1792, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +4.8 | 2e-04 | 17/48 (SK-MEL-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.15× | +4.6 | 5e-04 | 16/48 (A498, HOP62, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.21×** | +4.5 | 6e-04 | 11/48 (A498, A-172, …) | two highest doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | 1.16× | +3.6 | 0.033 | 5/48 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.16× | +3.5 | 0.034 | 13/48 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.038 | 6/48 (NCI-H460, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 1.15× | +3.4 | 0.048 | 9/48 (A498, NCI-H1792, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.15× | +3.3 | 0.055 | 15/48 (SNU-423, A-172, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.061 | 9/48 (A-427, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 1.09× | +3.0 | 0.12 | 0/48 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1137.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (C32 0.0998×, LoVo 0.174×, NCI-H23 0.244×, SW48 0.192×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (HEC-1-A 0.368×, SW48 0.166×, Panc 03.27 0.217×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 0.218×, A-427 0.417×; ⚠ cell-cycle shift, explains ~52% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.0883×); [[Auranofin (drug)]] 5 µM in 1 line (C32 0.295×); [[PH-797804 (drug)]] 5 µM in 1 line (C32 0.111×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.704×** | -8.3 | 4e-14 | 26/46 (C32, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.693×** | -8.1 | 2e-13 | 24/44 (SW48, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.707×** | -8.0 | 3e-13 | 23/39 (HEC-1-A, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.842× | -4.1 | 0.006 | 20/48 (KATO III, LoVo, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change | 0.846× | -4.0 | 0.008 | 17/46 (SW1417, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.873× | -3.8 | 0.015 | 13/48 (C32, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.874× | -3.2 | 0.083 | 13/48 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.871× | -3.2 | 0.083 | 7/48 (RKO, SW 1088, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.875× | -3.2 | 0.083 | 11/48 (C-33 A, HT-29, …) | inconsistent across doses |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | 0.876× | -3.2 | 0.083 | 5/48 (hTERT-HPNE, SW480, …) | all doses, flat |  |
| [[Allantoin (drug)]] 5 µM |  | 0.910× | -3.2 | 0.083 | 4/48 (LOX-IMVI, A549, …) | top dose only |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.879× | -3.1 | 0.10 | 9/48 (SW 1271, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1137. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 54.6 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0998× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.295× (z -10.4) |
| [[SW48 (line)]] | wt | 51.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -13.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 34.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +8.7) ⚠ cell-cycle shift, explains ~52% of this change | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0883× (z -15.8) |
| [[HEC-1-A (line)]] | alt | 59.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.368× (z -12.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 50.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -12.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 33.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -9.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 22.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -9.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 31.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -10.4) ⚠ cell-cycle shift, explains ~52% of this change |
| [[A498 (line)]] | wt | 25.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -9.0) ⚠ cell-cycle shift, explains ~52% of this change |
| [[AsPC-1 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -9.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 49.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -9.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 34.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +10.3) | — |
| [[LoVo (line)]] | wt | 42.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -17.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 36.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.351× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 32.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 25.7 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.418× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 26.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -10.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 41.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -10.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 43.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1137), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX31]] | +0.67 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[C1orf109]] | +0.66 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[CHCHD4]] | +0.63 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[TSR1]] | +0.62 | +0.53 / +0.63 | both halves | 1e-05 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol |
| [[POLR1B]] | +0.61 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[ZNG1E]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[EARS2]] | +0.60 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[NOP16]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[NAT10]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 | pathway: rRNA processing; STRING 609 |
| [[HDHD5]] | +0.59 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[ANGEL1]] | +0.59 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[PDCD11]] | +0.59 | +0.58 / +0.58 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 761 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR137C]] | -0.50 | -0.41 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5M]] | B | NT5M activity raises EXOSC7's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.54× lower at baseline in the lines without NT5M | 0.022 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[TSEN2]] | C | TSEN2 activity raises EXOSC7's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 1.89× lower at baseline in the lines without TSEN2 | 0.081 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.566). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.0, -38.2); signed map (-1.1, -48.8). **Vector** length 95.7, 20.2% of its response variance represented; |z| ≥ 3 in 831 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +14.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | +2.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.9 | +4.6 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +3.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +3.5 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -2.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.5 | -1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | exosome component 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:44,975,241-45,036,066 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hRrp42p, Rrp42p, RRP42, EAP1, KIAA0116, p8 |
| Gene groups (HGNC) | Exosome complex |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 20 pathways, smallest: mRNA decay by 3' to 5' exoribonuclease; Butyrate Response Factor 1 (BRF1) binds and destabilizes mRNA; KSRP (KHSRP) binds and destabilizes mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15024](https://www.uniprot.org/uniprotkb/Q15024) (Exosome complex component RRP42):

> Non-catalytic component of the RNA exosome complex which has 3'->5' exoribonuclease activity and participates in a multitude of cellular RNA processing and degradation events. In the nucleus, the RNA exosome complex is involved in proper maturation of stable RNA species such as rRNA, snRNA and snoRNA, in the elimination of RNA processing by-products and non-coding 'pervasive' transcripts, such as antisense RNA species and promoter-upstream transcripts (PROMPTs), and of mRNAs with processing …

**Summary**, from NCBI Gene [23016](https://www.ncbi.nlm.nih.gov/gene/23016):

> Predicted to enable mRNA 3'-UTR AU-rich region binding activity. Involved in RNA catabolic process and RNA processing. Located in cytosol; nuclear speck; and nucleolus. Part of exosome (RNase complex). [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28112](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28112) · Entrez [23016](https://www.ncbi.nlm.nih.gov/gene/23016) · UniProt [Q15024](https://www.uniprot.org/uniprotkb/Q15024) · Ensembl [ENSG00000075914](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075914)

## Data

Gene col 1137: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1137); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1137, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1137]; `tensor/DDL_lfc|DDL_z.npy` [1137]; `embed/gene_vectors.npy` [1137]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1137 or target_col == 1137). Every well: [[EXOSC7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXOSC7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
