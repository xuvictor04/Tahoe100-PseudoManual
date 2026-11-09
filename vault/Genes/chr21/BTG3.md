---
symbol: "BTG3"
type: "gene"
col: 7821
ensembl_id: "ENSG00000154640"
name: "BTG anti-proliferation factor 3"
location: "21q21.1"
module: 14
arm: "+"
pooled_cpm: 58.99
n_lines_expressing: 46
n_dd_up: 24
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# BTG3

*BTG anti-proliferation factor 3* — 21q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.82× (z +10.4, q 2e-22, up in 35 of 44 measured lines) ⚠ cell-cycle shift, explains ~55% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.72× (z +6.6, q 4e-09, up in 37 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.477× (z -9.1, q 6e-17, down in 37 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRRG4]] (+0.64, fdr 3e-05), [[DRAM1]] (+0.60, fdr 1e-05), [[CHMP2B]] (+0.59, fdr 3e-05); moves opposite to [[BLTP2]] (-0.59, fdr 3e-05), [[NOMO1]] (-0.55, fdr 3e-05), [[TUFM]] (-0.55, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NTN1]] → it (grade B ⚠); 3 go from it, the strongest it → [[NTN1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7821.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.82×** | +10.4 | 2e-22 | 35/44 (NCI-H1573, HOP62, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.08×** | +8.9 | 1e-16 | 39/44 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.85×** | +7.5 | 9e-12 | 41/44 (NCI-H460, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.80×** | +7.2 | 1e-10 | 34/43 (PANC-1, A549, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +6.6 | 4e-09 | 37/44 (MIA PaCa-2, SNU-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +6.2 | 5e-08 | 37/43 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.64×** | +6.1 | 1e-07 | 36/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.60×** | +5.5 | 2e-06 | 31/44 (NCI-H1573, HOP62, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.55×** | +5.3 | 6e-06 | 33/43 (NCI-H23, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.53×** | +5.2 | 1e-05 | 31/44 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.35×** | +5.2 | 1e-05 | 38/44 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.0 | 3e-05 | 29/43 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.47×** | +4.7 | 1e-04 | 28/44 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **1.44×** | +4.5 | 3e-04 | 33/44 (HOP62, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.44×** | +4.4 | 4e-04 | 30/43 (H4, RPMI-7951, …) | all doses, stronger at high dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.43×** | +4.2 | 0.001 | 29/43 (H4, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.36×** | +3.8 | 0.005 | 27/44 (C-33 A, SW 900, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.58×** | +3.7 | 0.006 | 27/44 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.014 | 24/44 (NCI-H2030, J82, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.70×** | +3.4 | 0.017 | 23/42 (MIA PaCa-2, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.042 | 21/44 (Panc 03.27, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +2.9 | 0.083 | 19/44 (SW480, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7821.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.477×** | -9.1 | 6e-17 | 37/44 (A549, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.497×** | -8.6 | 3e-15 | 38/44 (NCI-H23, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.593×** | -6.4 | 3e-08 | 36/44 (A549, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7821. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 52.3 | 7 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.10× (z +12.4) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A549 (line)]] | wt | 60.6 | 3 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +13.8) ⚠ cell-cycle shift, explains ~55% of this change | [[Panobinostat (drug)]] 5 µM 0.312× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 57.2 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +13.0) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[J82 (line)]] | alt | 57.5 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.7) ⚠ cell-cycle shift, explains ~55% of this change | [[Panobinostat (drug)]] 0.5 µM 0.342× (z -9.1) |
| [[HOP62 (line)]] | alt | 69.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +14.8) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[LoVo (line)]] | wt | 73.8 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.13× (z +11.0) ⚠ toxic | — |
| [[LOX-IMVI (line)]] | wt | 88.5 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.06× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LS 180 (line)]] | wt | 80.7 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.05× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 53.6 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.76× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.269× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 76.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +15.4) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[NCI-H23 (line)]] | alt | 86.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Panobinostat (drug)]] 0.5 µM 0.375× (z -9.7) |
| [[PANC-1 (line)]] | alt | 37.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +13.3) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[SNU-1 (line)]] | wt | 116 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.06× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 66.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.290× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 42.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +14.5) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[CFPAC-1 (line)]] | alt | 72.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.6) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 36.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +8.8) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[Panc 03.27 (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.9) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[RPMI-7951 (line)]] | alt | 84.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +10.2) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 94.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.04× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[SW 900 (line)]] | alt | 79.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +11.8) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[A-427 (line)]] | wt | 183 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.86 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 123 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 78.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 91.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.63 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 71.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 80.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 29.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7821), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRRG4]] | +0.64 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[DRAM1]] | +0.60 | +0.50 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CHMP2B]] | +0.59 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[TLCD5]] | +0.59 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[TCEAL3]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[RAB9A]] | +0.57 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[RAB32]] | +0.57 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[BTN2A2]] | +0.56 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[TBC1D9]] | +0.55 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[RASGRP1]] | +0.54 | +0.44 / +0.50 | both halves | 3e-05 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[APBB1]] | +0.54 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[HLA-F]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 | pathway: HALLMARK_UV_RESPONSE_UP |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLTP2]] | -0.59 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[NOMO1]] | -0.55 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[TUFM]] | -0.55 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[CHID1]] | -0.55 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[GTF3C1]] | -0.54 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[ZDHHC3]] | -0.54 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[PHB1]] | -0.53 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[UGGT1]] | -0.53 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[BPNT2]] | -0.52 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[GLG1]] | -0.52 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[SNRNP200]] | -0.52 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[PDCD6]] | -0.51 | -0.54 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NTN1]] | B | NTN1 activity raises BTG3's level | lines that do not express NTN1 (17) vs lines expressing it (33) | 1.58× lower at baseline in the lines without NTN1 | 0.013 | ⚠ within organs, on part of the lines; also absent: LINC00466, MCOLN3, ZMAT1; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises BTG3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DRAM1]] | B | DRAM1 activity raises BTG3's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 2.04× lower at baseline in the lines without DRAM1 | 0.028 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NTN1]] | C | BTG3 activity raises NTN1's level | lines that do not express BTG3 (4) vs lines expressing it (46) | 1.63× lower at baseline in the lines without BTG3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WTIP; its own permutation p |
| [[BCAP31]] | C | BTG3 activity raises BCAP31's level | lines that do not express BTG3 (4) vs lines expressing it (46) | 1.36× lower at baseline in the lines without BTG3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WTIP; its own permutation p |
| [[CETN2]] | C | BTG3 activity raises CETN2's level | lines that do not express BTG3 (4) vs lines expressing it (46) | 1.17× lower at baseline in the lines without BTG3 | 0.086 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WTIP |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.478). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.1, 9.6); signed map (7.0, -6.7). **Vector** length 90.5, 25.8% of its response variance represented; |z| ≥ 3 in 916 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +8.1 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.1 | +2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +7.3 | +10.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.4 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +6.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.5 | +0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +0.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.8 | +1.7 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -4.8 | -1.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.5 | -8.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.4 | -9.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +0.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.3 | -6.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -1.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.1 | -2.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | BTG anti-proliferation factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q21.1 — chr21:17,593,653-17,612,945 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ANA, tob55, APRO4, ANA/BTG3 |
| Gene groups (HGNC) | BTG/Tob family |
| Hallmark sets | APOPTOSIS, UV_RESPONSE_UP, ESTROGEN_RESPONSE_LATE, TNFA_SIGNALING_VIA_NFKB |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14201](https://www.uniprot.org/uniprotkb/Q14201) (Protein BTG3):

> Overexpression impairs serum-induced cell cycle progression from the G0/G1 to S phase.

**Summary**, from NCBI Gene [10950](https://www.ncbi.nlm.nih.gov/gene/10950):

> The protein encoded by this gene is a member of the BTG/Tob family. This family has structurally related proteins that appear to have antiproliferative properties. This encoded protein might play a role in neurogenesis in the central nervous system. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2008]

**Accessions** — [HGNC:1132](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1132) · Entrez [10950](https://www.ncbi.nlm.nih.gov/gene/10950) · UniProt [Q14201](https://www.uniprot.org/uniprotkb/Q14201) · Ensembl [ENSG00000154640](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154640)

## Data

Gene col 7821: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7821); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7821, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7821]; `tensor/DDL_lfc|DDL_z.npy` [7821]; `embed/gene_vectors.npy` [7821]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7821 or target_col == 7821). Every well: [[BTG3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTG3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
