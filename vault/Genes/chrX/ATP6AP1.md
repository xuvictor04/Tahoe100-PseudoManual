---
symbol: "ATP6AP1"
type: "gene"
col: 987
ensembl_id: "ENSG00000071553"
name: "ATPase H+ transporting accessory protein 1"
location: "Xq28"
module: 50
arm: "+"
pooled_cpm: 19.54
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 8
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# ATP6AP1

*ATPase H+ transporting accessory protein 1* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.05× (z +17.5, q 0e+00, up in 39 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.49× (z +6.2, q 7e-08, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Verteporfin (drug)]] 5 µM: 0.598× (z -7.8, q 4e-12, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMP1]] (+0.77, fdr 7e-06), [[GNS]] (+0.74, fdr 7e-06), [[CTSA]] (+0.73, fdr 7e-06); moves opposite to [[NIFK]] (-0.59, fdr 2e-05), [[BRIX1]] (-0.57, fdr 1e-05), [[EIF5B]] (-0.56, fdr 2e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[CLSTN1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 987.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.05×** | +17.5 | 0e+00 | 39/39 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.00×** | +16.6 | 0e+00 | 27/30 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.25×** | +11.8 | 9e-30 | 35/37 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +6.2 | 7e-08 | 25/48 (PANC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~20% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +6.0 | 2e-07 | 24/45 (SW1417, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +5.2 | 2e-05 | 23/48 (HOP62, HS-578T, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.37×** | +5.0 | 5e-05 | 23/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +5.0 | 5e-05 | 22/42 (CFPAC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.31×** | +4.3 | 0.001 | 20/48 (SNU-423, SW480, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.46×** | +4.2 | 0.001 | 15/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.21×** | +4.2 | 0.002 | 15/46 (A498, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.9 | 0.004 | 20/48 (PANC-1, RKO, …) | top dose only | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.006 | 15/47 (A-427, SW480, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.26×** | +3.6 | 0.014 | 10/48 (NCI-H460, PANC-1, …) | two highest doses | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.24×** | +3.4 | 0.027 | 6/48 (A-172, NCI-H460, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.51×** | +3.4 | 0.028 | 13/44 (RPMI-7951, COLO 205, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.034 | 13/48 (SK-MEL-2, A-172, …) | rises with dose | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.052 | 10/47 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.059 | 7/45 (Hs 766T, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.080 | 10/44 (HOP62, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.18× | +2.9 | 0.089 | 8/48 (SK-MEL-2, RKO, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 987.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.598×** | -7.8 | 4e-12 | 31/47 (hTERT-HPNE, HS-578T, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.677×** | -6.1 | 2e-07 | 30/48 (CFPAC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.566×** | -4.7 | 5e-04 | 18/38 (SK-MEL-2, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.763×** | -4.3 | 0.003 | 20/48 (NCI-H2347, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.772×** | -3.8 | 0.019 | 15/47 (HS-578T, HepG2/C3A, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.769×** | -3.6 | 0.032 | 12/48 (A-172, HT-29, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.800×** | -3.5 | 0.035 | 13/47 (PANC-1, SK-MEL-2, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 0.05 µM |  | **0.800×** | -3.3 | 0.081 | 13/47 (BT-474, CHP-212, …) | inconsistent across doses |  |
| [[Isocorydine (drug)]] 0.5 µM |  | 0.827× | -3.0 | 0.17 | 11/47 (SW1417, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 987. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 25.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +12.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 39.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +10.9) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 23.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +11.2) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 15.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.09× (z +12.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 21.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +10.5) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 19.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +8.8) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 0.05 µM 0.254× (z -9.0) |
| [[SW480 (line)]] | alt | 11.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +10.8) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 23.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +9.2) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.255× (z -10.1) |
| [[Hs 766T (line)]] | wt | 26.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +8.5) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 19.1 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.197× (z -8.7) |
| [[J82 (line)]] | alt | 24.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.45× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 24.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 24.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +11.8) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 41.6 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.105× (z -8.6) |
| [[SHP-77 (line)]] | alt | 20.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 25.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 35.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 987), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMP1]] | +0.77 | +0.77 / +0.71 | both halves | 7e-06 | STRING 462 |
| [[GNS]] | +0.74 | +0.73 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[CTSA]] | +0.73 | +0.74 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[LAMP2]] | +0.72 | +0.72 / +0.63 | both halves | 7e-06 | STRING 465 |
| [[TPP1]] | +0.70 | +0.63 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[GRN]] | +0.67 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[LAMB2]] | +0.66 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[LRPAP1]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[PIGT]] | +0.64 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[GAA]] | +0.64 | +0.57 / +0.61 | both halves | 9e-06 | pathway: HALLMARK_MYOGENESIS |
| [[TMED10]] | +0.63 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[GLMP]] | +0.63 | +0.62 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIFK]] | -0.59 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[BRIX1]] | -0.57 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[EIF5B]] | -0.56 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[CCDC137]] | -0.55 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[SURF6]] | -0.53 | -0.37 / -0.56 | both halves | 8e-05 |  |
| [[DNTTIP2]] | -0.53 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[REXO4]] | -0.51 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[FBXO45]] | -0.50 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[CEBPZ]] | -0.49 | -0.35 / -0.53 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLSTN1]] | C | ATP6AP1's natural level strengthens CLSTN1's drug response | ATP6AP1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.17; direction not clear | 0.078 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.5, -20.7); signed map (-24.5, -36.4). **Vector** length 83.0, 16.8% of its response variance represented; |z| ≥ 3 in 788 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glycosphingolipid catabolism* (reactome, mean cos +0.53 to 5); *Degradation of the extracellular matrix* (reactome, mean cos +0.51 to 7); *Glycosphingolipid metabolism* (reactome, mean cos +0.53 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.4 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +17.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +16.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +11.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.9 | +3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.6 | +3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.2 | +2.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -6.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.0 | -3.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.3 | -7.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | -2.8 | -3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ATPase H+ transporting accessory protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:154,428,633-154,436,516 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ORF, XAP-3, VATPS1, 16A, Ac45, XAP3, CF2; previously ATP6S1, ATP6IP1 |
| Hallmark sets | MYOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 11 pathways, smallest: Insulin receptor recycling; Transferrin endocytosis and recycling; Iron uptake and transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15904](https://www.uniprot.org/uniprotkb/Q15904) (V-type proton ATPase subunit S1):

> Accessory subunit of the V0 complex of vacuolar(H+)-ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that translocates protons. V-ATPase is responsible for acidifying and maintaining the pH of intracellular compartments and in some cell types, is targeted to the plasma membrane, where it promotes acidification of the extracellular environment. The V-ATPase complex also acts as an activator for mTORC1 on …

**Summary**, from NCBI Gene [537](https://www.ncbi.nlm.nih.gov/gene/537):

> This gene encodes a component of a multisubunit enzyme that mediates acidification of eukaryotic intracellular organelles. Vacuolar ATPase (V-ATPase) is comprised of a cytosolic V1 (site of the ATP catalytic site) and a transmembrane V0 domain. V-ATPase dependent organelle acidification is necessary for such intracellular processes as protein sorting, zymogen activation, and receptor-mediated endocytosis. The encoded protein of this gene may assist in the V-ATPase-mediated acidification of …

**Accessions** — [HGNC:868](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:868) · Entrez [537](https://www.ncbi.nlm.nih.gov/gene/537) · UniProt [Q15904](https://www.uniprot.org/uniprotkb/Q15904) · Ensembl [ENSG00000071553](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071553)

## Data

Gene col 987: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 987); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 987, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 987]; `tensor/DDL_lfc|DDL_z.npy` [987]; `embed/gene_vectors.npy` [987]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 987 or target_col == 987). Every well: [[ATP6AP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP6AP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
