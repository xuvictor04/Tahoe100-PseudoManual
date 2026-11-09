---
symbol: "HIF1A"
type: "gene"
col: 2007
ensembl_id: "ENSG00000100644"
name: "hypoxia inducible factor 1 subunit alpha"
location: "14q23.2"
module: 139
arm: "+"
pooled_cpm: 261.28
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 7
n_dd_up_clean: 18
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# HIF1A

*hypoxia inducible factor 1 subunit alpha* — 14q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.98× (z +19.7, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.704× (z -6.9, q 2e-09, down in 32 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.737× (z -6.3, q 9e-08, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VAPA]] (+0.64, fdr 7e-06), [[IRAK3]] (+0.64, fdr 7e-06), [[AGFG1]] (+0.64, fdr 7e-06); moves opposite to [[RABGEF1]] (-0.50, fdr 4e-05), [[C2CD2]] (-0.45, fdr 1e-04), [[BLZF1]] (-0.44, fdr 5e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[BICC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2007.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.98×** | +19.7 | 0e+00 | 41/48 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.26×** | +17.7 | 0e+00 | 49/49 (SW480, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +17.7 | 0e+00 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.30×** | +17.0 | 0e+00 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **4.18×** | +15.3 | 0e+00 | 47/48 (SW480, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.04×** | +14.5 | 1e-45 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.06×** | +14.2 | 1e-43 | 47/48 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.93×** | +13.4 | 2e-39 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +12.0 | 4e-31 | 42/47 (MIA PaCa-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +9.8 | 8e-21 | 34/48 (A-172, SNU-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +9.0 | 1e-17 | 30/48 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +6.3 | 2e-08 | 27/38 (NCI-H1573, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +5.9 | 2e-07 | 29/48 (J82, PANC-1, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.31×** | +5.5 | 2e-06 | 27/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +4.9 | 3e-05 | 29/48 (J82, HCT15, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.26×** | +4.6 | 1e-04 | 25/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **1.25×** | +4.4 | 3e-04 | 27/48 (LS 180, Panc 03.27, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.23×** | +4.1 | 0.001 | 22/48 (MIA PaCa-2, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2007.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.704×** | -6.9 | 2e-09 | 32/47 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.737×** | -6.3 | 9e-08 | 32/48 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.809×** | -6.2 | 1e-07 | 26/49 (HepG2/C3A, C32, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.814×** | -6.0 | 3e-07 | 24/49 (SNU-423, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.823×** | -4.0 | 0.005 | 24/48 (H4, NCI-H1792, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.823×** | -4.0 | 0.005 | 23/48 (C32, CFPAC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.828×** | -3.9 | 0.007 | 25/48 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.877× | -3.9 | 0.008 | 15/49 (CFPAC-1, HepG2/C3A, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.843× | -3.5 | 0.025 | 19/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.844× | -3.5 | 0.025 | 23/49 (A498, C32, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.859× | -3.1 | 0.085 | 16/48 (RPMI-7951, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2007. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 250 | 14 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.48× (z +22.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.72× (z +21.0) | — |
| [[A-172 (line)]] | wt | 148 | 12 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +25.0) | — |
| [[SW480 (line)]] | alt | 146 | 12 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.79× (z +20.4) | — |
| [[HS-578T (line)]] | alt | 236 | 11 (3 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 3.30× (z +14.1) | — |
| [[J82 (line)]] | alt | 351 | 10 (2 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 3.98× (z +17.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 269 | 10 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.93× (z +16.4) | — |
| [[NCI-H2347 (line)]] | alt | 570 | 8 (1 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.34× (z +11.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.490× (z -8.8) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.509× (z -8.7) |
| [[PANC-1 (line)]] | alt | 118 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +23.2) | — |
| [[SNU-1 (line)]] | wt | 176 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +22.5) | — |
| [[A-427 (line)]] | wt | 109 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +21.3) | — |
| [[hTERT-HPNE (line)]] | wt | 313 | 8 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +16.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 116 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +19.6) | — |
| [[SK-MEL-2 (line)]] | alt | 198 | 8 (2 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 3.39× (z +13.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.26× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -9.2) |
| [[C-33 A (line)]] | alt | 146 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +14.0) | — |
| [[C32 (line)]] | wt | 584 | 2 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 11.0× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -12.8) |
| [[HOP62 (line)]] | alt | 274 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +12.4) | — |
| [[LOX-IMVI (line)]] | wt | 149 | 8 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.28× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +11.1) | — |
| [[NCI-H23 (line)]] | alt | 200 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +18.4) | — |
| [[CFPAC-1 (line)]] | alt | 868 | 5 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +14.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -16.0) |
| [[LoVo (line)]] | wt | 84.2 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.96× (z +16.7) | — |
| [[SW48 (line)]] | wt | 132 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.52× (z +13.7) | — |
| [[HEC-1-A (line)]] | alt | 137 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +20.5) | — |
| [[A498 (line)]] | wt | 279 | 4 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -12.1) |
| [[H4 (line)]] | wt | 249 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 108 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.57× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.26× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 276 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +11.4) | — |
| [[RKO (line)]] | wt | 140 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +13.5) | — |
| [[AsPC-1 (line)]] | alt | 109 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +12.0) | — |
| [[KATO III (line)]] | alt | 116 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.65× (z +16.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +13.5) | — |
| [[LS 180 (line)]] | wt | 122 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.31× (z +12.5) | — |
| [[Panc 03.27 (line)]] | alt | 340 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.0) | — |
| [[SW1417 (line)]] | alt | 131 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +15.8) | — |
| [[Hs 766T (line)]] | wt | 145 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.23× (z +10.0) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 6.49× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 556 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 9.27× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -13.6) |
| [[SNU-423 (line)]] | alt | 667 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -20.6) |
| [[A549 (line)]] | wt | 394 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -18.9) |
| [[COLO 205 (line)]] | alt | 165 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 4.25× (z +13.6) | — |
| [[HCT15 (line)]] | alt | 149 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.7) | — |
| [[HepG2_C3A (line)]] | wt | 281 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.09× (z +10.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.416× (z -9.7) ⚠ toxic |
| [[SW 900 (line)]] | alt | 580 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -11.5) |
| [[AN3 CA (line)]] | alt | 407 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -8.5) |
| [[CHP-212 (line)]] | wt | 463 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 566 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -15.4) |
| [[SW 1088 (line)]] | alt | 462 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -8.9) |
| [[BT-474 (line)]] | alt | 342 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 300 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 289 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 163 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2007), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VAPA]] | +0.64 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[IRAK3]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[AGFG1]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[IL1R1]] | +0.63 | +0.54 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 434 |
| [[NAMPT]] | +0.62 | +0.52 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 554 |
| [[STOM]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[UBE2E1]] | +0.60 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[SAA2-SAA4]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[SAA2]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PID1]] | +0.57 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[C1RL]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[NNMT]] | +0.56 | +0.48 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABGEF1]] | -0.50 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[C2CD2]] | -0.45 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[BLZF1]] | -0.44 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[DPP9]] | -0.44 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[CHAF1B]] | -0.44 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[POLR3D]] | -0.43 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[RRP12]] | -0.43 | -0.40 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BICC1]] | B | BICC1 activity raises HIF1A's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 2.03× lower at baseline in the lines without BICC1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2 |
| [[BATF]] | B | BATF activity weakens HIF1A's drug response | lines that do not express BATF (33) vs lines expressing it (16) | the lines without BATF respond 1.32× as strongly (z diff -1.59); strongest at Homoharringtonine 0.5 µM: 1.78x vs 1.15x (z diff -3.5) | 0.043 | ⚠ within organs, on part of the lines; also absent: KRT23, WFDC2, TACSTD2; target measured in part of the lines; artifact flags |
| [[SAA1]] | B | SAA1 activity raises HIF1A's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 1.56× lower at baseline in the lines without SAA1 | 0.062 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11 |
| [[CP]] | B | CP activity raises HIF1A's level | lines that do not express CP (39) vs lines expressing it (11) | 1.91× lower at baseline in the lines without CP | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB |
| [[TLR2]] | B | TLR2 activity raises HIF1A's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 1.65× lower at baseline in the lines without TLR2 | 0.088 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |
| [[HSD11B1]] | B | HSD11B1 activity raises HIF1A's level | lines that do not express HSD11B1 (34) vs lines expressing it (16) | 1.65× lower at baseline in the lines without HSD11B1 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, NID2, EDNRA |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.717). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.0, 17.3); signed map (17.9, 29.5). **Vector** length 125, 45.0% of its response variance represented; |z| ≥ 3 in 1,776 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.55 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.9 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.9 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.8 | +0.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +6.6 | +1.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +5.5 | +3.1 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +4.7 | +2.8 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +4.7 | +1.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.2 | -6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.7 | -6.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.7 | -4.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.8 | -6.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | +4.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.5 | -3.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.1 | -3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | hypoxia inducible factor 1 subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.2 — chr14:61,695,513-61,748,259 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MOP1, HIF-1alpha, PASD8, HIF1, bHLHe78 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; PAS domain containing; Hypoxia inducible factor subunits |
| Hallmark sets | ALLOGRAFT_REJECTION, INFLAMMATORY_RESPONSE, INTERFERON_GAMMA_RESPONSE, G2M_CHECKPOINT |
| Reactome | 26 pathways, smallest: PTK6 Expression; PTK6 promotes HIF1A stabilization; Regulation of gene expression by Hypoxia-inducible Factor |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16665](https://www.uniprot.org/uniprotkb/Q16665) (Hypoxia-inducible factor 1-alpha):

> Functions as a master transcriptional regulator of the adaptive response to hypoxia. Under hypoxic conditions, activates the transcription of over 40 genes, including erythropoietin, glucose transporters, glycolytic enzymes, vascular endothelial growth factor, HILPDA, and other genes whose protein products increase oxygen delivery or facilitate metabolic adaptation to hypoxia. Plays an essential role in embryonic vascularization, tumor angiogenesis and pathophysiology of ischemic disease. …

**Summary**, from NCBI Gene [3091](https://www.ncbi.nlm.nih.gov/gene/3091):

> This gene encodes the alpha subunit of transcription factor hypoxia-inducible factor-1 (HIF-1), which is a heterodimer composed of an alpha and a beta subunit. HIF-1 functions as a master regulator of cellular and systemic homeostatic response to hypoxia by activating transcription of many genes, including those involved in energy metabolism, angiogenesis, apoptosis, and other genes whose protein products increase oxygen delivery or facilitate metabolic adaptation to hypoxia. HIF-1 thus plays …

**Accessions** — [HGNC:4910](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4910) · Entrez [3091](https://www.ncbi.nlm.nih.gov/gene/3091) · UniProt [Q16665](https://www.uniprot.org/uniprotkb/Q16665) · Ensembl [ENSG00000100644](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100644)

## Data

Gene col 2007: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2007); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2007, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2007]; `tensor/DDL_lfc|DDL_z.npy` [2007]; `embed/gene_vectors.npy` [2007]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2007 or target_col == 2007). Every well: [[HIF1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HIF1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
