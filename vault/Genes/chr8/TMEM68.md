---
symbol: "TMEM68"
type: "gene"
col: 9557
ensembl_id: "ENSG00000167904"
name: "transmembrane protein 68"
location: "8q12.1"
module: 15
arm: "+"
pooled_cpm: 28.25
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# TMEM68

*transmembrane protein 68* — 8q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.93× (z +17.6, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.718× (z -6.3, q 6e-08, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOPCHAP1]] (+0.76, fdr 7e-06), [[SDHAF4]] (+0.72, fdr 7e-06), [[FBXO22]] (+0.68, fdr 7e-06); moves opposite to [[BCL7B]] (-0.60, fdr 2e-05), [[IER2]] (-0.58, fdr 2e-05), [[KLF2]] (-0.58, fdr 6e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TP53]] → it (grade A ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9557.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +17.6 | 0e+00 | 42/48 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +11.8 | 2e-29 | 37/47 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +11.1 | 3e-26 | 38/48 (A549, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +7.8 | 1e-12 | 33/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +6.8 | 1e-09 | 29/46 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +6.3 | 4e-08 | 29/48 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.67×** | +5.1 | 3e-05 | 16/46 (A-172, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.28×** | +4.6 | 3e-04 | 20/48 (RKO, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.17× | +4.1 | 0.003 | 6/48 (Hs 766T, HCT15, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +4.1 | 0.003 | 19/48 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.31×** | +3.7 | 0.011 | 10/48 (A498, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.015 | 10/46 (KATO III, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +3.5 | 0.020 | 11/48 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.021 | 10/47 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.1 | 0.086 | 7/48 (A498, H4, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.35×** | +3.0 | 0.088 | 6/47 (MIA PaCa-2, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Cysteamine (hydrochloride) (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.088 | 12/48 (A498, C-33 A, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9557.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.718×** | -6.3 | 6e-08 | 24/48 (MIA PaCa-2, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.718×** | -6.3 | 6e-08 | 25/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.718×** | -6.3 | 6e-08 | 24/47 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.808×** | -5.7 | 2e-06 | 25/47 (A-427, A-172, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.744×** | -5.6 | 2e-06 | 24/43 (C-33 A, LoVo, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.744×** | -5.4 | 6e-06 | 21/47 (A498, PANC-1, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.765×** | -4.9 | 8e-05 | 18/37 (C32, SW 900, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.777×** | -4.4 | 7e-04 | 20/40 (C32, SW480, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | **0.828×** | -3.6 | 0.020 | 10/47 (Panc 03.27, LoVo, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.831×** | -3.5 | 0.026 | 10/48 (A498, BT-474, …) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | 0.836× | -3.4 | 0.033 | 14/47 (A-172, NCI-H23, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains <1% of this change | 0.841× | -3.3 | 0.048 | 13/48 (LS 180, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.845× | -3.2 | 0.057 | 11/46 (NCI-H661, H4, …) | two highest doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.845× | -3.2 | 0.057 | 11/47 (SNU-423, LS 180, …) | top dose only |  |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | 0.849× | -3.1 | 0.072 | 6/47 (H4, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9557. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 23.5 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.152× (z -13.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 49.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +17.8) | — |
| [[C32 (line)]] | wt | 38.9 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.0806× (z -14.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 59.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.345× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.351× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 24.3 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +14.7) | — |
| [[A-427 (line)]] | wt | 30.0 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -9.7) ⚠ cell-cycle shift, explains ~51% of this change |
| [[A549 (line)]] | wt | 26.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +10.3) | — |
| [[CHP-212 (line)]] | wt | 44.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0904× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.125× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 31.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +13.7) | — |
| [[RKO (line)]] | wt | 43.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +15.6) | — |
| [[C-33 A (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -11.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 24.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -9.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 26.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +8.9) | — |
| [[LoVo (line)]] | wt | 29.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -11.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 47.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +11.8) | — |
| [[NCI-H2030 (line)]] | alt | 30.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 27.3 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -14.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 31.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 27.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9557), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOPCHAP1]] | +0.76 | +0.62 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[SDHAF4]] | +0.72 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[FBXO22]] | +0.68 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[DCP1B]] | +0.66 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[CIAO2A]] | +0.66 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[ZUP1]] | +0.66 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[TIAL1]] | +0.65 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[PANK1]] | +0.64 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[ZNF343]] | +0.63 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[TMED8]] | +0.62 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[PMS2]] | +0.61 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[GOT1-DT]] | +0.61 | +0.48 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL7B]] | -0.60 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[IER2]] | -0.58 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[KLF2]] | -0.58 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[RALY]] | -0.56 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[GDF11]] | -0.55 | -0.61 / -0.28 | both halves | 3e-04 |  |
| [[VCL]] | -0.55 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[JUNB]] | -0.54 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[MFSD12]] | -0.54 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[LMCD1]] | -0.52 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[NR4A1]] | -0.52 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[DHRS2]] | -0.52 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[PILRB]] | -0.50 | -0.43 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 1, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53]] | A | TP53 activity strengthens TMEM68's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 0.57× as strongly (z diff +1.79); strongest at Topotecan (hydrochloride) 5 µM: 1.17x vs 2.03x (z diff +3.5) | 0.011 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |
| [[PINCR]] | B | PINCR activity strengthens TMEM68's drug response | lines that do not express PINCR (29) vs lines expressing it (19) | the lines without PINCR respond 0.62× as strongly (z diff +1.41); strongest at Topotecan (hydrochloride) 5 µM: 1.18x vs 1.88x (z diff +3.0) | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers TMEM68's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises TMEM68's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MDM2]] | C | MDM2's natural level strengthens TMEM68's drug response | MDM2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.34; direction not clear | 0.014 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[DDB2]] | C | DDB2's natural level strengthens TMEM68's drug response | DDB2's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.07; direction not clear | 0.089 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.593). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-14.7, 19.7); signed map (-30.5, -20.1). **Vector** length 112, 27.3% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.3 | +11.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +17.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +7.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +7.8 | +11.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.3 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +4.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.6 | +2.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -5.5 | -5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -5.1 | -5.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.0 | -6.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.0 | -6.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.5 | -6.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.0 | -3.5 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -1.9 | -2.4 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | -1.9 | -2.4 |
|  | [[Estrone sulfate (potassium) (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | -1.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 68 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q12.1 — chr8:55,696,424-55,773,407 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32370, DIESL |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96MH6](https://www.uniprot.org/uniprotkb/Q96MH6) (DGAT1/2-independent enzyme synthesizing storage lipids):

> Catalytic subunit of the alternative triglyceride biosynthesis pathway, which mediates formation of triacylglycerol from diacylglycerol and membrane phospholipids. Synthesizes triacylglycerol at the expense of membrane phospholipids, such as phosphatidylcholine (PC) and its ether-linked form (ePC), thereby altering the composition of membranes. The alternative triglyceride biosynthesis pathway is probably required to provide the energy required for rapid growth when fuel sources are limiting. …

**Summary**, from NCBI Gene [137695](https://www.ncbi.nlm.nih.gov/gene/137695):

> Enables phospholipid:diacylglycerol acyltransferase activity. Involved in triglyceride biosynthetic process. Is active in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26510](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26510) · Entrez [137695](https://www.ncbi.nlm.nih.gov/gene/137695) · UniProt [Q96MH6](https://www.uniprot.org/uniprotkb/Q96MH6) · Ensembl [ENSG00000167904](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167904)

## Data

Gene col 9557: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9557); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9557, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9557]; `tensor/DDL_lfc|DDL_z.npy` [9557]; `embed/gene_vectors.npy` [9557]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9557 or target_col == 9557). Every well: [[TMEM68 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM68.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
