---
symbol: "RAPH1"
type: "gene"
col: 10349
ensembl_id: "ENSG00000173166"
name: "Ras association (RalGDS/AF-6) and pleckstrin homology domains 1"
location: "2q33.2"
module: 101
arm: "+"
pooled_cpm: 135.45
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# RAPH1

*Ras association (RalGDS/AF-6) and pleckstrin homology domains 1* — 2q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.29× (z +32.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.772× (z -5.1, q 2e-04, down in 29 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change. The strongest without an alert is [[NG25 (drug)]] 5 µM: 0.637× (z -4.6, q 7e-04, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERPINB8]] (+0.61, fdr 1e-05), [[SOWAHC]] (+0.58, fdr 1e-05), [[ACOT9]] (+0.57, fdr 2e-05); moves opposite to [[ZFP14]] (-0.57, fdr 1e-05), [[CNNM2]] (-0.56, fdr 2e-05), [[KIAA2013]] (-0.56, fdr 2e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SCEL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10349.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.29×** | +32.7 | 0e+00 | 48/48 (hTERT-HPNE, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.74×** | +18.8 | 0e+00 | 46/48 (PANC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +10.7 | 1e-24 | 39/48 (hTERT-HPNE, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.31×** | +8.5 | 2e-15 | 35/49 (BT-474, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +7.0 | 3e-10 | 30/47 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +6.4 | 2e-08 | 32/48 (C32, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.35×** | +5.9 | 3e-07 | 34/48 (SNU-423, C32, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.34×** | +5.5 | 3e-06 | 28/47 (RPMI-7951, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.32×** | +5.3 | 7e-06 | 30/48 (NCI-H2030, A-427, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +5.1 | 2e-05 | 29/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +4.9 | 5e-05 | 21/48 (SW480, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +4.9 | 5e-05 | 27/48 (BT-474, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.28×** | +4.8 | 6e-05 | 30/48 (A-427, MIA PaCa-2, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.28×** | +4.8 | 8e-05 | 26/47 (NCI-H460, H4, …) | rises with dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +4.5 | 2e-04 | 25/48 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **1.52×** | +4.2 | 9e-04 | 25/48 (SW480, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +4.2 | 0.001 | 17/48 (NCI-H2030, MIA PaCa-2, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.002 | 25/47 (C32, SNU-423, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10349.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | **0.772×** | -5.1 | 2e-04 | 29/49 (KATO III, NCI-H460, …) | two highest doses | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.843× | -4.7 | 6e-04 | 22/49 (NCI-H460, COLO 205, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.637×** | -4.6 | 7e-04 | 27/47 (AsPC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.807×** | -4.0 | 0.008 | 24/47 (AsPC-1, SW480, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.689×** | -3.8 | 0.016 | 24/45 (SK-MEL-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.854× | -3.7 | 0.021 | 22/48 (AsPC-1, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.770×** | -3.6 | 0.021 | 22/47 (HCT15, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | **0.831×** | -3.5 | 0.032 | 21/44 (AsPC-1, KATO III, …) | two highest doses | composition shift |
| [[Arbutin (drug)]] 5 µM |  | 0.836× | -3.4 | 0.044 | 19/48 (HT-29, RPMI-7951, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.847× | -3.3 | 0.060 | 23/48 (LS 180, COLO 205, …) | two highest doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.856× | -3.1 | 0.11 | 22/49 (AsPC-1, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.898× | -3.0 | 0.12 | 9/48 (LoVo, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10349. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 444 | 0 | 11 (2 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.303× (z -13.2) |
| [[MIA PaCa-2 (line)]] | alt | 261 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +14.0) | [[Adagrasib (drug)]] 0.05 µM 0.535× (z -18.5) ⚠ position not correctable |
| [[BT-474 (line)]] | alt | 101 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +26.6) | [[Dinaciclib (drug)]] 5 µM 0.432× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[RPMI-7951 (line)]] | alt | 124 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.00× (z +28.2) | — |
| [[C32 (line)]] | wt | 51.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +23.9) | — |
| [[NCI-H460 (line)]] | wt | 269 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -13.9) ⚠ cell-cycle shift, explains ~6% of this change |
| [[A498 (line)]] | wt | 102 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +26.6) | — |
| [[HEC-1-A (line)]] | alt | 144 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +29.4) | — |
| [[hTERT-HPNE (line)]] | wt | 84.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.5× (z +33.8) | — |
| [[NCI-H23 (line)]] | alt | 128 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +23.5) | — |
| [[PANC-1 (line)]] | alt | 96.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +33.4) | — |
| [[A-172 (line)]] | wt | 127 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +27.7) | — |
| [[A549 (line)]] | wt | 107 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +23.1) | — |
| [[HOP62 (line)]] | alt | 123 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +28.3) | — |
| [[HS-578T (line)]] | alt | 109 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +31.7) | — |
| [[LoVo (line)]] | wt | 118 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -8.8) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Radotinib (drug)]] 5 µM 0.570× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 119 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +15.9) | [[Selinexor (drug)]] 5 µM 0.555× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 99.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +16.3) | — |
| [[SK-MEL-2 (line)]] | alt | 110 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.52× (z +27.2) | — |
| [[SNU-1 (line)]] | wt | 75.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +16.3) | — |
| [[SNU-423 (line)]] | alt | 112 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +27.4) | — |
| [[SW 900 (line)]] | alt | 122 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +26.9) | — |
| [[SW480 (line)]] | alt | 101 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +18.0) | [[Trametinib (drug)]] 0.5 µM 0.570× (z -8.8) |
| [[A-427 (line)]] | wt | 95.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.65× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.404× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[CFPAC-1 (line)]] | alt | 116 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +18.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -9.4) ⚠ cell-cycle shift, explains ~6% of this change |
| [[COLO 205 (line)]] | alt | 221 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -11.7) ⚠ cell-cycle shift, explains ~6% of this change |
| [[H4 (line)]] | wt | 82.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +15.0) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.343× (z -8.7) |
| [[HT-29 (line)]] | alt | 106 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +17.3) | — |
| [[J82 (line)]] | alt | 302 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +20.3) | — |
| [[KATO III (line)]] | alt | 115 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[LOX-IMVI (line)]] | wt | 104 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +20.5) | — |
| [[NCI-H1792 (line)]] | alt | 123 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +23.1) | — |
| [[NCI-H2347 (line)]] | alt | 150 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +18.4) | — |
| [[Panc 03.27 (line)]] | alt | 150 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +19.8) | — |
| [[RKO (line)]] | wt | 74.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +18.5) | — |
| [[SW1417 (line)]] | alt | 154 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +17.9) | — |
| [[SW48 (line)]] | wt | 123 | 0 | 2 (2 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.121× (z -8.8) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 73.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +11.0) | — |
| [[CHP-212 (line)]] | wt | 47.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.32× (z +12.9) | — |
| [[HepG2_C3A (line)]] | wt | 95.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 73.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.4) | — |
| [[NCI-H596 (line)]] | alt | 127 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.129× (z -8.5) |
| [[NCI-H661 (line)]] | alt | 171 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[SW 1088 (line)]] | alt | 136 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.124× (z -9.2) |
| [[SW 1271 (line)]] | alt | 121 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +9.8) | — |
| [[C-33 A (line)]] | alt | 86.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 92.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10349), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPINB8]] | +0.61 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[SOWAHC]] | +0.58 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[ACOT9]] | +0.57 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[ANXA5]] | +0.56 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[SLC22A3]] | +0.55 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[TRNP1]] | +0.55 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[MYO1C]] | +0.55 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[SGMS2]] | +0.54 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[VASP]] | +0.53 | +0.52 / +0.46 | both halves | 3e-05 | STRING 998 |
| [[UNC13D]] | +0.53 | +0.57 / +0.34 | both halves | 1e-04 |  |
| [[ZNF800]] | +0.52 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[TJP1]] | +0.52 | +0.52 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFP14]] | -0.57 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[CNNM2]] | -0.56 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[KIAA2013]] | -0.56 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[UBE4B]] | -0.55 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[ATG14]] | -0.55 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[TENT2]] | -0.54 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[ATPAF2]] | -0.54 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[CRYZL1]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[FNTB]] | -0.53 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[VDAC3]] | -0.52 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[PDSS2]] | -0.52 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[NFATC3]] | -0.52 | -0.45 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCEL]] | B | SCEL activity weakens RAPH1's drug response | lines that do not express SCEL (35) vs lines expressing it (14) | the lines without SCEL respond 1.38× as strongly (z diff -1.28); strongest at Homoharringtonine 0.5 µM: 2.08x vs 1.33x (z diff -3.5) | 0.097 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1; target measured in part of the lines; artifact flags |
| [[BCL2L1]] | B | BCL2L1 activity raises RAPH1's level | lines that do not express BCL2L1 (6) vs lines expressing it (44) | 1.64× lower at baseline in the lines without BCL2L1 | 0.099 | ⚠ within organs, on part of the lines; also absent: AMOTL2, RASSF7, CTSH; maybe low, not absent |
| [[TACC1]] | C | TACC1 activity lowers RAPH1's level | lines that do not express TACC1 (3) vs lines expressing it (47) | 2.35× higher at baseline in the lines without TACC1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLEC2D, TNNI3K, COL21A1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.581). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.4, 2.2); signed map (5.3, 34.1). **Vector** length 128, 40.0% of its response variance represented; |z| ≥ 3 in 1,501 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.1 | +18.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.9 | +32.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +10.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.8 | +5.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +5.0 | +4.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.8 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.8 | +3.7 |
|  | [[Neratinib (drug)]] 5 µM |  | +4.7 | +3.3 |
| fall | [[NG25 (drug)]] 5 µM |  | -5.9 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -2.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.1 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -0.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.4 | -2.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.1 | -3.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.1 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | Ras association (RalGDS/AF-6) and pleckstrin homology domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.2 — chr2:203,394,345-203,535,335 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Lpd, KIAA1681; previously ALS2CR9, ALS2CR18 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; MRL family adaptor proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q70E73](https://www.uniprot.org/uniprotkb/Q70E73) (Ras-associated and pleckstrin homology domains-containing protein 1):

> Mediator of localized membrane signals. Implicated in the regulation of lamellipodial dynamics. Negatively regulates cell adhesion.

**Summary**, from NCBI Gene [65059](https://www.ncbi.nlm.nih.gov/gene/65059):

> This gene encodes a protein that belongs to the Mig10/Rap1-interacting adaptor molecule/Lamellipodin family of adapter proteins, which function in cell migration. Members of this family contain pleckstrin-homology domains, Ras-association domains, and proline-rich C-termini. The protein encoded by this gene regulates actin dynamics through interaction with Ena/Vasodilator proteins as well as direct binding to filamentous actin to regulate actin network assembly. Alternative splicing results in …

**Accessions** — [HGNC:14436](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14436) · Entrez [65059](https://www.ncbi.nlm.nih.gov/gene/65059) · UniProt [Q70E73](https://www.uniprot.org/uniprotkb/Q70E73) · Ensembl [ENSG00000173166](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173166)

## Data

Gene col 10349: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10349); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10349, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10349]; `tensor/DDL_lfc|DDL_z.npy` [10349]; `embed/gene_vectors.npy` [10349]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10349 or target_col == 10349). Every well: [[RAPH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAPH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
