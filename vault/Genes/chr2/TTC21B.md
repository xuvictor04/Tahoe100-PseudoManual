---
symbol: "TTC21B"
type: "gene"
col: 4448
ensembl_id: "ENSG00000123607"
name: "tetratricopeptide repeat domain 21B"
location: "2q24.3"
module: 65
arm: "+"
pooled_cpm: 81.13
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# TTC21B

*tetratricopeptide repeat domain 21B* — 2q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.87× (z +19.0, q 0e+00, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.582× (z -11.5, q 5e-28, down in 37 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.755× (z -6.0, q 3e-07, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HAUS4]] (+0.57, fdr 2e-05), [[DIXDC1]] (+0.57, fdr 1e-05), [[MNS1]] (+0.55, fdr 3e-05); moves opposite to [[SMIM12]] (-0.63, fdr 1e-05), [[LINC02257]] (-0.55, fdr 3e-05), [[AVEN]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LINC02257]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4448.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.87×** | +19.0 | 0e+00 | 34/48 (A498, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.74×** | +11.8 | 8e-30 | 40/48 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.68×** | +11.1 | 2e-26 | 40/48 (A498, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +9.0 | 4e-17 | 35/48 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +7.6 | 2e-12 | 35/48 (A498, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +6.9 | 5e-10 | 30/48 (A498, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +6.0 | 2e-07 | 29/48 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +5.7 | 9e-07 | 28/48 (HOP62, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.29×** | +5.2 | 1e-05 | 24/48 (LoVo, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +5.0 | 3e-05 | 27/48 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +4.5 | 3e-04 | 27/49 (AsPC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.18× | +3.5 | 0.019 | 20/48 (LoVo, HepG2/C3A, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +3.3 | 0.037 | 13/48 (SW 900, SW1417, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.039 | 14/49 (HOP62, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.065 | 13/48 (HOP62, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4448.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.582×** | -11.5 | 5e-28 | 37/49 (HCT15, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.680×** | -7.9 | 9e-13 | 34/44 (C32, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.702×** | -7.0 | 6e-10 | 26/45 (NCI-H2030, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.753×** | -6.0 | 2e-07 | 27/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.755×** | -6.0 | 3e-07 | 37/48 (SW480, C32, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.783×** | -5.0 | 5e-05 | 27/47 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.801×** | -4.7 | 2e-04 | 28/48 (RPMI-7951, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.803×** | -4.7 | 2e-04 | 25/48 (NCI-H1573, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.867× | -4.3 | 0.001 | 19/48 (RKO, LOX-IMVI, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.813×** | -4.2 | 0.001 | 24/48 (PANC-1, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.833×** | -3.9 | 0.005 | 21/48 (PANC-1, C32, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.848× | -3.4 | 0.036 | 20/47 (A-427, NCI-H1573, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.782×** | -3.2 | 0.058 | 16/48 (HOP62, SW 900, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.860× | -3.1 | 0.083 | 12/47 (HT-29, C32, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4448. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 61.2 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +24.5) | [[Docetaxel (drug)]] 0.05 µM 0.506× (z -8.8) ⚠ transcription drop |
| [[C32 (line)]] | wt | 104 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.409× (z -12.9) |
| [[NCI-H1573 (line)]] | alt | 91.3 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.354× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.518× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 72.3 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +15.1) | [[Pimozide (drug)]] 0.05 µM 0.381× (z -8.5) |
| [[LoVo (line)]] | wt | 60.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +17.7) | — |
| [[NCI-H23 (line)]] | alt | 136 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.410× (z -15.5) |
| [[SW1417 (line)]] | alt | 78.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +14.8) | — |
| [[HOP62 (line)]] | alt | 76.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +12.9) | — |
| [[LS 180 (line)]] | wt | 58.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.208× (z -14.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 83.3 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.478× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.502× (z -11.3) |
| [[A-172 (line)]] | wt | 74.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.4) | — |
| [[A549 (line)]] | wt | 94.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.406× (z -9.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 143 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -11.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 140 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +11.7) | — |
| [[HT-29 (line)]] | alt | 44.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.46× (z +21.2) | — |
| [[J82 (line)]] | alt | 78.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.439× (z -9.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 98.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.352× (z -10.6) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 85.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +14.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.444× (z -9.0) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 44.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +19.8) | — |
| [[PANC-1 (line)]] | alt | 83.6 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.409× (z -11.4) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.509× (z -9.0) |
| [[RKO (line)]] | wt | 85.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +17.7) | — |
| [[RPMI-7951 (line)]] | alt | 64.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.4) | [[Docetaxel (drug)]] 0.05 µM 0.171× (z -16.2) ⚠ transcription drop |
| [[SK-MEL-2 (line)]] | alt | 74.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -10.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 97.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -15.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 125 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.286× (z -9.1) |
| [[BT-474 (line)]] | alt | 52.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +14.3) | — |
| [[HCT15 (line)]] | alt | 83.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0586× (z -26.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 83.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +17.0) | — |
| [[HS-578T (line)]] | alt | 54.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +16.9) | — |
| [[LOX-IMVI (line)]] | wt | 165 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.399× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.361× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 120 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.448× (z -10.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 60.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +12.1) | — |
| [[SHP-77 (line)]] | alt | 72.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -10.0) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 116 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.156× (z -9.5) |
| [[SW 900 (line)]] | alt | 68.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +15.1) | — |
| [[SW48 (line)]] | wt | 79.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +11.3) | — |
| [[AsPC-1 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 76.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 95.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 156 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 82.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4448), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HAUS4]] | +0.57 | +0.47 / +0.52 | both halves | 2e-05 | pathway: Assembly of the 9+0 primary cilium |
| [[DIXDC1]] | +0.57 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[MNS1]] | +0.55 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[PGAP1]] | +0.54 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CCDC34]] | +0.54 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[KANTR]] | +0.54 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[ARL6]] | +0.53 | +0.44 / +0.55 | both halves | 3e-05 | pathway: Assembly of the 9+0 primary cilium |
| [[WDR54]] | +0.53 | +0.45 / +0.37 | both halves | 9e-05 |  |
| [[ZDHHC20]] | +0.52 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[PDK3]] | +0.52 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[HACL1]] | +0.52 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[SPATA6]] | +0.52 | +0.33 / +0.61 | both halves | 1e-04 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM12]] | -0.63 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[LINC02257]] | -0.55 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[AVEN]] | -0.51 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[LTO1]] | -0.50 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[BCDIN3D]] | -0.49 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[SLC13A3]] | -0.48 | -0.33 / -0.29 | both halves | 3e-04 |  |
| [[MAEA]] | -0.48 | -0.45 / -0.36 | both halves | 9e-05 |  |
| [[TMEM186]] | -0.48 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[TEX22]] | -0.48 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[MYH3]] | -0.47 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[ITPRIPL2]] | -0.47 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[PURB]] | -0.45 | -0.31 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02257]] | B | LINC02257 activity lowers TTC21B's level | lines that do not express LINC02257 (15) vs lines expressing it (35) | 1.32× higher at baseline in the lines without LINC02257 | 0.045 | ⚠ within organs, on part of the lines; also absent: CTSS, PAG1, ZNF365; maybe low, not absent |
| [[LINC02257]] | B | LINC02257 activity strengthens TTC21B's drug response | lines that do not express LINC02257 (15) vs lines expressing it (34) | the lines without LINC02257 respond 0.83× as strongly (z diff +0.84); strongest at Belinostat 5 µM: 1.34x vs 1.83x (z diff +3.0) | 0.076 | ⚠ within organs, on part of the lines; also absent: CTSS, PAG1, ZNF365; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PSORS1C1]] | B | PSORS1C1 activity lowers TTC21B's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 1.39× higher at baseline in the lines without PSORS1C1 | 0.078 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |
| [[HDAC6]] | B | HDAC6 activity lowers TTC21B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers TTC21B's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HACE1]] | C | HACE1 activity raises TTC21B's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 2.01× lower at baseline in the lines without HACE1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.398). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (15.9, -10.9); signed map (-26.5, -10.4). **Vector** length 104, 28.7% of its response variance represented; |z| ≥ 3 in 1,133 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +4.7 | +9.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +5.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.5 | +6.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.5 | +2.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +1.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.2 | +3.3 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +3.0 | +1.1 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.9 | +3.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.3 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | +0.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -1.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.9 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -3.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 21B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.3 — chr2:165,857,475-165,953,851 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11457, JBTS11, NPHP12, IFT139B, THM1, FAP60, FLA17, IFT139 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; IFT-A complex |
| Reactome | 6 pathways, smallest: Intraflagellar transport; Hedgehog 'off' state; Signaling by Hedgehog |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z4L5](https://www.uniprot.org/uniprotkb/Q7Z4L5) (Tetratricopeptide repeat protein 21B):

> Component of the IFT complex A (IFT-A), a complex required for retrograde ciliary transport and entry into cilia of G protein-coupled receptors (GPCRs). Essential for retrograde trafficking of IFT-1, IFT-B and GPCRs. Negatively modulates the SHH signal transduction (By similarity).

**Summary**, from NCBI Gene [79809](https://www.ncbi.nlm.nih.gov/gene/79809):

> This gene encodes a member of TTC21 family, containing several tetratricopeptide repeat (TPR) domains. This protein is localized to the cilium axoneme, and may play a role in retrograde intraflagellar transport in cilia. Mutations in this gene are associated with various ciliopathies, nephronophthisis 12, and asphyxiating thoracic dystrophy 4. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:25660](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25660) · Entrez [79809](https://www.ncbi.nlm.nih.gov/gene/79809) · UniProt [Q7Z4L5](https://www.uniprot.org/uniprotkb/Q7Z4L5) · Ensembl [ENSG00000123607](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123607)

## Data

Gene col 4448: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4448); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4448, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4448]; `tensor/DDL_lfc|DDL_z.npy` [4448]; `embed/gene_vectors.npy` [4448]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4448 or target_col == 4448). Every well: [[TTC21B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC21B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
