---
symbol: "PRELID3A"
type: "gene"
col: 6511
ensembl_id: "ENSG00000141391"
name: "PRELI domain containing 3A"
location: "18p11.21"
module: 18
arm: "+"
pooled_cpm: 9.03
n_lines_expressing: 47
n_dd_up: 24
n_dd_down: 7
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# PRELID3A

*PRELI domain containing 3A* — 18p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 1.67× (z +8.5, q 1e-14, up in 25 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.329× (z -9.2, q 3e-17, down in 26 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.295×, A549 0.343×; ⚠ cell-cycle shift, explains ~51% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.172×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (A-427 0.0441×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RILPL1]] (+0.67, fdr 7e-06), [[GATD1]] (+0.59, fdr 1e-05), [[CAMKK2]] (+0.57, fdr 1e-05); moves opposite to [[TXN2]] (-0.51, fdr 5e-05), [[AGPAT1]] (-0.51, fdr 3e-05), [[ATP7A]] (-0.50, fdr 4e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NT5M]] → it (grade B ⚠); 5 go from it, the strongest it → [[LRFN4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6511.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.67×** | +8.5 | 1e-14 | 25/43 (LoVo, A-427, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.37×** | +7.4 | 3e-11 | 19/45 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +6.0 | 3e-07 | 9/34 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.26×** | +5.4 | 9e-06 | 14/44 (A-427, HCT15, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.38×** | +5.4 | 9e-06 | 12/43 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +5.2 | 2e-05 | 15/43 (LoVo, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +5.1 | 3e-05 | 16/42 (LoVo, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.37×** | +4.8 | 1e-04 | 11/40 (SNU-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +4.5 | 4e-04 | 5/37 (NCI-H460, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.31×** | +4.5 | 4e-04 | 12/43 (SK-MEL-2, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.31×** | +4.3 | 9e-04 | 16/42 (NCI-H2030, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +4.2 | 0.001 | 6/45 (SW480, NCI-H460, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.002 | 9/44 (A-427, LOX-IMVI, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.002 | 8/44 (SW480, NCI-H1792, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +3.8 | 0.006 | 10/44 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.007 | 6/42 (BT-474, A-172, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.009 | 2/42 (SW 900, C-33 A) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6511.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.295×, A549 0.343×; ⚠ cell-cycle shift, explains ~51% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.172×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (A-427 0.0441×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.329×** | -9.2 | 3e-17 | 26/42 (A-427, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.695×** | -8.5 | 4e-15 | 25/41 (MIA PaCa-2, A549, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.688×** | -6.0 | 5e-07 | 17/43 (A549, A-172, …) | top dose only | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.509×** | -5.6 | 3e-06 | 19/40 (A-172, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.766×** | -4.4 | 0.001 | 12/44 (PANC-1, SW1417, …) | top dose only | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.617×** | -4.0 | 0.006 | 4/39 (SW48, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.806×** | -3.6 | 0.029 | 16/41 (PANC-1, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6511. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 42.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0441× (z -13.6) |
| [[A549 (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -8.7) ⚠ cell-cycle shift, explains ~51% of this change |
| [[Hs 766T (line)]] | wt | 6.72 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0973× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 8.85 | 1 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 4.32× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -10.4) ⚠ cell-cycle shift, explains ~51% of this change |
| [[PANC-1 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.309× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.127× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.806 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6511), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RILPL1]] | +0.67 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[GATD1]] | +0.59 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[CAMKK2]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[SVIL-AS1-1]] | +0.56 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[FSD1L]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[TRIM65]] | +0.56 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[PLEKHJ1]] | +0.55 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[MPP3]] | +0.55 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[PUS7]] | +0.55 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[ZC3H8]] | +0.54 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[SFXN4]] | +0.53 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[TMEM267]] | +0.53 | +0.66 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXN2]] | -0.51 | -0.58 / -0.39 | both halves | 5e-05 |  |
| [[AGPAT1]] | -0.51 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[ATP7A]] | -0.50 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[SYAP1]] | -0.50 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[ARL5B]] | -0.49 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[AP1G1]] | -0.48 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[SLC39A9]] | -0.47 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[MDH1]] | -0.47 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[C4orf33]] | -0.46 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[EID1]] | -0.46 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[TMCO1]] | -0.45 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[STAU1]] | -0.45 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5M]] | B | NT5M activity raises PRELID3A's level | lines that do not express NT5M (7) vs lines expressing it (43) | 2.70× lower at baseline in the lines without NT5M | 0.003 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRFN4]] | C | PRELID3A activity raises LRFN4's level | lines that do not express PRELID3A (3) vs lines expressing it (47) | 2.99× lower at baseline in the lines without PRELID3A | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, HCN2, USP31; its own permutation p |
| [[GTF2H2]] | C | PRELID3A activity raises GTF2H2's level | lines that do not express PRELID3A (3) vs lines expressing it (47) | 1.85× lower at baseline in the lines without PRELID3A | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, HCN2, USP31 |
| [[SHLD2]] | C | PRELID3A activity raises SHLD2's level | lines that do not express PRELID3A (3) vs lines expressing it (47) | 1.21× lower at baseline in the lines without PRELID3A | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, HCN2, USP31 |
| [[PAM16]] | C | PRELID3A activity raises PAM16's level | lines that do not express PRELID3A (3) vs lines expressing it (47) | 1.61× lower at baseline in the lines without PRELID3A | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, HCN2, USP31 |
| [[C4orf33]] | C | PRELID3A activity lowers C4orf33's level | lines that do not express PRELID3A (3) vs lines expressing it (47) | 1.59× higher at baseline in the lines without PRELID3A | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, HCN2, USP31; its own permutation p |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.522). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-12.6, -29.4); signed map (-44.1, -16.1). **Vector** length 72.5, 12.9% of its response variance represented; |z| ≥ 3 in 794 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +8.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.8 | +6.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +1.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.9 | +5.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +7.4 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.7 | +5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +4.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.7 | -9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -2.9 | -8.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -5.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -1.9 | -4.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.2 | -1.3 |
|  | [[Docetaxel (drug)]] 5 µM |  | -1.0 | -2.7 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -0.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | PRELI domain containing 3A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.21 — chr18:12,407,896-12,432,238 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HFL-EDDG1, FLJ31484; previously C18orf43, SLMO1 |
| Gene groups (HGNC) | PRELI domain containing |
| Reactome | 3 pathways, smallest: TP53 Regulates Transcription of Genes Involved in Cytochrome C Release; TP53 Regulates Transcription of Cell Death Genes; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96N28](https://www.uniprot.org/uniprotkb/Q96N28) (PRELI domain containing protein 3A):

> In vitro, the TRIAP1:PRELID3A complex mediates the transfer of phosphatidic acid (PA) between liposomes and probably functions as a PA transporter across the mitochondrion intermembrane space. Phosphatidic acid import is required for cardiolipin (CL) synthesis in the mitochondrial inner membrane.

**Summary**, from NCBI Gene [10650](https://www.ncbi.nlm.nih.gov/gene/10650):

> Enables phosphatidic acid transfer activity. Involved in phospholipid transport. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24639](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24639) · Entrez [10650](https://www.ncbi.nlm.nih.gov/gene/10650) · UniProt [Q96N28](https://www.uniprot.org/uniprotkb/Q96N28) · Ensembl [ENSG00000141391](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141391)

## Data

Gene col 6511: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6511); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6511, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6511]; `tensor/DDL_lfc|DDL_z.npy` [6511]; `embed/gene_vectors.npy` [6511]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6511 or target_col == 6511). Every well: [[PRELID3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRELID3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
