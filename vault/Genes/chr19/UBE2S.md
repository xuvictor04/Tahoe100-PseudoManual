---
symbol: "UBE2S"
type: "gene"
col: 2919
ensembl_id: "ENSG00000108106"
name: "ubiquitin conjugating enzyme E2 S"
location: "19q13.42"
module: 22
arm: "+"
pooled_cpm: 22.24
n_lines_expressing: 49
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# UBE2S

*ubiquitin conjugating enzyme E2 S* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.37× (z +11.8, q 2e-29, up in 35 of 46 measured lines) ⚠ cell-cycle shift, explains ~65% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.76× (z +9.8, q 2e-20, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.665× (z -5.7, q 8e-06, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACBD7]] (+0.71, fdr 7e-06), [[GPSM2]] (+0.70, fdr 7e-06), [[NEK2]] (+0.69, fdr 7e-06); moves opposite to [[NOPCHAP1]] (-0.51, fdr 4e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2919.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **2.37×** | +11.8 | 2e-29 | 35/46 (A498, HS-578T, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.76×** | +9.8 | 2e-20 | 42/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **2.34×** | +8.2 | 3e-14 | 37/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.32×** | +8.1 | 6e-14 | 39/47 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.17×** | +7.5 | 9e-12 | 32/47 (HEC-1-A, HT-29, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **2.14×** | +7.4 | 2e-11 | 32/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.01×** | +7.0 | 2e-10 | 42/47 (HEC-1-A, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.51×** | +6.5 | 7e-09 | 34/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **3.42×** | +6.2 | 3e-08 | 34/46 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.89×** | +5.9 | 2e-07 | 31/47 (NCI-H2030, Panc 03.27, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.89×** | +5.9 | 2e-07 | 24/33 (LoVo, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.84×** | +5.9 | 2e-07 | 32/45 (KATO III, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~65% of this change | **1.79×** | +5.6 | 7e-07 | 35/44 (PANC-1, HT-29, …) | all doses, flat | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.48×** | +3.8 | 0.006 | 17/47 (NCI-H460, H4, …) | all doses, stronger at high dose | position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.008 | 20/47 (NCI-H2347, RPMI-7951, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.028 | 16/47 (HT-29, SW 1271, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.034 | 15/47 (H4, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2919.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.665×** | -5.7 | 8e-06 | 31/46 (NCI-H23, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.594×** | -4.9 | 3e-04 | 26/45 (SW48, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.654×** | -4.0 | 0.011 | 25/45 (Hs 766T, PANC-1, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.764×** | -3.8 | 0.023 | 25/47 (H4, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.716× | -3.3 | 0.11 | 20/46 (SNU-1, H4, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.720× | -3.2 | 0.11 | 20/47 (A498, HCT15, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.723× | -3.2 | 0.11 | 14/46 (A549, A-427, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.738× | -3.0 | 0.19 | 16/47 (A-427, HCT15, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.77 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2919. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 11.8 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.02× (z +10.0) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.75× (z +8.7) | — |
| [[AsPC-1 (line)]] | alt | 10.4 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.28× (z +9.7) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[HEC-1-A (line)]] | alt | 22.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +9.9) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.27× (z +9.5) | — |
| [[KATO III (line)]] | alt | 14.0 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.43× (z +9.7) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[SW480 (line)]] | alt | 21.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.62× (z +9.4) | — |
| [[A-427 (line)]] | wt | 34.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.261× (z -12.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 30.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +12.1) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[AN3 CA (line)]] | alt | 33.8 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0540× (z -10.2) |
| [[C32 (line)]] | wt | 29.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +9.8) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[H4 (line)]] | wt | 48.4 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.201× (z -9.8) |
| [[Hs 766T (line)]] | wt | 9.73 | 0 | 1 | — | [[Saquinavir (drug)]] 5 µM 0.161× (z -9.6) |
| [[HS-578T (line)]] | alt | 19.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +11.6) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[HT-29 (line)]] | alt | 24.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.41× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 19.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +9.2) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[LoVo (line)]] | wt | 15.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +10.4) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[LOX-IMVI (line)]] | wt | 23.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +8.8) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[NCI-H1573 (line)]] | alt | 9.37 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +8.6) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.7× (z +10.2) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[NCI-H23 (line)]] | alt | 30.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 13.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +9.2) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[PANC-1 (line)]] | alt | 25.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -9.2) |
| [[SNU-1 (line)]] | wt | 33.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 18.6 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0996× (z -8.6) |
| [[A-172 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.20 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2919), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACBD7]] | +0.71 | +0.63 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[GPSM2]] | +0.70 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[NEK2]] | +0.69 | +0.67 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 703 |
| [[FAM83D]] | +0.68 | +0.79 / +0.65 | both halves | 7e-06 |  |
| [[H2AX]] | +0.67 | +0.59 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[KIF20A]] | +0.67 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[INCENP]] | +0.67 | +0.66 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[CDC20]] | +0.66 | +0.66 / +0.58 | both halves | 8e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[PSRC1]] | +0.66 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[CCNF]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[DLGAP5]] | +0.65 | +0.62 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[DEPDC1B]] | +0.64 | +0.65 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOPCHAP1]] | -0.51 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises UBE2S's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.15× lower at baseline in the lines without PIMREG | 0.013 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises UBE2S's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity raises UBE2S's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[NEURL1B]] | B | NEURL1B activity raises UBE2S's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.85× lower at baseline in the lines without NEURL1B | 0.085 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[PBK]] | C | PBK activity raises UBE2S's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.66× lower at baseline in the lines without PBK | 0.011 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises UBE2S's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.22× lower at baseline in the lines without AURKB | 0.032 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[CDC20]] | C | CDC20 activity raises UBE2S's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.72× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.634). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.8, -58.1); signed map (-50.9, -40.1). **Vector** length 107, 30.4% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.59 to 28); *Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal* (reactome, mean cos +0.51 to 28); *Amplification of signal from the kinetochores* (reactome, mean cos +0.51 to 28).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.8 | +9.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.1 | +6.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.6 | +8.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~65% of this change | +3.5 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +3.5 | +11.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +6.2 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.1 | +3.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -4.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | +0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | +1.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.1 | -2.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 S |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:55,399,745-55,407,788 (-) |
| Ensembl biotype | protein_coding |
| Also known as | E2-EPF |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 44 pathways, smallest: Aberrant regulation of mitotic exit in cancer due to RB1 defects; Conversion from APC/C:Cdc20 to APC/C:Cdh1 in late anaphase; Phosphorylation of the APC/C |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16763](https://www.uniprot.org/uniprotkb/Q16763) (Ubiquitin-conjugating enzyme E2 S):

> Accepts ubiquitin from the E1 complex and catalyzes its covalent attachment to other proteins. Catalyzes 'Lys-11'-linked polyubiquitination. Acts as an essential factor of the anaphase promoting complex/cyclosome (APC/C), a cell cycle-regulated ubiquitin ligase that controls progression through mitosis. Acts by specifically elongating 'Lys-11'-linked polyubiquitin chains initiated by the E2 enzyme UBE2C/UBCH10 on APC/C substrates, enhancing the degradation of APC/C substrates by the proteasome …

**Summary**, from NCBI Gene [27338](https://www.ncbi.nlm.nih.gov/gene/27338):

> This gene encodes a member of the ubiquitin-conjugating enzyme family. The encoded protein is able to form a thiol ester linkage with ubiquitin in a ubiquitin activating enzyme-dependent manner, a characteristic property of ubiquitin carrier proteins. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17895](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17895) · Entrez [27338](https://www.ncbi.nlm.nih.gov/gene/27338) · UniProt [Q16763](https://www.uniprot.org/uniprotkb/Q16763) · Ensembl [ENSG00000108106](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108106)

## Data

Gene col 2919: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2919); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2919, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2919]; `tensor/DDL_lfc|DDL_z.npy` [2919]; `embed/gene_vectors.npy` [2919]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2919 or target_col == 2919). Every well: [[UBE2S — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2S.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
