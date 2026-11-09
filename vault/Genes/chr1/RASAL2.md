---
symbol: "RASAL2"
type: "gene"
col: 1115
ensembl_id: "ENSG00000075391"
name: "RAS protein activator like 2"
location: "1q25.2"
module: 120
arm: "+"
pooled_cpm: 263.64
n_lines_expressing: 49
n_dd_up: 26
n_dd_down: 10
n_dd_up_clean: 20
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# RASAL2

*RAS protein activator like 2* — 1q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.98× (z +15.8, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.545× (z -14.1, q 3e-42, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRGAP1]] (+0.68, fdr 7e-06), [[ACOT9]] (+0.67, fdr 1e-05), [[TRIO]] (+0.67, fdr 7e-06); moves opposite to [[SRP54-AS1]] (-0.67, fdr 7e-06), [[TUBE1]] (-0.58, fdr 1e-05), [[VDAC1P8]] (-0.58, fdr 2e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HNF1A]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1115.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.98×** | +15.8 | 0e+00 | 42/47 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.36×** | +14.0 | 5e-42 | 43/47 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.97×** | +11.1 | 4e-26 | 38/47 (NCI-H2030, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.13×** | +9.7 | 3e-20 | 36/47 (HOP62, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.78×** | +9.4 | 6e-19 | 37/47 (NCI-H2030, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.79×** | +9.1 | 1e-17 | 44/47 (C32, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.69×** | +8.6 | 9e-16 | 35/47 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.59×** | +8.1 | 3e-14 | 35/48 (NCI-H2030, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +7.4 | 1e-11 | 31/47 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +6.1 | 4e-08 | 33/47 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +6.0 | 1e-07 | 26/44 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.7 | 5e-07 | 33/47 (HOP62, SW480, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.35×** | +4.7 | 1e-04 | 29/46 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.30×** | +4.3 | 7e-04 | 26/47 (C32, A-427, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +4.2 | 0.001 | 29/47 (NCI-H1573, RKO, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +4.1 | 0.001 | 29/47 (HCT15, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | 1.19× | +4.0 | 0.002 | 16/47 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.28×** | +4.0 | 0.002 | 27/48 (A-427, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1115.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.545×** | -14.1 | 3e-42 | 35/48 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.573×** | -8.8 | 5e-16 | 32/43 (J82, C-33 A, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.638×** | -7.4 | 3e-11 | 38/47 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.713×** | -5.5 | 4e-06 | 29/48 (NCI-H2030, A-427, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.724×** | -5.1 | 4e-05 | 30/46 (NCI-H2030, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.815×** | -4.8 | 2e-04 | 22/47 (J82, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.763×** | -4.4 | 7e-04 | 26/47 (Hs 766T, NCI-H23, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.743×** | -3.5 | 0.036 | 26/47 (LS 180, NCI-H460, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.818×** | -3.3 | 0.058 | 24/47 (A-172, J82, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **0.815×** | -3.2 | 0.068 | 22/49 (A-172, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1115. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 187 | 15 (4 ⚠) | 2 | [[Homoharringtonine (drug)]] 0.5 µM 7.50× (z +20.6) | [[Selinexor (drug)]] 5 µM 0.523× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 501 | 10 (2 ⚠) | 7 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.65× (z +16.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -15.9) |
| [[NCI-H460 (line)]] | wt | 256 | 10 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 6.28× (z +19.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 3.44× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.429× (z -9.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 411 | 6 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.10× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -12.3) |
| [[NCI-H1573 (line)]] | alt | 167 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +15.0) | — |
| [[SNU-1 (line)]] | wt | 136 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +17.4) | — |
| [[SW1417 (line)]] | alt | 205 | 7 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +21.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -13.2) |
| [[KATO III (line)]] | alt | 198 | 6 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +14.9) | [[Docetaxel (drug)]] 0.05 µM 0.439× (z -9.2) ⚠ transcription drop |
| [[SK-MEL-2 (line)]] | alt | 387 | 7 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 7.70× (z +17.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.72× (z +16.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -10.3) |
| [[A-172 (line)]] | wt | 330 | 2 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -20.0) |
| [[A549 (line)]] | wt | 188 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 3.16× (z +13.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 282 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +22.2) | [[Dinaciclib (drug)]] 5 µM 0.262× (z -14.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 577 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -13.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 530 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.240× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -11.0) |
| [[A498 (line)]] | wt | 223 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +14.4) | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -13.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 140 | 4 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 4.74× (z +17.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -11.3) |
| [[J82 (line)]] | alt | 339 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.449× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 276 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -17.9) |
| [[MIA PaCa-2 (line)]] | alt | 231 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 7.67× (z +16.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -10.5) |
| [[SW 900 (line)]] | alt | 459 | 4 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.69× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -16.0) |
| [[SW480 (line)]] | alt | 105 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +21.6) | — |
| [[AsPC-1 (line)]] | alt | 565 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +14.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 340 | 3 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 3.03× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -13.4) |
| [[Panc 03.27 (line)]] | alt | 443 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.0) | — |
| [[RPMI-7951 (line)]] | alt | 145 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +16.2) | — |
| [[HS-578T (line)]] | alt | 239 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -19.9) |
| [[SNU-423 (line)]] | alt | 304 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +16.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -16.1) |
| [[SW48 (line)]] | wt | 202 | 2 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 5.63× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 8.02× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -9.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 188 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.45× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.220× (z -16.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 191 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 4.15× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -19.2) |
| [[HEC-1-A (line)]] | alt | 124 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +10.7) | — |
| [[HT-29 (line)]] | alt | 261 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +14.7) | — |
| [[hTERT-HPNE (line)]] | wt | 285 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -13.2) |
| [[NCI-H661 (line)]] | alt | 607 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -10.7) |
| [[H4 (line)]] | wt | 135 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +13.4) | — |
| [[HepG2_C3A (line)]] | wt | 207 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.379× (z -9.4) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 307 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -18.8) |
| [[NCI-H2347 (line)]] | alt | 279 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -13.4) |
| [[SW 1088 (line)]] | alt | 315 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -8.9) |
| [[AN3 CA (line)]] | alt | 149 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 62.4 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 156 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 180 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 217 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1115), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGAP1]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[ACOT9]] | +0.67 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[TRIO]] | +0.67 | +0.60 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[ABL2]] | +0.61 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[STARD13]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[PTPN21]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ASAP1]] | +0.59 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[EGFR]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 | pathway: MAPK family signaling cascades |
| [[PITPNB]] | +0.59 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[DDX10]] | +0.58 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[CYTOR]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[LINC00707]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP54-AS1]] | -0.67 | -0.58 / -0.68 | both halves | 7e-06 |  |
| [[TUBE1]] | -0.58 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[VDAC1P8]] | -0.58 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[PIK3C2A]] | -0.56 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[TSNAX-DISC1]] | -0.55 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[TGDS]] | -0.55 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[MAPKAPK5-AS1]] | -0.55 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[ATPAF1]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[ABCD4]] | -0.54 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[CLEC4A]] | -0.54 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[EPHX2]] | -0.54 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[SPICE1]] | -0.54 | -0.53 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HNF1A]] | C | HNF1A activity strengthens RASAL2's drug response | recorded loss-of-function mutation of HNF1A in 5 lines vs 43 not recorded | the HNF1A-altered lines respond 0.38× as strongly (z diff +4.37); strongest at Ouabain (Octahydrate) 5 µM: 0.88x vs 1.98x (z diff +8.3) | 0.025 | ⚠ tissue-confounded; across organs; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.647). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.8, 12.1); signed map (12.2, 39.8). **Vector** length 146, 51.7% of its response variance represented; |z| ≥ 3 in 1,680 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.4 | +14.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.9 | +4.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.8 | +9.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.6 | +8.1 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +6.4 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.3 | +5.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.8 | +4.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +5.3 | +4.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +4.5 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -14.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | -6.6 | -7.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.2 | -4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.2 | -4.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | -4.6 | -3.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -4.2 | -3.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.7 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -2.2 |
|  | [[Terfenadine (drug)]] 5 µM |  | -3.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | RAS protein activator like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.2 — chr1:178,094,104-178,484,147 (+) |
| Ensembl biotype | protein_coding |
| Also known as | nGAP |
| Gene groups (HGNC) | Pleckstrin homology domain containing; C2 and RasGAP domain containing |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE |
| Reactome | 9 pathways, smallest: RND1 GTPase cycle; RND3 GTPase cycle; Regulation of RAS by GAPs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJF2](https://www.uniprot.org/uniprotkb/Q9UJF2) (Ras GTPase-activating protein nGAP):

> Inhibitory regulator of the Ras-cyclic AMP pathway.

**Summary**, from NCBI Gene [9462](https://www.ncbi.nlm.nih.gov/gene/9462):

> This gene encodes a protein that contains the GAP-related domain (GRD), a characteristic domain of GTPase-activating proteins (GAPs). GAPs function as activators of Ras superfamily of small GTPases. The protein encoded by this gene is able to complement the defective RasGAP function in a yeast system. Two alternatively spliced transcript variants of this gene encoding distinct isoforms have been reported. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9874](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9874) · Entrez [9462](https://www.ncbi.nlm.nih.gov/gene/9462) · UniProt [Q9UJF2](https://www.uniprot.org/uniprotkb/Q9UJF2) · Ensembl [ENSG00000075391](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075391)

## Data

Gene col 1115: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1115); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1115, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1115]; `tensor/DDL_lfc|DDL_z.npy` [1115]; `embed/gene_vectors.npy` [1115]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1115 or target_col == 1115). Every well: [[RASAL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RASAL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
