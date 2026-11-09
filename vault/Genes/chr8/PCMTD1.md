---
symbol: "PCMTD1"
type: "gene"
col: 9632
ensembl_id: "ENSG00000168300"
name: "protein-L-isoaspartate (D-aspartate) O-methyltransferase domain containing 1"
location: "8q11.23"
module: 69
arm: "+"
pooled_cpm: 140.71
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 31
n_dd_up_clean: 5
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# PCMTD1

*protein-L-isoaspartate (D-aspartate) O-methyltransferase domain containing 1* — 8q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.38× (z +9.8, q 5e-20, up in 37 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (16 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.410× (z -18.7, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.504× (z -14.8, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MKRN1]] (+0.75, fdr 7e-06), [[TMEM59]] (+0.71, fdr 7e-06), [[NEK7]] (+0.69, fdr 7e-06); moves opposite to [[MPHOSPH6]] (-0.68, fdr 7e-06), [[ZKSCAN2]] (-0.60, fdr 7e-06), [[SMARCA4]] (-0.60, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9632.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +9.8 | 5e-20 | 37/49 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +7.4 | 4e-11 | 36/48 (A-427, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.19× | +5.3 | 3e-05 | 18/48 (LS 180, A-427, …) | rises with dose | low cells (technical?) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.70×** | +4.3 | 0.002 | 32/50 (HOP62, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.1 | 0.005 | 22/50 (RKO, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.22×** | +4.0 | 0.006 | 22/48 (SW 900, SW480, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.13× | +3.7 | 0.018 | 7/48 (SW 900, A498, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.27×** | +3.6 | 0.019 | 23/50 (HOP62, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.17× | +3.4 | 0.037 | 16/48 (J82, RPMI-7951, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.4 | 0.046 | 22/47 (Hs 766T, AsPC-1, …) | rises with dose |  |
| [[crizotinib (drug)]] 5 µM |  | 1.17× | +3.2 | 0.067 | 18/48 (AsPC-1, NCI-H2030, …) | top dose only |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.067 | 14/49 (PANC-1, HCT15, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 1.16× | +3.1 | 0.091 | 13/47 (NCI-H23, A-427, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.10 | 14/49 (Hs 766T, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 19 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9632.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.410×** | -18.7 | 0e+00 | 48/48 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.556×** | -18.0 | 0e+00 | 42/48 (SNU-423, A498, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.504×** | -14.8 | 0e+00 | 45/48 (HOP62, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.576×** | -11.5 | 3e-28 | 40/48 (HOP62, A498, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.591×** | -11.4 | 6e-28 | 46/48 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.608×** | -10.8 | 5e-25 | 41/48 (MIA PaCa-2, SW 900, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **0.600×** | -10.6 | 2e-24 | 37/44 (Panc 03.27, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.643×** | -9.5 | 1e-19 | 45/48 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **0.605×** | -8.6 | 7e-16 | 40/49 (A498, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.349×** | -8.5 | 1e-15 | 47/48 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.686×** | -8.2 | 2e-14 | 41/48 (LOX-IMVI, H4, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.370×** | -8.0 | 5e-14 | 47/48 (A498, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **0.674×** | -7.9 | 1e-13 | 30/45 (CFPAC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.393×** | -7.5 | 2e-12 | 42/48 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.396×** | -7.5 | 3e-12 | 45/48 (A498, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.397×** | -7.5 | 3e-12 | 43/48 (A498, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.695×** | -6.2 | 2e-08 | 36/48 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~25% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.779×** | -5.4 | 2e-06 | 31/48 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.781×** | -5.4 | 2e-06 | 30/48 (AsPC-1, A498, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.790×** | -4.8 | 4e-05 | 36/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.622×** | -4.1 | 7e-04 | 25/48 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.630×** | -4.0 | 0.001 | 28/49 (A498, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.886× | -3.7 | 0.004 | 13/48 (LOX-IMVI, MIA PaCa-2, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.658×** | -3.6 | 0.005 | 22/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9632. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 263 | 0 | 14 (8 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.240× (z -22.9) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.418× (z -14.5) |
| [[SW 900 (line)]] | alt | 212 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -15.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.333× (z -14.7) |
| [[MIA PaCa-2 (line)]] | alt | 162 | 1 | 7 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +8.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.257× (z -16.2) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.444× (z -10.0) |
| [[A549 (line)]] | wt | 154 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.375× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 169 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.395× (z -13.0) |
| [[NCI-H2347 (line)]] | alt | 176 | 0 | 6 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.263× (z -18.5) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.520× (z -9.4) |
| [[SW480 (line)]] | alt | 97.9 | 1 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +9.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.444× (z -10.7) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.500× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 154 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -20.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.350× (z -12.3) |
| [[C32 (line)]] | wt | 160 | 2 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +10.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.391× (z -11.4) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.482× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 144 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -18.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.387× (z -12.0) |
| [[HOP62 (line)]] | alt | 181 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -21.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.297× (z -16.5) |
| [[NCI-H23 (line)]] | alt | 167 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -19.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.341× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 109 | 0 | 5 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.343× (z -16.6) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.437× (z -13.3) |
| [[SNU-423 (line)]] | alt | 148 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -25.2) ⚠ cell-cycle shift, explains ~37% of this change |
| [[H4 (line)]] | wt | 150 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.382× (z -9.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HEC-1-A (line)]] | alt | 97.4 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +11.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.258× (z -15.9) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.494× (z -8.5) |
| [[HT-29 (line)]] | alt | 150 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.373× (z -12.3) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.460× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 135 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -14.7) |
| [[Panc 03.27 (line)]] | alt | 148 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.398× (z -11.2) |
| [[SNU-1 (line)]] | wt | 104 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.152× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[SW48 (line)]] | wt | 94.1 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.205× (z -13.1) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 133 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -17.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.395× (z -13.3) |
| [[Hs 766T (line)]] | wt | 150 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.345× (z -12.8) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 165 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -13.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.513× (z -8.9) |
| [[J82 (line)]] | alt | 114 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -13.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.509× (z -9.3) |
| [[LS 180 (line)]] | wt | 104 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[NCI-H1573 (line)]] | alt | 73.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.282× (z -14.3) |
| [[NCI-H1792 (line)]] | alt | 143 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -17.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.499× (z -9.2) |
| [[PANC-1 (line)]] | alt | 109 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.405× (z -14.2) |
| [[RKO (line)]] | wt | 150 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.308× (z -12.3) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 103 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +11.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.355× (z -12.6) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 101 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -19.4) ⚠ cell-cycle shift, explains ~37% of this change |
| [[COLO 205 (line)]] | alt | 113 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.340× (z -9.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.372× (z -9.4) |
| [[KATO III (line)]] | alt | 142 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.428× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[LoVo (line)]] | wt | 107 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +13.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.362× (z -13.2) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 210 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[SW 1088 (line)]] | alt | 124 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0331× (z -15.2) ⚠ unreliable plate only · without an alert: [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.104× (z -9.6) |
| [[AN3 CA (line)]] | alt | 130 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -15.2) |
| [[BT-474 (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.418× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[C-33 A (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[HCT15 (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.332× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[RPMI-7951 (line)]] | alt | 133 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -10.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SHP-77 (line)]] | alt | 155 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.434× (z -10.2) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.404× (z -10.3) ⚠ unreliable plate only |
| [[SW 1271 (line)]] | alt | 163 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.181× (z -9.4) ⚠ unreliable plate only |
| [[CHP-212 (line)]] | wt | 191 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 106 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 133 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9632), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MKRN1]] | +0.75 | +0.66 / +0.81 | both halves | 7e-06 |  |
| [[TMEM59]] | +0.71 | +0.59 / +0.78 | both halves | 7e-06 |  |
| [[NEK7]] | +0.69 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[HBP1]] | +0.69 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[YPEL5]] | +0.69 | +0.57 / +0.70 | both halves | 8e-06 |  |
| [[GPBP1L1]] | +0.68 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[CDIPT]] | +0.67 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[ELF2]] | +0.67 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[CHASERR]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[PIK3CA]] | +0.66 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[CREBRF]] | +0.65 | +0.42 / +0.71 | both halves | 4e-05 |  |
| [[H3-3A-DT]] | +0.65 | +0.38 / +0.67 | both halves | 6e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPHOSPH6]] | -0.68 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[ZKSCAN2]] | -0.60 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[SMARCA4]] | -0.60 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[TAF1B]] | -0.59 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[THOP1]] | -0.59 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[EIF2B3]] | -0.57 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[CMIP]] | -0.55 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[CAAP1]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[DGKD]] | -0.55 | -0.23 / -0.54 | both halves | 5e-04 |  |
| [[UTP14A]] | -0.54 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[METTL2A]] | -0.53 | -0.46 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PCMTD1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.7, -42.4); signed map (-14.2, 11.3). **Vector** length 129, 46.5% of its response variance represented; |z| ≥ 3 in 1,382 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.5 | +9.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +10.9 | +7.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +4.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.2 | +5.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.3 | +0.9 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.5 | +4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +2.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.1 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | -1.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.6 | -18.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -7.8 | -18.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.2 | -8.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.2 | -8.0 |
|  | [[EX229 (drug)]] 5 µM |  | -7.1 | -7.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.6 | -7.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.0 | -7.5 |

## What is on record

|  |  |
|---|---|
| Name | protein-L-isoaspartate (D-aspartate) O-methyltransferase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q11.23 — chr8:51,817,575-51,899,186 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10883 |
| Gene groups (HGNC) | 7BS protein methyltransferases; Isoaspartate methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96MG8](https://www.uniprot.org/uniprotkb/Q96MG8) (Protein-L-isoaspartate O-methyltransferase domain-containing protein 1):

> Substrate recognition component of an ECS (Elongin BC-CUL5-SOCS-box protein) E3 ubiquitin ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. Specifically binds to the methyltransferase cofactor S-adenosylmethionine (AdoMet) via the N-terminal AdoMet binding motif, but does not display methyltransferase activity. May provide an alternate maintenance pathway for modified proteins by acting as a damage-specific E3 ubiquitin ligase adaptor …

**Summary**, from NCBI Gene [115294](https://www.ncbi.nlm.nih.gov/gene/115294):

> Enables ubiquitin-like ligase-substrate adaptor activity. Involved in protein ubiquitination. Part of Cul5-RING ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30483](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30483) · Entrez [115294](https://www.ncbi.nlm.nih.gov/gene/115294) · UniProt [Q96MG8](https://www.uniprot.org/uniprotkb/Q96MG8) · Ensembl [ENSG00000168300](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168300)

## Data

Gene col 9632: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9632); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9632, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9632]; `tensor/DDL_lfc|DDL_z.npy` [9632]; `embed/gene_vectors.npy` [9632]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9632 or target_col == 9632). Every well: [[PCMTD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCMTD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
