---
symbol: "LIG1"
type: "gene"
col: 2610
ensembl_id: "ENSG00000105486"
name: "DNA ligase 1"
location: "19q13.33"
module: 6
arm: "+"
pooled_cpm: 36.25
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 27
n_dd_up_clean: 8
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# LIG1

*DNA ligase 1* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.66× (z +8.9, q 3e-16, up in 34 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 0.5 µM: 1.35× (z +5.3, q 1e-05, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.548× (z -15.0, q 0e+00, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX12P]] (+0.78, fdr 7e-06), [[RFC4]] (+0.75, fdr 7e-06), [[MMS22L]] (+0.74, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TCF19]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2610.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.66×** | +8.9 | 3e-16 | 34/45 (NCI-H1573, C32, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.67×** | +8.3 | 2e-14 | 27/41 (Panc 03.27, A-427, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.59×** | +7.9 | 7e-13 | 26/39 (C32, HT-29, …) | all doses, flat | composition shift |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.44×** | +6.1 | 1e-07 | 29/48 (RKO, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.6 | 2e-06 | 2/48 (NCI-H2030, NCI-H23) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +5.3 | 1e-05 | 22/48 (C32, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.34×** | +5.1 | 2e-05 | 21/47 (MIA PaCa-2, SW480, …) | all doses, flat | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +5.0 | 5e-05 | 20/48 (RKO, A549, …) | inconsistent across doses | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.30×** | +4.7 | 2e-04 | 20/47 (C32, NCI-H460, …) | all doses, flat |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.30×** | +4.3 | 0.001 | 20/47 (NCI-H460, LOX-IMVI, …) | all doses, flat |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.27×** | +4.1 | 0.002 | 15/47 (RKO, LS 180, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.25×** | +4.0 | 0.003 | 18/48 (HT-29, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.007 | 13/48 (LoVo, HS-578T, …) | rises with dose |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.013 | 12/47 (HEC-1-A, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.013 | 14/47 (RKO, NCI-H460, …) | all doses, flat | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.018 | 12/47 (A498, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Demeclocycline (drug)]] 5 µM |  | 1.14× | +3.3 | 0.032 | 9/48 (SW480, HOP62, …) | top dose only |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.15× | +3.3 | 0.032 | 14/48 (RKO, SW480, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.053 | 7/47 (A549, NCI-H2030, …) | top dose only |  |
| [[Cytarabine (drug)]] 0.05 µM |  | 1.20× | +2.9 | 0.095 | 12/48 (HT-29, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.18× | +2.9 | 0.095 | 12/48 (KATO III, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2610.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.548×** | -15.0 | 0e+00 | 36/47 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.540×** | -10.7 | 4e-24 | 38/47 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.684×** | -9.5 | 4e-19 | 31/48 (HT-29, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.612×** | -8.7 | 6e-16 | 37/48 (LS 180, KATO III, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.612×** | -8.4 | 8e-15 | 30/48 (Panc 03.27, COLO 205, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.751×** | -7.2 | 6e-11 | 30/48 (C-33 A, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.714×** | -6.0 | 2e-07 | 24/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.716×** | -5.9 | 2e-07 | 27/48 (HS-578T, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.707×** | -5.8 | 4e-07 | 29/48 (KATO III, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.801×** | -5.6 | 1e-06 | 25/48 (SW 1271, KATO III, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.723×** | -5.5 | 2e-06 | 25/47 (Panc 03.27, COLO 205, …) | rises with dose | position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **0.557×** | -5.4 | 3e-06 | 25/45 (RPMI-7951, hTERT-HPNE, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.766×** | -4.6 | 2e-04 | 24/48 (LS 180, HS-578T, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.769×** | -4.6 | 2e-04 | 20/48 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.835× | -4.5 | 2e-04 | 20/48 (LS 180, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.788×** | -4.2 | 8e-04 | 22/48 (KATO III, HT-29, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2610. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 57.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.532× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 94.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -15.4) |
| [[HS-578T (line)]] | alt | 37.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -9.9) |
| [[HT-29 (line)]] | alt | 35.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -12.9) |
| [[MIA PaCa-2 (line)]] | alt | 32.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -14.1) |
| [[NCI-H23 (line)]] | alt | 48.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -18.7) |
| [[A-427 (line)]] | wt | 55.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -14.5) |
| [[HOP62 (line)]] | alt | 21.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -10.0) |
| [[KATO III (line)]] | alt | 35.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.208× (z -11.0) |
| [[LS 180 (line)]] | wt | 46.5 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.457× (z -9.4) |
| [[SW480 (line)]] | alt | 43.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.298× (z -12.5) |
| [[BT-474 (line)]] | alt | 26.8 | 0 | 1 | — | [[Talc (drug)]] 0.5 µM 0.256× (z -8.8) |
| [[C-33 A (line)]] | alt | 85.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -11.8) |
| [[COLO 205 (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[H4 (line)]] | wt | 44.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -15.0) |
| [[HCT15 (line)]] | alt | 55.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -9.8) |
| [[Hs 766T (line)]] | wt | 19.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.218× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 38.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.393× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 28.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -9.9) |
| [[PANC-1 (line)]] | alt | 24.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -8.5) |
| [[A-172 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2610), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX12P]] | +0.78 | +0.81 / +0.74 | both halves | 7e-06 |  |
| [[RFC4]] | +0.75 | +0.83 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_DNA_REPAIR; STRING 959 |
| [[MMS22L]] | +0.74 | +0.72 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[FANCI]] | +0.73 | +0.76 / +0.70 | both halves | 7e-06 | STRING 509 |
| [[CHAF1A]] | +0.72 | +0.73 / +0.68 | both halves | 7e-06 | STRING 558 |
| [[RAD54L]] | +0.72 | +0.78 / +0.68 | both halves | 7e-06 | STRING 535 |
| [[TIMELESS]] | +0.72 | +0.68 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 580 |
| [[NCAPH2]] | +0.71 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[MSH2]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 720 |
| [[DDX11]] | +0.71 | +0.70 / +0.69 | both halves | 7e-06 | STRING 465 |
| [[POLD3]] | +0.71 | +0.65 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_DNA_REPAIR; STRING 857 |
| [[MYBL2]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF19]] | B | TCF19 activity raises LIG1's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.24× lower at baseline in the lines without TCF19 | 0.006 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[ZNF367]] | C | ZNF367 activity raises LIG1's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 2.27× lower at baseline in the lines without ZNF367 | 0.023 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises LIG1's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.49× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |
| [[MCM10]] | C | MCM10 activity raises LIG1's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 1.93× lower at baseline in the lines without MCM10 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises LIG1's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.95× lower at baseline in the lines without DSCC1 | 0.085 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[MELK]], [[TK1]] | C | MELK, TK1 activity raises LIG1's level | lines that do not express MELK, TK1 (3) vs lines expressing them (47) | 2.56× lower at baseline in the lines without MELK, TK1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.745). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-33.2, -45.3); signed map (-37.6, -43.0). **Vector** length 134, 39.3% of its response variance represented; |z| ≥ 3 in 1,201 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F G1/S* (control, mean cos +0.59 to 23); *Cell Cycle Checkpoints* (reactome, mean cos +0.59 to 45); *Activation of the pre-replicative complex* (reactome, mean cos +0.60 to 22).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | +7.0 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | +6.5 | +7.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +6.2 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +6.1 | +8.3 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +5.5 | +6.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.8 | +5.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.4 | +5.3 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +3.4 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +3.4 | +3.6 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +3.3 | +4.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.3 | -10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.3 | -8.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.2 | -5.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.9 | -9.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.7 | -8.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -6.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.2 | -5.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | -4.0 | -5.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.9 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | DNA ligase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,115,445-48,170,603 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LIGI, hLig1 |
| Gene groups (HGNC) | DNA ligases; Nucleotide excision repair |
| Hallmark sets | DNA_REPAIR, E2F_TARGETS |
| Reactome | 38 pathways, smallest: Regulation of MITF-M-dependent genes involved in DNA replication, damage repair and senescence; POLB-Dependent Long Patch Base Excision Repair; Early Phase of HIV Life Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P18858](https://www.uniprot.org/uniprotkb/P18858) (DNA ligase 1):

> DNA ligase that seals nicks in double-stranded during DNA repair. Also involved in DNA replication and DNA recombination.

**Summary**, from NCBI Gene [3978](https://www.ncbi.nlm.nih.gov/gene/3978):

> This gene encodes a member of the ATP-dependent DNA ligase protein family. The encoded protein functions in DNA replication, recombination, and the base excision repair process. Mutations in this gene that lead to DNA ligase I deficiency result in immunodeficiency and increased sensitivity to DNA-damaging agents. Disruption of this gene may also be associated with a variety of cancers. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2014]

**Accessions** — [HGNC:6598](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6598) · Entrez [3978](https://www.ncbi.nlm.nih.gov/gene/3978) · UniProt [P18858](https://www.uniprot.org/uniprotkb/P18858) · Ensembl [ENSG00000105486](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105486)

## Data

Gene col 2610: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2610); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2610, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2610]; `tensor/DDL_lfc|DDL_z.npy` [2610]; `embed/gene_vectors.npy` [2610]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2610 or target_col == 2610). Every well: [[LIG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
