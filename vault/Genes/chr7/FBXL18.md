---
symbol: "FBXL18"
type: "gene"
col: 7863
ensembl_id: "ENSG00000155034"
name: "F-box and leucine rich repeat protein 18"
location: "7p22.1"
module: 36
arm: "+"
pooled_cpm: 35.55
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# FBXL18

*F-box and leucine rich repeat protein 18* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.43× (z +18.8, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.595× (z -10.1, q 2e-21, down in 24 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.719× (z -9.9, q 1e-20, down in 37 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (HT-29 0.113×, RPMI-7951 0.0734×, HOP62 0.209×, KATO III 0.229×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (KATO III 0.0640×, PANC-1 0.237×, H4 0.0719×, A-427 0.233×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 0.341×, HT-29 0.237×, A498 0.327×; ⚠ toxic; transcription drop); [[Menadione (drug)]] 5 µM in 1 line (HepG2/C3A 0.0517×); [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 0.367×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.104×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IL9RP3]] (+0.71, fdr 7e-06), [[TMEM104]] (+0.67, fdr 1e-05), [[TRIM11]] (+0.67, fdr 1e-05); moves opposite to [[RBBP9]] (-0.59, fdr 3e-05), [[CISD2]] (-0.58, fdr 2e-05), [[GSTK1]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7863.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.43×** | +18.8 | 0e+00 | 46/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.11×** | +15.7 | 0e+00 | 47/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.00×** | +14.6 | 0e+00 | 46/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +11.9 | 1e-30 | 37/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +9.6 | 6e-20 | 26/47 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +9.2 | 4e-18 | 36/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +8.8 | 9e-17 | 33/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +8.4 | 2e-15 | 35/48 (SW480, LoVo, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.50×** | +4.5 | 4e-04 | 15/49 (NCI-H460, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.23×** | +4.3 | 8e-04 | 15/47 (RPMI-7951, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.47×** | +4.3 | 1e-03 | 13/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.22× | +3.0 | 0.11 | 7/47 (SW480, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7863.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (HT-29 0.113×, RPMI-7951 0.0734×, HOP62 0.209×, KATO III 0.229×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (KATO III 0.0640×, PANC-1 0.237×, H4 0.0719×, A-427 0.233×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 0.341×, HT-29 0.237×, A498 0.327×; ⚠ toxic; transcription drop); [[Menadione (drug)]] 5 µM in 1 line (HepG2/C3A 0.0517×); [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 0.367×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.104×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.595×** | -10.1 | 2e-21 | 24/42 (KATO III, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.719×** | -9.9 | 1e-20 | 37/48 (AsPC-1, H4, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.630×** | -9.8 | 3e-20 | 33/46 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.726×** | -6.5 | 1e-08 | 20/38 (HT-29, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -4.9 | 9e-05 | 1/48 (MIA PaCa-2) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.794×** | -4.7 | 3e-04 | 22/47 (A-427, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.803×** | -4.5 | 5e-04 | 20/48 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Terfenadine (drug)]] 0.5 µM |  | 0.849× | -3.4 | 0.047 | 13/48 (HCT15, A549, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -3.3 | 0.056 | 17/48 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.860× | -3.2 | 0.078 | 11/48 (H4, HEC-1-A, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.861× | -3.2 | 0.080 | 13/48 (H4, CHP-212, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.862× | -3.1 | 0.10 | 4/48 (RKO, SW480, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.861× | -3.0 | 0.10 | 17/48 (SNU-423, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7863. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 47.5 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.16× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -17.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 33.2 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 3.87× (z +17.0) | — |
| [[A498 (line)]] | wt | 49.6 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +15.2) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -12.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 28.4 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.37× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 34.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.5× (z +35.6) | — |
| [[NCI-H460 (line)]] | wt | 35.7 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +18.7) | [[Dinaciclib (drug)]] 0.5 µM 0.471× (z -8.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 48.2 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.75× (z +22.0) | [[Dinaciclib (drug)]] 5 µM 0.0734× (z -19.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 49.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0640× (z -22.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 37.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +22.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.392× (z -9.1) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 26.1 | 3 | 0 | [[Belinostat (drug)]] 5 µM 4.30× (z +11.4) | — |
| [[A-427 (line)]] | wt | 36.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -12.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 51.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.44× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -11.7) |
| [[HepG2_C3A (line)]] | wt | 16.5 | 0 | 2 | — | [[Menadione (drug)]] 5 µM 0.0517× (z -13.6) |
| [[HT-29 (line)]] | alt | 45.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -20.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 22.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.50× (z +17.3) | [[Dinaciclib (drug)]] 5 µM 0.120× (z -12.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 39.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -11.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 29.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.214× (z -11.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 21.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +21.6) | — |
| [[H4 (line)]] | wt | 62.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0719× (z -17.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 36.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 30.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +18.4) | — |
| [[LOX-IMVI (line)]] | wt | 27.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 25.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 26.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +11.9) | — |
| [[NCI-H23 (line)]] | alt | 51.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +12.8) | — |
| [[Panc 03.27 (line)]] | alt | 29.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 17.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.08× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7863), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL9RP3]] | +0.71 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[TMEM104]] | +0.67 | +0.50 / +0.73 | both halves | 1e-05 |  |
| [[TRIM11]] | +0.67 | +0.51 / +0.69 | both halves | 1e-05 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[ARPC5L]] | +0.64 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[ATG101]] | +0.63 | +0.40 / +0.69 | both halves | 5e-05 |  |
| [[GON4L]] | +0.63 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[CRK]] | +0.63 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[DMPK]] | +0.63 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[YRDC]] | +0.62 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[BRPF1]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[SLC25A44]] | +0.60 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[MARCHF2]] | +0.60 | +0.54 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBBP9]] | -0.59 | -0.43 / -0.68 | both halves | 3e-05 |  |
| [[CISD2]] | -0.58 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[GSTK1]] | -0.57 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[SCCPDH]] | -0.56 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[SH3BGRL]] | -0.56 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[TSPAN6]] | -0.56 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[FMR1]] | -0.55 | -0.38 / -0.64 | both halves | 6e-05 |  |
| [[ACADM]] | -0.55 | -0.23 / -0.55 | both halves | 5e-04 |  |
| [[KPNA5]] | -0.55 | -0.31 / -0.62 | both halves | 2e-04 |  |
| [[NT5DC1]] | -0.55 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[HACD2]] | -0.55 | -0.29 / -0.59 | both halves | 3e-04 |  |
| [[TAF9]] | -0.55 | -0.25 / -0.63 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers FBXL18's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.550). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-14.4, -1.1); signed map (-47.4, 1.2). **Vector** length 97.4, 22.8% of its response variance represented; |z| ≥ 3 in 979 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.4 | +8.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.5 | +8.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.7 | +14.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +11.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.3 | +2.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.3 | +1.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +1.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.2 | -9.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | -2.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.4 | -4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -6.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -1.4 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -2.2 | -2.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.1 | -3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | F-box and leucine rich repeat protein 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1 — chr7:5,431,335-5,513,809 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11467, Fbl18 |
| Gene groups (HGNC) | F-box and leucine rich repeat proteins; MicroRNA protein coding host genes |
| Reactome | 9 pathways, smallest: FBXL7 down-regulates AURKA during mitotic entry and in early mitosis; G2/M Transition; Mitotic G2-G2/M phases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96ME1](https://www.uniprot.org/uniprotkb/Q96ME1) (F-box/LRR-repeat protein 18):

> Substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex.

**Summary**, from NCBI Gene [80028](https://www.ncbi.nlm.nih.gov/gene/80028):

> The protein encoded by this gene is a member of a family of proteins that contain an approximately 40-amino acid F-box motif. This motif is important for interaction with SKP1 and for targeting some proteins for degradation. The encoded protein has been shown to control the cellular level of FBXL7, a protein that induces mitotic arrest, by targeting it for polyubiquitylation and proteasomal degradation. Members of the F-box protein family, such as FBXL18, are characterized by an approximately …

**Accessions** — [HGNC:21874](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21874) · Entrez [80028](https://www.ncbi.nlm.nih.gov/gene/80028) · UniProt [Q96ME1](https://www.uniprot.org/uniprotkb/Q96ME1) · Ensembl [ENSG00000155034](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155034)

## Data

Gene col 7863: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7863); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7863, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7863]; `tensor/DDL_lfc|DDL_z.npy` [7863]; `embed/gene_vectors.npy` [7863]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7863 or target_col == 7863). Every well: [[FBXL18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXL18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
