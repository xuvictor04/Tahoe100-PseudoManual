---
symbol: "PPT1"
type: "gene"
col: 5188
ensembl_id: "ENSG00000131238"
name: "palmitoyl-protein thioesterase 1"
location: "1p34.2"
module: 29
arm: "+"
pooled_cpm: 27.97
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# PPT1

*palmitoyl-protein thioesterase 1* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.81× (z +18.1, q 0e+00, up in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.49× (z +6.9, q 6e-10, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.454× (z -19.6, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRTAP]] (+0.82, fdr 7e-06), [[FUCA2]] (+0.82, fdr 7e-06), [[CIPC]] (+0.80, fdr 7e-06); moves opposite to [[WASHC1]] (-0.74, fdr 7e-06), [[FBXL6]] (-0.70, fdr 7e-06), [[NSRP1]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LGALS3BP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5188.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.81×** | +18.1 | 0e+00 | 41/44 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.78×** | +17.2 | 0e+00 | 34/37 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.24×** | +13.1 | 6e-37 | 39/42 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +6.9 | 6e-10 | 31/48 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +6.7 | 2e-09 | 31/48 (C32, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +6.5 | 8e-09 | 29/48 (NCI-H460, PANC-1, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +5.3 | 1e-05 | 26/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +5.0 | 4e-05 | 1/48 (MIA PaCa-2) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +4.7 | 1e-04 | 23/45 (RPMI-7951, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.29×** | +4.5 | 3e-04 | 20/48 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **1.29×** | +4.3 | 1e-03 | 20/45 (NCI-H2030, KATO III, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.3 | 1e-03 | 17/48 (A-172, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.26×** | +4.1 | 0.002 | 22/48 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.0 | 0.002 | 11/30 (A-172, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.24×** | +3.8 | 0.005 | 17/46 (PANC-1, NCI-H1573, …) | two highest doses |  |
| [[Lopinavir (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.032 | 11/47 (A-427, CFPAC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.037 | 7/48 (RKO, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.047 | 7/48 (SW480, SW 900, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.064 | 9/48 (HepG2/C3A, HEC-1-A, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5188.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.454×** | -19.6 | 0e+00 | 43/47 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.495×** | -11.9 | 5e-30 | 43/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.536×** | -10.9 | 1e-25 | 36/47 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.727×** | -5.4 | 1e-05 | 26/47 (PANC-1, J82, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.770×** | -4.6 | 5e-04 | 26/48 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.796×** | -4.0 | 0.006 | 16/48 (SNU-1, H4, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.683×** | -3.5 | 0.037 | 14/46 (HT-29, C32, …) | top dose only | noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.741×** | -3.4 | 0.047 | 10/48 (SHP-77, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.695×** | -3.3 | 0.052 | 11/46 (A-427, HCT15, …) | rises with dose | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.764× | -3.1 | 0.12 | 16/45 (H4, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5188. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 43.9 | 4 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.88× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -16.7) |
| [[MIA PaCa-2 (line)]] | alt | 29.8 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -15.7) |
| [[HOP62 (line)]] | alt | 30.1 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -20.2) |
| [[KATO III (line)]] | alt | 18.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.46× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.94× (z +9.4) | — |
| [[A498 (line)]] | wt | 24.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.79× (z +11.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -14.5) |
| [[C32 (line)]] | wt | 22.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.55× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 25.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -11.1) |
| [[HS-578T (line)]] | alt | 30.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.80× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -12.7) |
| [[LoVo (line)]] | wt | 15.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 29.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.46× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 39.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.19× (z +12.8) ⚠ toxic; transcription drop | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.168× (z -8.7) ⚠ toxic |
| [[SW480 (line)]] | alt | 25.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -14.2) |
| [[A549 (line)]] | wt | 16.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.84× (z +11.3) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 25.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 19.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.08× (z +11.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 19.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 36.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 41.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -19.6) |
| [[RKO (line)]] | wt | 34.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.264× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 30.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.0) |
| [[A-172 (line)]] | wt | 18.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.80× (z +8.8) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 29.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -9.0) |
| [[COLO 205 (line)]] | alt | 20.0 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.148× (z -11.0) |
| [[HCT15 (line)]] | alt | 32.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 22.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -9.5) |
| [[HT-29 (line)]] | alt | 28.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +9.4) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 22.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -9.7) |
| [[J82 (line)]] | alt | 42.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 20.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.1× (z +14.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 22.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -8.5) |
| [[SNU-1 (line)]] | wt | 50.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -12.3) |
| [[SW48 (line)]] | wt | 34.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -9.5) |
| [[A-427 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5188), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRTAP]] | +0.82 | +0.84 / +0.75 | both halves | 7e-06 |  |
| [[FUCA2]] | +0.82 | +0.79 / +0.83 | both halves | 7e-06 |  |
| [[CIPC]] | +0.80 | +0.81 / +0.78 | both halves | 7e-06 |  |
| [[PRDX3]] | +0.79 | +0.75 / +0.80 | both halves | 7e-06 |  |
| [[TMX1]] | +0.78 | +0.75 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION |
| [[FKBP9]] | +0.77 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[LAMP1]] | +0.74 | +0.63 / +0.75 | both halves | 7e-06 | STRING 449 |
| [[EMC1]] | +0.73 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[SELENON]] | +0.73 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[RPSA]] | +0.73 | +0.61 / +0.80 | both halves | 7e-06 |  |
| [[LAPTM4B]] | +0.72 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[ERMP1]] | +0.72 | +0.64 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASHC1]] | -0.74 | -0.72 / -0.74 | both halves | 7e-06 |  |
| [[FBXL6]] | -0.70 | -0.65 / -0.66 | both halves | 7e-06 |  |
| [[NSRP1]] | -0.69 | -0.72 / -0.64 | both halves | 7e-06 |  |
| [[CCDC174]] | -0.68 | -0.68 / -0.67 | both halves | 7e-06 |  |
| [[ATF4]] | -0.68 | -0.65 / -0.69 | both halves | 7e-06 |  |
| [[ZNF503]] | -0.68 | -0.69 / -0.62 | both halves | 7e-06 |  |
| [[OFD1]] | -0.67 | -0.68 / -0.67 | both halves | 7e-06 |  |
| [[NKAP]] | -0.65 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[MED19]] | -0.65 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[ZMYM5]] | -0.65 | -0.65 / -0.65 | both halves | 7e-06 |  |
| [[CROCCP2-1]] | -0.65 | -0.64 / -0.68 | both halves | 7e-06 |  |
| [[FRG1]] | -0.64 | -0.66 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LGALS3BP]] | B | LGALS3BP activity lowers PPT1's level | lines that do not express LGALS3BP (7) vs lines expressing it (43) | 1.49× higher at baseline in the lines without LGALS3BP | 0.041 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[RAP2B]] | C | RAP2B activity lowers PPT1's level | lines that do not express RAP2B (3) vs lines expressing it (47) | 1.80× higher at baseline in the lines without RAP2B | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, SPRY4-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.884). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.9, -22.2); signed map (-22.7, -38.7). **Vector** length 119, 31.0% of its response variance represented; |z| ≥ 3 in 912 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.7 | +13.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +17.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +18.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.1 | +6.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +5.2 | +6.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.0 | +2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.6 | +2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -10.4 | -19.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.3 | -11.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.1 | -10.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.7 | -4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.2 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -4.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -3.0 | -3.4 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -2.7 | -2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.7 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | palmitoyl-protein thioesterase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:40,072,710-40,097,260 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CLN1, INCL; previously PPT |
| Gene groups (HGNC) | Depalmitoylases; Thioester hydrolases |
| Hallmark sets | PROTEIN_SECRETION, APOPTOSIS, UV_RESPONSE_UP |
| Reactome | 3 pathways, smallest: Fatty acyl-CoA biosynthesis; Fatty acid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [P50897](https://www.uniprot.org/uniprotkb/P50897) (Palmitoyl-protein thioesterase 1):

> Has thioesterase activity against fatty acid thioesters with 14 -18 carbons, including palmitoyl-CoA, S-palmitoyl-N-acetylcysteamine, and palmitoylated proteins. In contrast to PPT2, PPT1 can hydrolyze palmitoylated proteins and palmitoylcysteine.

**Summary**, from NCBI Gene [5538](https://www.ncbi.nlm.nih.gov/gene/5538):

> The protein encoded by this gene is a small glycoprotein involved in the catabolism of lipid-modified proteins during lysosomal degradation. The encoded enzyme removes thioester-linked fatty acyl groups such as palmitate from cysteine residues. Defects in this gene are a cause of infantile neuronal ceroid lipofuscinosis 1 (CLN1, or INCL) and neuronal ceroid lipofuscinosis 4 (CLN4). Two transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Dec 2008]

**Accessions** — [HGNC:9325](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9325) · Entrez [5538](https://www.ncbi.nlm.nih.gov/gene/5538) · UniProt [P50897](https://www.uniprot.org/uniprotkb/P50897) · Ensembl [ENSG00000131238](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131238)

## Data

Gene col 5188: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5188); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5188, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5188]; `tensor/DDL_lfc|DDL_z.npy` [5188]; `embed/gene_vectors.npy` [5188]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5188 or target_col == 5188). Every well: [[PPT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
