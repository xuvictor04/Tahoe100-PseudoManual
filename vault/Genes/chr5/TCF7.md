---
symbol: "TCF7"
type: "gene"
col: 1306
ensembl_id: "ENSG00000081059"
name: "transcription factor 7"
location: "5q31.1"
module: 112
arm: "+"
pooled_cpm: 15.72
n_lines_expressing: 47
n_dd_up: 24
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# TCF7

*transcription factor 7* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (15 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.03× (z +14.5, q 6e-45, up in 30 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.746× (z -6.1, q 6e-07, down in 21 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.169×, SNU-423 0.294×); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.497×; ⚠ position not correctable); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H23 0.0864×); [[Binimetinib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.250×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FZD8]] (+0.54, fdr 2e-05), [[ABR]] (+0.54, fdr 1e-05), [[EPHB2]] (+0.53, fdr 1e-05); moves opposite to [[DTWD1]] (-0.48, fdr 4e-05), [[NNMT]] (-0.47, fdr 4e-05), [[GRAMD2B]] (-0.46, fdr 5e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02509]] → it (grade B ⚠); 2 go from it, the strongest it → [[SYNJ2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1306.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +14.5 | 6e-45 | 30/43 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.48×** | +13.2 | 3e-37 | 24/33 (LoVo, PANC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.51×** | +12.4 | 9e-33 | 18/24 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.02×** | +9.8 | 2e-20 | 14/20 (SW480, LoVo, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.89×** | +9.3 | 2e-18 | 27/45 (HOP62, LoVo, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.85×** | +8.9 | 4e-17 | 27/45 (NCI-H1792, A-172, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +8.0 | 7e-14 | 22/43 (HepG2/C3A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +7.8 | 5e-13 | 22/45 (HOP62, SHP-77, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.60×** | +6.8 | 5e-10 | 22/45 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +6.8 | 7e-10 | 19/43 (HOP62, NCI-H1792, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.56×** | +6.5 | 5e-09 | 22/44 (HOP62, LoVo, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.37×** | +4.4 | 5e-04 | 11/42 (LoVo, NCI-H2347, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.75×** | +4.1 | 0.002 | 10/39 (NCI-H1792, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.69×** | +3.8 | 0.006 | 8/40 (A-172, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.67×** | +3.7 | 0.007 | 9/42 (NCI-H1792, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.62×** | +3.5 | 0.015 | 8/40 (PANC-1, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.18× | +3.3 | 0.025 | 10/45 (SHP-77, A-172, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.043 | 11/45 (HOP62, J82, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +2.9 | 0.082 | 11/45 (J82, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +2.8 | 0.098 | 12/45 (NCI-H2347, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1306.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.169×, SNU-423 0.294×); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.497×; ⚠ position not correctable); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H23 0.0864×); [[Binimetinib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.250×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.746×** | -6.1 | 6e-07 | 21/45 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.722×** | -4.6 | 0.001 | 12/45 (MIA PaCa-2, COLO 205, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.758×** | -4.1 | 0.008 | 14/44 (NCI-H1792, HS-578T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.847× | -3.5 | 0.072 | 12/45 (HS-578T, A-172, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.834× | -3.1 | 0.17 | 17/45 (MIA PaCa-2, SW48, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.796× | -3.1 | 0.17 | 10/45 (MIA PaCa-2, CFPAC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.836× | -3.0 | 0.17 | 13/45 (MIA PaCa-2, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.809× | -3.0 | 0.17 | 11/43 (MIA PaCa-2, C-33 A, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.816× | -3.0 | 0.17 | 11/42 (HS-578T, SW480, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1306. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 86.2 | 0 | 7 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.169× (z -15.3) |
| [[HS-578T (line)]] | alt | 28.3 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.203× (z -9.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Budesonide (drug)]] 0.05 µM 0.207× (z -8.9) |
| [[LoVo (line)]] | wt | 15.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +12.1) | — |
| [[A549 (line)]] | wt | 8.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.91× (z +10.8) | — |
| [[AN3 CA (line)]] | alt | 28.4 | 0 | 1 | — | [[Fenofibrate (drug)]] 5 µM 0.0692× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 36.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 6.52 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0864× (z -10.4) |
| [[RKO (line)]] | wt | 16.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 36.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.294× (z -8.8) |
| [[A-172 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.75 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.70 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1306), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FZD8]] | +0.54 | +0.48 / +0.54 | both halves | 2e-05 | pathway: HALLMARK_WNT_BETA_CATENIN_SIGNALING; STRING 408 |
| [[ABR]] | +0.54 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[EPHB2]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[CALB2]] | +0.53 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[PTHLH]] | +0.53 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[SHISAL1]] | +0.52 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[KCNC4]] | +0.50 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[LIF]] | +0.50 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[CRTAC1]] | +0.50 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[WNT9A]] | +0.50 | +0.48 / +0.50 | both halves | 2e-05 | pathway: Signaling by WNT; STRING 603 |
| [[SLC4A7]] | +0.49 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[AFF3]] | +0.49 | +0.45 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTWD1]] | -0.48 | -0.50 / -0.43 | both halves | 4e-05 |  |
| [[NNMT]] | -0.47 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[GRAMD2B]] | -0.46 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[FPGT]] | -0.44 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[FGD4]] | -0.44 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[MBNL2]] | -0.43 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[SLC19A2]] | -0.42 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[COPS5]] | -0.42 | -0.38 / -0.45 | both halves | 7e-05 | pathway: Co-inhibition by PD-1 |
| [[TSC22D3]] | -0.41 | -0.47 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02509]] | B | LINC02509 activity raises TCF7's level | lines that do not express LINC02509 (35) vs lines expressing it (15) | 1.29× lower at baseline in the lines without LINC02509 | 0.023 | ⚠ within organs, on part of the lines; also absent: POSTN, ITGA11, IRAG2 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYNJ2]] | C | TCF7 activity raises SYNJ2's level | lines that do not express TCF7 (3) vs lines expressing it (47) | 3.37× lower at baseline in the lines without TCF7 | 0.091 | ⚠ few lines (3 vs 47); across organs; also absent: FHL3, SKAP2, IGF2BP2; maybe low, not absent |
| [[HBEGF]] | C | TCF7 activity raises HBEGF's level | lines that do not express TCF7 (3) vs lines expressing it (47) | 3.42× lower at baseline in the lines without TCF7 | 0.094 | ⚠ few lines (3 vs 47); across organs; also absent: FHL3, SKAP2, IGF2BP2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.450). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.5, -4.4); signed map (-2.6, 35.0). **Vector** length 89.2, 17.6% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +8.4 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +8.3 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +12.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +14.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +6.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | -0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +2.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -3.8 | -6.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.9 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.9 | -4.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.8 | -1.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.8 | -1.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.7 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | transcription factor 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:134,114,681-134,151,865 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TCF-1 |
| Gene groups (HGNC) | TCF/LEF transcription factor family; Wnt enhanceosome complex |
| Hallmark sets | WNT_BETA_CATENIN_SIGNALING |
| Reactome | 22 pathways, smallest: RUNX3 regulates WNT signaling; Binding of TCF/LEF:CTNNB1 to target gene promoters; Germ layer formation at gastrulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P36402](https://www.uniprot.org/uniprotkb/P36402) (Transcription factor 7):

> Transcriptional activator involved in T-cell lymphocyte differentiation. Necessary for the survival of CD4(+) CD8(+) immature thymocytes. Isoforms lacking the N-terminal CTNNB1 binding domain cannot fulfill this role. Binds to the T-lymphocyte-specific enhancer element (5'-WWCAAAG-3') found in the promoter of the CD3E gene. Represses expression of the T-cell receptor gamma gene in alpha-beta T-cell lineages (By similarity). Required for the development of natural killer receptor-positive …

**Summary**, from NCBI Gene [6932](https://www.ncbi.nlm.nih.gov/gene/6932):

> This gene encodes a member of the T-cell factor/lymphoid enhancer-binding factor family of high mobility group (HMG) box transcriptional activators. This gene is expressed predominantly in T-cells and plays a critical role in natural killer cell and innate lymphoid cell development. The encoded protein forms a complex with beta-catenin and activates transcription through a Wnt/beta-catenin signaling pathway. Mice with a knockout of this gene are viable and fertile, but display a block in …

**Accessions** — [HGNC:11639](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11639) · Entrez [6932](https://www.ncbi.nlm.nih.gov/gene/6932) · UniProt [P36402](https://www.uniprot.org/uniprotkb/P36402) · Ensembl [ENSG00000081059](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081059)

## Data

Gene col 1306: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1306); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1306, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1306]; `tensor/DDL_lfc|DDL_z.npy` [1306]; `embed/gene_vectors.npy` [1306]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1306 or target_col == 1306). Every well: [[TCF7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCF7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
