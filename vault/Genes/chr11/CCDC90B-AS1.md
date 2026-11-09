---
symbol: "CCDC90B-AS1"
type: "gene"
col: 14928
ensembl_id: "ENSG00000255234"
name: "CCDC90B antisense RNA 1"
location: "11q14.1"
module: 26
arm: "+"
pooled_cpm: 7.27
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# CCDC90B-AS1

*CCDC90B antisense RNA 1* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.89× (z +25.8, q 0e+00, up in 43 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.582× (z -5.1, q 2e-04, down in 22 of 47 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Niclosamide (olamine) (drug)]] 0.5 µM: 0.616× (z -4.6, q 1e-03, down in 20 of 47 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMADHC-DT]] (+0.87, fdr 7e-06), [[PKN2-AS1]] (+0.85, fdr 1e-05), [[TMEM202-AS1]] (+0.85, fdr 1e-05); moves opposite to [[BRAT1]] (-0.74, fdr 7e-06), [[MAST3]] (-0.72, fdr 4e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14928.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.89×** | +25.8 | 0e+00 | 43/43 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.37×** | +16.3 | 0e+00 | 39/45 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.41×** | +13.5 | 3e-39 | 36/41 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.31×** | +11.3 | 2e-27 | 39/45 (SW480, C32, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.42×** | +11.2 | 6e-27 | 36/44 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.16×** | +10.3 | 1e-22 | 36/47 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.15×** | +7.2 | 4e-11 | 28/42 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.93×** | +6.2 | 4e-08 | 28/46 (A-427, A549, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.48×** | +5.3 | 9e-06 | 21/48 (LS 180, A-427, …) | rises with dose | low cells (technical?) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.66×** | +4.8 | 9e-05 | 21/47 (A-172, H4, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.34×** | +3.5 | 0.025 | 9/48 (SW480, LS 180, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.025 | 9/46 (LS 180, A-172, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +3.4 | 0.027 | 7/45 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.034 | 18/47 (SW480, Hs 766T, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.070 | 10/48 (LoVo, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14928.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.582×** | -5.1 | 2e-04 | 22/47 (RPMI-7951, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.616×** | -4.6 | 1e-03 | 20/47 (SW48, A-427, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.619×** | -4.6 | 1e-03 | 21/44 (HT-29, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.634×** | -4.2 | 0.004 | 16/36 (SNU-423, HCT15, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.662×** | -3.9 | 0.010 | 20/47 (H4, Panc 03.27, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **0.686×** | -3.4 | 0.052 | 17/40 (PANC-1, HCT15, …) | two highest doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **0.698×** | -3.4 | 0.052 | 11/47 (SW 1088, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14928. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.00 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.04× (z +12.5) | [[Harringtonine (drug)]] 0.05 µM 0.0499× (z -13.8) |
| [[PANC-1 (line)]] | alt | 11.3 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.43× (z +11.7) | [[Digitoxin (drug)]] 5 µM 0.187× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -8.6) |
| [[SW480 (line)]] | alt | 7.10 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.26× (z +14.6) | — |
| [[HS-578T (line)]] | alt | 5.82 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +12.0) | — |
| [[LS 180 (line)]] | wt | 8.88 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.60× (z +12.7) | — |
| [[A-172 (line)]] | wt | 10.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.47× (z +11.9) | — |
| [[A498 (line)]] | wt | 4.94 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +12.1) | — |
| [[C32 (line)]] | wt | 9.26 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.37× (z +10.1) | — |
| [[H4 (line)]] | wt | 11.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.54× (z +9.1) | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0849× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 8.41 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.85× (z +11.2) | — |
| [[HT-29 (line)]] | alt | 5.85 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.54× (z +11.5) | [[Belinostat (drug)]] 0.5 µM 0.0859× (z -9.4) |
| [[J82 (line)]] | alt | 5.07 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.73× (z +9.9) | — |
| [[LoVo (line)]] | wt | 7.06 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.54× (z +14.2) | — |
| [[LOX-IMVI (line)]] | wt | 7.42 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.80× (z +12.7) | — |
| [[NCI-H1573 (line)]] | alt | 12.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 4.56 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +11.9) | — |
| [[NCI-H23 (line)]] | alt | 13.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +11.0) | [[Simotinib (drug)]] 5 µM 0.0743× (z -12.0) ⚠ toxic |
| [[A549 (line)]] | wt | 4.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.18× (z +9.5) | — |
| [[AsPC-1 (line)]] | alt | 3.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.2× (z +11.1) | — |
| [[BT-474 (line)]] | alt | 5.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.14× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 2.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 4.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.47× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 5.22 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.7× (z +9.9) | — |
| [[KATO III (line)]] | alt | 8.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.74× (z +12.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.39× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 4.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.08× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 6.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.40× (z +10.7) | — |
| [[RKO (line)]] | wt | 4.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 12.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.26× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 9.30 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0742× (z -9.9) ⚠ toxic |
| [[SW 900 (line)]] | alt | 7.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.47× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 4.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.68× (z +10.6) | — |
| [[A-427 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14928), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMADHC-DT]] | +0.87 | +0.82 / +0.60 | both halves | 7e-06 |  |
| [[PKN2-AS1]] | +0.85 | +0.80 / +0.55 | both halves | 1e-05 | same gene group |
| [[TMEM202-AS1]] | +0.85 | +0.82 / +0.49 | both halves | 1e-05 | same gene group |
| [[PPP1R12A-AS2]] | +0.85 | +0.83 / +0.52 | both halves | 1e-05 | same gene group |
| [[FBXL19-AS1]] | +0.84 | +0.73 / +0.67 | both halves | 7e-06 | same gene group |
| [[LINC00571]] | +0.84 | +0.79 / +0.54 | both halves | 1e-05 |  |
| [[PCNX4-DT]] | +0.83 | +0.84 / +0.42 | both halves | 4e-05 |  |
| [[ARRDC3-AS1]] | +0.83 | +0.84 / +0.52 | both halves | 1e-05 | same gene group |
| [[MZF1-AS1]] | +0.82 | +0.81 / +0.58 | both halves | 7e-06 | same gene group |
| [[CIBAR1-DT]] | +0.81 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[NEB]] | +0.81 | +0.80 / +0.60 | both halves | 7e-06 |  |
| [[NQO1-DT]] | +0.81 | +0.79 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRAT1]] | -0.74 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[MAST3]] | -0.72 | -0.60 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCDC90B-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02641]] | B | LINC02641 activity raises CCDC90B-AS1's level | lines that do not express LINC02641 (14) vs lines expressing it (36) | 1.53× lower at baseline in the lines without LINC02641 | 0.022 | ⚠ within organs, on part of the lines; also absent: PSD2, LINC02940, ENSG00000250101; maybe low, not absent |
| [[CYP1B1-AS1]] | B | CYP1B1-AS1 activity raises CCDC90B-AS1's level | lines that do not express CYP1B1-AS1 (14) vs lines expressing it (36) | 1.38× lower at baseline in the lines without CYP1B1-AS1 | 0.035 | ⚠ within organs, on part of the lines; also absent: KCNMA1, ENOX1, PDGFC; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises CCDC90B-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC01917]] | B | LINC01917 activity raises CCDC90B-AS1's level | lines that do not express LINC01917 (19) vs lines expressing it (31) | 1.36× lower at baseline in the lines without LINC01917 | 0.096 | ⚠ within organs, on part of the lines; also absent: LINC00504, RMEL3, TEK; maybe low, not absent |
| [[SOCS2-AS1]] | B | SOCS2-AS1 activity raises CCDC90B-AS1's level | lines that do not express SOCS2-AS1 (13) vs lines expressing it (37) | 1.40× lower at baseline in the lines without SOCS2-AS1 | 0.096 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.923). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (8.5, 13.4); signed map (24.7, -5.2). **Vector** length 100, 22.9% of its response variance represented; |z| ≥ 3 in 1,086 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.8 | +25.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.6 | +10.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.3 | +11.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +16.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +13.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +1.3 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -7.8 | -5.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -6.9 | -3.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | -1.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.6 | -4.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.5 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.2 | -2.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.3 | -4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -2.3 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | +1.0 |

## What is on record

|  |  |
|---|---|
| Name | CCDC90B antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q14.1 — chr11:83,286,120-83,423,516 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55505](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55505) · Entrez [120883614](https://www.ncbi.nlm.nih.gov/gene/120883614) · Ensembl [ENSG00000255234](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255234)

## Data

Gene col 14928: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14928); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14928, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14928]; `tensor/DDL_lfc|DDL_z.npy` [14928]; `embed/gene_vectors.npy` [14928]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14928 or target_col == 14928). Every well: [[CCDC90B-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC90B-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
