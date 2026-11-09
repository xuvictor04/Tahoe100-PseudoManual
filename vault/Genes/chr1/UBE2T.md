---
symbol: "UBE2T"
type: "gene"
col: 1176
ensembl_id: "ENSG00000077152"
name: "ubiquitin conjugating enzyme E2 T"
location: "1q32.1"
module: 67
arm: "+"
pooled_cpm: 14.39
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# UBE2T

*ubiquitin conjugating enzyme E2 T* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.37× (z +8.2, q 9e-14, up in 39 of 46 measured lines) ⚠ cell-cycle shift, explains ~68% of this change. The strongest without an alert is [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM: 1.42× (z +3.3, q 0.031, up in 14 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.517× (z -6.3, q 2e-07, down in 29 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEIL3]] (+0.89, fdr 7e-06), [[PBK]] (+0.87, fdr 7e-06), [[AURKB]] (+0.86, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 17 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1176.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **2.37×** | +8.2 | 9e-14 | 39/46 (A-172, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **2.20×** | +7.5 | 2e-11 | 35/46 (A549, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **2.18×** | +7.4 | 2e-11 | 38/46 (A549, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **2.05×** | +6.9 | 9e-10 | 28/37 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **2.04×** | +6.5 | 7e-09 | 17/24 (HT-29, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~70% of this change | **1.95×** | +6.1 | 8e-08 | 22/40 (C32, H4, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~84% of this change | **1.73×** | +5.2 | 1e-05 | 22/39 (CFPAC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.72×** | +5.2 | 2e-05 | 28/45 (C-33 A, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.71×** | +4.9 | 5e-05 | 22/41 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.44×** | +4.9 | 5e-05 | 29/47 (C32, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.62×** | +4.6 | 2e-04 | 25/46 (RKO, SW480, …) | all doses, stronger at high dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.47×** | +3.7 | 0.011 | 20/47 (A498, HOP62, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.47×** | +3.6 | 0.012 | 20/46 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.29×** | +3.4 | 0.028 | 15/47 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.42×** | +3.3 | 0.031 | 14/46 (NCI-H460, A-427, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.37×** | +3.0 | 0.072 | 16/47 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.40×** | +2.9 | 0.092 | 9/44 (SW 900, Panc 03.27, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1176.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.517×** | -6.3 | 2e-07 | 29/46 (SNU-1, RKO, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.707×** | -4.7 | 7e-04 | 28/47 (Hs 766T, H4, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.616×** | -4.6 | 7e-04 | 21/43 (A498, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.716×** | -4.5 | 9e-04 | 24/47 (NCI-H1792, Hs 766T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.726×** | -4.3 | 0.002 | 24/44 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.637×** | -4.1 | 0.003 | 20/45 (NCI-H23, C32, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.638×** | -4.0 | 0.004 | 25/47 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.656×** | -4.0 | 0.004 | 25/46 (A498, LS 180, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.667×** | -3.9 | 0.007 | 22/47 (COLO 205, A498, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **0.656×** | -3.8 | 0.008 | 23/45 (A-427, LS 180, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.756×** | -3.8 | 0.008 | 14/47 (SW 1271, A498, …) | rises with dose | position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | **0.457×** | -3.6 | 0.014 | 16/47 (SW480, SHP-77, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.502×** | -3.6 | 0.014 | 15/47 (A498, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.461×** | -3.6 | 0.014 | 16/47 (SW480, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.695×** | -3.5 | 0.019 | 17/46 (A-172, LS 180, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.89 per unit of S-phase module lfc, +0.67 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1176. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 22.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0364× (z -20.2) |
| [[H4 (line)]] | wt | 15.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0608× (z -9.8) |
| [[SNU-1 (line)]] | wt | 12.9 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0719× (z -9.3) |
| [[A-172 (line)]] | wt | 18.8 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.156× (z -9.4) ⚠ cell-cycle shift, explains ~85% of this change |
| [[A-427 (line)]] | wt | 28.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.350× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 4.23 | 0 | 1 | — | [[Resveratrol (drug)]] 0.05 µM 0.0682× (z -8.9) |
| [[Hs 766T (line)]] | wt | 13.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -9.8) |
| [[KATO III (line)]] | alt | 22.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -10.5) |
| [[LoVo (line)]] | wt | 8.14 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.223× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 5.24 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -10.6) |
| [[SW480 (line)]] | alt | 19.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -9.0) |
| [[A549 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1176), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEIL3]] | +0.89 | +0.89 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[PBK]] | +0.87 | +0.91 / +0.81 | both halves | 7e-06 | STRING 805 |
| [[AURKB]] | +0.86 | +0.88 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 435 |
| [[STIL]] | +0.86 | +0.82 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[SPC24]] | +0.85 | +0.82 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[BLM]] | +0.85 | +0.80 / +0.83 | both halves | 7e-06 | STRING 413 |
| [[NCAPH]] | +0.85 | +0.86 / +0.80 | both halves | 7e-06 | STRING 454 |
| [[CENPI]] | +0.85 | +0.85 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[SKA3]] | +0.84 | +0.86 / +0.84 | both halves | 7e-06 | STRING 533 |
| [[CIT]] | +0.84 | +0.86 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[POLQ]] | +0.83 | +0.85 / +0.81 | both halves | 7e-06 |  |
| [[BARD1]] | +0.83 | +0.80 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 655 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 4, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises UBE2T's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.34× lower at baseline in the lines without PIMREG | 0.007 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises UBE2T's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.30× lower at baseline in the lines without TCF19 | 0.008 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises UBE2T's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.15× lower at baseline in the lines without E2F8 | 0.024 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[NEURL1B]] | B | NEURL1B activity raises UBE2T's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.90× lower at baseline in the lines without NEURL1B | 0.090 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[DSCC1]] | C | DSCC1 activity raises UBE2T's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.29× lower at baseline in the lines without DSCC1 | 0.016 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises UBE2T's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.71× lower at baseline in the lines without AURKB | 0.020 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises UBE2T's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.35× lower at baseline in the lines without MCM10 | 0.027 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[PBK]] | C | PBK activity raises UBE2T's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.28× lower at baseline in the lines without PBK | 0.050 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[CENPM]], [[SKA3]] | C | CENPM, SKA3 activity raises UBE2T's level | lines that do not express CENPM, SKA3 (3) vs lines expressing them (47) | 2.81× lower at baseline in the lines without CENPM, SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.892). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-33.4, -52.1); signed map (-44.7, -40.2). **Vector** length 114, 34.0% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.78 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.76 to 8); *Deposition of new CENPA-containing nucleosomes at the centromere* (reactome, mean cos +0.76 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +5.1 | +7.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | +4.3 | +7.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +4.0 | +8.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | +3.8 | +4.6 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | +3.1 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.1 | +3.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.1 | +2.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.0 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.4 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.2 | -4.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.5 | -4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | -4.0 | -3.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.9 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -0.8 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -2.5 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 T |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:202,331,544-202,341,984 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC150, FANCT |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2; FA complementation groups |
| Hallmark sets | E2F_TARGETS |
| Reactome | 4 pathways, smallest: Synthesis of active ubiquitin: roles of E1 and E2 enzymes; Fanconi Anemia Pathway; Protein ubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPD8](https://www.uniprot.org/uniprotkb/Q9NPD8) (Ubiquitin-conjugating enzyme E2 T):

> Accepts ubiquitin from the E1 complex and catalyzes its covalent attachment to other proteins. Catalyzes monoubiquitination. Involved in mitomycin-C (MMC)-induced DNA repair. Acts as a specific E2 ubiquitin-conjugating enzyme for the Fanconi anemia complex by associating with E3 ubiquitin-protein ligase FANCL and catalyzing monoubiquitination of FANCD2, a key step in the DNA damage pathway. Also mediates monoubiquitination of FANCL and FANCI. May contribute to ubiquitination and degradation of …

**Summary**, from NCBI Gene [29089](https://www.ncbi.nlm.nih.gov/gene/29089):

> The protein encoded by this gene catalyzes the covalent attachment of ubiquitin to protein substrates. Defects in this gene have been associated with Fanconi anemia of complementation group T. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2015]

**Accessions** — [HGNC:25009](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25009) · Entrez [29089](https://www.ncbi.nlm.nih.gov/gene/29089) · UniProt [Q9NPD8](https://www.uniprot.org/uniprotkb/Q9NPD8) · Ensembl [ENSG00000077152](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077152)

## Data

Gene col 1176: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1176); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1176, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1176]; `tensor/DDL_lfc|DDL_z.npy` [1176]; `embed/gene_vectors.npy` [1176]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1176 or target_col == 1176). Every well: [[UBE2T — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2T.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
