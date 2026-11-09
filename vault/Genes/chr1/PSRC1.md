---
symbol: "PSRC1"
type: "gene"
col: 5524
ensembl_id: "ENSG00000134222"
name: "proline and serine rich coiled-coil 1"
location: "1p13.3"
module: 22
arm: "+"
pooled_cpm: 8.82
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 31
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# PSRC1

*proline and serine rich coiled-coil 1* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.75× (z +6.1, q 5e-07, up in 22 of 37 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~85% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.41× (z +3.7, q 0.026, up in 13 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (17 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.390× (z -10.3, q 5e-22, down in 36 of 46 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.562× (z -8.9, q 2e-16, down in 30 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNF]] (+0.89, fdr 7e-06), [[NEK2]] (+0.88, fdr 7e-06), [[KIF20A]] (+0.88, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5524.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~85% of this change | **1.75×** | +6.1 | 5e-07 | 22/37 (SW1417, HOP62, …) | all doses, flat | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **2.20×** | +4.5 | 0.002 | 15/40 (NCI-H23, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.32×** | +4.4 | 0.003 | 13/47 (NCI-H23, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.026 | 13/46 (KATO III, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.036 | 11/47 (HT-29, HEC-1-A, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.36×** | +3.4 | 0.072 | 13/45 (HT-29, HOP62, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.099 | 16/46 (RKO, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 17 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5524.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.390×** | -10.3 | 5e-22 | 36/46 (PANC-1, J82, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.562×** | -8.9 | 2e-16 | 30/43 (Hs 766T, HCT15, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.472×** | -8.2 | 5e-14 | 25/41 (C-33 A, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.444×** | -8.1 | 1e-13 | 27/44 (SK-MEL-2, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.553×** | -6.5 | 1e-08 | 26/46 (A498, A-427, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.553×** | -6.5 | 1e-08 | 28/45 (KATO III, HT-29, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.667×** | -6.2 | 4e-08 | 25/46 (PANC-1, A498, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.572×** | -6.1 | 8e-08 | 25/45 (AN3 CA, SW480, …) | top dose only | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.585×** | -5.8 | 3e-07 | 23/46 (A549, HS-578T, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.586×** | -5.8 | 3e-07 | 22/47 (SNU-1, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.593×** | -5.7 | 6e-07 | 22/44 (LOX-IMVI, Panc 03.27, …) | two highest doses | position effect removed |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.584×** | -5.6 | 8e-07 | 19/43 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.604×** | -5.5 | 2e-06 | 25/44 (SNU-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.602×** | -5.3 | 4e-06 | 18/44 (NCI-H2347, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.622×** | -5.2 | 9e-06 | 19/46 (LS 180, A-172, …) | two highest doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.719×** | -5.1 | 1e-05 | 21/47 (A498, NCI-H2347, …) | two highest doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.633×** | -4.8 | 6e-05 | 19/45 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.736×** | -4.7 | 8e-05 | 17/43 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.766×** | -3.7 | 0.005 | 16/47 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.720×** | -3.6 | 0.009 | 14/45 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.536×** | -3.6 | 0.009 | 11/42 (PANC-1, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.712×** | -3.4 | 0.014 | 14/45 (SNU-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.727×** | -3.3 | 0.017 | 15/42 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.763×** | -2.9 | 0.061 | 13/46 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +1.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5524. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 9.49 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.191× (z -9.3) |
| [[Hs 766T (line)]] | wt | 11.7 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -11.9) |
| [[SNU-1 (line)]] | wt | 11.7 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.120× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 8.37 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -8.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 8.86 | 0 | 2 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0867× (z -10.7) ⚠ cell-cycle shift, explains ~57% of this change |
| [[SK-MEL-2 (line)]] | alt | 21.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -12.4) |
| [[A-172 (line)]] | wt | 7.34 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.244× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 9.75 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0872× (z -9.3) |
| [[HCT15 (line)]] | alt | 16.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -10.5) |
| [[HS-578T (line)]] | alt | 8.21 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.118× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 6.06 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.116× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 6.55 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0549× (z -10.5) ⚠ cell-cycle shift, explains ~57% of this change |
| [[PANC-1 (line)]] | alt | 8.91 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -8.8) |
| [[SW 900 (line)]] | alt | 8.91 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0683× (z -10.4) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 8.25 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -8.8) |
| [[A-427 (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.08 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5524), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNF]] | +0.89 | +0.87 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[NEK2]] | +0.88 | +0.87 / +0.85 | both halves | 7e-06 |  |
| [[KIF20A]] | +0.88 | +0.90 / +0.88 | both halves | 7e-06 | STRING 505 |
| [[DLGAP5]] | +0.85 | +0.85 / +0.84 | both halves | 7e-06 | STRING 582 |
| [[CCNA2]] | +0.85 | +0.84 / +0.85 | both halves | 7e-06 |  |
| [[CDCA8]] | +0.85 | +0.85 / +0.87 | both halves | 7e-06 | STRING 629 |
| [[CDCA3]] | +0.85 | +0.87 / +0.82 | both halves | 7e-06 | STRING 500 |
| [[TTK]] | +0.84 | +0.79 / +0.81 | both halves | 7e-06 |  |
| [[INCENP]] | +0.84 | +0.86 / +0.79 | both halves | 7e-06 |  |
| [[GPSM2]] | +0.84 | +0.84 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[BUB1]] | +0.83 | +0.84 / +0.81 | both halves | 7e-06 |  |
| [[TOP2A]] | +0.83 | +0.83 / +0.80 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PSRC1's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.8% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PIMREG]] | B | PIMREG activity raises PSRC1's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.23× lower at baseline in the lines without PIMREG | 0.006 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NEURL1B]] | B | NEURL1B activity raises PSRC1's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.77× lower at baseline in the lines without NEURL1B | 0.077 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[AURKB]] | C | AURKB activity raises PSRC1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.47× lower at baseline in the lines without AURKB | 0.009 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[PBK]] | C | PBK activity raises PSRC1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.64× lower at baseline in the lines without PBK | 0.012 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[CDC20]] | C | CDC20 activity raises PSRC1's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.31× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[ACBD7]] | C | ACBD7 activity raises PSRC1's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 1.74× lower at baseline in the lines without ACBD7 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent; its own permutation p |
| [[CDCA3]] | C | CDCA3 activity raises PSRC1's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 2.58× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.821). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.9, -57.5); signed map (-50.4, -40.9). **Vector** length 115, 29.1% of its response variance represented; |z| ≥ 3 in 1,021 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.67 to 60); *DREAM G2/M down* (control, mean cos +0.76 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.62 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~85% of this change | +5.3 | +6.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | +4.4 | +4.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.2 | +3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.9 | +3.2 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.8 | +3.6 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +1.9 | +2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.8 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +0.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +1.2 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | -5.9 | -8.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -5.8 | -10.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.6 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -6.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.9 | -6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | proline and serine rich coiled-coil 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:109,279,556-109,283,186 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DDA3 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PGN9](https://www.uniprot.org/uniprotkb/Q6PGN9) (Proline/serine-rich coiled-coil protein 1):

> Required for normal progression through mitosis. Required for normal congress of chromosomes at the metaphase plate, and for normal rate of chromosomal segregation during anaphase. Plays a role in the regulation of mitotic spindle dynamics. Increases the rate of turnover of microtubules on metaphase spindles, and contributes to the generation of normal tension across sister kinetochores. Recruits KIF2A and ANKRD53 to the mitotic spindle and spindle poles. May participate in p53/TP53-regulated …

**Summary**, from NCBI Gene [84722](https://www.ncbi.nlm.nih.gov/gene/84722):

> This gene encodes a proline-rich protein that is a target for regulation by the tumor suppressor protein p53. The encoded protein plays an important role in mitosis by recruiting and regulating microtubule depolymerases that destabalize microtubules. Alternatively spliced transcript variants encoding different isoforms have been described. [provided by RefSeq, Apr 2014]

**Accessions** — [HGNC:24472](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24472) · Entrez [84722](https://www.ncbi.nlm.nih.gov/gene/84722) · UniProt [Q6PGN9](https://www.uniprot.org/uniprotkb/Q6PGN9) · Ensembl [ENSG00000134222](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134222)

## Data

Gene col 5524: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5524); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5524, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5524]; `tensor/DDL_lfc|DDL_z.npy` [5524]; `embed/gene_vectors.npy` [5524]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5524 or target_col == 5524). Every well: [[PSRC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSRC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
