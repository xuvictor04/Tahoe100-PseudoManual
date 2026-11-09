---
symbol: "RGS17"
type: "gene"
col: 1678
ensembl_id: "ENSG00000091844"
name: "regulator of G protein signaling 17"
location: "6q25.2"
module: 174
arm: "+"
pooled_cpm: 40.96
n_lines_expressing: 35
n_dd_up: 7
n_dd_down: 57
n_dd_up_clean: 7
n_dd_down_clean: 44
in_vector_space: true
direction_upstream: 21
direction_downstream: 18
tags: ["gene", "module/174"]
generated_by: "tahoemap"
---

# RGS17

*regulator of G protein signaling 17* — 6q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.51× (z +7.9, q 2e-12, up in 22 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 57 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.362× (z -19.4, q 0e+00, down in 29 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHC2]] (+0.73, fdr 7e-06), [[DUSP6]] (+0.69, fdr 7e-06), [[ITGB5]] (+0.67, fdr 7e-06).
> It is in [[Module 174]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[TSPAN5]] → it (grade B ⚠); 18 go from it, the strongest it → [[TSPAN5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1678.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +7.9 | 2e-12 | 22/33 (LoVo, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.71×** | +7.3 | 1e-10 | 24/33 (LoVo, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +6.8 | 2e-09 | 19/33 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.5 | 0.001 | 16/33 (SW480, A498, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +4.3 | 0.002 | 18/33 (NCI-H460, PANC-1, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.91×** | +4.3 | 0.002 | 18/33 (HOP62, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.82×** | +4.0 | 0.006 | 18/33 (NCI-H23, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 1.60× | +3.1 | 0.11 | 10/33 (HOP62, A-172, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 0.5 µM |  | 1.38× | +3.1 | 0.11 | 8/33 (HOP62, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | 1.26× | +3.1 | 0.11 | 16/33 (NCI-H460, LoVo, …) | two highest doses | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 60 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 57 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1678.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.362×** | -19.4 | 0e+00 | 29/33 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.475×** | -10.5 | 4e-23 | 29/33 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.486×** | -9.7 | 4e-20 | 26/33 (A549, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.491×** | -9.2 | 4e-18 | 25/32 (J82, A-172, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.253×** | -9.0 | 2e-17 | 24/34 (HOP62, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.511×** | -8.5 | 1e-15 | 28/33 (A549, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.594×** | -8.5 | 2e-15 | 28/33 (HOP62, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.528×** | -8.3 | 1e-14 | 24/33 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.542×** | -7.9 | 1e-13 | 19/27 (SHP-77, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.556×** | -7.9 | 1e-13 | 19/33 (A-427, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.552×** | -7.7 | 7e-13 | 27/33 (HOP62, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.592×** | -7.5 | 4e-12 | 25/33 (A-172, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.549×** | -7.5 | 4e-12 | 22/29 (SHP-77, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.681×** | -7.3 | 1e-11 | 21/33 (SNU-423, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.584×** | -7.2 | 2e-11 | 25/34 (C32, SW480, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.568×** | -7.2 | 2e-11 | 22/33 (SK-MEL-2, SHP-77, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.640×** | -7.1 | 6e-11 | 22/33 (C32, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1678. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 36.5 | 0 | 8 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0338× (z -15.2) |
| [[A549 (line)]] | wt | 160 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -13.5) |
| [[NCI-H23 (line)]] | alt | 67.1 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.201× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -10.0) |
| [[A-172 (line)]] | wt | 79.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -11.4) |
| [[HOP62 (line)]] | alt | 51.4 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -20.2) |
| [[SNU-423 (line)]] | alt | 131 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -13.6) |
| [[HT-29 (line)]] | alt | 78.9 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.316× (z -9.4) ⚠ cell-cycle shift, explains ~18% of this change |
| [[NCI-H1792 (line)]] | alt | 163 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0494× (z -32.1) |
| [[A-427 (line)]] | wt | 29.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -15.6) |
| [[PANC-1 (line)]] | alt | 46.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -19.5) |
| [[SK-MEL-2 (line)]] | alt | 49.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -18.0) |
| [[CFPAC-1 (line)]] | alt | 34.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -13.9) |
| [[HEC-1-A (line)]] | alt | 52.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -14.4) |
| [[J82 (line)]] | alt | 16.5 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.76× (z +9.0) | [[Cobimetinib (drug)]] 5 µM 0.132× (z -12.0) |
| [[LoVo (line)]] | wt | 11.7 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.97× (z +12.0) | — |
| [[NCI-H2030 (line)]] | alt | 52.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 12.1 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.78× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 42.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -15.6) |
| [[RPMI-7951 (line)]] | alt | 49.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.139× (z -12.8) |
| [[SHP-77 (line)]] | alt | 190 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -14.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 11.6 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.30× (z +11.2) | — |
| [[HS-578T (line)]] | alt | 69.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 41.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 21.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -11.7) |
| [[SW 900 (line)]] | alt | 59.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -16.4) |
| [[A498 (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.82 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.00 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.80 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.12 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.15 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.08 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.48 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.96 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1678), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHC2]] | +0.73 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[DUSP6]] | +0.69 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[ITGB5]] | +0.67 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[PTPN12]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[ST3GAL1]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[WWTR1]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[STC1]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[SPRY4]] | +0.64 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[TIMP1]] | +0.63 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[DUSP5]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[NPAS2]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[HTR7]] | +0.63 | +0.51 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 14, C 7. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN5]] | B | TSPAN5 activity raises RGS17's level | lines that do not express TSPAN5 (9) vs lines expressing it (41) | 3.20× lower at baseline in the lines without TSPAN5 | 0.009 | ⚠ within organs, on part of the lines; also absent: KLF12 |
| [[ABLIM3]] | B | ABLIM3 activity raises RGS17's level | lines that do not express ABLIM3 (15) vs lines expressing it (35) | 3.06× lower at baseline in the lines without ABLIM3 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: LINC00511, MILR1, TLR4; maybe low, not absent |
| [[MTSS1]] | B | MTSS1 activity raises RGS17's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 2.44× lower at baseline in the lines without MTSS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |
| [[ITGB3]] | B | ITGB3 activity raises RGS17's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 3.80× lower at baseline in the lines without ITGB3 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[ANKH]] | B | ANKH activity raises RGS17's level | lines that do not express ANKH (6) vs lines expressing it (44) | 4.24× lower at baseline in the lines without ANKH | 0.019 | ⚠ within organs, on part of the lines; also absent: GCNT1, LCA5, CA13; maybe low, not absent |
| [[EPAS1]] | B | EPAS1 activity raises RGS17's level | lines that do not express EPAS1 (9) vs lines expressing it (41) | 4.19× lower at baseline in the lines without EPAS1 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS |
| [[TGM2]] | B | TGM2 activity raises RGS17's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 2.21× lower at baseline in the lines without TGM2 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |
| [[MAP2K1]] | B | MAP2K1 activity raises RGS17's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 10.4% of all compounds | 0.062 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KLF12]] | B | KLF12 activity raises RGS17's level | lines that do not express KLF12 (9) vs lines expressing it (41) | 4.24× lower at baseline in the lines without KLF12 | 0.064 | ⚠ within organs, on part of the lines; also absent: RHOBTB1, ZC3H12C, GNAI1 |
| [[LINC02813]] | B | LINC02813 activity raises RGS17's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 2.69× lower at baseline in the lines without LINC02813 | 0.064 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN |
| [[NRP1]] | B | NRP1 activity raises RGS17's level | lines that do not express NRP1 (16) vs lines expressing it (34) | 2.06× lower at baseline in the lines without NRP1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: BDKRB2, MX2, FAM107B |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers RGS17's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 14, C 4. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN5]] | B | RGS17 activity raises TSPAN5's level | lines that do not express RGS17 (15) vs lines expressing it (35) | 2.28× lower at baseline in the lines without RGS17 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1 |
| [[MAP3K5]] | B | RGS17 activity raises MAP3K5's level | lines that do not express RGS17 (15) vs lines expressing it (35) | 2.11× lower at baseline in the lines without RGS17 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1 |
| [[EPAS1]] | B | RGS17 activity raises EPAS1's level | lines that do not express RGS17 (15) vs lines expressing it (35) | 2.73× lower at baseline in the lines without RGS17 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1 |
| [[ABLIM3]] | B | RGS17 activity raises ABLIM3's level | lines that do not express RGS17 (15) vs lines expressing it (35) | 2.92× lower at baseline in the lines without RGS17 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1 |
| [[DUSP5]] | B | RGS17 activity raises DUSP5's level | lines that do not express RGS17 (15) vs lines expressing it (35) | 2.38× lower at baseline in the lines without RGS17 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1 |
| [[JCAD]] | B | RGS17 activity raises JCAD's level | lines that do not express RGS17 (15) vs lines expressing it (35) | 3.03× lower at baseline in the lines without RGS17 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1 |
| [[SPRED1]] | B | RGS17 activity raises SPRED1's level | lines that do not express RGS17 (15) vs lines expressing it (35) | 1.23× lower at baseline in the lines without RGS17 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1 |
| [[SMOX]] | B | RGS17 activity raises SMOX's level | lines that do not express RGS17 (15) vs lines expressing it (35) | 2.00× lower at baseline in the lines without RGS17 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1 |
| [[NRP1]] | B | RGS17 activity raises NRP1's level | lines that do not express RGS17 (15) vs lines expressing it (35) | 2.76× lower at baseline in the lines without RGS17 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1 |
| [[SHB]] | B | RGS17 activity raises SHB's level | lines that do not express RGS17 (15) vs lines expressing it (35) | 1.35× lower at baseline in the lines without RGS17 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1 |
| [[ITGB3]] | B | RGS17 activity raises ITGB3's level | lines that do not express RGS17 (15) vs lines expressing it (35) | 4.12× lower at baseline in the lines without RGS17 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1 |
| cells under [[Cobimetinib (drug)]] 5 µM | B | RGS17 activity lowers the cells' numbers under Cobimetinib 5 µM (makes them more sensitive) | lines that do not express RGS17 (15) vs lines expressing it (33) | the lines without RGS17: 1.20× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1 |

## Where it sits

- **Module**: [[Module 174]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.811). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.0, 5.7); signed map (7.7, 48.7). **Vector** length 124, 36.6% of its response variance represented; |z| ≥ 3 in 1,241 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.5 | +7.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.4 | +7.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.9 | +6.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.1 | +4.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.8 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +1.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.0 | +4.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -8.0 | -10.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -7.2 | -8.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -6.7 | -7.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -6.6 | -7.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.5 | -7.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -6.5 | -9.2 |

## What is on record

|  |  |
|---|---|
| Name | regulator of G protein signaling 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.2 — chr6:153,004,459-153,131,282 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RGSZ2, RGS-17 |
| Gene groups (HGNC) | Regulators of G-protein signaling |
| Reactome | 5 pathways, smallest: G alpha (z) signalling events; G alpha (q) signalling events; G alpha (i) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UGC6](https://www.uniprot.org/uniprotkb/Q9UGC6) (Regulator of G protein signaling 17):

> Regulates G protein-coupled receptor signaling cascades, including signaling via muscarinic acetylcholine receptor CHRM2 and dopamine receptor DRD2. Inhibits signal transduction by increasing the GTPase activity of G protein alpha subunits, thereby driving them into their inactive GDP-bound form. Binds selectively to GNAZ and GNAI2 subunits, accelerates their GTPase activity and regulates their signaling activities. Negatively regulates mu-opioid receptor-mediated activation of the G proteins …

**Summary**, from NCBI Gene [26575](https://www.ncbi.nlm.nih.gov/gene/26575):

> This gene encodes a member of the regulator of G-protein signaling family. This protein contains a conserved, 120 amino acid motif called the RGS domain and a cysteine-rich region. The protein attenuates the signaling activity of G-proteins by binding to activated, GTP-bound G alpha subunits and acting as a GTPase activating protein (GAP), increasing the rate of conversion of the GTP to GDP. This hydrolysis allows the G alpha subunits to bind G beta/gamma subunit heterodimers, forming inactive …

**Accessions** — [HGNC:14088](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14088) · Entrez [26575](https://www.ncbi.nlm.nih.gov/gene/26575) · UniProt [Q9UGC6](https://www.uniprot.org/uniprotkb/Q9UGC6) · Ensembl [ENSG00000091844](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091844)

## Data

Gene col 1678: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1678); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1678, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1678]; `tensor/DDL_lfc|DDL_z.npy` [1678]; `embed/gene_vectors.npy` [1678]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1678 or target_col == 1678). Every well: [[RGS17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RGS17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
