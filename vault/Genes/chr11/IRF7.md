---
symbol: "IRF7"
type: "gene"
col: 11690
ensembl_id: "ENSG00000185507"
name: "interferon regulatory factor 7"
location: "11p15.5"
module: 70
arm: "+"
pooled_cpm: 22.58
n_lines_expressing: 39
n_dd_up: 6
n_dd_down: 24
n_dd_up_clean: 2
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 19
direction_downstream: 1
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# IRF7

*interferon regulatory factor 7* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.83× (z +6.8, q 8e-09, up in 26 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (C32 4.35×, AsPC-1 2.81×, PANC-1 2.75×, COLO 205 3.26×, …; ⚠ cell-cycle shift, explains ~60% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HOP62 8.55×, hTERT-HPNE 14.4×, A549 3.21×); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 5.53×).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.449× (z -8.9, q 3e-16, down in 28 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ISG15]] (+0.84, fdr 7e-06), [[HELZ2]] (+0.82, fdr 7e-06), [[DHX58]] (+0.81, fdr 7e-06); moves opposite to [[IPO5]] (-0.60, fdr 1e-05), [[OPA1]] (-0.60, fdr 1e-05), [[AGO1]] (-0.59, fdr 1e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[TYMP]] → it (grade B ⚠); 1 goes from it, the strongest it → [[GSDMD]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11690.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (C32 4.35×, AsPC-1 2.81×, PANC-1 2.75×, COLO 205 3.26×, …; ⚠ cell-cycle shift, explains ~60% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HOP62 8.55×, hTERT-HPNE 14.4×, A549 3.21×); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 5.53×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +6.8 | 8e-09 | 26/35 (HOP62, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.75×** | +6.3 | 9e-08 | 24/37 (C32, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.82×** | +4.8 | 3e-04 | 22/33 (J82, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.82×** | +4.6 | 5e-04 | 20/36 (PANC-1, C32, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.78×** | +4.6 | 5e-04 | 22/35 (C32, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.73×** | +4.4 | 0.001 | 27/36 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.49× | +3.2 | 0.11 | 18/34 (HOP62, PANC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.31× | +3.0 | 0.17 | 16/37 (SHP-77, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11690.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.449×** | -8.9 | 3e-16 | 28/36 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.576×** | -6.1 | 2e-07 | 22/37 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.469×** | -6.0 | 5e-07 | 27/35 (RKO, LoVo, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.485×** | -5.7 | 2e-06 | 24/36 (NCI-H23, LoVo, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.489×** | -5.6 | 2e-06 | 22/34 (RKO, LoVo, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.516×** | -5.2 | 2e-05 | 28/36 (AsPC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.279×** | -4.7 | 3e-04 | 24/36 (NCI-H1792, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.570×** | -4.4 | 7e-04 | 23/34 (RPMI-7951, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.579×** | -4.3 | 0.001 | 23/36 (A549, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.332×** | -4.0 | 0.003 | 25/35 (LOX-IMVI, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.599×** | -3.8 | 0.007 | 23/34 (A498, COLO 205, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.626×** | -3.7 | 0.011 | 16/36 (NCI-H1792, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.628×** | -3.7 | 0.011 | 21/36 (BT-474, CHP-212, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.636×** | -3.6 | 0.015 | 19/36 (NCI-H1792, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.732×** | -3.4 | 0.020 | 19/37 (NCI-H1573, COLO 205, …) | rises with dose | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **0.645×** | -3.4 | 0.020 | 17/37 (LoVo, CFPAC-1, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.658×** | -3.3 | 0.032 | 18/35 (LoVo, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.642×** | -3.2 | 0.037 | 20/36 (SK-MEL-2, NCI-H2347, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11690. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 31.2 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +8.5) | [[Tofacitinib (drug)]] 5 µM 0.197× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 56.0 | 0 | 4 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.237× (z -13.5) |
| [[NCI-H1792 (line)]] | alt | 30.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.152× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 59.9 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +9.3) ⚠ cell-cycle shift, explains ~60% of this change | [[Dinaciclib (drug)]] 5 µM 0.0639× (z -16.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 18.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +9.4) ⚠ cell-cycle shift, explains ~60% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -8.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 25.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.248× (z -11.4) |
| [[LoVo (line)]] | wt | 31.3 | 0 | 3 | — | [[Tofacitinib (drug)]] 5 µM 0.150× (z -14.7) |
| [[SK-MEL-2 (line)]] | alt | 31.6 | 0 | 3 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.152× (z -13.5) |
| [[COLO 205 (line)]] | alt | 64.8 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +8.9) ⚠ cell-cycle shift, explains ~60% of this change | [[Tofacitinib (drug)]] 5 µM 0.237× (z -10.9) |
| [[HOP62 (line)]] | alt | 7.41 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.55× (z +13.0) | — |
| [[NCI-H23 (line)]] | alt | 19.6 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0486× (z -13.3) |
| [[A-172 (line)]] | wt | 19.6 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.280× (z -9.2) |
| [[BT-474 (line)]] | alt | 21.2 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0931× (z -10.0) |
| [[Hs 766T (line)]] | wt | 14.4 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.229× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 5.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.4× (z +10.4) | — |
| [[NCI-H2347 (line)]] | alt | 117 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.308× (z -11.5) |
| [[PANC-1 (line)]] | alt | 20.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +8.9) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[RKO (line)]] | wt | 17.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.144× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 16.5 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0416× (z -12.5) |
| [[SW480 (line)]] | alt | 9.44 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.53× (z +9.1) | — |
| [[A-427 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.46 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.33 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11690), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISG15]] | +0.84 | +0.72 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 973 |
| [[HELZ2]] | +0.82 | +0.73 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 596 |
| [[DHX58]] | +0.81 | +0.77 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 909 |
| [[IRF9]] | +0.80 | +0.71 / +0.77 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 900 |
| [[IFI6]] | +0.79 | +0.63 / +0.85 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 914 |
| [[IFI27]] | +0.79 | +0.69 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 821 |
| [[HLA-F]] | +0.77 | +0.70 / +0.80 | both halves | 7e-06 | pathway: Interferon Signaling |
| [[TYMP]] | +0.76 | +0.67 / +0.80 | both halves | 7e-06 | STRING 504 |
| [[TRIM5]] | +0.76 | +0.74 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 551 |
| [[PARP10]] | +0.76 | +0.79 / +0.75 | both halves | 7e-06 | pathway: SARS-CoV-2 Infection; STRING 471 |
| [[IFITM3]] | +0.76 | +0.57 / +0.83 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 715 |
| [[OASL]] | +0.76 | +0.70 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 913 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO5]] | -0.60 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[OPA1]] | -0.60 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[AGO1]] | -0.59 | -0.51 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 15, C 4. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TYMP]] | B | TYMP activity raises IRF7's level | lines that do not express TYMP (20) vs lines expressing it (30) | 2.45× lower at baseline in the lines without TYMP | 0.015 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |
| [[DLX2]] | B | DLX2 activity lowers IRF7's level | lines that do not express DLX2 (8) vs lines expressing it (42) | 1.80× higher at baseline in the lines without DLX2 | 0.026 | ⚠ within organs, on part of the lines; also absent: LINC01145-1, SCHIP1, NPHS1; maybe low, not absent |
| [[DUOX2]] | B | DUOX2 activity raises IRF7's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 2.04× lower at baseline in the lines without DUOX2 | 0.036 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |
| [[MX1]] | B | MX1 activity strengthens IRF7's drug response | lines that do not express MX1 (12) vs lines expressing it (25) | the lines without MX1 respond 0.79× as strongly (z diff +0.18); strongest at Auranofin 5 µM: 0.59x vs 0.37x (z diff +2.7) | 0.039 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1; target measured in part of the lines; both ways |
| [[MX1]] | B | MX1 activity raises IRF7's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.12× lower at baseline in the lines without MX1 | 0.048 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[MMP13]] | B | MMP13 activity raises IRF7's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 2.22× lower at baseline in the lines without MMP13 | 0.053 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[GBP4]] | B | GBP4 activity raises IRF7's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.76× lower at baseline in the lines without GBP4 | 0.057 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[PARP9]] | B | PARP9 activity raises IRF7's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 2.34× lower at baseline in the lines without PARP9 | 0.058 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[PLSCR1]] | B | PLSCR1 activity raises IRF7's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 1.58× lower at baseline in the lines without PLSCR1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[IFI6]] | B | IFI6 activity raises IRF7's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 1.67× lower at baseline in the lines without IFI6 | 0.060 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[HLA-F]] | B | HLA-F activity raises IRF7's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 2.71× lower at baseline in the lines without HLA-F | 0.064 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[ETV7]] | B | ETV7 activity raises IRF7's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 2.25× lower at baseline in the lines without ETV7 | 0.064 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GSDMD]] | C | IRF7 activity raises GSDMD's level | lines that do not express IRF7 (11) vs lines expressing it (39) | 2.16× lower at baseline in the lines without IRF7 | 0.083 | ⚠ within organs, on part of the lines; also absent: PLSCR4, GSDMD, LRRK1; co-absent with the target |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.743). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (49.0, 51.5); signed map (64.9, 29.3). **Vector** length 113, 37.6% of its response variance represented; |z| ≥ 3 in 750 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Antigen processing-Cross presentation* (reactome, mean cos +0.61 to 14); *Endosomal/Vacuolar pathway* (reactome, mean cos +0.60 to 8); *ER-Phagosome pathway* (reactome, mean cos +0.61 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +6.8 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +6.0 | +4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.3 | +4.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +4.8 | +4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +6.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.1 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +1.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.4 | +2.2 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.3 | +2.1 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -5.9 | -8.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | -5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.3 | -3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -4.1 | -3.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.0 | -6.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -4.0 | -5.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.9 | -6.0 |

## What is on record

|  |  |
|---|---|
| Name | interferon regulatory factor 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:612,553-615,983 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Interferon regulatory factors |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, ALLOGRAFT_REJECTION, INFLAMMATORY_RESPONSE, COMPLEMENT, INTERFERON_GAMMA_RESPONSE |
| Reactome | 26 pathways, smallest: DEx/H-box helicases activate type I IFN and inflammatory cytokines production; TRAF6 mediated IRF7 activation in TLR7/8 or 9 signaling; TICAM1-dependent activation of IRF3/IRF7 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92985](https://www.uniprot.org/uniprotkb/Q92985) (Interferon regulatory factor 7):

> Key transcriptional regulator of type I interferon (IFN)-dependent immune responses and plays a critical role in the innate immune response against DNA and RNA viruses. Regulates the transcription of type I IFN genes (IFN-alpha and IFN-beta) and IFN-stimulated genes (ISG) by binding to an interferon-stimulated response element (ISRE) in their promoters. Can efficiently activate both the IFN-beta (IFNB) and the IFN-alpha (IFNA) genes and mediate their induction via both the virus-activated, …

**Summary**, from NCBI Gene [3665](https://www.ncbi.nlm.nih.gov/gene/3665):

> This gene encodes interferon regulatory factor 7, a member of the interferon regulatory transcription factor (IRF) family. It has been shown to play a role in the transcriptional activation of virus-inducible cellular genes, including interferon beta chain genes. Inducible expression of IRF7 is largely restricted to lymphoid tissue. The encoded protein plays an important role in the innate immune response against DNA and RNA viruses. [provided by RefSeq, Jul 2021]

**Accessions** — [HGNC:6122](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6122) · Entrez [3665](https://www.ncbi.nlm.nih.gov/gene/3665) · UniProt [Q92985](https://www.uniprot.org/uniprotkb/Q92985) · Ensembl [ENSG00000185507](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185507)

## Data

Gene col 11690: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11690); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11690, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11690]; `tensor/DDL_lfc|DDL_z.npy` [11690]; `embed/gene_vectors.npy` [11690]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11690 or target_col == 11690). Every well: [[IRF7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IRF7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
