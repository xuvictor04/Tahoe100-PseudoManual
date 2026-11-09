---
symbol: "PCGF2"
type: "gene"
col: 15889
ensembl_id: "ENSG00000277258"
name: "polycomb group ring finger 2"
location: "17q12"
module: 126
arm: "+"
pooled_cpm: 22.07
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# PCGF2

*polycomb group ring finger 2* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.25× (z +5.8, q 3e-06, up in 24 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.506× (z -17.8, q 0e+00, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKT1]] (+0.64, fdr 7e-06), [[CACNB3]] (+0.62, fdr 1e-05), [[BCL2L2]] (+0.60, fdr 1e-05); moves opposite to [[MRFAP1]] (-0.54, fdr 1e-05), [[ING3]] (-0.52, fdr 3e-05), [[PSMB1]] (-0.51, fdr 8e-05).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15889.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.8 | 3e-06 | 24/48 (SW480, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.32×** | +5.1 | 7e-05 | 22/42 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.32×** | +5.1 | 7e-05 | 21/44 (HEC-1-A, BT-474, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +5.0 | 7e-05 | 16/31 (NCI-H1792, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.008 | 11/47 (HEC-1-A, HOP62, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.6 | 0.027 | 15/48 (A-427, SW1417, …) | top dose only | position effect removed |
| [[Dexmedetomidine (drug)]] 0.05 µM |  | **1.23×** | +3.6 | 0.027 | 5/47 (NCI-H2347, BT-474, …) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.027 | 15/46 (RKO, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | 1.13× | +3.1 | 0.10 | 3/48 (HEC-1-A, J82, …) | top dose only |  |
| [[Pentoxifylline (drug)]] 5 µM |  | 1.18× | +3.1 | 0.10 | 0/48 | rises with dose | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.38× | +3.1 | 0.10 | 7/35 (MIA PaCa-2, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.10 | 8/48 (A-172, A549, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.12× | +3.0 | 0.12 | 3/48 (BT-474, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15889.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.506×** | -17.8 | 0e+00 | 38/47 (BT-474, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.451×** | -14.7 | 0e+00 | 39/47 (NCI-H1573, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.506×** | -12.6 | 4e-34 | 43/48 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.565×** | -10.6 | 6e-24 | 40/48 (BT-474, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.568×** | -10.0 | 1e-21 | 35/48 (HOP62, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.661×** | -7.7 | 2e-12 | 31/47 (BT-474, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.706×** | -6.4 | 9e-09 | 27/47 (AN3 CA, C32, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.757×** | -5.2 | 2e-05 | 20/47 (HEC-1-A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.748×** | -5.1 | 2e-05 | 22/48 (HT-29, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.777×** | -4.7 | 2e-04 | 19/48 (SNU-1, SW48, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.794×** | -4.3 | 0.001 | 16/47 (AN3 CA, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.815×** | -3.8 | 0.008 | 14/47 (SW48, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.840× | -3.2 | 0.055 | 12/47 (BT-474, SW48, …) | all doses, flat | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.732× | -3.0 | 0.10 | 11/48 (SK-MEL-2, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15889. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 156 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -16.5) |
| [[NCI-H1573 (line)]] | alt | 16.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -11.9) |
| [[A-172 (line)]] | wt | 26.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -11.8) |
| [[AN3 CA (line)]] | alt | 39.9 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.0900× (z -10.7) |
| [[HOP62 (line)]] | alt | 18.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 23.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.210× (z -11.4) |
| [[RKO (line)]] | wt | 23.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -9.7) |
| [[SW480 (line)]] | alt | 14.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -9.1) |
| [[A549 (line)]] | wt | 22.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -9.4) |
| [[C-33 A (line)]] | alt | 33.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.163× (z -11.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 29.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -9.1) |
| [[CHP-212 (line)]] | wt | 42.9 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.120× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 15.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.174× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 26.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.363× (z -8.9) |
| [[Hs 766T (line)]] | wt | 21.8 | 0 | 1 (1 ⚠) | — | [[Elimusertib hydrochloride (drug)]] 5 µM 0.0792× (z -8.5) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 19.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -11.6) |
| [[J82 (line)]] | alt | 19.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -12.7) |
| [[KATO III (line)]] | alt | 20.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -10.3) |
| [[LS 180 (line)]] | wt | 13.1 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0861× (z -9.9) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 26.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -8.9) |
| [[SHP-77 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.138× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[SK-MEL-2 (line)]] | alt | 38.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -11.3) |
| [[SNU-1 (line)]] | wt | 26.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0679× (z -13.8) |
| [[SW48 (line)]] | wt | 20.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -9.4) |
| [[A-427 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15889), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKT1]] | +0.64 | +0.65 / +0.63 | both halves | 7e-06 | STRING 496 |
| [[CACNB3]] | +0.62 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[BCL2L2]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[SEC61A2]] | +0.60 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[GRK2]] | +0.59 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[INPPL1]] | +0.57 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[UBTD1]] | +0.57 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[METTL9]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[DHRS11]] | +0.56 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[LLGL1]] | +0.55 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[SMARCD2]] | +0.55 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[EML3]] | +0.55 | +0.60 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRFAP1]] | -0.54 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[ING3]] | -0.52 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[PSMB1]] | -0.51 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[AGGF1]] | -0.49 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[LARP7]] | -0.49 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[WDR70]] | -0.49 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[SEC62]] | -0.49 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[GOLGB1]] | -0.48 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[ZMYM1]] | -0.48 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[SMIM30]] | -0.47 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[PSMA7]] | -0.47 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[MRFAP1L1]] | -0.47 | -0.52 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PCGF2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises PCGF2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[KLHL9]] | C | KLHL9 activity strengthens PCGF2's drug response | lines that do not express KLHL9 (3) vs lines expressing it (45) | the lines without KLHL9 respond 0.43× as strongly (z diff +1.59); strongest at Homoharringtonine 5 µM: 0.80x vs 0.49x (z diff +5.7) | 0.089 | ⚠ few lines (3 vs 47); across organs; also absent: MTAP, TMEM117, CFL1P1-1; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.594). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.4, -20.3); signed map (-49.1, -11.2). **Vector** length 85.4, 16.8% of its response variance represented; |z| ≥ 3 in 893 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +5.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +3.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +0.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.6 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.0 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | +1.6 | +1.7 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.6 | +0.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.5 | -1.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.5 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.8 | -14.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -17.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -10.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -4.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.6 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | polycomb group ring finger 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:38,733,898-38,749,817 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MEL-18; previously ZNF144, RNF110 |
| Gene groups (HGNC) | Ring finger proteins; Polycomb group ring fingers |
| Reactome | 10 pathways, smallest: SUMOylation of DNA methylation proteins; Transcriptional Regulation by E2F6; SUMOylation of transcription cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [P35227](https://www.uniprot.org/uniprotkb/P35227) (Polycomb group RING finger protein 2):

> Transcriptional repressor. Binds specifically to the DNA sequence 5'-GACTNGACT-3'. Has tumor suppressor activity. May play a role in control of cell proliferation and/or neural cell development. Regulates proliferation of early T progenitor cells by maintaining expression of HES1. Also plays a role in antero-posterior specification of the axial skeleton and negative regulation of the self-renewal activity of hematopoietic stem cells (By similarity). Component of a Polycomb group (PcG) …

**Summary**, from NCBI Gene [7703](https://www.ncbi.nlm.nih.gov/gene/7703):

> The protein encoded by this gene contains a RING finger motif and is similar to the polycomb group (PcG) gene products. PcG gene products form complexes via protein-protein interaction and maintain the transcription repression of genes involved in embryogenesis, cell cycles, and tumorigenesis. This protein was shown to act as a negative regulator of transcription and has tumor suppressor activity. The expression of this gene was detected in various tumor cells, but is limited in neural organs …

**Accessions** — [HGNC:12929](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12929) · Entrez [7703](https://www.ncbi.nlm.nih.gov/gene/7703) · UniProt [P35227](https://www.uniprot.org/uniprotkb/P35227) · Ensembl [ENSG00000277258](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000277258)

## Data

Gene col 15889: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15889); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15889, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15889]; `tensor/DDL_lfc|DDL_z.npy` [15889]; `embed/gene_vectors.npy` [15889]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15889 or target_col == 15889). Every well: [[PCGF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCGF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
