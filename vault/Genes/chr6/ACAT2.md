---
symbol: "ACAT2"
type: "gene"
col: 4182
ensembl_id: "ENSG00000120437"
name: "acetyl-CoA acetyltransferase 2"
location: "6q25.3"
module: 86
arm: "+"
pooled_cpm: 26.35
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 13
n_dd_up_clean: 22
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# ACAT2

*acetyl-CoA acetyltransferase 2* — 6q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (12 with an alert ⚠); the strongest is [[Cepharanthine (drug)]] 5 µM: 2.17× (z +16.5, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[5-Azacytidine (drug)]] 5 µM: 0.631× (z -7.0, q 2e-09, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IDI1]] (+0.80, fdr 7e-06), [[HMGCS1]] (+0.77, fdr 7e-06), [[FDPS]] (+0.76, fdr 7e-06); moves opposite to [[TMEM168]] (-0.39, fdr 6e-05), [[EEFSEC]] (-0.39, fdr 2e-04), [[ZNF12]] (-0.35, fdr 1e-04).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PCSK9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4182.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cepharanthine (drug)]] 5 µM |  | **2.17×** | +16.5 | 0e+00 | 46/48 (HS-578T, NCI-H2030, …) | rises with dose |  |
| [[Berbamine (drug)]] 5 µM |  | **2.03×** | +15.0 | 0e+00 | 46/48 (LoVo, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +13.7 | 4e-40 | 40/47 (A549, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.64×** | +10.5 | 9e-24 | 34/48 (hTERT-HPNE, A-172, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.02×** | +9.9 | 5e-21 | 28/35 (J82, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.92×** | +9.8 | 1e-20 | 31/43 (NCI-H460, J82, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +8.3 | 9e-15 | 35/46 (C-33 A, C32, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.60×** | +7.0 | 1e-10 | 32/47 (NCI-H2030, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.65×** | +7.0 | 2e-10 | 22/40 (J82, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +6.6 | 3e-09 | 30/48 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.54×** | +6.5 | 5e-09 | 32/47 (C32, HS-578T, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.58×** | +6.4 | 6e-09 | 32/48 (NCI-H2030, HOP62, …) | inconsistent across doses |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.50×** | +5.7 | 5e-07 | 29/48 (C32, HS-578T, …) | top dose only | plate-row cell shift |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.6 | 7e-07 | 25/47 (HS-578T, HOP62, …) | top dose only | plate-row cell shift |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.7 | 1e-04 | 21/48 (C32, A498, …) | top dose only |  |
| [[Posaconazole (drug)]] 5 µM |  | **1.39×** | +4.6 | 1e-04 | 23/48 (AsPC-1, NCI-H2030, …) | rises with dose | plate-row cell shift |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.37×** | +4.4 | 3e-04 | 22/47 (NCI-H2030, HS-578T, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | **1.23×** | +4.3 | 4e-04 | 24/48 (NCI-H2030, AsPC-1, …) | top dose only |  |
| [[Ritonavir (drug)]] 5 µM |  | **1.22×** | +4.2 | 7e-04 | 14/48 (PANC-1, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4182.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[5-Azacytidine (drug)]] 5 µM |  | **0.631×** | -7.0 | 2e-09 | 30/47 (KATO III, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.736×** | -4.7 | 9e-04 | 23/48 (NCI-H1792, A-427, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.820×** | -4.3 | 0.003 | 23/48 (RKO, COLO 205, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.755×** | -4.3 | 0.003 | 20/47 (KATO III, COLO 205, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.762×** | -4.1 | 0.004 | 17/48 (BT-474, SHP-77, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.746×** | -4.1 | 0.004 | 22/47 (hTERT-HPNE, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Quinestrol (drug)]] 5 µM |  | **0.832×** | -4.0 | 0.005 | 16/48 (KATO III, RKO, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.774×** | -3.7 | 0.017 | 16/48 (KATO III, SW480, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.801×** | -3.4 | 0.045 | 15/47 (HCT15, SHP-77, …) | all doses, flat | position effect removed |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.738×** | -3.3 | 0.056 | 12/48 (A-427, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.05 µM |  | **0.815×** | -3.1 | 0.084 | 10/48 (HCT15, LS 180, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.815×** | -3.1 | 0.084 | 13/47 (MIA PaCa-2, HepG2/C3A, …) | all doses, flat |  |
| [[Erlotinib (drug)]] 5 µM |  | **0.806×** | -3.1 | 0.088 | 11/47 (KATO III, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4182. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 21.6 | 4 | 0 | [[Cepharanthine (drug)]] 5 µM 3.02× (z +12.2) | — |
| [[LoVo (line)]] | wt | 18.3 | 4 | 0 | [[Berbamine (drug)]] 5 µM 4.82× (z +14.2) | — |
| [[AsPC-1 (line)]] | alt | 10.4 | 3 | 0 | [[Berbamine (drug)]] 5 µM 4.67× (z +10.2) | — |
| [[HOP62 (line)]] | alt | 17.3 | 3 | 0 | [[Cepharanthine (drug)]] 5 µM 4.52× (z +14.3) | — |
| [[HS-578T (line)]] | alt | 25.8 | 3 | 0 | [[Cepharanthine (drug)]] 5 µM 5.83× (z +15.9) | — |
| [[hTERT-HPNE (line)]] | wt | 28.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.88× (z +15.1) | — |
| [[NCI-H2030 (line)]] | alt | 40.8 | 3 | 0 | [[Cepharanthine (drug)]] 5 µM 4.25× (z +14.3) | — |
| [[SNU-423 (line)]] | alt | 40.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +13.4) | — |
| [[A-172 (line)]] | wt | 19.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +14.2) | — |
| [[A549 (line)]] | wt | 13.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.06× (z +11.0) | — |
| [[C-33 A (line)]] | alt | 29.5 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 4.60× (z +11.7) | — |
| [[C32 (line)]] | wt | 18.3 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 4.51× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 29.5 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.48× (z +11.9) | — |
| [[J82 (line)]] | alt | 43.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 32.5 | 2 | 0 | [[Berbamine (drug)]] 5 µM 3.51× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 13.0 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 4.80× (z +11.5) | — |
| [[NCI-H460 (line)]] | wt | 19.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +12.3) | — |
| [[SNU-1 (line)]] | wt | 35.6 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 4.10× (z +9.6) | — |
| [[A-427 (line)]] | wt | 40.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.436× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0866× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 26.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +10.2) | — |
| [[KATO III (line)]] | alt | 48.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -10.7) ⚠ cell-cycle shift, explains ~3% of this change |
| [[NCI-H2347 (line)]] | alt | 19.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +10.3) | — |
| [[Panc 03.27 (line)]] | alt | 17.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[PANC-1 (line)]] | alt | 41.3 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 2.28× (z +9.1) | — |
| [[SW48 (line)]] | wt | 26.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +8.6) | — |
| [[SW480 (line)]] | alt | 26.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[AN3 CA (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4182), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDI1]] | +0.80 | +0.83 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 828 |
| [[HMGCS1]] | +0.77 | +0.80 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 998 |
| [[FDPS]] | +0.76 | +0.69 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 829 |
| [[DBI]] | +0.75 | +0.76 / +0.73 | both halves | 7e-06 | STRING 592 |
| [[HMGCR]] | +0.75 | +0.78 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 900 |
| [[CYP51A1]] | +0.72 | +0.71 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 732 |
| [[EBP]] | +0.72 | +0.70 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 701 |
| [[DHCR7]] | +0.70 | +0.74 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 759 |
| [[FASN]] | +0.70 | +0.74 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 571 |
| [[SCD]] | +0.70 | +0.68 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 497 |
| [[PCSK9]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[MMAB]] | +0.68 | +0.73 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM168]] | -0.39 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[EEFSEC]] | -0.39 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[ZNF12]] | -0.35 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[PSMF1]] | -0.34 | -0.40 / -0.27 | both halves | 3e-04 |  |
| [[MOCS1]] | -0.33 | -0.29 / -0.30 | both halves | 2e-04 |  |
| [[MECR]] | -0.33 | -0.37 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCSK9]] | B | PCSK9 activity lowers ACAT2's level | lines that do not express PCSK9 (28) vs lines expressing it (22) | 1.06× higher at baseline in the lines without PCSK9 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: C6orf132, RNF223, CDH1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.820). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.1, -49.3); signed map (-52.6, 32.2). **Vector** length 119, 33.3% of its response variance represented; |z| ≥ 3 in 1,209 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Regulation of cholesterol biosynthesis by SREBP (SREBF)* (reactome, mean cos +0.66 to 17); *Activation of gene expression by SREBF (SREBP)* (reactome, mean cos +0.67 to 16); *mTORC1 signaling* (hallmark, mean cos +0.62 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +8.7 | +16.5 |
|  | [[Berbamine (drug)]] 5 µM |  | +7.9 | +15.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +13.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +6.7 | +9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +10.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +4.7 | +7.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +4.6 | +6.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.3 | +3.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.0 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.5 | -7.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | acetyl-CoA acetyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.3 — chr6:159,762,045-159,779,112 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Acetyl-CoA acetyltransferases |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, FATTY_ACID_METABOLISM |
| Reactome | 4 pathways, smallest: Lanosterol biosynthesis; Cholesterol biosynthesis; Metabolism of steroids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BWD1](https://www.uniprot.org/uniprotkb/Q9BWD1) (Acetyl-CoA acetyltransferase, cytosolic):

> Involved in the biosynthetic pathway of cholesterol.

**Summary**, from NCBI Gene [39](https://www.ncbi.nlm.nih.gov/gene/39):

> The product of this gene is an enzyme involved in lipid metabolism, and it encodes cytosolic acetoacetyl-CoA thiolase. This gene shows complementary overlapping with the 3-prime region of the TCP1 gene in both mouse and human. These genes are encoded on opposite strands of DNA, as well as in opposite transcriptional orientation. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:94](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:94) · Entrez [39](https://www.ncbi.nlm.nih.gov/gene/39) · UniProt [Q9BWD1](https://www.uniprot.org/uniprotkb/Q9BWD1) · Ensembl [ENSG00000120437](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120437)

## Data

Gene col 4182: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4182); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4182, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4182]; `tensor/DDL_lfc|DDL_z.npy` [4182]; `embed/gene_vectors.npy` [4182]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4182 or target_col == 4182). Every well: [[ACAT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACAT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
