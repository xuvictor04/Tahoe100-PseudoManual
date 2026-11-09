---
symbol: "SLC4A5"
type: "gene"
col: 12039
ensembl_id: "ENSG00000188687"
name: "solute carrier family 4 member 5"
location: "2p13.1"
module: 39
arm: "+"
pooled_cpm: 19.25
n_lines_expressing: 48
n_dd_up: 17
n_dd_down: 16
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# SLC4A5

*solute carrier family 4 member 5* — 2p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.47× (z +5.4, q 3e-05, up in 29 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.353× (z -10.3, q 6e-22, down in 31 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.387× (z -4.9, q 8e-05, down in 24 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLN]] (+0.64, fdr 8e-06), [[FRZB]] (+0.62, fdr 7e-06), [[TMEM236]] (+0.61, fdr 7e-06); moves opposite to [[TTC8]] (-0.50, fdr 1e-04), [[TMEM237]] (-0.48, fdr 3e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC26A4]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LINC02936]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12039.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +5.4 | 3e-05 | 29/46 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +5.3 | 3e-05 | 25/46 (SHP-77, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.66×** | +5.0 | 1e-04 | 25/46 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +4.5 | 1e-03 | 27/45 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +4.4 | 1e-03 | 23/46 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +4.4 | 1e-03 | 23/45 (KATO III, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.33×** | +4.4 | 1e-03 | 28/45 (SK-MEL-2, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.54×** | +4.1 | 0.003 | 22/45 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.003 | 21/46 (SW1417, NCI-H2347, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.47×** | +3.6 | 0.015 | 18/45 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.027 | 16/45 (HOP62, LS 180, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.032 | 18/45 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.92×** | +3.4 | 0.032 | 14/46 (HOP62, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.43×** | +3.3 | 0.034 | 15/46 (HEC-1-A, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.39×** | +3.3 | 0.043 | 12/46 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.053 | 12/45 (HOP62, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.058 | 11/46 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12039.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.353×** | -10.3 | 6e-22 | 31/44 (HOP62, J82, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.418×** | -8.6 | 2e-15 | 33/46 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.487×** | -7.1 | 2e-10 | 34/45 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.508×** | -6.4 | 2e-08 | 26/40 (LOX-IMVI, C-33 A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.533×** | -6.0 | 3e-07 | 23/42 (NCI-H1792, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.594×** | -4.9 | 7e-05 | 25/45 (H4, HOP62, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.387×** | -4.9 | 8e-05 | 24/46 (HOP62, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.611×** | -4.9 | 8e-05 | 23/45 (H4, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.612×** | -4.8 | 8e-05 | 27/45 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.450×** | -4.1 | 0.002 | 22/43 (Panc 03.27, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.464×** | -4.0 | 0.004 | 22/42 (C32, RKO, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.708×** | -3.4 | 0.032 | 16/45 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.717×** | -3.3 | 0.043 | 18/46 (NCI-H2030, NCI-H1792, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.628×** | -3.3 | 0.043 | 12/46 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.793×** | -3.2 | 0.045 | 20/46 (SNU-1, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12039. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 55.1 | 0 | 8 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.114× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0820× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 21.4 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.101× (z -11.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 32.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 51.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.107× (z -8.7) |
| [[A549 (line)]] | wt | 34.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -14.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.211× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 19.1 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0413× (z -16.3) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[NCI-H23 (line)]] | alt | 47.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 28.3 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0916× (z -10.3) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.113× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 35.4 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.219× (z -8.9) ⚠ toxic |
| [[SW480 (line)]] | alt | 16.5 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.255× (z -9.4) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A498 (line)]] | wt | 5.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.41× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.163× (z -10.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[C-33 A (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.129× (z -8.6) ⚠ toxic |
| [[HCT15 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0901× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[HEC-1-A (line)]] | alt | 33.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.115× (z -8.6) ⚠ transcription drop; unreliable plate only |
| [[J82 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0592× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 9.40 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 13.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.223× (z -8.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[Panc 03.27 (line)]] | alt | 15.5 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0306× (z -9.6) |
| [[RKO (line)]] | wt | 6.82 | 0 | 1 | — | [[Fluvoxamine (drug)]] 5 µM 0.0733× (z -8.5) |
| [[SNU-423 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[AN3 CA (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.05 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12039), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLN]] | +0.64 | +0.71 / +0.58 | both halves | 8e-06 |  |
| [[FRZB]] | +0.62 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[TMEM236]] | +0.61 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[SCUBE2]] | +0.60 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[SLC22A14]] | +0.59 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[SLC23A3]] | +0.59 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[HSD17B3]] | +0.58 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[SLC26A4]] | +0.57 | +0.67 / +0.53 | both halves | 1e-05 | pathway: SLC-mediated transmembrane transport; STRING 475 |
| [[ANKDD1B]] | +0.57 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[FLACC1]] | +0.57 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[ALDH8A1]] | +0.57 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[ADAM32]] | +0.56 | +0.54 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC8]] | -0.50 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[TMEM237]] | -0.48 | -0.44 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC26A4]] | B | SLC26A4 activity raises SLC4A5's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.71× lower at baseline in the lines without SLC26A4 | 0.008 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[IMPG2]] | C | IMPG2 activity raises SLC4A5's level | lines that do not express IMPG2 (4) vs lines expressing it (46) | 2.93× lower at baseline in the lines without IMPG2 | 0.083 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HECTD2, CLEC2D, LINC01341; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02936]] | C | SLC4A5's natural level weakens LINC02936's drug response | SLC4A5's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.69, reverse +0.21; direction not clear | 0.022 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.549). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.7, -15.3); signed map (15.6, 6.6). **Vector** length 82.7, 19.1% of its response variance represented; |z| ≥ 3 in 1,025 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.6 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.4 | -0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.1 | -1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | -0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +2.9 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.1 | +1.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.6 | -6.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.8 | -3.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.7 | -4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -2.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.5 | -2.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -1.8 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.2 | -0.5 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -2.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 4 member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.1 — chr2:74,216,242-74,343,416 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NBC4 |
| Gene groups (HGNC) | Solute carrier family 4 |
| Reactome | 4 pathways, smallest: Bicarbonate transporters; SLC-mediated transport of inorganic anions; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BY07](https://www.uniprot.org/uniprotkb/Q9BY07) (Electrogenic sodium bicarbonate cotransporter 4):

> Mediates sodium- and bicarbonate-dependent electrogenic sodium bicarbonate cotransport, with a Na(+):HCO3(-) stoichiometry varying from 1:2 to 1:3.

**Summary**, from NCBI Gene [57835](https://www.ncbi.nlm.nih.gov/gene/57835):

> This gene encodes a member of the sodium bicarbonate cotransporter (NBC) family, part of the bicarbonate transporter superfamily. Sodium bicarbonate cotransporters are involved in intracellular pH regulation and electroneural or electrogenic sodium bicarbonate transport. This protein is thought to be an integral membrane protein. Multiple transcript variants encoding different isoforms have been found for this gene, but the biological validity of some variants has not been determined. [provided …

**Accessions** — [HGNC:18168](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18168) · Entrez [57835](https://www.ncbi.nlm.nih.gov/gene/57835) · UniProt [Q9BY07](https://www.uniprot.org/uniprotkb/Q9BY07) · Ensembl [ENSG00000188687](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188687)

## Data

Gene col 12039: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12039); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12039, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12039]; `tensor/DDL_lfc|DDL_z.npy` [12039]; `embed/gene_vectors.npy` [12039]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12039 or target_col == 12039). Every well: [[SLC4A5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC4A5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
