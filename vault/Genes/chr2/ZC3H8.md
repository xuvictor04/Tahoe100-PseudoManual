---
symbol: "ZC3H8"
type: "gene"
col: 6850
ensembl_id: "ENSG00000144161"
name: "zinc finger CCCH-type containing 8"
location: "2q14.1"
module: 1
arm: "+"
pooled_cpm: 36.65
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 8
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# ZC3H8

*zinc finger CCCH-type containing 8* — 2q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.73× (z +11.1, q 6e-26, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.461× (z -15.7, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMA16]] (+0.69, fdr 1e-05), [[RPAP2]] (+0.65, fdr 2e-05), [[TATDN1]] (+0.62, fdr 1e-05); moves opposite to [[CALM3]] (-0.60, fdr 5e-05), [[PRKACA]] (-0.57, fdr 4e-05), [[H2AZ2]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[COL1A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6850.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +11.1 | 6e-26 | 33/47 (NCI-H1792, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +10.3 | 3e-22 | 31/47 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +8.8 | 3e-16 | 35/48 (NCI-H2347, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +8.0 | 1e-13 | 34/48 (LoVo, NCI-H2347, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +7.8 | 9e-13 | 29/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +7.4 | 1e-11 | 36/47 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +6.8 | 9e-10 | 28/48 (SW480, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.9 | 2e-07 | 29/47 (NCI-H460, A498, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.31×** | +5.5 | 2e-06 | 24/47 (SW480, HT-29, …) | two highest doses | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.27×** | +4.8 | 7e-05 | 20/48 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.27×** | +4.6 | 2e-04 | 20/48 (NCI-H460, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.25×** | +4.5 | 3e-04 | 20/48 (SW 900, A-427, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.52×** | +4.5 | 3e-04 | 19/48 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | **1.22×** | +4.0 | 0.003 | 19/41 (LS 180, HT-29, …) | two highest doses | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +4.0 | 0.003 | 20/48 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.43×** | +3.8 | 0.006 | 14/47 (RPMI-7951, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.19× | +3.6 | 0.010 | 14/47 (NCI-H1573, LoVo, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.012 | 10/47 (NCI-H1573, C32, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.035 | 13/46 (NCI-H2030, RKO, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.055 | 10/48 (AsPC-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.068 | 10/47 (MIA PaCa-2, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 1.11× | +2.9 | 0.080 | 9/48 (A549, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6850.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.461×** | -15.7 | 0e+00 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.477×** | -15.0 | 0e+00 | 39/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.527×** | -13.0 | 3e-36 | 39/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.305×** | -12.6 | 3e-34 | 44/48 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.375×** | -10.4 | 2e-23 | 37/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.630×** | -9.4 | 7e-19 | 33/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.767×** | -5.2 | 2e-05 | 25/47 (NCI-H23, HCT15, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.802×** | -4.5 | 6e-04 | 19/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.836× | -3.6 | 0.018 | 14/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6850. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 39.2 | 1 | 7 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +9.9) | [[Digitoxin (drug)]] 5 µM 0.188× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.190× (z -20.7) |
| [[NCI-H23 (line)]] | alt | 48.3 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.257× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.341× (z -11.3) |
| [[SW480 (line)]] | alt | 64.4 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.205× (z -22.9) |
| [[NCI-H460 (line)]] | wt | 47.6 | 1 | 4 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.436× (z -10.3) |
| [[HOP62 (line)]] | alt | 32.9 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -16.1) |
| [[HEC-1-A (line)]] | alt | 53.0 | 0 | 3 | — | [[TAK-901 (drug)]] 5 µM 0.228× (z -9.5) |
| [[SHP-77 (line)]] | alt | 40.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.356× (z -8.8) |
| [[HCT15 (line)]] | alt | 30.5 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.135× (z -11.1) ⚠ toxic · without an alert: [[Ipatasertib (drug)]] 0.5 µM 0.0842× (z -10.2) |
| [[J82 (line)]] | alt | 35.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.299× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.360× (z -8.9) |
| [[RKO (line)]] | wt | 48.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -12.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 27.8 | 0 | 1 (1 ⚠) | — | [[Elimusertib hydrochloride (drug)]] 5 µM 0.0697× (z -9.4) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 18.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.73× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 30.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.83× (z +9.9) | — |
| [[KATO III (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[LoVo (line)]] | wt | 45.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.439× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 32.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.324× (z -9.7) |
| [[LS 180 (line)]] | wt | 31.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.260× (z -10.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 48.8 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0988× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 43.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.72× (z +11.0) | — |
| [[NCI-H2347 (line)]] | alt | 18.1 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.16× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 36.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.70× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 50.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[SNU-1 (line)]] | wt | 32.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.141× (z -11.2) |
| [[SW 1271 (line)]] | alt | 51.8 | 0 | 1 | — | [[Resveratrol (drug)]] 0.05 µM 0.0725× (z -8.9) |
| [[SW 900 (line)]] | alt | 30.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.233× (z -10.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 45.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.398× (z -9.3) |
| [[A-172 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6850), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMA16]] | +0.69 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[RPAP2]] | +0.65 | +0.79 / +0.48 | both halves | 2e-05 | pathway: RNA polymerase II transcribes snRNA genes |
| [[TATDN1]] | +0.62 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[NIFK]] | +0.61 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[DNAJC2]] | +0.61 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[ZNF485]] | +0.59 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[MRPL15]] | +0.59 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[DCAF17]] | +0.59 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[METTL8]] | +0.59 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[WDR75]] | +0.59 | +0.66 / +0.60 | both halves | 7e-06 | STRING 430 |
| [[RSL1D1]] | +0.59 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[MLH3]] | +0.59 | +0.58 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALM3]] | -0.60 | -0.70 / -0.40 | both halves | 5e-05 |  |
| [[PRKACA]] | -0.57 | -0.58 / -0.43 | both halves | 4e-05 |  |
| [[H2AZ2]] | -0.55 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[BAIAP2-DT]] | -0.54 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[NRM]] | -0.54 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[GGH]] | -0.52 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[GRN]] | -0.52 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[BSG]] | -0.51 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ITM2C]] | -0.51 | -0.61 / -0.35 | both halves | 1e-04 |  |
| [[PIGS]] | -0.51 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[USP9X]] | -0.50 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[NUMA1]] | -0.50 | -0.57 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL1A1]] | B | COL1A1 activity lowers ZC3H8's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 1.25× higher at baseline in the lines without COL1A1 | 0.032 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411 |
| [[TCN1]] | B | TCN1 activity weakens ZC3H8's drug response | lines that do not express TCN1 (37) vs lines expressing it (11) | the lines without TCN1 respond 1.05× as strongly (z diff -0.56); strongest at Digitoxin 5 µM: 0.43x vs 0.61x (z diff -2.5) | 0.075 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B; target measured in part of the lines; artifact flags |
| [[GGH]] | B | GGH activity raises ZC3H8's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.33× lower at baseline in the lines without GGH | 0.091 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.543). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-40.4, -1.0); signed map (-1.4, -39.0). **Vector** length 97.8, 24.3% of its response variance represented; |z| ≥ 3 in 1,064 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.7 | +8.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.4 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.3 | +11.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.6 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.6 | +7.4 |
|  | [[EX229 (drug)]] 5 µM |  | +3.7 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.4 | +3.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.2 | +2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.0 | +1.7 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.7 | -12.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.5 | -15.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.9 | -15.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.4 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | +1.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.0 | +0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CCCH-type containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.1 — chr2:112,211,529-112,255,136 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Fliz1; previously ZC3HDC8 |
| Gene groups (HGNC) | Zinc fingers CCCH-type |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5P1](https://www.uniprot.org/uniprotkb/Q8N5P1) (Zinc finger CCCH domain-containing protein 8):

> Acts as a transcriptional repressor of the GATA3 promoter. Sequence-specific DNA-binding factor that binds to the 5'-AGGTCTC-3' sequence within the negative cis-acting element intronic regulatory region (IRR) of the GATA3 gene (By similarity). Component of the little elongation complex (LEC), a complex required to regulate small nuclear RNA (snRNA) gene transcription by RNA polymerase II and III. Induces thymocyte apoptosis when overexpressed, which may indicate a role in regulation of …

**Summary**, from NCBI Gene [84524](https://www.ncbi.nlm.nih.gov/gene/84524):

> Enables RNA binding activity. Involved in several processes, including positive regulation of thymocyte apoptotic process; regulation of DNA-templated transcription; and snRNA transcription. Located in Cajal body; euchromatin; and histone locus body. Part of transcription elongation factor complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30941](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30941) · Entrez [84524](https://www.ncbi.nlm.nih.gov/gene/84524) · UniProt [Q8N5P1](https://www.uniprot.org/uniprotkb/Q8N5P1) · Ensembl [ENSG00000144161](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144161)

## Data

Gene col 6850: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6850); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6850, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6850]; `tensor/DDL_lfc|DDL_z.npy` [6850]; `embed/gene_vectors.npy` [6850]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6850 or target_col == 6850). Every well: [[ZC3H8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZC3H8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
