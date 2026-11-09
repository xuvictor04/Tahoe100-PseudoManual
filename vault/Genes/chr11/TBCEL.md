---
symbol: "TBCEL"
type: "gene"
col: 7770
ensembl_id: "ENSG00000154114"
name: "tubulin folding cofactor E like"
location: "11q23.3"
module: 28
arm: "+"
pooled_cpm: 25.13
n_lines_expressing: 46
n_dd_up: 19
n_dd_down: 14
n_dd_up_clean: 14
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# TBCEL

*tubulin folding cofactor E like* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.54× (z +8.4, q 2e-14, up in 35 of 44 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.45× (z +7.3, q 8e-11, up in 31 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Abemaciclib (drug)]] 5 µM: 0.471× (z -5.4, q 3e-05, down in 31 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AASDHPPT]] (+0.70, fdr 7e-06), [[DCUN1D1]] (+0.69, fdr 7e-06), [[MRRF]] (+0.68, fdr 7e-06); moves opposite to [[CARD19]] (-0.63, fdr 1e-05), [[DPM1]] (-0.60, fdr 2e-05), [[DHDDS]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ITGB8]] → it (grade B ⚠); 1 goes from it, the strongest it → [[TRIM44]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7770.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.54×** | +8.4 | 2e-14 | 35/44 (NCI-H1573, HT-29, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +7.3 | 8e-11 | 31/44 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +7.3 | 8e-11 | 31/44 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.4 | 1e-05 | 26/44 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +5.0 | 6e-05 | 24/44 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.44×** | +4.9 | 8e-05 | 21/44 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.94×** | +4.8 | 1e-04 | 20/43 (HEC-1-A, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.42×** | +4.6 | 3e-04 | 21/44 (NCI-H2347, SW1417, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +4.1 | 0.003 | 20/44 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.71×** | +3.9 | 0.006 | 19/44 (HCT15, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.31×** | +3.8 | 0.008 | 20/44 (SW 900, Panc 03.27, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.30×** | +3.7 | 0.011 | 18/44 (A498, J82, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.27×** | +3.4 | 0.033 | 12/44 (SNU-1, J82, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.58×** | +3.3 | 0.034 | 10/44 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.33×** | +3.3 | 0.043 | 7/44 (SW480, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.058 | 11/44 (SW480, SW 900, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.088 | 11/44 (SW480, NCI-H460, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.093 | 10/44 (LoVo, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +2.9 | 0.093 | 12/43 (SW480, A549, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.24×** | +2.9 | 0.097 | 8/43 (SW480, hTERT-HPNE, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7770.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Abemaciclib (drug)]] 5 µM |  | **0.471×** | -5.4 | 3e-05 | 31/44 (SW480, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.602×** | -5.0 | 2e-04 | 25/44 (SHP-77, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.702×** | -4.9 | 2e-04 | 29/44 (SW1417, LoVo, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.704×** | -4.8 | 2e-04 | 24/43 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.697×** | -4.8 | 2e-04 | 26/43 (SHP-77, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.737×** | -4.2 | 0.002 | 22/44 (SW480, LS 180, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.657×** | -4.1 | 0.003 | 19/44 (SW480, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.665×** | -4.0 | 0.004 | 18/44 (MIA PaCa-2, SW 900, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.755×** | -3.9 | 0.006 | 21/43 (BT-474, SW480, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.620×** | -3.5 | 0.030 | 15/43 (COLO 205, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.635×** | -3.3 | 0.048 | 17/43 (RPMI-7951, SNU-1, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.777×** | -3.3 | 0.048 | 19/44 (MIA PaCa-2, SW48, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.640×** | -3.2 | 0.051 | 17/39 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.641×** | -3.2 | 0.051 | 15/43 (A-427, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7770. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 48.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 70.6 | 0 | 2 (1 ⚠) | — | [[Cyclosporin A (drug)]] 0.5 µM 0.141× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 17.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +12.7) | — |
| [[NCI-H460 (line)]] | wt | 13.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +8.9) ⚠ cell-cycle shift, explains ~2% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 14.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +9.4) | — |
| [[A549 (line)]] | wt | 18.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.146× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.180× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[C-33 A (line)]] | alt | 44.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.240× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 47.9 | 0 | 1 | — | [[Pimitespib (drug)]] 5 µM 0.0674× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 39.9 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.127× (z -10.6) ⚠ toxic |
| [[LoVo (line)]] | wt | 17.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.319× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 43.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 36.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.387× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.41 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 43.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7770), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AASDHPPT]] | +0.70 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[DCUN1D1]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[MRRF]] | +0.68 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[ZMYND11]] | +0.65 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[IQCH-AS1]] | +0.65 | +0.72 / +0.40 | both halves | 5e-05 |  |
| [[ZNF507]] | +0.64 | +0.71 / +0.45 | both halves | 3e-05 |  |
| [[MED12]] | +0.64 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[LDAH]] | +0.63 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[MTPAP]] | +0.63 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ZNF747]] | +0.63 | +0.68 / +0.33 | both halves | 1e-04 |  |
| [[ZNF252P-1]] | +0.63 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[THOC7]] | +0.62 | +0.63 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CARD19]] | -0.63 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[DPM1]] | -0.60 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[DHDDS]] | -0.59 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[STK32C]] | -0.59 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[AZIN2]] | -0.59 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[ANKMY2]] | -0.59 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[CIB1]] | -0.58 | -0.63 / -0.39 | both halves | 5e-05 |  |
| [[IGSF8]] | -0.58 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[YIF1B]] | -0.58 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[GMCL1]] | -0.58 | -0.60 / -0.39 | both halves | 5e-05 |  |
| [[SDHAP2]] | -0.58 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[MYO9B]] | -0.57 | -0.61 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGB8]] | B | ITGB8 activity lowers TBCEL's level | lines that do not express ITGB8 (17) vs lines expressing it (33) | 1.65× higher at baseline in the lines without ITGB8 | 0.034 | ⚠ within organs, on part of the lines; also absent: LRATD2, HNMT, B3GALT5 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM44]] | C | TBCEL activity raises TRIM44's level | lines that do not express TBCEL (4) vs lines expressing it (46) | 1.99× lower at baseline in the lines without TBCEL | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: C2orf92, HHAT, RUNDC3A-AS1; its own permutation p |

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.530). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.5, 6.3); signed map (15.4, -30.3). **Vector** length 89.8, 20.2% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +6.3 | +8.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.3 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +4.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.4 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +2.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | -4.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | +1.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.3 | -5.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.8 | -5.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.7 | -3.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.5 | -4.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | tubulin folding cofactor E like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:121,024,072-121,090,776 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10233; previously LRRC35 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5QJ74](https://www.uniprot.org/uniprotkb/Q5QJ74) (Tubulin-specific chaperone cofactor E-like protein):

> Acts as a regulator of tubulin stability.

**Summary**, from NCBI Gene [219899](https://www.ncbi.nlm.nih.gov/gene/219899):

> Predicted to enable alpha-tubulin binding activity. Predicted to be involved in microtubule cytoskeleton organization; post-chaperonin tubulin folding pathway; and tubulin complex assembly. Predicted to be located in cytoskeleton. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28115](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28115) · Entrez [219899](https://www.ncbi.nlm.nih.gov/gene/219899) · UniProt [Q5QJ74](https://www.uniprot.org/uniprotkb/Q5QJ74) · Ensembl [ENSG00000154114](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154114)

## Data

Gene col 7770: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7770); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7770, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7770]; `tensor/DDL_lfc|DDL_z.npy` [7770]; `embed/gene_vectors.npy` [7770]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7770 or target_col == 7770). Every well: [[TBCEL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBCEL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
