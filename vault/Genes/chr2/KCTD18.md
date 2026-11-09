---
symbol: "KCTD18"
type: "gene"
col: 7911
ensembl_id: "ENSG00000155729"
name: "potassium channel tetramerization domain containing 18"
location: "2q33.1"
module: 28
arm: "+"
pooled_cpm: 11.5
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 25
n_dd_up_clean: 7
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# KCTD18

*potassium channel tetramerization domain containing 18* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.40× (z +7.0, q 2e-09, up in 21 of 48 measured lines) ⚠ cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.35× (z +4.4, q 0.002, up in 15 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.286× (z -18.3, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF18]] (+0.75, fdr 7e-06), [[TMEM128]] (+0.74, fdr 7e-06), [[EBAG9]] (+0.73, fdr 7e-06); moves opposite to [[SFXN5]] (-0.54, fdr 6e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[C17orf75]] → it (grade C ⚠); 2 go from it, the strongest it → [[RMDN1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7911.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.40×** | +7.0 | 2e-09 | 21/48 (CFPAC-1, A498, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +4.4 | 0.002 | 15/48 (KATO III, J82, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.016 | 10/47 (HOP62, A-172, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.035 | 12/48 (LOX-IMVI, AsPC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +3.5 | 0.039 | 4/48 (A498, PANC-1, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.039 | 14/46 (SK-MEL-2, AsPC-1, …) | rises with dose |  |
| [[Adenosine (drug)]] 5 µM |  | 1.18× | +3.5 | 0.039 | 2/48 (Panc 03.27, SHP-77) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.18× | +3.5 | 0.039 | 7/48 (A-172, Panc 03.27, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +3.3 | 0.058 | 4/23 (HEC-1-A, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.058 | 5/47 (KATO III, hTERT-HPNE, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.064 | 9/47 (HOP62, hTERT-HPNE, …) | all doses, flat |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.065 | 6/47 (SW48, Panc 03.27, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.24×** | +3.1 | 0.073 | 3/48 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7911.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.286×** | -18.3 | 0e+00 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.333×** | -16.1 | 0e+00 | 39/44 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.390×** | -13.8 | 5e-41 | 43/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.419×** | -12.7 | 5e-35 | 37/47 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.441×** | -12.0 | 4e-31 | 42/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.523×** | -9.5 | 2e-19 | 34/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.541×** | -9.0 | 2e-17 | 33/47 (PANC-1, Hs 766T, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.596×** | -7.3 | 2e-11 | 24/39 (A498, NCI-H1792, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.594×** | -7.2 | 4e-11 | 26/47 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.617×** | -7.1 | 9e-11 | 32/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **0.684×** | -5.6 | 1e-06 | 17/35 (SW1417, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.689×** | -5.5 | 2e-06 | 21/46 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.785×** | -5.0 | 2e-05 | 20/48 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.747×** | -4.3 | 8e-04 | 16/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.742×** | -4.2 | 0.001 | 18/47 (NCI-H460, PANC-1, …) | top dose only | composition shift |
| [[Gefitinib (drug)]] 5 µM |  | **0.780×** | -3.6 | 0.009 | 10/48 (NCI-H460, H4, …) | top dose only |  |
| [[Ritonavir (drug)]] 0.5 µM |  | **0.806×** | -3.2 | 0.045 | 11/45 (SHP-77, COLO 205, …) | inconsistent across doses |  |
| [[Bendamustine (drug)]] 5 µM |  | **0.805×** | -3.0 | 0.059 | 14/45 (C-33 A, SW48, …) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.868× | -2.9 | 0.077 | 4/48 (NCI-H2347, hTERT-HPNE, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.758×** | -2.9 | 0.084 | 13/48 (J82, NCI-H661, …) | all doses, flat | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7911. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 16.3 | 0 | 7 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.172× (z -15.4) |
| [[SW480 (line)]] | alt | 11.0 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0816× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0985× (z -17.4) |
| [[NCI-H460 (line)]] | wt | 13.5 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.223× (z -10.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.232× (z -9.9) |
| [[HOP62 (line)]] | alt | 11.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0650× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.195× (z -9.9) |
| [[A-172 (line)]] | wt | 19.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.172× (z -13.0) |
| [[H4 (line)]] | wt | 18.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0552× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0989× (z -10.1) |
| [[HS-578T (line)]] | alt | 10.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.162× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.187× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 13.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +13.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.77× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 11.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -10.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.177× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[A549 (line)]] | wt | 16.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.228× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[C-33 A (line)]] | alt | 11.5 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0817× (z -9.8) |
| [[C32 (line)]] | wt | 7.45 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0679× (z -10.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 14.6 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.113× (z -9.6) |
| [[LoVo (line)]] | wt | 8.76 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.154× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 15.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.209× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.207× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.134× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[NCI-H23 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0399× (z -18.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 8.59 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.227× (z -9.0) |
| [[RKO (line)]] | wt | 8.52 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0742× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0626× (z -12.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 9.99 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.125× (z -9.2) |
| [[SNU-423 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -11.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7911), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF18]] | +0.75 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[TMEM128]] | +0.74 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[EBAG9]] | +0.73 | +0.78 / +0.58 | both halves | 7e-06 |  |
| [[RAD52]] | +0.71 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[FRG1BP]] | +0.70 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[GIN1]] | +0.70 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[SUPT20H]] | +0.68 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[ELAC1]] | +0.68 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[ZSCAN21]] | +0.66 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[ZNF777]] | +0.66 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[FAM114A2]] | +0.65 | +0.81 / +0.49 | both halves | 1e-05 |  |
| [[SEPSECS]] | +0.65 | +0.72 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFXN5]] | -0.54 | -0.38 / -0.62 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C17orf75]] | C | C17orf75's natural level strengthens KCTD18's drug response | C17orf75's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.11; direction not clear | 0.053 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RMDN1]] | C | KCTD18's natural level strengthens RMDN1's drug response | KCTD18's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.22; direction not clear | 0.051 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | KCTD18's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | KCTD18's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.56 | 0.530 over the table, 0.099 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.711). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-27.8, 6.2); signed map (6.8, -23.4). **Vector** length 67.5, 11.6% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +4.5 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.0 | +2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.5 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | -0.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | -1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +1.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.7 | +3.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.6 | -13.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -9.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.3 | -16.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.2 | -12.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.2 | -12.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -9.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.1 | -2.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.8 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | potassium channel tetramerization domain containing 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:200,488,958-200,519,784 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31322, 6530404F10Rik, FLJ37818 |
| Gene groups (HGNC) | KCTD family |
| Matched by | ensembl_id |

UniProt [Q6PI47](https://www.uniprot.org/uniprotkb/Q6PI47) carries no function annotation.

**Summary**, from NCBI Gene [130535](https://www.ncbi.nlm.nih.gov/gene/130535):

> Predicted to enable identical protein binding activity. Predicted to be involved in monoatomic ion transmembrane transport and protein homooligomerization. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26446](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26446) · Entrez [130535](https://www.ncbi.nlm.nih.gov/gene/130535) · UniProt [Q6PI47](https://www.uniprot.org/uniprotkb/Q6PI47) · Ensembl [ENSG00000155729](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155729)

## Data

Gene col 7911: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7911); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7911, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7911]; `tensor/DDL_lfc|DDL_z.npy` [7911]; `embed/gene_vectors.npy` [7911]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7911 or target_col == 7911). Every well: [[KCTD18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCTD18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
