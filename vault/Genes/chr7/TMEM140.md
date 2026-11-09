---
symbol: "TMEM140"
type: "gene"
col: 7129
ensembl_id: "ENSG00000146859"
name: "transmembrane protein 140"
location: "7q33"
module: 32
arm: "+"
pooled_cpm: 8.4
n_lines_expressing: 42
n_dd_up: 33
n_dd_down: 22
n_dd_up_clean: 30
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 67
direction_downstream: 26
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# TMEM140

*transmembrane protein 140* — 7q33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (3 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 2.77× (z +9.2, q 3e-17, up in 32 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.340× (z -10.1, q 5e-21, down in 30 of 39 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Tofacitinib (drug)]] 5 µM: 0.532× (z -8.3, q 2e-14, down in 23 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM22]] (+0.86, fdr 7e-06), [[TRANK1]] (+0.86, fdr 7e-06), [[RSAD2]] (+0.86, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 67 arrows point to it, the strongest [[SLC15A3]] → it (grade B ⚠); 26 go from it, the strongest it → [[IFIT3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 3 with an alert ⚠; shown: the 15 strongest. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7129.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **2.77×** | +9.2 | 3e-17 | 32/35 (A498, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.86×** | +6.9 | 1e-09 | 28/39 (CFPAC-1, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **2.08×** | +6.6 | 1e-08 | 27/37 (C32, HepG2/C3A, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.65×** | +6.5 | 1e-08 | 23/38 (AsPC-1, C32, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **1.97×** | +6.5 | 1e-08 | 26/39 (AsPC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.95×** | +6.2 | 4e-08 | 27/38 (SK-MEL-2, A549, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.93×** | +6.2 | 6e-08 | 24/38 (C32, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.95×** | +5.8 | 6e-07 | 25/38 (C32, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.84×** | +5.7 | 1e-06 | 23/40 (CFPAC-1, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.81×** | +5.5 | 2e-06 | 25/38 (NCI-H2347, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.52×** | +5.0 | 4e-05 | 22/39 (C32, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.47×** | +4.9 | 4e-05 | 21/39 (CFPAC-1, COLO 205, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.44×** | +4.8 | 6e-05 | 17/40 (KATO III, HS-578T, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.71×** | +4.7 | 1e-04 | 18/37 (CFPAC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **2.61×** | +4.7 | 1e-04 | 19/38 (AsPC-1, C32, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7129.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.340×** | -10.1 | 5e-21 | 30/39 (HS-578T, COLO 205, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.532×** | -8.3 | 2e-14 | 23/38 (LoVo, BT-474, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.420×** | -8.1 | 1e-13 | 28/38 (NCI-H1792, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.563×** | -7.6 | 5e-12 | 28/38 (LoVo, COLO 205, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.513×** | -6.2 | 6e-08 | 25/38 (SNU-423, SW 900, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.515×** | -6.2 | 6e-08 | 21/38 (BT-474, KATO III, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.541×** | -5.7 | 9e-07 | 24/39 (HS-578T, BT-474, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.549×** | -5.6 | 2e-06 | 22/38 (LoVo, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.661×** | -5.5 | 3e-06 | 19/39 (SNU-423, COLO 205, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.567×** | -5.3 | 7e-06 | 20/38 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.578×** | -5.1 | 2e-05 | 22/34 (LoVo, COLO 205, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.583×** | -5.0 | 2e-05 | 20/38 (SHP-77, COLO 205, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.673×** | -3.5 | 0.017 | 11/37 (LoVo, CFPAC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.690×** | -3.5 | 0.023 | 15/37 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.686×** | -3.4 | 0.028 | 8/37 (BT-474, AsPC-1, …) | top dose only |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.524×** | -3.2 | 0.053 | 12/32 (RPMI-7951, LoVo, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.713×** | -3.1 | 0.053 | 14/37 (RPMI-7951, LoVo, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.714×** | -3.1 | 0.053 | 10/33 (HS-578T, CFPAC-1, …) | two highest doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.530×** | -3.1 | 0.057 | 9/34 (Hs 766T, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.542×** | -3.0 | 0.072 | 13/36 (LoVo, A549, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.53 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7129. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 31.1 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0482× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.174× (z -10.5) |
| [[LoVo (line)]] | wt | 12.1 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0443× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.170× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 26.9 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0134× (z -20.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 24.0 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -14.2) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 13.0 | 0 | 3 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.118× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 17.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0682× (z -17.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.184× (z -11.0) |
| [[A549 (line)]] | wt | 10.6 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0564× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~70% of this change |
| [[HS-578T (line)]] | alt | 9.29 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0494× (z -12.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SK-MEL-2 (line)]] | alt | 21.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -13.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 20.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 14.5 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.179× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 33.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 8.36 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0489× (z -10.4) ⚠ cell-cycle shift, explains ~65% of this change |
| [[A-172 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7129), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM22]] | +0.86 | +0.79 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[TRANK1]] | +0.86 | +0.80 / +0.86 | both halves | 7e-06 | STRING 400 |
| [[RSAD2]] | +0.86 | +0.81 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFI35]] | +0.85 | +0.78 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[XAF1]] | +0.85 | +0.76 / +0.88 | both halves | 7e-06 |  |
| [[IFIT3]] | +0.85 | +0.78 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[SLC15A3]] | +0.85 | +0.71 / +0.87 | both halves | 7e-06 |  |
| [[EPSTI1]] | +0.84 | +0.74 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFIT1]] | +0.84 | +0.78 / +0.85 | both halves | 7e-06 |  |
| [[MX1]] | +0.83 | +0.74 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[OAS1]] | +0.83 | +0.77 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[SAMD9L]] | +0.83 | +0.71 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*67 arrows, 67 of them with an alert ⚠; grade A 0, B 55, C 12. Shown: the 12 strongest; 55 more arrows (55 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC15A3]] | B | SLC15A3 activity raises TMEM140's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 3.05× lower at baseline in the lines without SLC15A3 | 0.001 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |
| [[OAS1]] | B | OAS1 activity raises TMEM140's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.73× lower at baseline in the lines without OAS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[BST2]] | B | BST2 activity raises TMEM140's level | lines that do not express BST2 (18) vs lines expressing it (32) | 2.84× lower at baseline in the lines without BST2 | 0.001 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[DUOX2]] | B | DUOX2 activity raises TMEM140's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 2.25× lower at baseline in the lines without DUOX2 | 0.002 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |
| [[MMP13]] | B | MMP13 activity raises TMEM140's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 1.87× lower at baseline in the lines without MMP13 | 0.004 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[IFI27]] | B | IFI27 activity raises TMEM140's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 2.16× lower at baseline in the lines without IFI27 | 0.005 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[RASGRP3]] | B | RASGRP3 activity raises TMEM140's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 2.69× lower at baseline in the lines without RASGRP3 | 0.006 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[SAMD9L]] | B | SAMD9L activity raises TMEM140's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 2.19× lower at baseline in the lines without SAMD9L | 0.006 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[APOL1]] | B | APOL1 activity raises TMEM140's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 2.42× lower at baseline in the lines without APOL1 | 0.007 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[GBP4]] | B | GBP4 activity raises TMEM140's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.38× lower at baseline in the lines without GBP4 | 0.007 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[XAF1]] | B | XAF1 activity raises TMEM140's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 2.63× lower at baseline in the lines without XAF1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |
| [[TRIM22]] | B | TRIM22 activity raises TMEM140's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.47× lower at baseline in the lines without TRIM22 | 0.009 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 26, C 0. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFIT3]] | B | TMEM140 activity raises IFIT3's level | lines that do not express TMEM140 (8) vs lines expressing it (42) | 3.47× lower at baseline in the lines without TMEM140 | 0.022 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NCOA7]] | B | TMEM140 activity raises NCOA7's level | lines that do not express TMEM140 (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without TMEM140 | 0.027 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MYD88]] | B | TMEM140 activity raises MYD88's level | lines that do not express TMEM140 (8) vs lines expressing it (42) | 1.70× lower at baseline in the lines without TMEM140 | 0.030 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[OAS1]] | B | TMEM140 activity raises OAS1's level | lines that do not express TMEM140 (8) vs lines expressing it (42) | 3.26× lower at baseline in the lines without TMEM140 | 0.030 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SAMD9]] | B | TMEM140 activity raises SAMD9's level | lines that do not express TMEM140 (8) vs lines expressing it (42) | 3.89× lower at baseline in the lines without TMEM140 | 0.040 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MX2]] | B | TMEM140 activity raises MX2's level | lines that do not express TMEM140 (8) vs lines expressing it (42) | 5.78× lower at baseline in the lines without TMEM140 | 0.041 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NUB1]] | B | TMEM140 activity raises NUB1's level | lines that do not express TMEM140 (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without TMEM140 | 0.042 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[OAS2]] | B | TMEM140 activity raises OAS2's level | lines that do not express TMEM140 (8) vs lines expressing it (42) | 4.45× lower at baseline in the lines without TMEM140 | 0.043 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[IFI44]] | B | TMEM140 activity raises IFI44's level | lines that do not express TMEM140 (8) vs lines expressing it (42) | 3.48× lower at baseline in the lines without TMEM140 | 0.045 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SAMHD1]] | B | TMEM140 activity raises SAMHD1's level | lines that do not express TMEM140 (8) vs lines expressing it (42) | 2.05× lower at baseline in the lines without TMEM140 | 0.053 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PML]] | B | TMEM140 activity raises PML's level | lines that do not express TMEM140 (8) vs lines expressing it (42) | 2.08× lower at baseline in the lines without TMEM140 | 0.054 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NAPA]] | B | TMEM140 activity raises NAPA's level | lines that do not express TMEM140 (8) vs lines expressing it (42) | 1.48× lower at baseline in the lines without TMEM140 | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.869). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.2, 53.0); signed map (63.2, 31.0). **Vector** length 116, 32.5% of its response variance represented; |z| ≥ 3 in 1,155 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.73 to 60); *interferon* (control, mean cos +0.78 to 23); *Interferon Signaling* (reactome, mean cos +0.74 to 45).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cobimetinib (drug)]] 5 µM |  | +5.6 | +9.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.8 | +6.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.7 | +6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.6 | +2.8 |
|  | [[Trametinib (drug)]] 5 µM |  | +4.2 | +6.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.0 | +5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.0 | +6.2 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -6.4 | -8.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -5.6 | -7.6 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -5.4 | -6.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.9 | -5.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.1 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 140 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q33 — chr7:135,148,072-135,166,215 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11000 |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE |
| Matched by | ensembl_id |

UniProt [Q9NV12](https://www.uniprot.org/uniprotkb/Q9NV12) carries no function annotation.

**Summary**, from NCBI Gene [55281](https://www.ncbi.nlm.nih.gov/gene/55281):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21870](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21870) · Entrez [55281](https://www.ncbi.nlm.nih.gov/gene/55281) · UniProt [Q9NV12](https://www.uniprot.org/uniprotkb/Q9NV12) · Ensembl [ENSG00000146859](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146859)

## Data

Gene col 7129: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7129); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7129, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7129]; `tensor/DDL_lfc|DDL_z.npy` [7129]; `embed/gene_vectors.npy` [7129]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7129 or target_col == 7129). Every well: [[TMEM140 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM140.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
